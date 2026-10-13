"""The language's reference spec as data (roadmap phase 2a, 2026-10-11).

spec/reference.toml is the source of truth; docs/language.md is generated from it.
Each heading, rule, paragraph and table is an [[item]] with a stable id:
headings "4.2", items inside them "4.2.3" (intro items "0.n").

  python spec.py build      # write docs/language.md from spec/reference.toml
  python spec.py check      # fail if docs/language.md differs from what build would write
  python spec.py examples   # list every example (rule id, Apupiwe, English) as TSV
  python spec.py lessons    # fail if a rule a lesson teaches changed since the lesson was last reviewed
  python spec.py lessons --ack   # after reviewing those lessons: record the rules' current wording as seen

Every rule, paragraph and numbered item gets an anchor (#r-4-2-3) so other pages can link to it.
Lessons tag the rule a paragraph teaches with a visible link, [§4.2.3](language.md#r-4-2-3);
spec/lesson-sync.tsv stores a fingerprint of each tagged rule's wording as last reviewed.
Blocks in learn.md between <!-- generated: NAME --> and <!-- end generated --> are rewritten by build.
"""
import hashlib, os, re, sys, tomllib

ROOT = os.path.join(os.path.dirname(__file__), "..")
SRC = os.path.join(ROOT, "spec", "reference.toml")
OUT = os.path.join(ROOT, "docs", "language.md")
NOTE = "<!-- Generated from spec/reference.toml by tools/spec.py build. Edit the spec, not this file. -->"
LEARN = os.path.join(ROOT, "docs", "learn.md")
SYNC = os.path.join(ROOT, "spec", "lesson-sync.tsv")
TAG = re.compile(r"\[§([0-9.]+)\]\(language\.md#r-[0-9-]+\)")


def anchor(item_id):
    return "r-" + item_id.replace(".", "-")


def anchored(it):
    """The item's text with an anchor at its start (rules, paragraphs and numbered items only)."""
    t = it["text"]
    if it["type"] == "table" or t.startswith("|"):
        return f'<span id="{anchor(it["id"])}"></span>\n\n' + t  # a table can't hold an anchor inside
    if it["type"] in ("heading", "rule") or t.startswith("---"):
        return t
    span = f'<span id="{anchor(it["id"])}"></span>'
    m = re.match(r"(- |\d+\. )", t)
    return t[:m.end()] + span + t[m.end():] if m else span + t


def load():
    with open(SRC, "rb") as fh:
        return tomllib.load(fh)


def render(spec):
    lines = [spec["title"], NOTE]
    for it in spec["item"]:
        lines += [""] * it.get("gap", 1)
        lines.append(anchored(it))
    return "\n".join(lines) + "\n"


def fingerprint(text):
    return hashlib.sha1(text.encode()).hexdigest()[:12]


def template_list(spec):
    """Lesson 14's sentence order, generated from the template table in 4.1."""
    table = next(it["text"] for it in spec["item"] if it["type"] == "table" and "| 1 |" in it["text"])
    rows = [r.strip("|").split("|") for r in table.splitlines() if re.match(r"\| *\d+ *\|", r)]
    return "\n".join(f"{n.strip()}. {slot.strip()}: {what.strip()}" for n, slot, what, *_ in rows)


def item_text(item_id):
    return lambda spec: next(it["text"] for it in spec["item"] if it["id"] == item_id).strip()


GENERATED = {"template": template_list, "digits": item_text("9.1.1")}


def build_learn(spec):
    text = open(LEARN).read()
    def fill(m):
        return f"<!-- generated: {m.group(1)} -->\n{GENERATED[m.group(1)](spec)}\n<!-- end generated -->"
    new = re.sub(r"<!-- generated: (\w+) -->.*?<!-- end generated -->", fill, text, flags=re.S)
    if new != text:
        open(LEARN, "w").write(new)
    return new


def lessons(spec, ack=False):
    """Compare each rule a lesson tags with the wording recorded when the lesson was last reviewed."""
    texts = {it["id"]: it["text"] for it in spec["item"]}
    learn = open(LEARN).read()
    tagged = {}
    for section in re.split(r"^(?=## )", learn, flags=re.M):
        title = section.splitlines()[0].lstrip("# ") if section.strip() else ""
        for rid in TAG.findall(section):
            tagged.setdefault(rid, set()).add(title)
    seen = {}
    if os.path.exists(SYNC):
        for line in open(SYNC).read().splitlines()[1:]:
            rid, fp = line.split("\t")[:2]
            seen[rid] = fp
    problems = []
    for rid, where in sorted(tagged.items()):
        if rid not in texts:
            problems.append(f"§{rid}: no such rule (tagged in {', '.join(sorted(where))})")
        elif seen.get(rid) != fingerprint(texts[rid]) and not ack:
            problems.append(f"§{rid} changed since last review: check {', '.join(sorted(where))}")
    if ack:
        with open(SYNC, "w") as fh:
            fh.write("rule\tfingerprint\tlessons\n")
            for rid, where in sorted(tagged.items()):
                if rid in texts:
                    fh.write(f"{rid}\t{fingerprint(texts[rid])}\t{'; '.join(sorted(where))}\n")
        print(f"recorded {len(tagged)} tagged rules as reviewed")
        return 0
    print("\n".join(problems) if problems else f"lessons in step with the reference ({len(tagged)} tagged rules)")
    return 1 if problems else 0


def examples(spec):
    """Every **apu pi we** span followed by an English gloss in quotes, with its item id."""
    pat = re.compile(r'\*\*([a-z][^*]*?)\*\*\s*(?:=\s*)?"([^"]+)"')
    for it in spec["item"]:
        if it["type"] == "heading":
            continue
        for apu, en in pat.findall(it["text"]):
            yield it["id"], apu.strip(), en.strip()


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    spec = load()
    if cmd == "build":
        open(OUT, "w").write(render(spec))
        build_learn(spec)
        print(f"wrote {OUT}: {len(spec['item'])} items")
    elif cmd == "check":
        same = open(OUT).read() == render(spec)
        print("docs/language.md matches the spec" if same else "docs/language.md differs from the spec: run build")
        sys.exit(0 if same else 1)
    elif cmd == "lessons":
        sys.exit(lessons(spec, ack="--ack" in sys.argv))
    elif cmd == "examples":
        for row in examples(spec):
            print("\t".join(row))
