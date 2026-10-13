"""Measures behind research/notes/globasa.md §4.3 (2026-10-13).

Input: Globasa's dictionary export, https://cdn.globasa.net/api2/word-list.csv
(download it next to this script or pass its path). Apupiwe's data is read from
the repo. Run: direnv exec <repo> python3 research/notes/globasa-data.py [word-list.csv]
"""
import collections, csv, re, statistics, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
rows = list(csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else 'word-list.csv', encoding='utf-8')))
roots = [r for r in rows if r['Category'] == 'root']
core = [r for r in roots if '500 maxim pimpan' in r['Tags']]

# Origin blocs (mine): European languages count as one, as in Globasa's own method.
BLOCS = {
    'EUR': 'Englisa Espanisa Fransesa Doycisa Rusisa Italisa Portugalsa Elinisa Nederisa Swerisa Polskasa Rumanisa Makedonisa Bulgarisa Norgesa Ceskisa Eslovakisa Hervatskasa Serbihervatskasa Danisa Katalunisa Syensilatinsa Latinsa',
    'EA': 'Putunhwa Niponsa Koreasa Vyetnamsa Gwondunsa', 'ARA': 'Arabisa Ivrisa Maltasa', 'PER': 'Parsisa',
    'TUR': 'Turkisa Azerbayjansa', 'IND': 'Hindi Urdu Banglasa Panjabisa Gujaratisa Maharaxtrasa Nepalsa Sanskritam',
    'DRA': 'Telugusa Tamilsa Karnatakasa Keralasa Telugu', 'MP': 'Indonesisa Pilipinasa Malaysisa Hawayisa Maorisa',
    'SW': 'Swahilisa'}
BLOC = {l: b for b, ls in BLOCS.items() for l in ls.split()}
PANEL17 = set('Englisa Fransesa Doycisa Rusisa Espanisa Putunhwa Niponsa Koreasa Vyetnamsa Hindi Telugusa Arabisa Swahilisa Parsisa Turkisa Indonesisa Pilipinasa'.split())

def sources(r):
    e = re.sub(r'^kwasilexi\s*-\s*', '', r['LexiliAsel'])
    return [m.group(1) for m in re.finditer(r'([A-Z][A-Za-z]+)\s*\(', e)]

def origin_report(sub, name):
    first, single, nl, wide = collections.Counter(), collections.Counter(), [], 0
    for r in sub:
        ls = sources(r)
        if not ls: continue
        first[BLOC.get(ls[0], 'OTHER')] += 1
        bs = {BLOC[l] for l in ls if l in BLOC}
        if len(bs) == 1: single[next(iter(bs))] += 1
        nl.append(len(ls))
        p = set(ls) & PANEL17
        wide += len(p) >= 10 and len({BLOC[l] for l in p}) >= 4
    n = len(sub)
    print(f'== {name}: {n} roots')
    print('  first-listed bloc %:', [(b, round(100 * c / n, 1)) for b, c in first.most_common()])
    print('  single-bloc roots:', sum(single.values()), dict(single), '| median sources/root:', statistics.median(nl))
    print(f'  >=10 of 17 panel languages and >=4 blocs: {wide} ({100 * wide / n:.1f}%)')

V = set('aeiou')
def syl(w): return sum(c in V for c in w)

def lev(a, b):
    p = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (x != y)))
        p = c
    return p[-1]

def minimal_pairs(words, name):
    ws = sorted({w.lower() for w in words if re.fullmatch(r'[a-z]+', w.lower())})
    nb, pairs = set(), 0
    for i, a in enumerate(ws):
        for b in ws[i + 1:]:
            if abs(len(a) - len(b)) <= 1 and lev(a, b) == 1: nb |= {a, b}; pairs += 1
    s = [syl(w) for w in ws]
    print(f'== {name}: n={len(ws)}, mean syllables {statistics.mean(s):.2f}, '
          f'with a one-letter neighbour {100 * len(nb) / len(ws):.1f}%, pairs {pairs}')

def antonym_distances(pairs, name):
    c = collections.Counter(min(lev(a, b), 4) for a, b in pairs)
    print(f'== {name}: {len(pairs)} pairs, edit distance 1/2/3/>=4:', [c[k] for k in (1, 2, 3, 4)])

origin_report(roots, 'Globasa, all roots')
origin_report(core, 'Globasa, 500-most-common roots')
minimal_pairs([r['Word'] for r in core if syl(r['Word'].lower()) >= 2], 'Globasa core roots, >=2 syllables')
minimal_pairs([r['Word'] for r in roots], 'Globasa all roots')
lex = {}
for line in (REPO / 'data/lexicon.tsv').read_text().splitlines()[1:]:
    g, f, t, form = line.split('\t'); lex[g] = form
minimal_pairs(lex.values(), 'Apupiwe lexicon')
R = {r['Word'].lower() for r in roots}
gp = {tuple(sorted((r['Word'].lower(), a.strip().lower()))) for r in roots
      for a in re.split(r'[,;]\s*', r['Antonyms']) if a.strip().lower() in R}
antonym_distances(gp, 'Globasa root antonyms')
ap = [l.split('\t') for l in (REPO / 'data/antonyms.tsv').read_text().splitlines() if l.strip()]
antonym_distances([(lex[a], lex[b]) for a, b, *_ in ap if a in lex and b in lex], 'Apupiwe antonyms')
