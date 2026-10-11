"""Build examples/udhr.md: each Apupiwe paragraph of translation.md with the English paragraph below it.

  python make_page.py   # rerun after any change to translation.md
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "examples", "01-udhr.md")
INTRO = '''# Universal Declaration of Human Rights

The United Nations adopted the Universal Declaration of Human Rights in 1948. It is the most translated document in the world, which makes it a good first long text for any language. This translation was made from the English and checked against the French, which is equally official.

Each paragraph is followed by the original English. Point at or tap an Apupiwe word to see what it means.

Some ideas in the declaration don't have a single word in Apupiwe yet, so they are described. Religion is **lite pi nosen** "the way of God", a court is **pu pi wabun** "a place of law", and the United Nations is **funti pi gigin la** "the group of countries".

The English text is from the United Nations, as published by the UDHR in Unicode project.
'''


def sections(path):
    out, cur = {}, None
    for line in open(path):
        line = line.rstrip()
        if line.startswith("## "):
            cur = line[3:]
            out[cur] = []
        elif cur and line and not line.startswith("{"):
            out[cur].append(line)
    return out


apu, en = sections(os.path.join(HERE, "translation.md")), sections(os.path.join(HERE, "source.md"))
# The translation joins "Now, therefore, / The General Assembly / Proclaims ..." into one paragraph.
pre = en["Preamble"]
en["Preamble"] = pre[:7] + [" ".join(pre[7:])]
def heading(name):
    """Section headings in Apupiwe, as other translations use their own language."""
    if name == "Preamble":
        return "tuko pi kemin"  # beginning of the document
    return "wabun pi " + name.split()[1]  # Article 5 -> rule 5 (noun + pi + number is a label)


title = open(os.path.join(HERE, "translation.md")).readline().lstrip("# ").strip()
lines = [INTRO, f"## {title} {{.apu}}\n"]
for name, paras in en.items():
    assert len(paras) == len(apu[name]), name
    lines.append(f"## {heading(name)} {{.apu}}\n")
    for a, e in zip(apu[name], paras):
        # "1." alone between quotes would start a new list each time and show as 1; escape it to keep the number.
        a, e = (re.sub(r"^(\d+)\. ", r"\1\\. ", x) for x in (a, e))
        lines += [a, "{.apu}", "", "> " + e, ""]
open(OUT, "w").write("\n".join(lines))
print("wrote", OUT)
