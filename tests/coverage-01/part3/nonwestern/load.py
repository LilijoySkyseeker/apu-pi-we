import csv, glob, os, collections
D=os.path.expanduser("~/work/cache/coverage/wordbank")
LANG={}
for f in sorted(glob.glob(D+"/*.csv")):
    n=os.path.basename(f)[:-7]
    lang=n.split("_")[0]
    if lang=="Greek": lang="Greek"
    LANG.setdefault(lang,[]).append(f)
NONEU={"Arabic","Cantonese","Hebrew","Japanese","Kigiriama","Kiswahili","Korean","Mandarin","Persian","Turkish"}
def rows(f):
    return [r for r in csv.DictReader(open(f,encoding="utf-8")) if r["type"]=="word"]

def rows(f):
    out={}
    for r in csv.DictReader(open(f,encoding="utf-8-sig")):
        if r.get("type")!="word": continue
        k=r["itemID"]
        if k in out and out[k].get("gloss") not in (None,"NA",""): continue
        out[k]=r
    return list(out.values())
def v(r,k):
    x=(r.get(k) or "").strip()
    return "" if x in ("NA",) else x
import re
def norm(s):
    s=s.lower().strip()
    s=re.sub(r"\s+"," ",s)
    return s
EU={l for l in LANG if l not in NONEU and l not in ()}
def langsets():
    U={};G={}
    for l,fs in LANG.items():
        U[l]=set();G[l]=set()
        for f in fs:
            for r in rows(f):
                if v(r,"uni_lemma"): U[l].add(norm(v(r,"uni_lemma")))
                if v(r,"gloss"):
                    g=norm(v(r,"gloss")); G[l].add(g)
                    for p in re.split(r"[/,;]| \(",g): G[l].add(p.strip(" )"))
    return U,G
