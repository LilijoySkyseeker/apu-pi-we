"""Carry texts and docs over to renamed word forms (data/rename-*.tsv).

Only language text is converted: a code-block line or a **bold** span counts as language
if every word in it is a known old form or a capitalized name. English glosses are left alone.
Content words get their stress capitals back; code-block glosses are re-aligned under them.

  python convert.py ../data/rename-2026-10-08.tsv FILE...
"""
import csv, re, sys

VOWEL = "aeiou"


def syllables(form):
    return re.findall(r"[^aeiou]?[aeiou](?:n(?![aeiou]))?", form)


def load(path):
    with open(path) as fh:
        return {r["old"]: (r["new"], r["kind"]) for r in csv.DictReader(fh, delimiter="\t") if r["old"]}


def is_name(tok):
    return tok[:1].isupper() and tok.lower() not in OLD and re.fullmatch(r"[A-Za-z]+", tok)


def convert_token(tok):
    m = re.fullmatch(r"([^A-Za-z]*)([A-Za-z]+)(.*)", tok)
    if not m:
        return tok
    lead, word, rest = m.groups()
    low = word.lower()
    if low not in OLD:
        return tok
    new, kind = OLD[low]
    if kind == "content":
        s = syllables(new)
        new = s[0].upper() + "".join(s[1:]) if word[:1].isupper() else new
    return lead + new + rest


def is_language(text):
    toks = re.findall(r"[A-Za-z]+", text)
    return (any(t.lower() in OLD for t in toks)
            and all(t.lower() in OLD or is_name(t) for t in toks))


def realign(lang, gloss):
    a, b = lang.split(), gloss.split()
    if len(a) != len(b):
        return lang, gloss
    w = [max(len(x), len(y)) for x, y in zip(a, b)]
    return (" ".join(x.ljust(n) for x, n in zip(a, w)).rstrip(),
            " ".join(y.ljust(n) for y, n in zip(b, w)).rstrip())


def convert_file(path):
    lines = open(path).read().split("\n")
    out, in_code, i = [], False, 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            in_code = not in_code
            out.append(line); i += 1; continue
        if in_code and is_language(line):
            new = " ".join(convert_token(t) for t in line.split())
            nxt = lines[i + 1] if i + 1 < len(lines) else None
            if nxt is not None and nxt.strip() and not is_language(nxt):
                # the gloss line may carry an English translation after the glosses
                n_lang, gtoks = len(new.split()), nxt.split()
                if len(gtoks) >= n_lang:
                    new, gl = realign(new, " ".join(gtoks[:n_lang]))
                    tail = ("    " + " ".join(gtoks[n_lang:])) if len(gtoks) > n_lang else ""
                else:
                    gl, tail = nxt, ""
                out += [new, gl + tail]
                i += 2
                continue
            out.append(new); i += 1; continue
        if not in_code:
            line = re.sub(r"\*\*([^*]+)\*\*",
                          lambda m: "**" + " ".join(convert_token(t) for t in m.group(1).split()) + "**"
                          if is_language(m.group(1)) else m.group(0), line)
        out.append(line); i += 1
    open(path, "w").write("\n".join(out))


if __name__ == "__main__":
    OLD = load(sys.argv[1])
    for p in sys.argv[2:]:
        convert_file(p)
        print("converted", p)
