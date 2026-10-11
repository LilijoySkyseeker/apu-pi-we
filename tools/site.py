"""Build the website from the docs and word lists into build/site.

  python site.py              # build
  python site.py serve        # build, then serve at http://127.0.0.1:8000

Pages are generated, never edited: the learner guide is split into one page per lesson, the
dictionary is built from data/*.tsv, and links to repo files the site doesn't carry become
plain text. Look and behaviour live in site/style.css and site/site.js.
Needs python-markdown: nix-shell -p 'python3.withPackages(ps: [ps.markdown])'
"""
import csv, html, json, os, re, shutil, sys
import markdown

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "build", "site")
REPO = "https://github.com/LilijoySkyseeker/apupiwe"
LINKS = {"../data/lexicon.tsv": "dictionary.md", "../data/grammar.tsv": "language.md#13-grammar-words",
         "../data/compounds.tsv": "dictionary.md#compounds"}
# grammar.tsv glosses are short labels; these read better as hover text
GRAMMAR_GLOSS = {"Q": "question", "WH": "what, which", "UNSPEC": "some (unspecified)", "CONF": "confidence (sixths)",
                 "OBVIATIVE": "he/she (another one)", "LOGOPHOR": "he/she (the one reported)", "PART": "some, not all",
                 "THAT.dem": "that", "THAT.comp": "that (a clause)", "WHO.rel": "who, which (describes)",
                 "WE.incl": "we (with you)", "WE.excl": "we (not you)", "YOUKNOW": "you know", "GENERIC": "one, people",
                 "UNSPEC": "some, any", "DONE": "done (aspect)", "ONGOING": "ongoing (aspect)", "AGENT": "one who",
                 "RESULT": "thing done", "TOOL": "thing for", "PLACE": "place for", "NAME": "name follows"}


def tsv(name):
    with open(os.path.join(ROOT, "data", name), newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def read(path):
    return open(os.path.join(ROOT, path)).read()


def split_learn(text):
    """One page per lesson; the part before lesson 1 is the guide's front page."""
    parts = re.split(r"^(?=## )", text, flags=re.M)
    lessons, intro = [], parts[0]
    for part in parts[1:]:
        title = part.splitlines()[0][3:]
        if not title.startswith("Lesson") and not lessons:
            intro += part
            continue
        name = f"learn-{len(lessons) + 1:02d}" if title.startswith("Lesson") else "learn-next"
        lessons.append((name, title, "#" + part[2:]))
    return intro, lessons


def words():
    """Every word with its meaning, for the dictionary and hover glosses."""
    lex = tsv("lexicon.tsv")
    form = {w["gloss"]: w["form"] for w in lex}
    opp = {}
    for a, b in (r.values() for r in tsv("antonyms.tsv")):
        if a in form and b in form:
            opp[a], opp[b] = form[b], form[a]
    for w in lex:
        w["opposite"] = opp.get(w["gloss"], "")
    gram = [{"form": g["form"], "gloss": GRAMMAR_GLOSS.get(g["gloss"], g["gloss"].lower()), "class": g["class"]}
            for g in tsv("grammar.tsv")]
    return lex, gram, tsv("compounds.tsv")


def dictionary_html(lex, gram, comp):
    fields = sorted({w["field"] for w in lex})
    rows = "\n".join(
        f'<tr id="w-{w["form"]}" data-f="{w["field"]}"><td><a href="#w-{w["form"]}"><b>{w["form"]}</b></a></td>'
        f'<td>{html.escape(w["gloss"])}</td><td>{w["field"]}</td><td>{w["tier"]}</td>'
        f'<td>{f"<a href=#w-{w["opposite"]}>{w["opposite"]}</a>" if w["opposite"] else ""}</td></tr>'
        for w in sorted(lex, key=lambda w: w["form"]))
    grows = "\n".join(f'<tr id="g-{g["form"]}" data-f="grammar"><td><b>{g["form"]}</b></td><td>{html.escape(g["gloss"])}</td>'
                      f'<td>{g["class"]}</td></tr>' for g in sorted(gram, key=lambda g: g["form"]))
    crows = "\n".join(f'<tr data-f="compound"><td><b>{c["form"]}</b></td><td>{html.escape(c["gloss"])}</td>'
                      f'<td>{html.escape(c["literal"])}</td></tr>' for c in sorted(comp, key=lambda c: c["form"]))
    opts = "".join(f"<option>{f}</option>" for f in fields) + '<option value="grammar">grammar words</option><option value="compound">compounds</option>'
    return f'''<h1 id="dictionary">Dictionary</h1>
<p>There are {len(lex)} root words and loans, {len(gram)} grammar words and {len(comp)} compounds.
The Common column runs from 5, the words to learn first, down to 1. Type in the box to filter, or click a
column heading to sort. The grammar words are explained in <a href="language.html#13-grammar-words">section 13
of the reference</a>.</p>
<p class="filter"><input id="dict-filter" type="search" placeholder="filter: word or meaning" autocomplete="off">
<select id="dict-field"><option value="">all topics</option>{opts}</select> <span id="dict-count"></span></p>
<table class="dict sortable" id="dict"><thead><tr><th>Word</th><th>Meaning</th><th>Topic</th><th>Common</th><th>Opposite</th></tr></thead>
<tbody>
{rows}
</tbody></table>
<h2 id="grammar-words">Grammar words</h2>
<table class="dict sortable"><thead><tr><th>Word</th><th>Meaning</th><th>Kind</th></tr></thead><tbody>
{grows}
</tbody></table>
<h2 id="compounds">Compounds</h2>
<table class="dict sortable"><thead><tr><th>Word</th><th>Meaning</th><th>Literally</th></tr></thead><tbody>
{crows}
</tbody></table>
'''


def md_to_html(text, pages):
    def link(m):
        label, target = m.group(1), m.group(2)
        target = LINKS.get(target, target)
        base = target.split("#")[0]
        if target.startswith(("http", "#")):
            return m.group(0)
        if base.endswith(".md") and base[:-3] in pages:
            if label.endswith(".md"):
                label = TITLES.get(base[:-3], label)
            return f"[{label}]({base[:-3]}.html{target[len(base):]})"
        return label  # a repo file the site doesn't carry
    text = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", link, text)
    md = markdown.Markdown(extensions=["tables", "attr_list", "toc"],
                           extension_configs={"toc": {"permalink": "§", "toc_depth": "2-3"}})
    body = md.convert(text)
    return body, md.toc_tokens


TITLES = {"language": "the reference", "rationale": "why it is this way", "design-log": "changelog",
          "measurement": "senary measurement", "learn": "learner guide", "dictionary": "dictionary"}
NOTES = {"rationale", "design-log"}
NOTES_BANNER = ('<p class="notes">These are the project\'s working notes, kept for whoever works on the language next, '
                'which is often an AI assistant. They are dense, but the reasons for everything are here.</p>')
NAV = [("index", "Home"), ("learn", "Learn"), ("language", "Reference"), ("dictionary", "Dictionary"), ("examples", "Examples"),
       ("rationale", "Design")]
SECTION = {"design-log": "rationale", "measurement": "rationale"}  # pages shown under another menu item


def page(name, title, body, toc, prev=None, nxt=None, extra=""):
    current = SECTION.get(name, "learn" if name.startswith("learn") else "examples" if name.startswith("example") else name)
    nav = " ".join(f'<a href="{n}.html"{" class=here" if n == current else ""}>{t}</a>' for n, t in NAV)
    lesson = name.startswith("learn-")
    def flat(tokens):
        for t in tokens:
            yield t
            yield from flat(t["children"])
    items = [f'<li class="l{t["level"]}"><a href="#{t["id"]}">{t["name"]}</a></li>'
             for t in flat(toc) if t["level"] == 2 or (t["level"] == 3 and (name == "language" or lesson))]
    side = f'<nav class="toc"><b>On this page</b><ul>{"".join(items)}</ul></nav>' if len(items) > 1 else ""
    pn = ""
    if prev or nxt:
        pn = '<p class="pn">' + (f'<a href="{prev[0]}.html" rel="prev">← {prev[1]}</a>' if prev else "<span></span>") + \
             (f'<a href="{nxt[0]}.html" rel="next">{nxt[1]} →</a>' if nxt else "") + "</p>"
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Apupiwe</title>
<link rel="stylesheet" href="style.css">
<script>try {{ var t = localStorage.getItem("theme"); if (t) document.documentElement.dataset.theme = t; }} catch (e) {{}}</script>
</head><body>
<header><a class="site" href="index.html">Apupiwe</a> <nav>{nav} <a href="{REPO}">Source</a> <button id="theme" type="button" hidden>dark</button></nav>
<form class="search" action="search.html" role="search"><input id="q" name="q" type="search" placeholder="search  ( / )" autocomplete="off" aria-label="Search"><ol id="hits" hidden></ol></form></header>
<div class="wrap">{side}<main>
{body}
{pn}{extra}
</main></div>
<footer>Still in design: words and rules may change. Public domain (CC0) · <a href="{REPO}">source</a> · <a href="{REPO}/issues">report a problem</a></footer>
<script src="site.js"></script>
</body></html>
'''


def plain(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def sections(name, title, body):
    """Search entries: one per h1-h3 section."""
    out = []
    for m in re.finditer(r'<h([123])[^>]*? id="([^"]+)"[^>]*>(.*?)</h\1>(.*?)(?=<h[123][ >]|\Z)', body, re.S):
        head = plain(re.sub(r'<a class="headerlink".*?</a>', "", m.group(3)))
        out.append({"t": head, "p": title, "u": f"{name}.html#{m.group(2)}", "x": plain(m.group(4))[:2000]})
    return out


def build():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT)
    for f in ("style.css", "site.js"):
        shutil.copy(os.path.join(ROOT, "site", f), OUT)
    lex, gram, comp = words()
    intro, lessons = split_learn(read("docs/learn.md"))
    lesson_list = "\n## Lessons\n\n" + "\n".join(f"- [{t}]({n}.md)" for n, t, _ in lessons) + "\n"
    sources = [("index", "Home", read("site/index.md")), ("learn", "Learn", intro + lesson_list)]
    sources += [(n, t, b) for n, t, b in lessons]
    sources += [("language", "Reference", read("docs/language.md")), ("rationale", "Why it is this way", read("docs/rationale.md")),
                ("design-log", "Changelog", read("docs/design-log.md")), ("measurement", "Senary measurement", read("docs/measurement.md"))]
    # examples/*.md: one page each, listed on examples.html in the order of their file names
    ex_dir = os.path.join(ROOT, "examples")
    ex = []
    for f in sorted(os.listdir(ex_dir)) if os.path.isdir(ex_dir) else []:
        if f.endswith(".md") and f != "index.md":
            text = read(f"examples/{f}")
            ex.append(("example-" + f[:-3], text.splitlines()[0].lstrip("# "), text))
    ex_index = read("examples/index.md") + "\n" + "\n".join(f"- [{t}]({n}.md)" for n, t, _ in ex) + "\n"
    sources += [("examples", "Examples", ex_index)] + ex
    names = {n for n, _, _ in sources} | {"dictionary"}
    index = []
    order = ["learn"] + [n for n, _, _ in lessons]
    titles = dict((n, t) for n, t, _ in sources)
    for name, title, text in sources:
        body, toc = md_to_html(text, names)
        if name in NOTES:
            body = body.replace("</h1>", "</h1>" + NOTES_BANNER, 1)
        if name == "rationale":
            body += '<p class="also">Also: <a href="design-log.html">changelog</a> · <a href="measurement.html">senary measurement</a></p>'
        i = order.index(name) if name in order else None
        prev = (order[i - 1], titles[order[i - 1]]) if i else None
        nxt = (order[i + 1], titles[order[i + 1]]) if i is not None and i + 1 < len(order) else None
        open(os.path.join(OUT, f"{name}.html"), "w").write(page(name, title, body, toc, prev, nxt))
        index += sections(name, title, body)
    body = dictionary_html(lex, gram, comp)
    open(os.path.join(OUT, "dictionary.html"), "w").write(page("dictionary", "Dictionary", body, []))
    index += [{"t": w["form"], "p": "Dictionary", "u": f"dictionary.html#w-{w['form']}", "x": w["gloss"]} for w in lex]
    index += [{"t": g["form"], "p": "Grammar word", "u": f"dictionary.html#g-{g['form']}", "x": g["gloss"]} for g in gram]
    index += [{"t": c["form"], "p": "Compound", "u": "dictionary.html#compounds", "x": c["gloss"]} for c in comp]
    open(os.path.join(OUT, "search.html"), "w").write(page("search", "Search", '<h1 id="search">Search</h1><ol id="results"></ol>', []))
    gloss = {w["form"]: w["gloss"] for w in lex} | {g["form"]: g["gloss"] for g in gram}
    with open(os.path.join(OUT, "index.json"), "w") as f:
        json.dump({"pages": index, "words": gloss}, f, ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print(f"wrote {OUT}: {len(sources) + 2} pages, {len(index)} search entries")


if __name__ == "__main__":
    build()
    if sys.argv[1:] == ["serve"]:
        import functools, http.server
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=OUT)
        http.server.ThreadingHTTPServer(("127.0.0.1", 8000), handler).serve_forever()
