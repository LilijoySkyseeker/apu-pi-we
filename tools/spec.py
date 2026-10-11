"""The language's reference spec as data (roadmap phase 2a, 2026-10-11).

spec/reference.toml is the source of truth; docs/language.md is generated from it.
Each heading, rule, paragraph and table is an [[item]] with a stable id:
headings "4.2", items inside them "4.2.3" (intro items "0.n").

  python spec.py build      # write docs/language.md from spec/reference.toml
  python spec.py check      # fail if docs/language.md differs from what build would write
  python spec.py examples   # list every example (rule id, Apupiwe, English) as TSV
"""
import os, re, sys, tomllib

ROOT = os.path.join(os.path.dirname(__file__), "..")
SRC = os.path.join(ROOT, "spec", "reference.toml")
OUT = os.path.join(ROOT, "docs", "language.md")
NOTE = "<!-- Generated from spec/reference.toml by tools/spec.py build. Edit the spec, not this file. -->"


def load():
    with open(SRC, "rb") as fh:
        return tomllib.load(fh)


def render(spec):
    lines = [spec["title"], NOTE]
    for it in spec["item"]:
        lines += [""] * it.get("gap", 1)
        lines.append(it["text"])
    return "\n".join(lines) + "\n"


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
        print(f"wrote {OUT}: {len(spec['item'])} items")
    elif cmd == "check":
        same = open(OUT).read() == render(spec)
        print("docs/language.md matches the spec" if same else "docs/language.md differs from the spec: run build")
        sys.exit(0 if same else 1)
    elif cmd == "examples":
        for row in examples(spec):
            print("\t".join(row))
