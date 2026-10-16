"""Regional-balance audit (balance-01): counts only, from files already in the repo.

  direnv exec /home/agent/work/repos/universal-language python3 tests/balance-01/balance.py

Writes the TSV tables next to this file and prints the headline numbers. Reads, never writes, anything
outside tests/balance-01/. Method and sources: README.md.
"""
import collections, csv, glob, importlib.util, math, os, pickle, sys
sys.dont_write_bytecode = True  # leave no caches outside this folder

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
COV = os.path.join(REPO, "tests", "coverage-01")
P3 = os.path.join(COV, "part3")
LW = os.path.join(P3, "loanwork")

REG = ["EA", "SEA", "SA", "WA", "EU", "SSA", "AM"]
REGION = {"zh": "EA", "ja": "EA", "ko": "EA", "vi": "SEA", "th": "SEA", "id": "SEA", "tl": "SEA",
          "hi": "SA", "bn": "SA", "ta": "SA", "fa": "WA", "ar": "WA", "tr": "WA", "ru": "EU", "es": "EU",
          "fr": "EU", "sw": "SSA", "ha": "SSA", "yo": "SSA", "qu": "AM"}
NLANG = collections.Counter(REGION.values())  # languages per region: 3 4 3 3 3 3 1


def tsv_write(name, header, rows):
    with open(os.path.join(HERE, name), "w") as f:
        f.write("\t".join(header) + "\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")


def tsv_read(path):
    return list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"))


def spearman(xs, ys):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2
            i = j + 1
        return r
    a, b = ranks(xs), ranks(ys)
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
    return num / den


# ---------------------------------------------------------------- 1. loans

def load_emit():
    cwd = os.getcwd()
    spec = importlib.util.spec_from_file_location("emit", os.path.join(LW, "emit.py"))
    emit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(emit)  # emit.py chdirs to tools/ on import
    os.chdir(cwd)
    return emit


# Two-shape rule (author, 2026-10-13): columns of the other shape don't count. Recorded in
# loans-final.tsv only as a note, so the columns are listed here from the entries' own text.
SHAPE_DROP = {"sauce": {"tl", "ar", "es", "qu"},                 # salsa form (loans.md, sauce)
              "channel": {"id", "fa", "tr", "ru", "es", "qu"}}   # kanal form (loans.md, channel)

# Median shape: which languages' variant won where the entry records a contested position.
# My reading of each entry's "text"/"note" lines (added). W = languages whose variant the median took,
# L = languages whose variant lost. Entries whose text names no languages are left out.
MEDIAN = {
    "chocolate": [("vi id tl fa ar tr ru es fr", "ja hi bn ta sw yo th"), ("", "fa ar ru fr yo vi")],
    "doctor": [("tl fa ar tr ru es", "hi bn ta sw")],
    "motorcycle": [("", "id tl hi bn fa")],
    "coffee": [("zh vi th tl ru es fr qu", "ja ko id hi bn ta ha yo")],
    "sweater": [("id tl hi bn ta ar ru", "")],
    "pajamas": [("id fa ar tr ru es fr qu", "ja tl hi bn ta"), ("ja tl hi bn ta ar", "fa tr ru fr es qu id")],
    "radio": [("ja ko vi id tl fa ar tr ru es fr qu", "hi bn sw ha yo")],
    "helicopter": [("id tl fa tr es fr", "ja ko th hi bn sw")],
    "tractor": [("ja ko th hi bn ta sw ha", "id fa ru es qu")],
    "tomato": [("es qu tr", "ja ko bn ar ha yo")],
    "tea": [("hi fa ar tr ru sw ha", "zh ja ko vi th tl bn"), ("", "ar ha"), ("", "id ta es fr yo qu")],
    "garage": [("fa ar tr ru fr", "ja hi bn sw")],
    "cookie": [("", "ja ko th tl")],
    "sandwich": [("th tl es fr sw ar", "hi ta tr fa")],
    "pizza": [("th tl bn ta fa ar tr ru fr", "ja ko id hi sw")],
    "sauce": [("", "tl ar es qu")],
    "balcony": [("", "ja ko bn ta")],
    "circus": [("vi id tl fa ar tr ru es fr qu", "ja ko hi bn sw")],
    "T-shirt": [("ja hi bn", "fa sw tr fr")],
    "video": [("vi id tl tr ru es fr qu", "th hi bn ta fa ar ha yo")],
    "bank": [("ta sw ha yo tl es qu tr", "id hi bn fa ar ru fr")],
    "program": [("th id hi bn tr fr ko", "tl ru es qu ja sw")],
    "technology": [("hi ar tr sw", "tl es qu fa fr id ru"), ("th id hi fa tr fr", "tl ar ru es sw qu")],
    "computer": [("ja th id tl es sw yo", "hi bn ta fa ar ru ha")],
    "machine": [("bn fa ru fr sw ha", "tl ar tr es qu")],
    "beer": [("vi th hi bn ta sw yo", ""), ("", "vi th sw yo")],
    "website": [("ja ko th tl hi bn ru", "id tr es fr")],
    "bomb": [("tl tr ru es qu", "yo fa fr")],
    "model": [("ko id hi bn fa tr ru fr", "tl es qu")],
    "virus": [("", "ko th hi bn")],
    "league": [("id tl ru es qu ja ko sw", "th hi bn ta fa tr fr")],
    "album": [("ja id tl ar es fr qu tr", "ko th hi bn ta sw vi fa ru")],
    "cigarette": [("hi bn ta fa ru fr", "ar tr sw")],
    "club": [("ja tl hi bn sw vi", "id ru es qu tr")],
    "gas": [("ko th id tl hi bn es sw ha yo qu", "fa ar tr ru fr")],
    "gene": [("zh hi bn ar sw", "id tr ru vi fa fr tl es qu")],
    "engineer": [("ja ko hi sw ha yo", "")],
    "studio": [("", "tl fa ar es qu")],
    "medal": [("tl ar tr es qu", "")],
    "mask": [("ru tl es qu", "")],
    "dollar": [("id tl hi bn ta fa ar tr ru es fr qu", "ja ko vi th sw ha yo")],
    "internet": [("id tl fa tr ru es fr qu", "ja hi bn ar sw ha")],
    "email": [("ko tl bn fa ar tr ru es sw", "th id hi fr ha")],
    "battery": [("ko th bn ta ar tr ru", "ja id tl es")],
    "euro": [("ja ko th hi bn fa ar ru yo", "vi id tl tr es fr sw")],
    "rupee": [("tl hi ta fa ar ru es sw", "zh ja ko vi th id tr fr")],
    "hashtag": [("", "ko th ru")],
}

# Lexicon loans with no panel file under the 2026-10-13 rules. Columns as recorded:
#  kilometre: tests/lexicon-ladder-01/loans.md table (zh ✗; ha, qu from memory).
#  kilo: design log 2026-10-13 "kilo is the everyday word for kilogram" (12 languages named).
#  metre, centimetre, millimetre, gram, kilogram, litre: metric-panel.txt lists the Wiktionary forms but
#  no ✓/✗; my reading (added): every listed form is the international word except Mandarin 米/克/升/毫米
#  (other shapes) and the Tagalog/Hindi variants that the same row also lists. Languages absent from
#  the listing don't count.
METRIC = {
    "kilometre": "ja ko vi th id tl hi bn ta fa ar tr ru es fr sw yo",   # Wt-sourced columns only (ha qu M)
    "kilo": "ja ko vi th hi bn ta tr ru fr sw yo",
    "metre": "ja ko vi th id tl hi bn ta fa ar tr ru es fr sw yo",
    "gram": "ja ko vi th id tl hi bn ta fa ar tr ru es fr sw yo",
    "kilogram": "ja ko vi th id tl hi bn ta fa ar tr ru es fr sw yo",
    "litre": "ja ko vi th id tl hi bn ta fa ar tr ru es fr sw yo",
    "centimetre": "ja ko vi th id tl hi bn fa ar tr ru es fr sw yo",
    "millimetre": "ja ko vi th tl hi fa ar tr ru es fr sw yo",
}


def counted_cols(item, ver):
    """Columns that count, as deciding.py's with-memory count (the one loans-final.tsv reports)."""
    out = set()
    for code, (word, mark, src) in item["rows"].items():
        if mark not in ("y", "b"):
            continue
        memory_only = not any(s in src for s in ("Wt", "We", "M*"))
        if memory_only and ver.get((item["concept"], code)) is False:
            continue
        out.add(code)
    return out - SHAPE_DROP.get(item["concept"], set())


def passes(cols):
    return len(cols) >= 12 and len({REGION[c] for c in cols}) >= 4


def loans():
    emit = load_emit()
    ver = {}
    for r in tsv_read(os.path.join(LW, "verified.tsv")):
        ver[(r["concept"], r["lang"])] = r["result"] == "yes"
    final = {r["concept"]: r for r in tsv_read(os.path.join(P3, "loans-final.tsv"))}
    rerun = {r["loan"]: r for r in tsv_read(os.path.join(P3, "loans-rerun.tsv"))}
    items = []
    for f in sorted(glob.glob(os.path.join(LW, "c[0-9][0-9].txt"))):
        items += [("coverage", it) for it in emit.parse(f)]
    items += [("older", it) for it in emit.parse(os.path.join(LW, "older.txt"))]

    rows, check = [], []
    for group, it in items:
        c = it["concept"]
        cols = counted_cols(it, ver)
        if group == "coverage":
            rec = final[c]
            recorded, verdict = rec["count/regions"], rec["verdict"]
        else:
            rec = rerun[c]
            recorded, verdict = rec["count/regions"], rec["new_verdict"]
        ok = verdict.startswith("pass") or verdict.startswith("loan as a currency")
        mine = f"{len(cols)}/{len({REGION[x] for x in cols})}"
        check.append((c, group, recorded, mine, "same" if mine == recorded or c in SHAPE_DROP else "DIFFERENT"))
        rows.append(dict(concept=c, group=group, verdict=verdict, passed=ok, cols=cols))

    # symbols-01: .com and hashtag (lexicon loans komu, asutagu); sourced columns only, as that test counts
    sym = collections.defaultdict(set)
    for r in tsv_read(os.path.join(REPO, "tests", "symbols-01", "panel.tsv")):
        if r["symbol"] in (".com", "hashtag") and r["shared"] == "y" and r["src"].strip() != "M":
            sym[r["symbol"]].add(r["lang"])
    for s, cols in sym.items():
        rows.append(dict(concept=s, group="symbols", verdict="pass", passed=True, cols=cols))
        check.append((s, "symbols", {".com": "14/6", "hashtag": "13/5"}[s],
                      f"{len(cols)}/{len({REGION[x] for x in cols})}", ""))
    for u, codes in METRIC.items():
        rows.append(dict(concept=u, group="metric", verdict="pass", passed=True, cols=set(codes.split())))
    tsv_write("loans-check.tsv", ["concept", "group", "recorded", "recomputed", "match"], check)

    # per loan
    per = []
    for r in rows:
        cols = r["cols"]
        byreg = {g: sorted(x for x in cols if REGION[x] == g) for g in REG}
        decisive = [g for g in REG if byreg[g] and not passes(cols - set(byreg[g]))] if r["passed"] else []
        per.append([r["concept"], r["group"], r["verdict"], len(cols), sum(1 for g in REG if byreg[g])]
                   + [" ".join(byreg[g]) or "-" for g in REG] + [" ".join(decisive) or "-"])
    tsv_write("loans-per-loan.tsv", ["concept", "group", "verdict", "columns", "regions"] + REG + ["decisive"], per)

    # aggregates over passing loans; main set = panel-marked loans (coverage + older); others shown apart
    def agg(sel):
        tot = collections.Counter(); dec = collections.Counter(); absent = collections.Counter()
        n = 0
        for r in sel:
            n += 1
            cols = r["cols"]
            for g in REG:
                k = sum(1 for x in cols if REGION[x] == g)
                tot[g] += k
                if k == 0:
                    absent[g] += 1
                elif r["passed"] and not passes(cols - {x for x in cols if REGION[x] == g}):
                    dec[g] += 1
        return n, tot, dec, absent
    out = []
    sets = [("panel loans (coverage + older), passing", [r for r in rows if r["passed"] and r["group"] in ("coverage", "older")]),
            ("all lexicon-bound passing loans (+ symbols, metric)", [r for r in rows if r["passed"]]),
            ("panel candidates that failed the count", [r for r in rows if r["verdict"].startswith("fail") and r["group"] in ("coverage", "older")])]
    head = {}
    for name, sel in sets:
        n, tot, dec, absent = agg(sel)
        allc = sum(tot.values())
        for g in REG:
            out.append([name, g, NLANG[g], n, tot[g], f"{tot[g] / allc:.3f}", f"{NLANG[g] / 20:.2f}",
                        f"{tot[g] / (NLANG[g] * n):.3f}", dec[g], absent[g]])
        head[name] = (n, tot, dec, absent, allc)
    tsv_write("loans-by-region.tsv", ["set", "region", "panel_languages", "loans", "cognate_columns",
                                      "share_of_columns", "share_of_panel", "columns_per_language_slot",
                                      "decisive", "region_absent"], out)

    # median shape: wins and losses per region at recorded contested positions
    passing = {r["concept"] for r in rows if r["passed"]}
    win, lose = collections.Counter(), collections.Counter()
    mrows = []
    for c, pos in MEDIAN.items():
        assert c in passing, c
        for w, l in pos:
            for x in w.split():
                win[REGION[x]] += 1
            for x in l.split():
                lose[REGION[x]] += 1
            mrows.append([c, w or "-", l or "-"])
    tsv_write("loans-median-positions.tsv", ["loan", "won (languages whose variant the median took)", "lost"], mrows)
    med = []
    for g in REG:
        t = win[g] + lose[g]
        med.append([g, NLANG[g], win[g], lose[g], f"{win[g] / t:.2f}" if t else "-",
                    f"{win[g] / NLANG[g]:.1f}", f"{lose[g] / NLANG[g]:.1f}"])
    tsv_write("loans-median-by-region.tsv", ["region", "panel_languages", "won", "lost", "win_rate",
                                             "won_per_language", "lost_per_language"], med)
    return head, med, len(MEDIAN)


# ---------------------------------------------------------------- 2. boundaries

# Decisions on lump/split by modern-use evidence (design log 2026-10-13: "Moon and month", "Word and
# language", "The remaining boundary cases"; religion entries for soul/ghost/devil). Labels as in the
# coverage glosses; boundary.py's own lump test is used unchanged.
DECISIONS = [
    ("moon|month", "split", "Moon and month are two words"),
    ("word|language", "split", "Word and language are two words"),
    ("protect|keep", "split", "remaining boundary cases: kuwi = protect / keep"),
    ("ask|request", "split", "remaining boundary cases: mido = ask / request"),
    ("day|daytime", "split", "remaining boundary cases: dili = day / daytime (rung 1 standard)"),
    ("law|rule", "split", "remaining boundary cases: wabun = law / rule"),
    ("need|should", "split", "remaining boundary cases: wupi narrowed; should is advice (fon)"),
    ("power|strength", "split", "remaining boundary cases: lula = power; strength is konke"),
    ("live|life", "lump", "remaining boundary cases: nume also means life (pata removed)"),
    ("leg|foot", "split", "remaining boundary cases: kept apart"),
    ("tree|wood", "split", "remaining boundary cases: kept apart"),
    ("hear|listen", "split", "remaining boundary cases: 20-50% band deleted, two roots"),
    ("see|look", "split", "remaining boundary cases: 20-50% band deleted, two roots"),
    ("paper|book", "split", "remaining boundary cases: 20-50% band deleted, two roots"),
    ("land|country", "split", "remaining boundary cases: 20-50% band deleted, two roots"),
    ("take|get", "split", "remaining boundary cases: 20-50% band deleted, two roots"),
    ("arm|hand", "split", "remaining boundary cases: 20-50% band deleted, two roots"),
    ("soul|spirit", "split", "soul, ghost, miracle and devil are core concepts"),
    ("ghost|spirit", "split", "soul, ghost, miracle and devil are core concepts"),
    ("devil|demon", "lump", "soul, ghost, miracle and devil: evil spirit, demon, devil one concept"),
]
BLANG = "zh ja ko vi th id fil hi bn ta fa ar tr ru es fr sw ha yo qu".split()


def boundaries():
    spec = importlib.util.spec_from_file_location("boundary", os.path.join(P3, "boundary.py"))
    b = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(b)
    data = {c: b.load(c) for c in BLANG}
    rows, tally = [], {g: collections.Counter() for g in REG}
    for pair, dec, src in DECISIONS:
        a, bb = pair.split("|")
        st = {}
        for c in BLANG:
            fr, senses = data[c]
            wa, wb = b.words_for(a, fr, senses), b.words_for(bb, fr, senses)
            if not wa or not wb:
                st[c] = "nodata"; continue
            both = [w for w, _ in wa if w in {x for x, _ in wb}]
            only_a = [(w, f) for w, f in wa if w not in both]
            only_b = [(w, f) for w, f in wb if w not in both]
            if wa[0][0] in both or wb[0][0] in both:
                fl = max(f for w, f in wa + wb if w in both)
                sep = [w for w, f in (only_a[:1] + only_b[:1]) if f / fl >= 0.1]
                st[c] = "lump+sep" if sep else "lump"
            else:
                st[c] = "split"
        code = lambda c: "tl" if c == "fil" else c
        reg = {g: collections.Counter(st[c] for c in BLANG if REGION[code(c)] == g) for g in REG}
        # whose pattern the decision followed: a split follows languages that split (or separate in
        # modern use); a lump follows languages that lump
        for g in REG:
            r = reg[g]
            if pair == "live|life":  # verb vs noun labels: one concept in two roles, not a modern-use lump (added)
                continue
            if dec == "split":
                fol, ag = r["split"] + r["lump+sep"], r["lump"]
            else:
                fol, ag = r["lump"] + r["lump+sep"], r["split"]
            tally[g]["followed"] += fol; tally[g]["against"] += ag; tally[g]["nodata"] += r["nodata"]
        cell = lambda g, k: " ".join(code(c) for c in BLANG if REGION[code(c)] == g and st[c] == k) or "-"
        rows.append([pair, dec, src,
                     " ".join(code(c) for c in BLANG if st[c] == "lump") or "-",
                     " ".join(code(c) for c in BLANG if st[c] == "lump+sep") or "-",
                     " ".join(code(c) for c in BLANG if st[c] == "split") or "-",
                     " ".join(code(c) for c in BLANG if st[c] == "nodata") or "-"]
                    + [f"{reg[g]['lump']}/{reg[g]['lump+sep']}/{reg[g]['split']}/{reg[g]['nodata']}" for g in REG])
    tsv_write("boundaries-per-decision.tsv",
              ["pair", "decision", "design_log", "lump", "lump_but_separate_word_in_modern_use", "split", "no_data"]
              + [f"{g} lump/lump+sep/split/nodata" for g in REG], rows)
    out = []
    for g in REG:
        t = tally[g]
        d = t["followed"] + t["against"]
        out.append([g, NLANG[g], t["followed"], t["against"], t["nodata"], f"{t['followed'] / d:.2f}" if d else "-"])
    tsv_write("boundaries-by-region.tsv", ["region", "panel_languages", "language_decisions_followed",
                                           "language_decisions_against", "no_data", "share_followed"], out)
    return out, rows


# ---------------------------------------------------------------- 3. the concept list

COV_LANGS = ["zh", "ja", "ko", "vi", "th", "id", "fil", "hi", "bn", "ta", "fa", "ar", "tr", "ru", "es", "fr",
             "sw", "ha", "yo", "qu"]


def shares():
    """Per-language concept shares, exactly as concepts.py build() computes them (not written)."""
    data = os.path.join(COV, "data")
    out = {}
    for code in COV_LANGS:
        gl = {}
        for l in open(os.path.join(data, f"gloss-{code}.tsv"), encoding="utf-8").read().split("\n")[1:]:
            if l:
                w, _, labs = l.split("\t")
                gl[w] = [x for x in labs.split(" | ") if x]
        per_source = []
        for fn in (f"freq-{code}.tsv", f"sfreq-{code}.tsv"):
            fp = os.path.join(data, fn)
            if not os.path.exists(fp):
                continue
            fr = dict(l.split("\t") for l in open(fp, encoding="utf-8").read().split("\n")[1:] if l)
            sc = collections.Counter()
            for w, f in fr.items():
                labs = gl.get(w, [])
                wt = [1 / (i + 1) for i in range(len(labs))]
                for lab, x in zip(labs, wt):
                    if lab != "#fn":
                        sc[lab] += float(f) * x / sum(wt)
            total = sum(sc.values())
            per_source.append({k: v / total for k, v in sc.items()})
        keys = set().union(*per_source)
        out["tl" if code == "fil" else code] = {k: sum(s.get(k, 0) for s in per_source) / len(per_source) for k in keys}
    return out


def concept_status():
    """label -> (canonical, status): root (on the ~1,500 list), phrase, grammar, other, missing."""
    lex_forms = {r["form"] for r in tsv_read(os.path.join(REPO, "data", "lexicon.tsv"))}
    r1500 = {l.strip() for l in open(os.path.join(COV, "part2b", "roots-1500.txt")) if l.strip()}
    adds = {r["concept"] for r in tsv_read(os.path.join(P3, "additions.tsv"))}
    st = {}
    for fn in ("merged.tsv", "merged-add.tsv"):
        for l in open(os.path.join(COV, fn), encoding="utf-8"):
            p = l.rstrip("\n").split("\t")
            if len(p) < 5:
                continue
            label, canon, kind, cover = p[1], p[2], p[3], p[4]
            if label in st:
                continue
            if kind != "content":
                s = "grammar" if kind == "grammar" else "other"
            elif canon in r1500 or canon in adds or label in r1500 or label in adds:
                s = "root"
            elif cover != "none" and " " not in cover and cover in lex_forms:
                s = "root"
            elif cover != "none":
                s = "phrase"
            else:
                s = "missing"
            st[label] = (canon, s)
    return st


def concept_list():
    sh = shares()
    floor = 1e-7
    labels = set().union(*[s.keys() for s in sh.values()])
    logs = {lab: {c: math.log10(sh[c].get(lab, 0) + floor) for c in sh} for lab in labels}
    def med(v):
        v = sorted(v); return (v[len(v) // 2] + v[(len(v) - 1) // 2]) / 2
    glob_score = {lab: med(list(d.values())) for lab, d in logs.items()}
    # check against concepts.tsv
    rec = {}
    for r in tsv_read(os.path.join(COV, "concepts.tsv")):
        if int(r["rank"]) > 4000:
            break
        rec[r["concept"]] = float(r["score"])
    diffs = sum(1 for k, v in rec.items() if abs(glob_score.get(k, -99) - v) > 0.0015)
    ranked = sorted(labels, key=lambda k: (-glob_score[k], k))
    grank = {k: i + 1 for i, k in enumerate(ranked)}
    reg_score = {g: {lab: sum(logs[lab][c] for c in sh if REGION[c] == g) / NLANG[g] for lab in labels} for g in REG}

    status = concept_status()
    top = [k for k in ranked if status.get(k, ("", ""))[1] not in ("grammar", "other")][:3000]
    # (a) per-region rank correlation with the final (median) score over the top 3,000 global labels
    corr = []
    gs = [glob_score[k] for k in top]
    lang_corr = {c: spearman([logs[k][c] for k in top], gs) for c in sh}
    for g in REG:
        rc = spearman([reg_score[g][k] for k in top], gs)
        lc = [lang_corr[c] for c in sh if REGION[c] == g]
        corr.append([g, NLANG[g], f"{rc:.3f}", f"{sum(lc) / len(lc):.3f}",
                     " ".join(f"{c}:{lang_corr[c]:.2f}" for c in sh if REGION[c] == g)])
    # leave-one-region-out: how far does the final ranking move without each region?
    for row, g in zip(corr, REG):
        rest = [c for c in sh if REGION[c] != g]
        alt = [med([logs[k][c] for c in rest]) for k in top]
        row.append(f"{spearman(alt, gs):.4f}")
    tsv_write("concepts-correlation.tsv", ["region", "panel_languages", "spearman_region_mean_vs_final",
                                           "mean_spearman_of_its_languages", "per_language",
                                           "spearman_final_without_region"], corr)

    # (b) each region's own top concepts: how many are on the ~1,500 list
    miss = []
    examples = []
    for K in (300, 1000):
        for g in REG:
            own = sorted(labels, key=lambda k: -reg_score[g][k])
            cnt = collections.Counter()
            n = 0
            for k in own:
                s = status.get(k, (k, "below_cut"))[1]
                if s in ("grammar", "other"):
                    continue
                n += 1
                cnt[s] += 1
                if s == "below_cut" and "," in k:
                    cnt["below_comma"] += 1
                if K == 1000 and s in ("missing", "below_cut") and len([e for e in examples if e[0] == g]) < 40:
                    examples.append([g, k, s, grank[k], f"{reg_score[g][k]:.2f}"])
                if n == K:
                    break
            merged_n = cnt["root"] + cnt["phrase"] + cnt["missing"]
            miss.append([K, g, NLANG[g], cnt["root"], cnt["phrase"], cnt["missing"], cnt["below_cut"],
                         cnt["below_comma"], f"{cnt['missing'] / merged_n:.3f}",
                         f"{(cnt['missing'] + cnt['below_cut']) / K:.3f}"])
    tsv_write("concepts-region-top.tsv", ["top_K", "region", "panel_languages", "on_list_root", "covered_by_phrase",
                                          "content_not_on_list", "below_merge_cut", "below_cut_multi_synonym_label",
                                          "share_missing_of_merged", "share_not_on_list_incl_below_cut"], miss)
    tsv_write("concepts-region-top-missing-examples.tsv", ["region", "label", "status", "global_rank",
                                                           "region_log_share"], examples)
    return corr, miss, diffs, len(rec)


def wordbank():
    """Deep layer: children's first words. Wordbank has 21 European and 9 non-European checklists
    (coverage-01 README/RESULTS); items.pkl holds the non-European items, so each deep concept's
    non-European count is direct and its European count is its total minus that."""
    total = {}
    for l in open(os.path.join(COV, "wordbank.tsv"), encoding="utf-8").read().splitlines()[1:]:
        p = l.split("\t")
        total[p[0]] = int(p[1])
    canon2uni = collections.defaultdict(set)
    for l in open(os.path.join(COV, "wordbank-merged.tsv"), encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        canon2uni[p[2]].add(p[0])
    items = pickle.load(open(os.path.join(P3, "nonwestern", "items.pkl"), "rb"))
    WREG = {"Mandarin": "EA", "Cantonese": "EA", "Japanese": "EA", "Korean": "EA", "Persian": "WA",
            "Turkish": "WA", "Hebrew": "WA", "Kiswahili": "SSA", "Kigiriama": "SSA"}
    has = collections.defaultdict(set)
    for lang, _, _, _, _, uni, _ in items:
        if uni:
            has[uni.strip().lower()].add(lang)
    final = tsv_read(os.path.join(P3, "wordbank-final.tsv"))
    rows = []
    for r in final:
        unis = canon2uni.get(r["concept"], {r["concept"]})
        n = max((total.get(u, 0) for u in unis), default=0)
        nonl = set().union(*[has.get(u.lower(), set()) for u in unis]) if unis else set()
        rows.append([r["concept"], r["final"], n, len(nonl), n - len(nonl)]
                    + [sum(1 for x in nonl if WREG[x] == g) for g in ("EA", "WA", "SSA")])
    tsv_write("wordbank-deep.tsv", ["concept", "final", "wordbank_languages", "non_european", "european",
                                    "EA_of_4", "WA_of_3", "SSA_of_2"], rows)
    keep = [x for x in rows if x[1] == "keep"]
    summ = dict(n=len(keep), eu=sum(x[4] for x in keep), non=sum(x[3] for x in keep),
                ea=sum(x[5] for x in keep) / (4 * len(keep)), wa=sum(x[6] for x in keep) / (3 * len(keep)),
                ssa=sum(x[7] for x in keep) / (2 * len(keep)),
                eu_rate=sum(x[4] for x in keep) / (21 * len(keep)),
                eu_only=sum(1 for x in keep if x[3] == 0))
    # non-European checklist items absent from European lists, by status and by region
    nw = tsv_read(os.path.join(P3, "wordbank-nonwestern.tsv"))
    AB = {"Can": "EA", "Cmn": "EA", "Jpn": "EA", "Kor": "EA", "Fas": "WA", "Tur": "WA", "Heb": "WA",
          "Swa": "SSA", "Kig": "SSA", "Ara": "WA"}
    by = {g: collections.Counter() for g in ("EA", "WA", "SSA")}
    for r in nw:
        abbrs = r["checklists"].split("|")[0].strip().split(",")
        regs = {AB[a.strip()] for a in abbrs if a.strip() in AB}
        now = r["apupiwe_now"].strip().lower()
        s = "none" if now.startswith("none") or not now else "some word"
        for g in regs:
            by[g][s] += 1
    nwrows = [[g, by[g]["some word"], by[g]["none"]] for g in by]
    tsv_write("wordbank-nonwestern-by-region.tsv", ["checklist_region", "items_with_some_apupiwe_word",
                                                    "items_with_none"], nwrows)
    return summ, nwrows


if __name__ == "__main__":
    lo, med, nmed = loans()
    print("== 1. loans")
    for name, (n, tot, dec, absent, allc) in lo.items():
        print(f"-- {name}: {n} loans, {allc} cognate columns")
        for g in REG:
            print(f"   {g:4} cols {tot[g]:4} share {tot[g] / allc:.3f} (panel {NLANG[g] / 20:.2f}) "
                  f"per-slot {tot[g] / (NLANG[g] * n):.2f}  decisive {dec[g]:3}  absent {absent[g]:3}")
    print(f"-- median positions ({nmed} loans with recorded languages)")
    for r in med:
        print("  ", r)
    bo, brows = boundaries()
    print("== 2. boundaries")
    for r in brows:
        print("  ", r[0], r[1], "| lump:", r[3], "| lump+sep:", r[4], "| nodata:", r[6])
    for r in bo:
        print("  ", r)
    corr, miss, diffs, nrec = concept_list()
    print(f"== 3. concept list (score check: {diffs} of {nrec} recorded top labels differ)")
    for r in corr:
        print("  ", r)
    for r in miss:
        print("  ", r)
    wb, nw = wordbank()
    print("   wordbank deep:", wb)
    print("   nonwestern:", nw)
