"""Fetch the 20-language panel from English Wiktionary translation tables.

  python3 panel.py PAGE[#BLOCK] ...   # prints translation blocks (those whose name contains BLOCK)

Source of every entry: https://en.wiktionary.org/wiki/PAGE#Translations (the block named).
Cache in /tmp/wikt/. Working tool for loans.md, not part of the language's tooling.
"""
import os, re, sys, urllib.parse, urllib.request

PANEL = [("Mandarin", "cmn"), ("Japanese", "ja"), ("Korean", "ko"), ("Vietnamese", "vi"), ("Thai", "th"),
         ("Indonesian", "id"), ("Tagalog", "tl"), ("Hindi", "hi"), ("Bengali", "bn"), ("Tamil", "ta"),
         ("Persian", "fa"), ("Arabic", "ar"), ("Turkish", "tr"), ("Russian", "ru"), ("Spanish", "es"),
         ("French", "fr"), ("Swahili", "sw"), ("Hausa", "ha"), ("Yoruba", "yo"), ("Quechua", "qu")]
CODES = {c for _, c in PANEL}
CACHE = "/tmp/wikt"


def raw(title):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, title.replace("/", "__"))
    if not os.path.exists(path):
        url = "https://en.wiktionary.org/w/index.php?action=raw&title=" + urllib.parse.quote(title)
        req = urllib.request.Request(url, headers={"User-Agent": "apupiwe-research/0.1"})
        try:
            data = urllib.request.urlopen(req, timeout=30).read().decode()
        except Exception as e:
            data = ""
        open(path, "w").write(data)
    return open(path).read()


T = re.compile(r"\{\{tt?\+?\|([a-z-]+)\|([^}]*)\}\}")


def entries(line):
    out = []
    for code, rest in T.findall(line):
        code = {"fa-ira": "fa", "prs": "fa"}.get(code, code)
        if code not in CODES:
            continue
        parts = rest.split("|")
        word = parts[0]
        tr = [p[3:] for p in parts[1:] if p.startswith("tr=")]
        out.append((code, word + (f" ({tr[0]})" if tr else "")))
    return out


def blocks(title):
    text = raw(title)
    if "{{see translation subpage" in text or "{{trans-see" in text and not "{{trans-top" in text:
        text += raw(title + "/translations")
    out, cur, name = [], None, None
    for line in text.splitlines():
        m = re.match(r"\{\{(?:trans-top-see|trans-top|checktrans-top)(?:\|(?:id=[^|}]*\|)?([^}]*))?\}\}", line)
        if m:
            cur, name = {}, (m.group(1) or "(unchecked)")
            continue
        if line.startswith("{{trans-bottom") and cur is not None:
            out.append((name, cur)); cur = None; continue
        if cur is not None:
            for code, w in entries(line):
                cur.setdefault(code, []).append(w)
    return out


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        page, _, want = arg.partition("#")
        print(f"=== {page}")
        for name, d in blocks(page):
            if want and want not in name:
                continue
            n = sum(1 for _, c in PANEL if c in d)
            print(f"--- [{name}] ({n}/20 panel languages present)")
            for lang, c in PANEL:
                if c in d:
                    print(f"  {lang}: {', '.join(d[c][:4])}")
