"""Build the website from the docs and word lists.

  python site.py          # stage pages into build/site-src, then build build/site
  python site.py serve    # the same, served at http://127.0.0.1:8000 with live reload

The pages are generated, never edited: the learner guide is split into one page per lesson,
the dictionary is built from data/*.tsv, and links to files outside the site become plain text.
Needs mkdocs-material: nix-shell -p 'python3.withPackages(ps: [ps.mkdocs-material])'
"""
import csv, os, re, shutil, subprocess, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "build", "site-src")
CONFIG = os.path.join(ROOT, "site", "mkdocs.yml")
PAGES = ["language.md", "rationale.md", "design-log.md", "measurement.md"]
LINKS = {"../data/lexicon.tsv": "dictionary.md", "../data/grammar.tsv": "language.md#13-grammar-words",
         "../data/compounds.tsv": "dictionary.md#compounds"}


def tsv(name):
    with open(os.path.join(ROOT, "data", name), newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def fix_links(text, pages):
    def repl(m):
        label, target = m.group(1), m.group(2)
        target = LINKS.get(target, target)
        if target.split("#")[0] in pages or target.startswith(("http", "#")):
            return f"[{label}]({target})"
        return label  # a repo file the site doesn't carry
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, text)


def split_learn(text):
    """One page per lesson; the part before lesson 1 is the guide's front page."""
    parts = re.split(r"^(?=## )", text, flags=re.M)
    pages, intro = [], parts[0]
    for part in parts[1:]:
        title = part.splitlines()[0][3:]
        if not title.startswith("Lesson") and not pages:
            intro += part
            continue
        name = f"learn-{len(pages) + 1:02d}.md" if title.startswith("Lesson") else "learn-next.md"
        pages.append((name, title, "#" + part[2:]))
    return intro, pages


def dictionary():
    lex = tsv("lexicon.tsv")
    form = {w["gloss"]: w["form"] for w in lex}
    opp = {}
    for a, b in (r.values() for r in tsv("antonyms.tsv")):
        if a in form and b in form:
            opp[a], opp[b] = form[b], form[a]
    out = ["# Dictionary", "",
           "Every root and borrowed word. Use the search box to look up a word in either direction. "
           "**Common** runs from 5 (learn first) to 1. Grammar words are in the "
           "[reference, section 13](language.md#13-grammar-words).", "",
           "| Word | Meaning | Topic | Common | Opposite |", "|---|---|---|---|---|"]
    for w in sorted(lex, key=lambda w: w["form"]):
        out.append(f"| **{w['form']}** | {w['gloss']} | {w['field']} | {w['tier']} | {opp.get(w['gloss'], '')} |")
    out += ["", "## Compounds", "", "| Word | Meaning | Literally |", "|---|---|---|"]
    for c in sorted(tsv("compounds.tsv"), key=lambda c: c["form"]):
        out.append(f"| **{c['form']}** | {c['gloss']} | {c['literal']} |")
    return "\n".join(out) + "\n"


def stage():
    shutil.rmtree(SRC, ignore_errors=True)
    os.makedirs(SRC)
    intro, lessons = split_learn(open(os.path.join(ROOT, "docs", "learn.md")).read())
    names = set(PAGES) | {"index.md", "learn.md", "dictionary.md"} | {n for n, _, _ in lessons}
    files = {"index.md": open(os.path.join(ROOT, "site", "index.md")).read(), "dictionary.md": dictionary()}
    files["learn.md"] = intro + "\n## Lessons\n\n" + "\n".join(f"- [{t}]({n})" for n, t, _ in lessons) + "\n"
    files.update({n: body for n, _, body in lessons})
    files.update({p: open(os.path.join(ROOT, "docs", p)).read() for p in PAGES})
    for name, text in files.items():
        with open(os.path.join(SRC, name), "w") as f:
            f.write(fix_links(text, names))
    nav = [{"Home": "index.md"}, {"Learn": ["learn.md"] + [{t: n} for n, t, _ in lessons]},
           {"Reference": "language.md"}, {"Dictionary": "dictionary.md"},
           {"Design": [{"Why it is this way": "rationale.md"}, {"Changelog": "design-log.md"},
                       {"Senary measurement": "measurement.md"}]}]
    return nav


if __name__ == "__main__":
    import json
    nav = stage()
    # mkdocs reads YAML; JSON is valid YAML, so the nav is appended without a YAML library.
    config = os.path.join(ROOT, "build", "mkdocs.yml")
    with open(config, "w") as f:
        f.write(open(CONFIG).read().replace("../build/", "") + "\nnav: " + json.dumps(nav) + "\n")
    cmd = ["mkdocs", "serve", "-f", config] if sys.argv[1:] == ["serve"] else ["mkdocs", "build", "--strict", "-q", "-f", config]
    sys.exit(subprocess.call(cmd))
