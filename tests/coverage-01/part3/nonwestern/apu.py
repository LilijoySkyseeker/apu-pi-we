import sys,re,os
R="/home/agent/work/repos/universal-language/"
F={"lex":"data/lexicon.tsv","cmp":"data/compounds.tsv","r1500":"tests/coverage-01/part2b/roots-1500.txt","ladder":"tests/coverage-01/part3/ladder.tsv","wbf":"tests/coverage-01/part3/wordbank-final.tsv","rel":"tests/coverage-01/part3/religion.tsv","add":"tests/coverage-01/part3/additions.tsv","loan":"tests/coverage-01/part3/loans-final.tsv"}
L={k:[l.split("\t") for l in open(R+p,encoding="utf-8").read().splitlines()] for k,p in F.items()}
# which column holds the concept, which the status
KC={"lex":(0,3),"cmp":(0,1),"r1500":(0,None),"ladder":(1,2),"wbf":(1,2),"rel":(1,2),"add":(0,None),"loan":(0,2)}
def look(t):
    rx=re.compile(r"(^|[ ,;(/])"+re.escape(t.lower())+r"(s|es)?($|[ ,;)/])")
    out=[]
    for k,rows in L.items():
        c,s=KC[k]
        for cols in (rows if k=="r1500" else rows[1:]):
            if len(cols)<=c: continue
            if rx.search(cols[c].lower()):
                out.append(f"{k}:{cols[c]}" + (f"={cols[s]}" if s is not None and len(cols)>s else ""))
    return out
if __name__=="__main__":
    for t in sys.argv[1:]: print(f"{t}: {look(t)[:7]}")
