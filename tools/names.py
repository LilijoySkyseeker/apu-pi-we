"""Adapt names from any language into this language's sounds (2026-10-08).

Input: a broad IPA transcription. Each sound maps to the native sound listeners most often
hear it as (place-of-articulation confusions per Miller & Nicely where data exist; standard
loanword practice otherwise). Consonants are never dropped (research/notes/names-and-loans.md):
a consonant that can't stand where it is gets an added vowel instead.

  python names.py [default|echo]   # adapt the test list; the language uses default (added vowel u)
"""
import re, sys
import words as W

CONS = {
    "p": "p", "b": "b", "t": "t", "ʈ": "t", "d": "d", "ɖ": "d", "k": "k", "q": "k", "c": "k", "g": "g", "ɡ": "g",
    "m": "m", "n": "n", "ɲ": "n", "ɳ": "n", "ŋ": "n",
    "f": "f", "ɸ": "f", "θ": "f", "v": "b", "β": "b", "ð": "d",
    "s": "s", "z": "s", "ʃ": "s", "ʒ": "s", "ɕ": "s", "ʑ": "s", "ʂ": "s", "ʐ": "s", "ç": "s",
    "x": "k", "χ": "k", "ɣ": "g", "h": "", "ɦ": "", "ħ": "", "ʔ": "", "ʕ": "",
    "l": "l", "ɫ": "l", "ɭ": "l", "ʎ": "l", "r": "l", "ɾ": "l", "ɹ": "l", "ʁ": "l", "ʀ": "l", "ɻ": "l",
    "j": "y", "w": "w", "ɥ": "w", "ʋ": "w",
}
AFFRICATES = {"tʃ": "t", "tɕ": "t", "ʈʂ": "t", "ts": "s", "dʒ": "d", "dʑ": "d", "dz": "s"}
VOWELS = {
    "i": "i", "ɪ": "i", "y": "i", "ɨ": "i", "e": "e", "ɛ": "e", "ø": "e", "œ": "e", "æ": "a", "ə": "a", "ɜ": "a",
    "a": "a", "ɑ": "a", "ɐ": "a", "ʌ": "a", "o": "o", "ɔ": "o", "ɒ": "o", "ɤ": "o", "u": "u", "ʊ": "u", "ɯ": "u", "ʉ": "u",
}
DROP = "ˈˌːʰʲˑ.ˀ̥̩̯̪̚ʷ"
NASAL = "̃"


def segments(ipa):
    ipa = ipa.replace("ɡ", "g")
    out, i = [], 0
    while i < len(ipa):
        ch = ipa[i]
        if ch in DROP or ch in "̣́̀":  # stress, length, aspiration, tone, dots
            i += 1; continue
        two = ipa[i:i + 2]
        if two in AFFRICATES:
            out.append(("C", AFFRICATES[two])); i += 2; continue
        if ch in VOWELS:
            out.append(("V", VOWELS[ch]))
            if i + 1 < len(ipa) and ipa[i + 1] == NASAL:
                out.append(("C", "n")); i += 1
            i += 1; continue
        if ch in CONS:
            if CONS[ch]:
                out.append(("C", CONS[ch]))
            i += 1; continue
        if ch == NASAL:
            i += 1; continue
        raise ValueError(f"unmapped symbol {ch!r} in {ipa}")
    return out


def adapt(ipa, epenthesis="default"):
    seg = segments(ipa)
    vowels = [k for k, (t, _) in enumerate(seg) if t == "V"]

    def added_vowel(k):
        if epenthesis == "default":
            return "u"
        nxt = [v for v in vowels if v > k]
        prv = [v for v in vowels if v < k]
        return seg[nxt[0]][1] if nxt else (seg[prv[-1]][1] if prv else "u")

    out = ""
    for k, (t, s) in enumerate(seg):
        nxt = seg[k + 1] if k + 1 < len(seg) else None
        if t == "C":
            if s == "n" and out and out[-1] in "aeiou" and (nxt is None or nxt[0] == "C"):
                out += "n"                        # the one allowed final consonant
            elif s == "m" and out and out[-1] in "aeiou" and nxt is not None and nxt[0] == "C":
                out += "n"                        # m before a consonant becomes n
            elif nxt is not None and nxt[0] == "V":
                out += s
            else:
                out += s + added_vowel(k)         # never drop a consonant
        else:
            if out and out[-1] in "aeiou":
                prev = out[-1]
                if prev == s:
                    continue                      # aa -> a
                out += ("y" if prev in "ie" or (prev == "a" and s in "ie") else "w") + s
            else:
                out += s
    if len(re.findall(r"[aeiou]", out)) < 2:   # names have at least two syllables
        out += "u"
    return out


NAMES = [
    ("Christopher", "ˈkɹɪstəfəɹ"), ("Elizabeth", "ɪˈlɪzəbəθ"), ("Muhammad", "muˈħammad"), ("Xi Jinping", "ɕi tɕinpʰiŋ"),
    ("Priya", "pɾijaː"), ("Olusegun", "olusɛgun"), ("Ngozi", "ŋgozi"), ("Hiroshi", "çiɾoɕi"), ("Yuki", "jɯki"),
    ("Svetlana", "svʲɪtlanə"), ("Dmitri", "dmʲitrʲij"), ("Zeynep", "zejnep"), ("Nguyen", "ŋwiən"), ("Fatima", "faːtima"),
    ("Guadalupe", "gwaðalupe"), ("João", "ʒuɐ̃w̃"), ("François", "fʁɑ̃swa"), ("Siobhan", "ʃɪvɔːn"), ("Björk", "bjœrk"),
    ("Kwame", "kwame"), ("Aisha", "ʕaːʔiʃa"), ("Ingrid", "ɪŋgɾɪd"), ("Wojciech", "vɔjtɕɛx"), ("Thandiwe", "tʰandiwe"),
    ("London", "lʌndən"), ("Paris", "paʁi"), ("Tokyo", "toːkʲoː"), ("Beijing", "peɪtɕiŋ"), ("Mumbai", "mʊmbaɪ"),
    ("Lagos", "leɪgɒs"), ("Cairo", "kaɪɹoʊ"), ("Moskva (Moscow)", "mɐskva"), ("Istanbul", "istanbul"),
    ("Jakarta", "dʒakarta"), ("México", "mexiko"), ("São Paulo", "sɐ̃w̃pawlu"), ("Buenos Aires", "bwenosajɾes"),
    ("Nairobi", "naɪɾobi"), ("Sydney", "sɪdni"), ("Reykjavík", "reiːcaviːk"), ("Kathmandu", "kaʈʰmaɳɖu"),
    ("Brasil", "bɾaziw"), ("Germany", "dʒɜːmənɪ"), ("Amazon", "æməzən"),
]

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "default"
    lex = W.read("lexicon.tsv")
    forms = {w["form"]: w["gloss"] for w in lex}
    keys = {W.INV.content_key(W.split(w["form"])): w["gloss"] for w in lex}
    clash = 0
    for name, ipa in NAMES:
        a = adapt(ipa.replace(" ", ""), mode)
        W.split(a)  # asserts the result is pronounceable in the language
        hit = forms.get(a) or keys.get(W.INV.content_key(W.split(a)))
        clash += bool(hit)
        print(f"{name:18} {a:16} {'= ' + hit if hit else ''}")
    print(f"{clash} of {len(NAMES)} adapted names sound like an existing word")
