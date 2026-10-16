"""balance-02 part 1: merge multi-synonym gloss labels ("house, home") and rerun the concept ranking.

  direnv exec /home/agent/work/repos/universal-language python3 tests/balance-02/concepts_fix.py

Reads coverage-01 (gloss/freq files, merged.tsv, merged-add.tsv) and reuses balance-01's share code
(its functions that don't write). Writes only into tests/balance-02/. Method: README.md, part 1.
"""
import collections, math, os, re, sys
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
COV = os.path.join(REPO, "tests", "coverage-01")
P3 = os.path.join(COV, "part3")
sys.path.insert(0, os.path.join(REPO, "tests", "balance-01"))
import balance as B  # noqa: E402  (only read-only helpers are called)

REG, REGION, NLANG = B.REG, B.REGION, B.NLANG
FLOOR = 1e-7


def tsv_write(name, header, rows):
    with open(os.path.join(HERE, name), "w") as f:
        f.write("\t".join(header) + "\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")


def merged():
    """label -> (canonical, type, covered), first occurrence wins (as balance-01)."""
    m = {}
    for fn in ("merged.tsv", "merged-add.tsv"):
        for l in open(os.path.join(COV, fn), encoding="utf-8"):
            p = l.rstrip("\n").split("\t")
            if len(p) >= 5 and p[1] not in m:
                m[p[1]] = (p[2], p[3], p[4])
    return m


def parts(lab):
    out = []
    for x in lab.split(","):
        x = re.sub(r"^(to|a|an|the)\s+", "", x.strip()).strip(" .")
        if x and x not in out:
            out.append(x)
    return out


def target(lab, M, mode):
    """Where a label's weight goes: list of (label, fraction).

    mode 'orig': unchanged. 'head' (the fix): a comma label is split into its parts; parts that are merged
    labels are 'known'. If every known part has the same canonical concept the parts are synonyms and the
    weight goes to the first known part's label. If they have different canonicals (distinct senses by the
    merge's own judgement) the weight goes to the first known part only: the gloss's head word; later words
    are not merged into it and get nothing (sense check, added). 'split': distinct canonicals share the weight
    by gloss order, 1/(i+1) as concepts.py weights a word's senses (sensitivity, added).
    No known part: unchanged."""
    if mode == "orig" or "," not in lab:
        return [(lab, 1.0)]
    known = [p for p in parts(lab) if p in M]
    if not known:
        return [(lab, 1.0)]
    if mode == "head":
        return [(known[0], 1.0)]
    seen, heads = set(), []
    for p in known:
        if M[p][0] not in seen:
            seen.add(M[p][0]); heads.append(p)
    wt = [1 / (i + 1) for i in range(len(heads))]
    return [(p, w / sum(wt)) for p, w in zip(heads, wt)]


def remap(sh, M, mode):
    out = {}
    for c, s in sh.items():
        d = collections.Counter()
        for lab, v in s.items():
            for t, f in target(lab, M, mode):
                d[t] += v * f
        out[c] = d
    return out


def med(v):
    v = sorted(v)
    return (v[len(v) // 2] + v[(len(v) - 1) // 2]) / 2


def rank_labels(sh):
    labels = set().union(*[s.keys() for s in sh.values()])
    score = {k: med([math.log10(sh[c].get(k, 0) + FLOOR) for c in sh]) for k in labels}
    nl = {k: sum(1 for c in sh if sh[c].get(k, 0) > 0) for k in labels}
    ranked = sorted(labels, key=lambda k: (score[k], nl[k], k), reverse=True)  # as concepts.py build()
    return ranked, score, nl


def canon_rank(ranked, M):
    """Canonical content concepts by their best label's rank (how the merge ordered them)."""
    seen, order = set(), []
    for k in ranked:
        if k in M and M[k][1] == "content":
            cn = M[k][0]
            if cn not in seen:
                seen.add(cn); order.append((cn, k))
    return order


def canon_shares(sh, M):
    """Sensitivity (added): sum every merged label's share into its canonical before the median."""
    out = {}
    for c, s in sh.items():
        d = collections.Counter()
        for lab, v in s.items():
            d[("C:" + M[lab][0]) if lab in M and M[lab][1] == "content" else lab] += v
        out[c] = d
    return out


def list_status():
    """canonical -> where it stands today: root / list (roots-1500 or additions) / phrase / ladder note."""
    lex = {r["gloss"].strip().lower() for r in B.tsv_read(os.path.join(REPO, "data", "lexicon.tsv"))}
    comp = {r["gloss"].strip().lower(): r["form"] for r in B.tsv_read(os.path.join(REPO, "data", "compounds.tsv"))}
    r1500 = {l.strip() for l in open(os.path.join(COV, "part2b", "roots-1500.txt")) if l.strip()}
    adds = {r["concept"] for r in B.tsv_read(os.path.join(P3, "additions.tsv"))}
    lad = {}
    for r in B.tsv_read(os.path.join(P3, "ladder.tsv")):
        lad.setdefault(r["concept"], r["status"])
    return lex, comp, r1500, adds, lad


def main():
    M = merged()
    sh0 = B.shares()
    runs = {m: remap(sh0, M, m) for m in ("orig", "head", "split")}
    res = {m: rank_labels(s) for m, s in runs.items()}
    # check: orig reproduces concepts.tsv ordering for the top 4,000
    rec = [r["concept"] for r in B.tsv_read(os.path.join(COV, "concepts.tsv"))[:4000]]
    same = sum(1 for a, b in zip(rec, res["orig"][0][:4000]) if a == b)
    print(f"check: orig reproduces {same}/4000 of concepts.tsv top ranks")

    # concepts-fixed.tsv: the fix ('head'), same columns as concepts.tsv
    ranked, score, nl = res["head"]
    with open(os.path.join(HERE, "concepts-fixed.tsv"), "w") as f:
        f.write(f"rank\tconcept\tlanguages\tscore\t# balance-02 fix: comma labels merged (head rule)\n")
        for i, k in enumerate(ranked, 1):
            f.write(f"{i}\t{k}\t{nl[k]}\t{score[k]:.3f}\n")

    # how much weight moved, per region
    moved = []
    for c in B.COV_LANGS:
        cc = "tl" if c == "fil" else c
        s = sh0[cc]
        tot = sum(s.values())
        com = sum(v for k, v in s.items() if "," in k)
        kn = sum(v for k, v in s.items() if "," in k and any(p in M for p in parts(k)))
        moved.append([cc, REGION[cc], f"{com / tot:.3f}", f"{kn / tot:.3f}"])
    tsv_write("concepts-comma-weight.tsv", ["lang", "region", "share_in_comma_labels", "share_remapped"], moved)

    # canonical rankings
    cr = {m: canon_rank(res[m][0], M) for m in runs}
    # sensitivity: canonical-level summing on top of the fix
    shc = canon_shares(runs["head"], M)
    rc, scc, _ = rank_labels(shc)
    cr["canon"] = [(k[2:], k) for k in rc if k.startswith("C:")]
    pos = {m: {cn: i + 1 for i, (cn, _) in enumerate(o)} for m, o in cr.items()}

    out = {}
    base = [cn for cn, _ in cr["orig"]]
    for m in ("head", "split", "canon"):
        common = [cn for cn in base if cn in pos[m]]
        rho_all = B.spearman([pos["orig"][c] for c in common], [pos[m][c] for c in common])
        top = base[:1500]
        rho3 = B.spearman([pos["orig"][c] for c in top], [pos[m].get(c, 99999) for c in top])
        t0, t1 = set(base[:1500]), {cn for cn, _ in cr[m][:1500]}
        out[m] = (rho_all, rho3, len(t1 - t0), len(t0 - t1))
        print(f"{m}: spearman all canon {rho_all:.3f}, orig top3000 {rho3:.3f}; top-1500 in {len(t1 - t0)} out {len(t0 - t1)}")

    # regional correlation as balance-01, for orig and the fix
    status = B.concept_status()
    corr_rows = []
    for m in ("orig", "head"):
        sh = runs[m]
        ranked_m, score_m, _ = res[m]
        logs = lambda k: {c: math.log10(sh[c].get(k, 0) + FLOOR) for c in sh}
        # balance-01's order: score, then label (its tie-break; over half the top 3,000 tie at the floor)
        order = sorted(ranked_m, key=lambda k: (-score_m[k], k))
        top = [k for k in order if status.get(k, ("", ""))[1] not in ("grammar", "other")][:3000]
        L = {k: logs(k) for k in top}
        gs = [score_m[k] for k in top]
        lang = {c: B.spearman([L[k][c] for k in top], gs) for c in sh}
        for g in REG:
            rs = B.spearman([sum(L[k][c] for c in sh if REGION[c] == g) / NLANG[g] for k in top], gs)
            lc = [lang[c] for c in sh if REGION[c] == g]
            rest = [c for c in sh if REGION[c] != g]
            loo = B.spearman([med([L[k][c] for c in rest]) for k in top], gs)
            corr_rows.append([m, g, f"{rs:.3f}", f"{sum(lc) / len(lc):.3f}",
                              " ".join(f"{c}:{lang[c]:.2f}" for c in sh if REGION[c] == g), f"{loo:.4f}"])
    tsv_write("concepts-correlation.tsv", ["run", "region", "spearman_region_mean_vs_final",
                                           "mean_spearman_of_its_languages", "per_language",
                                           "spearman_final_without_region"], corr_rows)

    # region top-1000 below-cut counts, as balance-01 (labels never reached the merge)
    top_rows = []
    for m in ("orig", "head"):
        sh = runs[m]
        labels = set().union(*[s.keys() for s in sh.values()])
        for g in REG:
            rs = {k: sum(math.log10(sh[c].get(k, 0) + FLOOR) for c in sh if REGION[c] == g) / NLANG[g] for k in labels}
            cnt, n = collections.Counter(), 0
            for k in sorted(labels, key=lambda k: -rs[k]):
                s = status.get(k, (k, "below_cut"))[1]
                if s in ("grammar", "other"):
                    continue
                n += 1; cnt[s] += 1
                if s == "below_cut" and "," in k:
                    cnt["comma"] += 1
                if n == 1000:
                    break
            mn = cnt["root"] + cnt["phrase"] + cnt["missing"]
            top_rows.append([m, g, cnt["root"], cnt["phrase"], cnt["missing"], cnt["below_cut"], cnt["comma"],
                             f"{cnt['missing'] / mn:.3f}"])
    tsv_write("concepts-region-top.tsv", ["run", "region", "on_list_root", "covered_by_phrase",
                                          "content_not_on_list", "below_merge_cut", "below_cut_multi_synonym",
                                          "share_missing_of_merged"], top_rows)

    # entrants and leavers of the ~1,500 list's frequency segment, rebuilt the way part2b built it:
    # roots-1500.txt = 235 first-word (deep-layer) concepts, then the first 748 canonicals in rank order with
    # no root covering them (phrase-only counts as uncovered). Rebuilding the original this way gives 739 of 748.
    lex, comp, r1500, adds, lad = list_status()
    lexf = {r["form"] for r in B.tsv_read(os.path.join(REPO, "data", "lexicon.tsv"))}
    L = [l.strip() for l in open(os.path.join(COV, "part2b", "roots-1500.txt")) if l.strip()]
    deep = set(L[:235])
    canon_cover = {}
    for lab, (cn, ty, cov) in M.items():
        if ty == "content":
            canon_cover.setdefault(cn, cov)
    def uncovered(cn):
        fs = [x.strip() for x in canon_cover.get(cn, "none").split(",")]
        return not any(" " not in f and f in lexf for f in fs)
    seg = {m: [cn for cn, _ in cr[m] if cn not in deep and uncovered(cn)][:748] for m in cr}
    print("rebuilt original segment matches roots-1500:", len(set(seg["orig"]) & set(L[235:])), "of 748")
    def where(cn):
        if cn in adds: return "on list (additions.tsv)"
        if cn in r1500: return "on list (roots-1500)"
        st = lad.get(cn, "")
        if st.startswith("covered") or st.startswith("merge"): return f"ladder {st}"
        if cn in comp: return f"phrase {comp[cn]}"
        cov = canon_cover.get(cn, "none")
        if cov != "none": return f"phrase {cov}"
        return "not on list"
    rows = []
    for m in ("head", "split", "canon"):
        a, b = set(seg["orig"]), set(seg[m])
        for cn in sorted(b - a, key=lambda c: pos[m][c]):
            rows.append([m, "enters", cn, pos["orig"].get(cn, "-"), pos[m][cn], where(cn)])
        for cn in sorted(a - b, key=lambda c: pos["orig"][c]):
            rows.append([m, "leaves", cn, pos["orig"][cn], pos[m].get(cn, "-"), where(cn)])
        out[m] = out[m] + (len(b - a), len(a - b))
    tsv_write("concepts-list-changes.tsv", ["run", "change", "canonical", "canon_rank_orig", "canon_rank_new",
                                            "status_today"], rows)
    tsv_write("concepts-summary.tsv", ["run", "spearman_all_canonicals", "spearman_orig_top1500",
                                       "enter_first1500_canonicals", "leave_first1500_canonicals",
                                       "enter_list_segment", "leave_list_segment"],
              [[m, f"{v[0]:.3f}", f"{v[1]:.3f}", *v[2:]] for m, v in out.items()])
    for r in corr_rows: print(r)
    for r in top_rows: print(r)


if __name__ == "__main__":
    main()
