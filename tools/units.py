"""Carry the senary measurement units into the lexicon (2026-10-08).

The senary repo (~/work/repos/senary) owns the quantities: definitions and values. This repo
owns the words. Each unit keeps its senary name where the name survives this language's
rules after adapting sounds the language lacks (r -> l, v -> w, z -> s). Otherwise the
optimizer picks a new form. Writes data/units.tsv and adds the words to data/lexicon.tsv.

  python units.py
"""
import math
import words as W

# A kept name must be no more confusable than the 90th percentile of ordinary words (measured 2026-10-08).
MAX_CONFUSION = 0.0032

# senary name, quantity, approximate SI value (from senary_tables.py r19), tier
UNITS = [
    ("Kena", "time", "0.3086 s (day / 6^7)", 4),
    ("Nira", "length", "1.530 m", 4),
    ("Woba", "mass", "1.513 kg", 4),
    ("Vema", "charge", "0.7592 C", 2),
    ("Buda", "temperature interval", "2.031 K", 3),
    ("Faga", "angle", "1 turn", 3),
    ("Beva", "frequency", "3.24 Hz (1 cycle per Kena)", 2),
    ("Wida", "force", "24.30 N", 2),
    ("Fuka", "pressure", "10.38 Pa", 2),
    ("Koda", "energy", "37.19 J", 3),
    ("Noza", "power", "120.5 W", 3),
    ("Kiwa", "voltage", "48.99 V", 2),
    ("Nawa", "resistance", "19.92 ohm", 1),
    ("Wela", "capacitance", "0.01550 F", 1),
    ("Fiba", "inductance", "6.147 H", 1),
    ("Bora", "magnetic flux density", "6.457 T", 1),
    ("Vona", "temperature scale", "t/Vo = T/Bu - 134.5", 3),
    ("Vuta", "information", "ln 6 natural units (one senary digit)", 2),
    ("Kuza", "count of entities", "6^34 entities (role of the mole)", 1),
    ("Neta", "particle mass", "6^-34 Woba", 1),
]
ADAPT = str.maketrans({"r": "l", "v": "w", "z": "s"})


def try_keep(form, lexicon, digits):
    """Accept the adapted senary name if it passes the rules new content words must pass."""
    try:
        sy = W.split(form)
    except (AssertionError, KeyError):
        return "uses a syllable the language lacks"
    if sy[0] in digits:
        return "begins with a digit syllable"
    if any(W.INV.syl[s][0] == "" for s in sy[1:]):
        return "vowel-only later syllable"
    keys = {W.INV.content_key(W.split(w["form"])): w["gloss"] for w in lexicon}
    k = W.INV.content_key(sy)
    if k in keys:
        return f"would merge with '{keys[k]}' after drift"
    worst, near = 0.0, ""
    for w in lexicon:
        o = W.split(w["form"])
        if len(o) == len(sy):
            p = math.prod(W.S[a, b] for a, b in zip(sy, o)) + math.prod(W.S[b, a] for a, b in zip(sy, o))
            if p > worst:
                worst, near = p, w["gloss"]
    if worst > MAX_CONFUSION:
        return f"too easily misheard as '{near}' ({worst:.3f})"
    return None


def main():
    digits = W.digit_syllables()
    rows = []
    for name, qty, si, tier in UNITS:
        lexicon = W.read("lexicon.tsv")
        adapted = name.lower().translate(ADAPT)
        why = try_keep(adapted, lexicon, digits)
        if why is None:
            lexicon.append({"gloss": name, "field": "unit", "tier": tier, "form": adapted})
            W.write("lexicon.tsv", lexicon, ["gloss", "field", "tier", "form"])
            form, how = adapted, "kept" if adapted == name.lower() else f"adapted from {name}"
        else:
            W.add_content(name, "unit", tier)
            form = next(w["form"] for w in W.read("lexicon.tsv") if w["gloss"] == name)
            how = f"new ({adapted}: {why})"
        rows.append({"senary": name, "quantity": qty, "si": si, "form": form, "how": how})
        print(f"{name:5} {qty:22} -> {form:7} {how}")
    W.write("units.tsv", rows, ["senary", "quantity", "si", "form", "how"])


if __name__ == "__main__":
    main()
