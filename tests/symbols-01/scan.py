"""Find Wiktionary entries (kaikki.org extracts) in the panel languages whose senses name a symbol.

  python3 scan.py              # prints lang, word, gloss for every matching sense -> stdout

Source: kaikki.org per-language Wiktionary extracts, cached by the coverage run in
~/work/cache/coverage/kaikki-LANG.jsonl.gz (fetched 2026-10-13). Working tool for this test only.
"""
import gzip, json, os, re

CACHE = os.path.expanduser("~/work/cache/coverage")
LANGS = ["Chinese", "Japanese", "Korean", "Vietnamese", "Thai", "Indonesian", "Tagalog", "Hindi", "Bengali", "Tamil",
         "Persian", "Arabic", "Turkish", "Russian", "Spanish", "French", "Swahili", "Hausa", "Yoruba", "Quechua"]
PAT = {
    "@": r"(@|\bat sign|\bat symbol|commercial at)",
    "dot": r"(\bdot\b.*(url|address|domain|e-?mail|internet)|(url|address|domain|e-?mail).*\bdot\b|\bfull stop\b|\bperiod \(punctuation|punctuation mark ⟨\.⟩)",
    "slash": r"(\bslash\b|\bsolidus\b|\boblique\b.*(stroke|mark|line)|⟨/⟩|\(/\))",
    "underscore": r"(\bunderscore\b|\bunderbar\b|⟨_⟩|\(_\))",
    "hyphen/dash": r"(\bhyphen\b|\bdash\b.*(symbol|punctuation|mark|character)|⟨-⟩)",
    "hash": r"(\bhash\b|\bnumber sign\b|\bpound sign\b|\bhashtag\b|\boctothorpe\b|⟨#⟩|\(#\))",
    "asterisk": r"(\basterisk\b|⟨\*⟩|\(\*\))",
    "ampersand": r"(\bampersand\b|⟨&⟩|\(&\))",
    "plus": r"(\bplus\b|⟨\+⟩|\(\+\))",
    "minus": r"(\bminus\b|⟨−⟩)",
    "times": r"(\btimes\b.*multipl|multiplied by|multiplication sign|⟨×⟩)",
    "divided": r"(divided by|division sign|\bobelus\b|⟨÷⟩)",
    "equals": r"(\bequals\b|equals sign|equal sign|⟨=⟩|\bis equal to\b)",
    "percent": r"(\bpercent\b|\bper cent\b|⟨%⟩)",
    "www": r"(\bwww\b|world wide web|\bdouble u\b|\bdouble-u\b|letter W\b)",
    "com": r"(\.com\b|dot-?com)",
}
RX = {k: re.compile(v, re.I) for k, v in PAT.items()}

if __name__ == "__main__":
    for lang in LANGS:
        path = os.path.join(CACHE, f"kaikki-{lang}.jsonl.gz")
        for line in gzip.open(path, "rt"):
            e = json.loads(line)
            for s in e.get("senses", []):
                g = " / ".join(s.get("glosses", []))
                for k, rx in RX.items():
                    if rx.search(g) and len(g) < 200:
                        ipa = next((x["ipa"] for x in e.get("sounds", []) if "ipa" in x), "")
                        print(f"{k}\t{lang}\t{e['word']}\t{e.get('pos','')}\t{ipa}\t{g}")
