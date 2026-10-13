"""Which memory-only columns decide a loan's verdict? (author, 2026-10-13: count everyday loans beside a
formal word, with a source; check the deciding memory columns.)

A column counts when it is cognate (y) or an everyday loan beside a formal word (b), and it is attested:
its source includes Wiktionary (Wt, We, M*) or a verification in verified.tsv. A column sourced from memory
alone (M) is unattested until verified. A candidate passes with at least 12 counted columns across at
least 4 of the 7 regions.

  python3 deciding.py            # verdicts now, and the memory columns that decide them -> deciding.tsv
"""
import csv, glob, os, sys
sys.argv += [] ; HERE = os.path.dirname(os.path.abspath(__file__))
import importlib.util
spec = importlib.util.spec_from_file_location("emit", os.path.join(HERE, "emit.py"))
emit = importlib.util.module_from_spec(spec)
_cwd = os.getcwd(); spec.loader.exec_module(emit); os.chdir(_cwd)
REGION = {c: r for c, _, r in emit.LANGS}


def verified():
    p = os.path.join(HERE, "verified.tsv")
    out = {}
    if os.path.exists(p):
        for r in csv.DictReader(open(p), delimiter="\t"):
            out[(r["concept"], r["lang"])] = r["result"] == "yes"
    return out


def counts(item, use_memory, ver):
    n, regs = 0, set()
    for code, (word, mark, src) in item["rows"].items():
        if mark not in ("y", "b"):
            continue
        memory_only = not any(s in src for s in ("Wt", "We", "M*"))
        if memory_only:
            v = ver.get((item["concept"], code))
            if v is False or (v is None and not use_memory):
                continue
        n += 1; regs.add(REGION[code])
    return n, len(regs)


def verdict(n, r):
    return "pass" if n >= 12 and r >= 4 else "fail"


def main():
    items = []
    for f in sorted(glob.glob(os.path.join(HERE, "c[0-9][0-9].txt"))):
        items += emit.parse(f)
    ver = verified()
    rows, todo = [], []
    for it in items:
        hi = counts(it, True, ver); lo = counts(it, False, ver)
        vh, vl = verdict(*hi), verdict(*lo)
        state = vh if vh == vl else "depends on memory"
        rows.append((it["concept"], hi, lo, state))
        if vh != vl:
            for code, (word, mark, src) in it["rows"].items():
                if mark in ("y", "b") and not any(s in src for s in ("Wt", "We", "M*")) and (it["concept"], code) not in ver:
                    todo.append((it["concept"], code, word))
    with open(os.path.join(HERE, "deciding.tsv"), "w") as f:
        f.write("concept\tlang\tclaimed\n")
        for c, l, w in todo:
            f.write(f"{c}\t{l}\t{w}\n")
    from collections import Counter
    print(Counter(s for *_, s in rows))
    print(len(todo), "memory columns decide a verdict; by language:", Counter(l for _, l, _ in todo))
    with open(os.path.join(HERE, "verdicts.tsv"), "w") as f:
        f.write("concept\twith_memory\twithout_memory\tstate\n")
        for c, hi, lo, s in rows:
            f.write(f"{c}\t{hi[0]}/{hi[1]}\t{lo[0]}/{lo[1]}\t{s}\n")


if __name__ == "__main__":
    main()
