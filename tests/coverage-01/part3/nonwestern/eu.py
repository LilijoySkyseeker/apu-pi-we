import sys,re; sys.path.insert(0,'/tmp/nw'); from load import *
# usage: eu.py term [term...]  -> per term, EU languages whose uni_lemma/gloss matches \bterm\b, with matched labels
lab={}
for l in EU:
    s=set()
    for f in LANG[l]:
        for r in rows(f):
            for k in ("uni_lemma","gloss"):
                if v(r,k): s.add(norm(v(r,k)))
    lab[l]=s
for t in sys.argv[1:]:
    rx=re.compile(r"\b"+re.escape(t.lower())+r"s?\b")
    hit={l:sorted(x for x in s if rx.search(re.sub(r"\([^)]*\)","",x))) for l,s in lab.items()}
    hit={l:x for l,x in hit.items() if x}
    labs=sorted({y for x in hit.values() for y in x})
    print(f"{t}: {len(hit)}/21  {labs[:8]}")
