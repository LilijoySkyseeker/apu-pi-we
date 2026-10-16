"""Check the spec's examples against the sentence and noun-phrase templates (language.md 4.1, 5.1).

Only grammar words are parsed. A run of content words is one chunk, because whether a content
word is a thing, an event or a manner is left to meaning (4.2); so is everything context
supplies. What it checks: every grammar word sits in a slot the templates allow, and where
units (relation phrases, relative clauses, clauses, calls, stance) begin and end has exactly
one reading under the pause rules (4.6).

  python parse.py               # every example in spec/reference.toml: no parse / several readings
  python parse.py "to min unfu"   # one sentence and its readings
  python parse.py --file F      # every sentence in a text (headings and {.attr} lines skipped)

Needs lark: nix-shell -p 'python3.withPackages(ps: [ps.lark])'
"""
import re, sys
import lark
import words as W
import spec as SPEC

LEX = W.read("lexicon.tsv")
# Two-syllable grammar words kept in the lexicon (language.md 13)
OPS2 = {"genso", "wanme", "inwun", "wemen", "konsin", "nedin", "tason", "mesun", "manni", "buntu", "buni", "donon", "lanno", "anko", "nuwen", "kiyo"}
NUMS = {r["form"] for r in W.read("numbers.tsv")} | {w["form"] for w in LEX if w["field"] == "number"}
CONTENT = sorted({w["form"] for w in LEX} - OPS2 - NUMS)
NAME_ENDS = {r["form"] for r in W.read("grammar.tsv")} | OPS2 | NUMS


GRAMMAR = r"""
?start: utterance
utterance: sentence | fragment
sentence: (call ",")? (opener ",")* actp? clop* clause ("," choice)? end*
        | (call ",")? (opener ",")* actp clop* fragment end*
choice: "yu"
end: ","? stance | "," call
call: np
opener: "bo" "win" | JOIN | relp | "pi" np | subcl
subcl: phop* SUBLINK clop* clause
actp: ("genso" | "ba")? ACT "fin"* | "fin"+
clop: "pe" (N | "pa") | SOURCE
clause: (np | heavy)? predicate (","? JOIN (np | heavy)? predicate)*
heavy: np ","
predicate: phop* "manni"? (asp* | "le" "su") C (phop+ C)? det* ("pi" np)* relcl? obj? (obj | "," longobj)? result? ("gun" gunarg)? trail* | phop* "gun" gunarg trail*
// C (phop+ C): verb, operator, verb, as in keya mu neke "must not give"; le mu "still not" (8.1.3)
result: phop* C  // after a pronoun object: muge go bi yomo, "make/do it so" (4.2)
longobj: np
obj: np
gunarg: np obj? result? | relp | "wun" clause
trail: ","? relp | ","? subcl | "wun" "bi"? clop* clause
relp: phop* REL (np | np predicate | relp) | "fan" C obj | "fan" "gun" gunarg  // li + verb + its object: purpose
np: phop* head det* ("pi" npi)* relcl? (JOIN np)?
npi: phop* head det* ("pi" npi)* relcl?  // a pi phrase is one noun: a yen/lu list stays outside it (5.2)
head: PRON | NAME | "lanno"? C N? | C ("ke" | "ten" | PHOP) C | DERIV C? (np | relp)? | DERIV "pi" np | N | DET | "yu" | "lanno" NAME?
relcl: "gi" clause REL?
date: C "pi" N "," C "pi" N
stance: "bi" | "yan" | "buni" | "donon"
phop: PHOP | "min" | "su" | "pon" | "yon" | "ga" | "ke" | "ten"
asp: "sin" | "le" | "buntu"
det: DET | "mesun" | "yu" | "pa" | "nen"
fragment: np | date | predicate | relp | subcl | "pi" np | stance | clop+ clause? | actp clause?
ACT: "bi" | "ta" | "ti" | "fon" | "me" | "yo"
SOURCE: "wanme" | "inwun" | "wemen"
JOIN: "yen" | "lu" | "ka"
SUBLINK: "don" | "lin" | "kon" | "ya" | "bo"
REL: "anko" | "nuwen" | "mon" | "tun" | "se" | "nan" | "fan" | "ya" | "kon" | "fun" | "lin"
PHOP: "konsin" | "nedin" | "tason"
DET: "la" | "win" | "ben" | "we" | "go" | "kin" | "fen"
PRON: "to" | "nun" | "kan" | "din" | "wan" | "yi" | "son" | "dan" | "nen" | "bun"
DERIV: "no" | "gen" | "du" | "pu"
C: "C"
N: "N"
NAME: "NAME"
%import common.WS
%ignore WS
"""
GRAMMAR_WORDS = set(re.findall(r'"([a-z]+)"', GRAMMAR))
# Every word ends in "_" so the lexer can't split one word into two (mesun -> me sun).
GRAMMAR = re.sub(r'"([a-z]+)"', r'"\1_"', GRAMMAR)
CONTENT = set(CONTENT)
PRONOUNS = set(re.search(r'PRON: (.*)', GRAMMAR).group(1).replace('"', "").split(" | "))


def chunk(sentence):
    """Collapse what the grammar can't see into placeholders: a run of content words is C,
    a run of number words N, en + the next word NAME. Doubled words count once."""
    out, words = [], sentence.replace(",", " , ").split()
    i = 0
    while i < len(words):
        w = words[i]
        if w in (",", "kiyo"):  # kiyo "end of phrase" does what a pause does (5.3)
            out.append(","); i += 1; continue
        if out and w == out[-1] and w not in ("C", "N"):
            i += 1
            continue
        if w == "fo" and i + 1 < len(words):
            # a name runs to the next grammar word or pause (11.1)
            i += 2
            while i < len(words) and words[i] != "," and words[i] not in NAME_ENDS:
                i += 1
            out.append("NAME"); continue
        if w in NUMS:
            kind = "N"
        elif w in CONTENT or w.startswith("[") or w not in GRAMMAR_WORDS:
            kind = "C"
        else:
            out.append(w + "_"); i += 1; continue
        if not out or out[-1] != kind:
            out.append(kind)
        i += 1
    return " ".join(out)


PARSER = lark.Lark(GRAMMAR, parser="earley", lexer="dynamic", ambiguity="explicit", keep_all_tokens=True)


# Units whose boundaries change meaning. Everything else is transparent, so a bare content
# chunk read as a thing or as an event counts as one reading: that choice is left to meaning
# (language.md 4.2), not to grammar words.
UNITS = {"longobj", "heavy", "relp", "relcl", "subcl", "call", "choice", "obj", "opener", "stance", "trail"}
SAME = {"subcl": "relp"}  # wo/ya/nin + a thing or + an event: the same relation, chosen by meaning
STANCE = {"bi", "yan", "buni", "donon"}


def signature(tree):
    if not isinstance(tree, lark.Tree):
        return str(tree).rstrip("_")
    inner = " ".join(signature(c) for c in tree.children if signature(c))
    if tree.data == "obj" or tree.data == "trail":
        return inner
    label = SAME.get(tree.data, tree.data)
    return f"{label}[{inner}]" if tree.data in UNITS else inner


def closed_by_pause(sig):
    """language.md 5.3: no word closes a relative clause; a pause (or the sentence end) does."""
    for m in re.finditer(r"relcl\[", sig):
        depth, j = 1, m.end()
        while depth:
            depth += {"[": 1, "]": -1}.get(sig[j], 0)
            j += 1
        body, depth = "", 0
        for ch in sig[m.end():j - 1]:
            depth += {"[": 1, "]": -1}.get(ch, 0)
            body += ch if depth == 0 else ""
        if " , " in f" {body} ":
            return False  # the pause would have closed it
        rest = sig[j:].lstrip(" ]").split()
        if rest and rest[0] != "," and not rest[0].startswith(("end[", "stance[")) and rest[0] not in STANCE:
            return False
    return True


def readings(tree):
    """Distinct readings, comparing only where grammar-word units begin and end."""
    trees = lark.visitors.CollapseAmbiguities().transform(tree)
    sigs = {signature(t) for t in trees[:5000]}
    # 4.6: a pause before the verb only after a subject holding a clause or a phrasal derived word
    sigs = {sg for sg in sigs if all("relcl[" in h or re.match(r"(no|ge|du|pu) ", h)
                                     for h in re.findall(r"heavy\[([^]]*)", sg))}
    # 4.6: a pause between a recipient and a long object (here: more than one word)
    sigs = {sg for sg in sigs if all(len(o.split()) > 1 for o in re.findall(r"longobj\[([^]]*)", sg))}
    sigs = {re.sub(r"longobj\[(.*?)\]", r"\1", sg) for sg in sigs}
    sigs = {re.sub(r"heavy\[(.*?) ,\]", r"\1 ,", sg) for sg in sigs}
    return sorted(sg for sg in sigs if closed_by_pause(sg) and not re.search(r"call\[[^]]*\byu\b", sg)  # nobody is called "what"
              and not re.search(r"call\[[^]]*(relcl|\bN\b)", sg))  # a call is a name, title, role or kin word (4.1)


def clean(text):
    return [s.strip(" ,") for s in re.split(r"[.?!](?!\d)", text) if s.strip(" ,")]


def parse(sentence):
    try:
        sigs = readings(PARSER.parse(chunk(sentence)))
        return len(sigs), sigs or ["every reading leaves a relative clause unclosed"]
    except lark.exceptions.LarkError as e:
        return 0, str(e).split("\n")[0]


if __name__ == "__main__":
    if sys.argv[1:2] == ["--file"]:
        # A text file: every line that isn't a heading or a {.attr} line is Apupiwe prose.
        counts, worst = {0: 0, 1: 0, 2: 0}, []
        for line in open(sys.argv[2]):
            line = re.sub(r"^\d+\. ", "", line.strip())
            if not line or line.startswith(("#", "{")):
                continue
            for s in clean(line):
                n, t = parse(s)
                counts[min(n, 2)] += 1
                if n != 1:
                    worst.append((n, s))
        print(f"one reading: {counts[1]}   several readings: {counts[2]}   no parse: {counts[0]}")
        for n, s in worst:
            print(f"  {n}  {s}")
        sys.exit()
    if len(sys.argv) > 1:
        for s in clean(" ".join(sys.argv[1:])):
            n, t = parse(s)
            print(f"{n} reading(s): {s}")
            for sig in (t if n else [t]):
                print("   ", sig)
        sys.exit()
    fails, multi, ok = [], [], 0
    for rid, apu, en in SPEC.examples(SPEC.load()):
        if re.search(r"\b[A-Z]\b|\bX\b", apu) or "…" in apu:
            continue  # templates and partial examples
        if not set(re.sub(r"kon_ N", "", chunk(apu)).split()) & ({"C", "N", "NAME"} | PRONOUNS):
            continue  # a grammar word cited on its own
        for s in clean(apu):
            n, t = parse(s)
            if n == 0:
                fails.append((rid, s, en))
            elif n > 1:
                multi.append((rid, s, en, n))
            else:
                ok += 1
    print(f"one reading: {ok}   several readings: {len(multi)}   no parse: {len(fails)}\n")
    print("NO PARSE")
    for r in fails:
        print("  %-7s %-40s %s" % r)
    print("\nSEVERAL READINGS")
    for r in sorted(multi, key=lambda x: -x[3]):
        print("  %-7s %-40s %-35s %d" % r)
