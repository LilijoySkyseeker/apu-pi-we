"""Median Zipf frequency per grammar meaning from a table of everyday equivalents (15 languages).

The original frequency.tsv was made this way (design log, grammar rebuild: "median Zipf from wordfreq")
but its script wasn't kept; this one is checked against it first (`check`), then applied to the
Codex table (`compare`).

  python3 zipf.py check                 # recompute from ../equivalents.tsv, compare with ../frequency.tsv
  python3 zipf.py compare FILE          # median Zipf for FILE vs the original; rank comparison
"""
import csv, math, os, statistics, sys
import wordfreq

_DICT = {}


def zipf(w, lang):
    """wordfreq's Zipf; Japanese and Korean looked up in the frequency list directly (their tokenizers need MeCab dictionaries,
    which isn't installed; the coverage work did the same)."""
    if lang not in ("ja", "ko"):
        return wordfreq.zipf_frequency(w, lang)
    if lang not in _DICT:
        _DICT[lang] = wordfreq.get_frequency_dict(lang)
    f = _DICT[lang].get(w, 0.0)
    return round(math.log10(f * 1e9), 2) if f > 0 else 0.0

HERE = os.path.dirname(os.path.abspath(__file__))
UP = os.path.join(HERE, "..")


def table(path):
    """Rows as dicts; the first column is renamed "key" (the header has "id" twice: the row id and
    Indonesian)."""
    rows = list(csv.reader(open(path), delimiter="\t"))
    head = ["key"] + rows[0][1:]
    return [dict(zip(head, r)) for r in rows[1:] if r]


def medians(rows):
    out = {}
    for r in rows:
        zs = []
        for lang, w in r.items():
            if lang == "key" or not w or w.strip() in ("-", ""):
                continue
            w = w.strip().split("/")[0].strip()
            z = zipf(w, lang)
            if z > 0:
                zs.append(z)
        out[r["key"]] = (statistics.median(zs) if zs else 0.0, len(zs))
    return out


def ranks(d):
    order = sorted(d, key=lambda k: -d[k])
    return {k: i + 1 for i, k in enumerate(order)}


def spearman(a, b):
    ks = [k for k in a if k in b]
    ra, rb = ranks({k: a[k] for k in ks}), ranks({k: b[k] for k in ks})
    n = len(ks)
    return 1 - 6 * sum((ra[k] - rb[k]) ** 2 for k in ks) / (n * (n * n - 1))


if __name__ == "__main__":
    orig = {r["key"]: float(r["median_zipf"] or 0) for r in table(os.path.join(UP, "frequency.tsv"))}
    form = {r["key"]: r["form"] for r in table(os.path.join(UP, "frequency.tsv"))}
    if sys.argv[1] == "check":
        mine = {k: v for k, (v, _) in medians(table(os.path.join(UP, "equivalents.tsv"))).items()}
        diff = [(k, orig[k], mine.get(k)) for k in orig if abs(orig[k] - mine.get(k, 0)) > 0.05]
        print(f"rows {len(orig)}; differing by > 0.05: {len(diff)}; Spearman {spearman(orig, mine):.3f}")
        for d in diff[:10]:
            print("  ", d)
    else:
        cod = medians(table(sys.argv[2]))
        new = {k: v for k, (v, _) in cod.items()}
        mine = {k: v for k, (v, _) in medians(table(os.path.join(UP, "equivalents.tsv"))).items()}
        print(f"Spearman, all {len(new)} meanings: original vs Codex {spearman(mine, new):.3f}")
        ro, rn = ranks(mine), ranks(new)
        top = sorted(mine, key=lambda k: -mine[k])[:20]
        print(f"top 20 by the original: Spearman {spearman({k: mine[k] for k in top}, {k: new[k] for k in top}):.3f}")
        print("id\tform\torig_zipf\tcodex_zipf\torig_rank\tcodex_rank\tcodex_langs")
        for k in sorted(mine, key=lambda k: -mine[k]):
            print(f"{k}\t{form.get(k, '')}\t{mine[k]:.2f}\t{new.get(k, 0):.2f}\t{ro[k]}\t{rn.get(k, '')}\t{cod.get(k, (0, 0))[1]}")
