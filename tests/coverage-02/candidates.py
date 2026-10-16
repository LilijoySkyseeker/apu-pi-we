"""coverage-02: the corrected canonical ranking with each concept's status on today's list.

  direnv exec /home/agent/work/repos/universal-language python3 tests/coverage-02/candidates.py

Recomputes balance-02's head-rule ranking (concepts_fix.py, read-only helpers), ranks canonical content
concepts by their best label, and marks what today's list already says about each. Writes candidates.tsv here.
"""
import os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tests", "balance-02"))
import concepts_fix as F  # noqa: E402
B = F.B
COV, P3 = F.COV, F.P3


def rd(p):
    return B.tsv_read(p)


def main():
    M = F.merged()
    sh = F.remap(B.shares(), M, "head")
    ranked, score, nl = F.rank_labels(sh)
    order = F.canon_rank(ranked, M)
    lexrows = rd(os.path.join(REPO, "data", "lexicon.tsv"))
    lexf = {r["form"]: r["gloss"] for r in lexrows}
    lexg = {}
    for r in lexrows:
        for g in r["gloss"].split(","):
            lexg.setdefault(g.strip().lower(), r["form"])
    comp = {}
    for r in rd(os.path.join(REPO, "data", "compounds.tsv")):
        for g in r["gloss"].split(","):
            comp.setdefault(g.strip().lower(), r["form"])
    L = [l.strip() for l in open(os.path.join(COV, "part2b", "roots-1500.txt")) if l.strip()]
    deep, r1500 = set(L[:235]), set(L)
    adds = {r["concept"] for r in rd(os.path.join(P3, "additions.tsv"))}
    lad = {}
    for r in rd(os.path.join(P3, "ladder.tsv")):
        lad.setdefault(r["concept"], (r["status"], r["route"], r["note"]))
    rel = {r["concept"]: r["class"] + " " + r["note"] for r in rd(os.path.join(P3, "religion.tsv"))}
    loans = {r["concept"]: r["verdict"] + " " + r["adapted"] for r in rd(os.path.join(P3, "loans-final.tsv"))}
    ent = {r["canonical"]: r["judgement"] for r in rd(os.path.join(REPO, "tests", "balance-02", "concepts-entrants.tsv"))}
    cover = {}
    for lab, (cn, ty, cov) in M.items():
        if ty == "content":
            cover.setdefault(cn, cov)
    notes = {}
    for fn in ("merged.tsv", "merged-add.tsv"):
        for l in open(os.path.join(COV, fn), encoding="utf-8"):
            p = l.rstrip("\n").split("\t")
            if len(p) >= 6 and p[2] not in notes and p[5]:
                notes[p[2]] = p[5]

    def rooted(cn):
        fs = [x.strip() for x in cover.get(cn, "none").split(",")]
        return [f for f in fs if " " not in f and f in lexf]

    out = []
    seg_n = 0
    for i, (cn, lab) in enumerate(order, 1):
        st = []
        if cn in adds: st.append("additions")
        if cn in r1500: st.append("roots-1500" + (" deep" if cn in deep else ""))
        if cn in lad: st.append("ladder:" + "/".join(x for x in lad[cn][:2] if x))
        if cn in loans: st.append("loan:" + loans[cn])
        if cn in rel: st.append("religion:" + rel[cn])
        if cn in ent: st.append("entrant:" + ent[cn])
        rf = rooted(cn)
        if rf: st.append("root:" + "+".join(rf))
        elif cover.get(cn, "none") != "none": st.append("cover:" + cover[cn])
        if cn in lexg and not rf: st.append("lexgloss:" + lexg[cn])
        if cn in comp: st.append("compound:" + comp[cn])
        if cn not in deep and not rf:
            seg_n += 1
        out.append([i, cn, lab, nl[lab], f"{score[lab]:.3f}", seg_n if (cn not in deep and not rf) else "",
                    "; ".join(st), notes.get(cn, "")])
    with open(os.path.join(HERE, "candidates.tsv"), "w") as f:
        f.write("crank\tcanonical\tbest_label\tlanguages\tscore\tuncovered_n\tstatus\tmerge_note\n")
        for r in out:
            f.write("\t".join(str(x) for x in r) + "\n")
    print(len(out), "canonicals; uncovered (non-deep, no root):", seg_n)


if __name__ == "__main__":
    main()
