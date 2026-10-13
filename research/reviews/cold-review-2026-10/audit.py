"""Audit a review agent's transcript: files it touched, web searches and URLs.
usage: python audit.py TRANSCRIPT ALLOWED_DIR [ALLOWED_DIR ...]
Flags any file path outside the allowed directories and any search or URL mentioning the language."""
import json, sys, re
path, allowed = sys.argv[1], sys.argv[2:] + ["/home/agent/work/apupiwe-review/prompts", "/home/agent/work/apupiwe-review/reports"]
LEAK = re.compile(r"apupiwe|apu.?pi.?we|universal-language|lilijoyskyseeker", re.I)
files, flags, searches, urls = set(), [], [], []
for line in open(path, errors="replace"):
    try: d = json.loads(line)
    except Exception: continue
    c = d.get("message", {}).get("content")
    if not isinstance(c, list): continue
    for x in c:
        if not (isinstance(x, dict) and x.get("type") == "tool_use"): continue
        i, n = x.get("input", {}), x.get("name")
        text = json.dumps(i)
        for p in re.findall(r"/home/agent/[^\s\"'\\)]*", text):
            files.add(p)
            if not any(p.startswith(a) for a in allowed): flags.append(f"{n}: outside allowed: {p}")
        if n == "WebSearch": searches.append(i.get("query"))
        if n == "WebFetch": urls.append(i.get("url"))
        if LEAK.search(text) and n in ("WebSearch", "WebFetch"): flags.append(f"{n}: mentions the language: {text[:200]}")
print("files:", *sorted(files), sep="\n  ")
print("searches:", len(searches), " urls:", len(urls))
for u in urls: print("  ", u)
print("FLAGS:" if flags else "no flags", *flags, sep="\n  ")
