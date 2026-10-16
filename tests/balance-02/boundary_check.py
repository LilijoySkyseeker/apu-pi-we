"""balance-02 part 2: the boundary pairs split against a Persian or Turkish lump, re-read.

  direnv exec /home/agent/work/repos/universal-language python3 tests/balance-02/boundary_check.py

Runs coverage-01/part3/boundary.py's own functions (unchanged) per language, twice: as recorded, and with
multi-synonym sense labels split into their parts (part 1's defect: "leg, the lower limb ..." never matched
"leg", so Turkish bacak was invisible). Prints every language's words so the readings can be checked by eye,
and writes boundaries-recheck.tsv. Writes only into tests/balance-02/.
"""
import importlib.util, os, re, sys
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
spec = importlib.util.spec_from_file_location("boundary", os.path.join(REPO, "tests", "coverage-01", "part3", "boundary.py"))
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)

PAIRS = ["moon|month", "day|daytime", "hear|listen", "take|get", "arm|hand", "ghost|spirit", "leg|foot"]


def split_senses(senses):
    out = {}
    for w, labs in senses.items():
        new = []
        for lab in labs:
            for p in lab.split(","):
                p = re.sub(r"^(to|a|an|the)\s+", "", p.strip()).strip(" .")
                if p and p not in new:
                    new.append(p)
        out[w] = new
    return out


def classify(a, bb, fr, senses):
    wa, wb = b.words_for(a, fr, senses), b.words_for(bb, fr, senses)
    if not wa or not wb:
        return "nodata", wa, wb, ""
    both = [w for w, _ in wa if w in {x for x, _ in wb}]
    only_a = [(w, f) for w, f in wa if w not in both]
    only_b = [(w, f) for w, f in wb if w not in both]
    if wa[0][0] in both or wb[0][0] in both:
        fl = max(f for w, f in wa + wb if w in both)
        sep = [(w, f / fl) for w, f in (only_a[:1] + only_b[:1]) if f / fl >= 0.1]
        return ("lump+sep" if sep else "lump"), wa, wb, ", ".join(f"{w} {r:.0%}" for w, r in sep)
    return "split", wa, wb, ""


def main():
    rows = []
    data = {c: b.load(c) for c in b.LANGS}
    for pair in PAIRS:
        a, bb = pair.split("|")
        print(f"\n== {pair}")
        for c in b.LANGS:
            fr, senses = data[c]
            s0 = classify(a, bb, fr, senses)
            s1 = classify(a, bb, fr, split_senses(senses))
            code = "tl" if c == "fil" else c
            flag = "" if s0[0] == s1[0] else "  <- changed"
            print(f"  {code:3} {s0[0]:8} -> {s1[0]:8} {a}: {', '.join(w for w, _ in s1[1][:3])} | "
                  f"{bb}: {', '.join(w for w, _ in s1[2][:3])}  {s1[3]}{flag}")
            rows.append([pair, code, s0[0], s1[0], " ".join(w for w, _ in s1[1][:3]), " ".join(w for w, _ in s1[2][:3]),
                         s1[3] or "-"])
    with open(os.path.join(HERE, "boundaries-recheck.tsv"), "w") as f:
        f.write("pair\tlang\tscript_as_recorded\tscript_comma_split\twords_a\twords_b\tseparate_word\n")
        for r in rows:
            f.write("\t".join(r) + "\n")


if __name__ == "__main__":
    main()
