import sys
sys.path.insert(0, "/home/agent/work/repos/universal-language/tests/lexicon-ladder-01")
import panel
for page in sys.argv[1:]:
    bl = panel.blocks(page)
    print(f"=== {page}: " + " || ".join(f"{n} ({sum(1 for _,c in panel.PANEL if c in d)})" for n, d in bl if sum(1 for _,c in panel.PANEL if c in d) > 0))
