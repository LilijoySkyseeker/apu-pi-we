import sys,re,pickle,collections; sys.path.insert(0,'/tmp/nw'); from load import *
from apu import look
U,G=langsets()
def strip(x): return re.sub(r"\([^)]*\)","",x).replace("_"," ").strip()
def sing(x): return re.sub(r"(es|s)$","",x)
LAB={l:{sing(strip(y)) for y in (U[l]|G[l])} for l in EU}
def eucount(keys):
    ks={sing(strip(k)) for k in keys if k}
    ks={k for k in ks if k}
    return sum(1 for l in EU if ks & LAB[l]) if ks else -1
KEEP={'action_words','food_drink','descriptive_words','games_routines','household','animals','people','outside','clothing','toys','furniture_rooms','places','time_words','body_parts','vehicles','others','descriptive_words (adjectives)','descriptive_words (adverbs)','sounds2'}
agg=collections.defaultdict(lambda:{'langs':set(),'eu':99,'cat':collections.Counter(),'ex':[]})
for l in sorted(NONEU):
    for f in LANG[l]:
        for r in rows(f):
            cat=r["category"]
            if cat not in KEEP: continue
            u=norm(v(r,"uni_lemma")); g=norm(v(r,"gloss")); d=v(r,"definition") or v(r,"item")
            if l=="Japanese": d=v(r,"definition")
            eu=eucount([u,g] + [p for p in re.split(r"[/\\,;]",g)])
            if eu>5: continue
            key=strip(u or g) or ('?'+d)
            a=agg[key]; a['langs'].add(l); a['eu']=min(a['eu'],eu); a['cat'][cat]+=1; a['ex'].append(d+(f"[{g}]" if g and strip(g)!=key else ""))
AB={"Cantonese":"Can","Hebrew":"Heb","Japanese":"Jpn","Kigiriama":"Kig","Kiswahili":"Swa","Korean":"Kor","Mandarin":"Cmn","Persian":"Fas","Turkish":"Tur","Arabic":"Ara"}
with open('/tmp/nw/draft.tsv','w') as o:
    for k,a in sorted(agg.items(),key=lambda x:(x[1]['cat'].most_common(1)[0][0],-len(x[1]['langs']),x[0])):
        o.write("\t".join([k,a['cat'].most_common(1)[0][0],",".join(AB[x] for x in sorted(a['langs'])),str(a['eu']),"; ".join(look(k)[:4]) if not k.startswith('?') else "", " | ".join(a['ex'][:4])])+"\n")
