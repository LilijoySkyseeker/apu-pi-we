"""Find Wiktionary entries (kaikki.org extracts) in the panel languages whose senses name a tested concept.

  python3 scan.py [CONCEPT ...]    # prints concept, lang, word, ipa, tags, flags, gloss -> stdout

A sense is listed when its first gloss starts with one of the concept's English words (so "mother" finds
"mother", "mom (childish)", but not "a mother's love"). Flags: N = the sense or entry is tagged childish,
baby talk, hypocoristic, informal or colloquial; O = the etymology says onomatopoeic, imitative or
echoic. Source: kaikki.org per-language Wiktionary extracts, cached by the coverage run in
~/work/cache/coverage/kaikki-LANG.jsonl.gz (fetched 2026-10-13). Working tool for this test only.
"""
import gzip, json, os, re, sys

CACHE = os.path.expanduser("~/work/cache/coverage")
LANGS = ["Chinese", "Japanese", "Korean", "Vietnamese", "Thai", "Indonesian", "Tagalog", "Hindi", "Bengali", "Tamil",
         "Persian", "Arabic", "Turkish", "Russian", "Spanish", "French", "Swahili", "Hausa", "Yoruba", "Quechua"]
C = {
    "cat": r"(domestic )?cats?\b|kitty|pussy ?cat|puss\b|meow|miaow",
    "cow": r"cows?\b|cattle|moo\b|moo-cow",
    "duck": r"ducks?\b|quack",
    "sheep": r"sheep|lamb\b|baa\b",
    "goat": r"goats?\b",
    "dog": r"dogs?\b|doggy|doggie|puppy|bow-?wow|woof",
    "bird": r"birds?\b|birdie|chirp|tweet|cheep|peep",
    "frog": r"frogs?\b|toad|croak|ribbit",
    "bee": r"bees?\b|honeybee|buzz",
    "owl": r"owls?\b|hoot",
    "cuckoo": r"cuckoo",
    "chicken": r"chicken|rooster|cock\b|hen\b|chick\b|cock-a-doodle|cluck",
    "wolf": r"wolf|wolves|howl",
    "pig": r"pigs?\b|piggy|swine|oink",
    "horse": r"horses?\b|horsey|neigh|gee-?gee",
    "mouse": r"mouse|mice|squeak",
    "crow": r"crows?\b|caw\b",
    "baby": r"baby|babies|infant|newborn",
    "mother": r"mother|mom\b|mum\b|mommy|mummy|mama\b|mamma|ma\b",
    "father": r"father|dad\b|daddy|papa\b|pa\b|pop\b",
    "grandmother": r"grand(mother|ma|mom|mum)|granny|gran\b|nan\b|nana\b|nanna",
    "grandfather": r"grand(father|pa|dad)|grampa|gramps",
    "kiss": r"kiss|smooch",
    "knock": r"knock|rap\b|tap\b",
    "laugh": r"laugh|giggle|ha ha|haha",
    "cry": r"cry\b|to cry|weep|sob\b|wail",
    "sneeze": r"sneez|achoo|atishoo",
    "cough": r"cough",
    "hiccup": r"hiccup|hiccough",
    "burp": r"burp|belch",
    "vomit": r"vomit|throw up|puke|barf",
    "sleep": r"sleep|nap\b|beddy|night-night|nighty",
    "eat": r"eat\b|to eat|food\b|yum|nom\b|meal",
    "pee": r"pee\b|wee\b|wee-wee|urinat|urine|piss|pee-pee",
    "poo": r"poo\b|poop|poo-poo|feces|faeces|defecat|excrement|shit\b|crap\b|dung",
    "bang": r"bang\b|boom\b|explo|blast\b|bam\b|pow\b",
    "yawn": r"yawn",
    "snore": r"snor",
}
NURSERY = re.compile(r"childish|baby[- ]talk|hypocoristic|informal|colloquial|endearing|familiar|nursery|"
                     r"child-directed|children'?s", re.I)
ONOM = re.compile(r"onomatop|imitative|echoic|mimetic|ideophon|sound of", re.I)


def ipa(e):
    return next((x["ipa"] for x in e.get("sounds", []) if "ipa" in x), "")


if __name__ == "__main__":
    want = sys.argv[1:] or list(C)
    RX = {k: re.compile(r"^(\(.*?\) )?(to |a |an |the )?(" + C[k] + ")", re.I) for k in want}
    for lang in LANGS:
        for line in gzip.open(os.path.join(CACHE, f"kaikki-{lang}.jsonl.gz"), "rt"):
            e = json.loads(line)
            ety = e.get("etymology_text", "")
            for s in e.get("senses", []):
                gl = s.get("glosses", [])
                if not gl or len(gl[0]) > 90:
                    continue
                tags = s.get("tags", []) + s.get("raw_tags", [])
                for k, rx in RX.items():
                    if rx.search(gl[0]):
                        flags = ("N" if NURSERY.search(" ".join(map(str, tags)) + " " + gl[0]) else "") + \
                                ("O" if ONOM.search(ety + " " + gl[0]) else "")
                        rom = next((f["form"] for f in e.get("forms", []) if "romanization" in f.get("tags", [])), "")
                        print(f"{k}\t{lang}\t{e['word']}\t{rom}\t{ipa(e)}\t{e.get('pos','')}\t"
                              f"{','.join(map(str, tags))}\t{flags}\t{' / '.join(gl)[:140]}")
