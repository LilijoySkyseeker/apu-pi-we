"""Format one chunk of hand-made panel judgments into loans.tsv rows and loans.md sections."""
import os, re, sys, urllib.parse
REPO = "/home/agent/work/repos/universal-language"
sys.path.insert(0, REPO + "/tools")
os.chdir(REPO + "/tools")
import names, words as W
OUT = REPO + "/tests/coverage-01/part3/"
TSV, MD = OUT + "loans.tsv", OUT + "loans.md"
LANGS = [("zh","Mandarin","EA"),("ja","Japanese","EA"),("ko","Korean","EA"),("vi","Vietnamese","SEA"),("th","Thai","SEA"),
 ("id","Indonesian","SEA"),("tl","Tagalog","SEA"),("hi","Hindi","SA"),("bn","Bengali","SA"),("ta","Tamil","SA"),
 ("fa","Persian","WA"),("ar","Arabic","WA"),("tr","Turkish","WA"),("ru","Russian","EU"),("es","Spanish","EU"),
 ("fr","French","EU"),("sw","Swahili","SSA"),("ha","Hausa","SSA"),("yo","Yoruba","SSA"),("qu","Quechua","AM")]
REG = ["EA","SEA","SA","WA","EU","SSA","AM"]

def parse(path):
    items, cur = [], None
    for line in open(path):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        if line.startswith("@ "):
            concept, page, sense = [x.strip() for x in line[2:].split("|", 2)]
            cur = dict(concept=concept, page=page, sense=sense, rows={}, median="", note="", text=[], verdict="")
            items.append(cur); continue
        m = re.match(r"(median|note|verdict|text):\s?(.*)", line)
        if m:
            k, v = m.groups()
            if k == "text": cur["text"].append(v)
            else: cur[k] = v
            continue
        code, rest = line.split(" ", 1)
        word, mark, src = [x.strip() for x in rest.rsplit("|", 2)]
        assert mark in ("y","n","b"), line
        assert code in dict((c,1) for c,_,_ in LANGS), line
        cur["rows"][code] = (word, mark, src)
    for it in items:
        missing = [c for c,_,_ in LANGS if c not in it["rows"]]
        assert not missing, (it["concept"], missing)
    return items

def score(it):
    reg = {c: r for c,_,r in LANGS}
    s = [c for c,(w,m,_) in it["rows"].items() if m == "y"]
    l = [c for c,(w,m,_) in it["rows"].items() if m in "yb"]
    rs = sorted({reg[c] for c in s}, key=REG.index); rl = sorted({reg[c] for c in l}, key=REG.index)
    ok = lambda n, r: n >= 12 and len(r) >= 4
    v = "pass" if ok(len(s), rs) else ("borderline" if ok(len(l), rl) else "fail")
    soft = any("M" in it["rows"][c][2] for c in s)
    if v == "pass" and (len(s) == 12 or len(rs) == 4) and soft:
        v = "pass, borderline"
    return len(s), rs, len(l), rl, it["verdict"] or v

def regtext(r):
    if len(r) == 7: return "all 7"
    missing = [x for x in REG if x not in r]
    return f"{len(r)} (no {' '.join(missing)})" if len(r) >= 4 else f"{len(r)} ({' '.join(r)})"

def done():
    if not os.path.exists(TSV): return []
    return [l.split("\t")[0] for l in open(TSV).read().splitlines()[1:]]

def main(paths):
    items = [it for p in paths for it in parse(p)]
    have = set()
    open(TSV, "w").write("concept\tcognates\tregions\tverdict\tmedian_ipa\tadapted\tnote\n")
    head = open(MD).read().split("\n### ", 1)[0]
    open(MD, "w").write(head.rstrip("\n") + "\n")
    tsv, md = [], []
    for it in items:
        if it["concept"] in have:
            print("skip", it["concept"]); continue
        s, rs, l, rl, v = score(it)
        ad = ""
        if it["median"]:
            ad = names.adapt(it["median"].replace(" ", "")); W.split(ad)
        cog = f"{s}/20" + (f" ({l} lenient)" if l != s else "")
        rg = regtext(rs) + (f" ({len(rl)} lenient)" if len(rl) != len(rs) else "")
        tsv.append("\t".join([it["concept"], cog, rg, v, f"[{it['median']}]" if it["median"] else "", ad, it["note"]]))
        page = it["page"]
        url = "https://en.wiktionary.org/wiki/" + urllib.parse.quote(page.replace(" ", "_")) + "#Translations"
        sec = [f"### {it['concept']} (Wt: [{page}]({url}), \"{it['sense']}\")", "| Lang | Everyday word | Shared | src |", "|---|---|---|---|"]
        for c, name, _ in LANGS:
            w, m, src = it["rows"][c]
            sec.append(f"| {name} | {w} | {dict(y='✓', n='✗', b='✗ (✓ lenient)')[m]} | {src} |")
        line = f"**{cog}; regions {rg} → {v}.**"
        if it["median"]:
            line += f" Median [{it['median']}] → *{ad}*."
        sec += ["", line]
        if it["text"]:
            sec += [" ".join(it["text"])]
        md.append("\n".join(sec) + "\n")
        print(f"{it['concept']:22} {cog:16} {rg:22} {v:12} {it['median']:14} {ad}")
    open(TSV, "a").write("".join(r + "\n" for r in tsv))
    open(MD, "a").write("".join("\n" + s for s in md))

if __name__ == "__main__":
    main(sys.argv[1:])
