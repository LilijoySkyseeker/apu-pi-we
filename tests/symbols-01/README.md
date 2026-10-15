# Symbol names through the loan panel (symbols-01)

Proposals only; no word was changed. Task: `PROMPT.md`. Decision behind it: design log 2026-10-15, "Spelling aloud: the ICAO alphabet, adapted" (symbols go through the L4 panel; where no world-shared name passes, they are described with existing words). Roadmap item: "Symbol names through the loan panel".

## Question

For each symbol people read aloud (@, the dot in addresses, / \ _ - # * & + − × ÷ = %, "www", ".com"), is there a spoken name the world already shares (goal L4: borrow only where the world shares the form)? Where yes, what is its adapted form; where no, what description from existing words would do (a proposal for the author)?

## Method

The panel method of `tests/coverage-01/part3/loans.md` ("Method" and the author's decisions at its top), unchanged:

- For each symbol I recorded the everyday spoken name in each of the 20 panel languages, and whether a speaker would hear it as the same word as the international form tested (the `form` column). Translations and calques don't count. For symbols, "everyday" means how people say it when reading an email address, a URL or a sum aloud.
- **Pass:** at least 12 of 20, across at least 4 of the 7 regions EA (zh ja ko), SEA (vi th id tl), SA (hi bn ta), WA (fa ar tr), EU (ru es fr), SSA (sw ha yo), AM (qu).
- **Author's rules applied** (2026-10-13): an everyday loan beside a formal native word counts, with a source (pattern 1); memory columns need a source, so a pass that needs a memory-only column fails ("thin deciding columns fail", pattern 2); two shapes are one form when their adapted consonants are the same (pattern 3: Spanish *menos* counts with *minus*, French *moins* doesn't; *at the rate* is not *at*); the five-times rival rule, applied only where the rival names the same thing (a broad rival such as Spanish *etiqueta* "label" against *hashtag* leaves the column as listed); median ties by regions, then length; shared short forms preferred.
- **One reading of my own, flagged:** a generic classifier after the name doesn't make a new form (Japanese *atto māku* "at mark" counts as *at*, as "plus sign" would count as "plus").
- **Counts** are computed by `emit.py` from `panel.tsv`: *sourced* (the verdict), *with memory* (adds memory-only columns), *lenient* (adds the "✗ (✓ lenient)" columns).

### Sources (column `src`)

- **Wt**: English Wiktionary translation tables, fetched 2026-10-15 with `tests/lexicon-ladder-01/panel.py` (pages: at sign, dot "dot in URLs or email addresses", slash, backslash, underscore, underline, hyphen, dash, hash "the # symbol", hashtag, asterisk, star, ampersand, plus, plus sign, minus, minus sign, times, multiply, multiplication sign, divide, division sign, equal, equal sign, percent, double-u, World Wide Web).
- **We**: the Wiktionary entry for the foreign word, from the kaikki.org extracts cached by the coverage run (`~/work/cache/coverage/kaikki-*.jsonl.gz`); `scan.py` lists every sense that names a symbol.
- **Wp**: Wikipedia. The English article [At sign](https://en.wikipedia.org/wiki/At_sign), section "Names in other languages" (fetched 2026-10-15), and the titles of the panel languages' own articles, from the language links of the English articles At sign, Slash (punctuation), Backslash, Underscore, Hyphen, Dash, Number sign, Hashtag, Asterisk, Plus and minus signs, Multiplication sign, Division sign, Equals sign, Percent sign, .com, Dot-com bubble and Dot-com company (e.g. Korean *닷컴 버블*, Persian *حباب دات-کام*, Bengali *.কম*).
- **Sub**: token counts in the OpenSubtitles 50k frequency lists (`~/work/cache/coverage/subs/`, 16 languages; the Japanese list is unusable for katakana words). Subtitles are written speech, so they also serve the rival rule.
- **Lz**: Leipzig community-2017 sentence corpora for Thai, Swahili, Hausa, Yoruba and Quechua (`~/work/cache/coverage/*_community_2017.tar.gz`).
- **Web** (each read 2026-10-15):
  - banjirembun: [Arti dan Fungsi Tanda @ Pada Alamat Email](https://www.banjirembun.com/2020/04/arti-dan-fungsi-tanda-pada-alamat-email.html) (Indonesian: @ "diucapkan 'et'", "banjirembun(et)banjirembun(dot)com").
  - haberler: [Et işareti](https://www.haberler.com/soguk-haber/et-isareti-klavyeden-et-isareti-nasil-13496779-haberi/) (Turkish: "mailadresim et gmail nokta kom").
  - hankook: [‘닷컴’ 그리고 ‘쩜콤’](https://www.hankookilbo.com/News/Read/200003070014187713), Hankook Ilbo 2000-03-07 (Korean TV ads say both *닷컴* and *쩜콤*).
  - morningside: [Indian English 101](https://www.morningtrans.com/indian-english-101/) ("At the rate = the @ sign. … Sirena at the rate Morningside dot com").
- **M**: from memory. **M\***: Wiktionary lists the word, but my judgment of the everyday word differs from its first-listed one.

Web pages were fetched with a generic User-Agent. Searching for sources on how Tagalog, Swahili, Hausa and Yoruba speakers read an address aloud found nothing usable (Leipzig has no spelled-out addresses; style guides only describe writing), so those columns stay M.

### Forms

Passing forms: median pronunciation of the cognate forms in broad IPA, adapted with `tools/names.py`, then checked with `check.py` (this folder) against `data/lexicon.tsv`, `data/grammar.tsv` and `data/numbers.tsv` (same form or same content key, as `names.py` does), the spelling-alphabet words in `docs/language.md` 11.5, and `tools/offensive.py` (`blocked`, `matches`). The same check is given for the near-misses, so a later sourcing can adopt them directly.

## Results

| Symbol | Tested form | Sourced (verdict) | With memory | Verdict | Form, or proposed description |
|---|---|---|---|---|---|
| .com | com | 14/20, 6 regions | 20, 7 | **pass** | **komu** [kom]; the dot before it as for "dot" |
| hashtag (# before a tag) | hashtag | 13/20, 5 | 19, 7 | **pass** | **asutagu** [haʃtag] |
| @ | at | 8/20, 4 | 12, 5 | fail, near miss (needs tl sw ha yo sourced) | proposal: **mon** "at"; if sourced: **etu** [et] |
| . (in addresses) | dot | 10/20, 5 | 13, 5 | fail, near miss (needs 2 of tl ha yo) | proposal: the queued root POINT (ladder 268), **mimi** "point" until it has a form; if sourced: **dotu** [dot] |
| www | double-u | 8/20, 4 | 12, 5 | fail, near miss (needs ta fa sw ha) | proposal: spell it, **wisuki wisuki wisuki** (11.5), or leave it out in speech |
| / | slash | 5/20, 4 | 10, 6 | fail | proposal: LINE (queued root, ladder 271) |
| \ | backslash | 3/20, 3 | 9, 5 | fail | proposal: LINE **nebe** "back line" |
| _ | underscore | 1/20, 1 | 6, 3 | fail | proposal: LINE **linku** "low line" |
| - | dash (also hyphen, tire) | 2/20, 1 | 6, 3 | fail | proposal: LINE **eten** "short line" |
| # (the sign) | hash | 1/20, 1 | 5, 2 | fail | proposal: **asutagu** before a tag; **mena** before a number (#3 = **mena ka**); key name open |
| * | asterisk | 3/20, 2 | 4, 3 | fail | proposal: **uwan** "star" |
| & | ampersand | 10/20, 6 | 10, 6 | fail | proposal: **yen** "and" |
| + | plus | 7/20, 3 | 7, 3 | fail | proposal: **ginni** "add" |
| − | minus | 4/20, 2 | 4, 2 | fail | proposal: **guti** (already the minus word, 9.2.4) |
| × | times | 0/20 | 0 | fail | proposal: **gimu** "occasion, time" |
| ÷ | divided by | 2/20, 1 | 2, 1 | fail | proposal: the queued root DIVIDE (ladder 533); **buyan** "split" only as a stopgap |
| = | equals | 2/20, 1 | 2, 1 | fail | proposal: **gun** "is" in a spoken equation; **kige** "same" to name the sign |
| % | percent | 8/20, 3 | 9, 4 | fail | no shared spoken name; the native root decided 2026-10-13 stands |

**Count:** 2 pass (com, hashtag), 3 near misses that pass only with memory columns (@, dot, www), 13 fail.

### The passes

- **com → *komu*.** Every panel language says the domain ending as one syllable [kom] after its own word for the dot: *punto com*, *point com*, *nokta kom*, *точка ком*, *chấm com*, *닷컴*/*쩜콤*, *ดอท คอม*, *dot com*. All forms agree on [kom], so there is no median question. `check.py`: no word or spelling-alphabet clash; an offensive tie-break match only (English and Spanish *cum*), not blocked. The thinnest sourced column is Tamil (one subtitle token); without it the count is still 13. Other endings (*.org*, *.net*) presumably work the same way (said as one syllable where the letters allow it); not tested.
- **hashtag → *asutagu*.** The tag word, which in social-media use also names the sign in front of a tag ("hashtag blessed"). Median [haʃtag]: vowel a in 10 of the 13 sourced forms (ɛ in ko th ru), final g over k. `check.py`: clear. The thinnest sourced columns are Tagalog and Bengali (their Wikipedias' article titles only); without both, 11, so the pass rests on accepting a Wikipedia title as a source. Rivals: the official coinages Indonesian *tagar* and French *mot-dièse* lose to *hashtag* in the subtitle lists (*tagar* 0 against *hashtag* 34); Spanish *etiqueta*, Turkish *etiket* and Russian *метка* are broad words ("label", "mark"), so they don't trigger the rival rule. Mandarin is the only clear native holdout (话题标签).

### The near misses: what would flip them

All three have spoken English behind them across Asia and the Middle East, and fail on the usual memory columns (Tagalog and the African languages), as half the coverage passes did before sourcing.

- **@ (*at*):** sourced in zh (艾特), ja, th, id (*et*), hi, fa, ar, tr (*et*): 8 in 4 regions. Tagalog, Swahili, Hausa and Yoruba speakers read addresses in English and say "at"; none is sourced. All four are needed. South Asia's own form is Indian English *at the rate* (sourced), a longer phrase that pattern 3 keeps apart; counting it (bn ta) would give 10 sourced. If it passes: median [et] (th id hi fa tr against zh ja ar) → **etu**, clear in `check.py`.
- **dot:** 10 sourced in 5 regions (ja ko th id hi bn ta fa ar sw). Two of Tagalog, Hausa, Yoruba are needed. Two sourced columns are thin: Tamil (2 subtitle tokens) and Swahili (the word *dotcom* in "kizazi cha dotcom", not an address read aloud). If it passes: **dotu**; offensive tie-break matches only (Hindi *chod*, Spanish *toto* and others, near), not blocked.
- **www (*double-u*):** 8 sourced (zh *sān dǎbùliù*, ja ko th tl hi bn ar). Even if Tamil, Persian, Swahili and Hausa were sourced, the loan would be **dabaluyu** three times, 12 syllables for a prefix most sites no longer need, and the letter W already has its word (**wisuki**, 11.5). Recommendation: don't pursue it.

Whether to buy the sourcing is a C1-style cost question for the author: @ needs four columns, dot two. The descriptions below work without it.

### Proposals for the failures (author decides)

Each proposal is the build most panel languages use, made from words the language has. Where the build needs a root the coverage batch has queued but not yet formed, it says so; no root is coined here.

- **@ → mon "at".** The panel's majority name is literally "at" (8 sourced, Esperanto *ĉe* does the same), and **mon** is the grammar word AT: *mara@gmail.com* → **mara mon gmail mimi komu**. The other names (dog, snail, whelk, little mouse, bent a, arroba) share nothing.
- **. → POINT.** Every panel language without the loan says its own word for "point, dot": *diǎn, jeom, chấm, titik, tuldok, nokta, nuqṭa, точка, punto, point, nukta*. The coverage ladder queues a root "point, dot" (row 268) and keeps **mimi** for the decimal point. Until POINT has a form, **mimi** works, as Mandarin 点 and Spanish *punto* serve both.
- **/ \ _ -: one LINE root with modifiers.** The panel names these as kinds of line: "slant line" for / (zh 斜线, ja 斜線, ko 빗금, id *garis miring*, ar *ḵaṭṭ māʾil*, tr *eğik çizgi*, ru *косая черта*, fr *barre oblique*); "reverse/back slant" for \ (zh 反斜线, ko 역슬래시, ru *обратная косая*, es *barra invertida*, tr *ters bölü*; ja th fa borrow *backslash*); "under/low line" for _ (zh 下划线, ko 밑줄, ta *aṭikkōṭu*, tr *alt çizgi*, fa *zir-xatt*, id *garis bawah*, es *guion bajo*, fr *tiret bas*, ar *šarṭa sufliyya*); "short line/stroke" for - (tr *kısa çizgi*, ru *чёрточка*, vi *gạch*, th *khìit*). The language has no "line" yet; the coverage ladder queues it (row 271, "line, stripe, row"). Proposed: / **LINE**, \ **LINE nebe** "back line", _ **LINE linku** "low line", - **LINE eten** "short line". The panel's "slant" has no word, so / is the unmarked line; a slant word would be a new root, not proposed.
- **# → asutagu / mena.** No shared name for the sign itself (hash, sharp, well, grid, fence, square, window, cushion). Before a tag it is the hashtag loan; before a number it means "number", which the language already says with **mena** (*#3* = **mena ka**, as *kemin mena sa* "document 2"). The phone key needs a name only if the author wants one; open.
- **\* → uwan "star".** The panel's own build in 11 languages (zh 星号, ko 별표, vi *dấu sao*, id *tanda bintang*, hi *tārak*, ta *uṭukkuṟi*, fa *setāre*, ar *nujayma*, tr *yıldız*, ru *звёздочка*; fr *étoile* on phone keys).
- **& → yen "and".** People read & as their "and" (vi *ký hiệu "và"*, ta "and mark", tr *ve imi*, id *tanda dan*, es *y comercial*, fr *et commercial*, zh 和号). *Ampersand* is listed in 10 Wiktionary tables but as a dictionary name; it fails even counted.
- **+ → ginni "add"**, **− → guti**, **× → gimu**, **÷ → DIVIDE**, **= → gun / kige.** Arithmetic is where the panel is most native: "add" (zh 加, ja 足す, ko 더하기, vi *cộng*, th *bùak*, id *tambah*, tl *dagdag*), "take away" (zh 减, ja 引く, vi *trừ*, id *kurang*, tl *bawas*, tr *eksi*), "times" as occasions (id *kali*, tr *kere*, fr *fois*, sw *mara*, ha *sau*), "divide/share" (vi *chia*, id *bagi*, sw *gawanya*, ko 나누기), and for = either a copula or topic marker (ko 는, ja は, tl *ay*, sw *ni*) or "same/equal" (id *sama dengan*, vi *bằng*). **guti** already is the minus word (9.2.4); **ginni** "add, put in more" and **gimu** "occasion" exist. "2 + 3 = 5" → **sa ginni ka gun te**. For ÷ the ladder queues DIVIDE (row 533) and separates it from **buyan** "split, break apart", so **buyan** is only a stopgap. Open for the author: the word order of a product (**gimu sa** is "twice", so "3 × 4" could be **ka gimu da** or **da gimu ka**), and whether **guti** between two numbers (*te guti ka* "5 − 3") can be confused with a negative number.
- **% →** the native root decided 2026-10-13 stands. The loan has 8 sourced columns (ja ko th id tl ru es fr); spoken *parsent* in Hindi, Bengali and Tamil fails the rival rule in the subtitles (Bengali native words 59 against 6, Hindi 32 against 0), and Swahili *asilimia* beats *pasenti* 2759 to 3 in Leipzig.

### Findings along the way

1. **Internet addresses are where the world shares most**, and the shared part is spoken English: *com*, *hashtag*, and nearly *at* and *dot*. Arithmetic is the opposite: almost every panel language uses native verbs.
2. **The deciding columns are again Tagalog, Swahili, Hausa and Yoruba**, as in the coverage run. For reading addresses aloud, text corpora barely help (people write the symbol, not its name); a short question to one speaker of each would settle @ and dot.
3. **Four symbol descriptions need the queued root LINE**, and the dot needs POINT. Both are in the coverage batch already; this test adds a use for them, not a new requirement.
4. **One reading of mine to confirm:** Japanese *atto māku* counted as *at* (a classifier after the name doesn't make a new form). It doesn't change any verdict: without it @ has 7 sourced columns instead of 8.
5. **To track in `docs/roadmap.md`** (not edited here; this test changes nothing outside its folder): the author's decisions on the two passes and the proposals; whether to source @ and dot; the product word order; the forms of LINE, POINT and DIVIDE now carry symbol uses.

## Files

- `panel.tsv`: one row per symbol and language (symbol, form tested, language, everyday word, shared, source, note).
- `emit.py`: counts and the tables below (`python3 emit.py counts`, `python3 emit.py tables`).
- `scan.py`: lists kaikki Wiktionary senses in the panel languages that name a symbol.
- `check.py`: checks adapted forms against the language's words, the spelling alphabet and `offensive.py`.

Re-run inside the dev shell: `direnv exec <repo> python3 tests/symbols-01/emit.py counts`.

## Per-symbol evidence

Legend: ✓ the same word as the tested form, ✗ not; "✗ (✓ lenient)" an everyday loan beside a native word without a source for its everyday use, or a longer form built on the tested one. Romanisation is mine where the source gives none.

#### `@` (at)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 艾特 àitè (mainland, younger speakers); 小老鼠 xiǎo lǎoshǔ (Taiwan), 圈a | ✓ | Wp, We | Wp: "for most of China's youth" 艾特; We 艾特 "from English at" |
| Japanese | アットマーク atto māku "at mark"; アット in addresses | ✓ | Wt, Wp | "mark" is a classifier, the name is at |
| Korean | 골뱅이 golbaengi "whelk" | ✗ | Wt, Wp |  |
| Vietnamese | a còng, a móc "bent/hooked a" | ✗ | Wt, Wp |  |
| Thai | แอท [ʔɛ́t] | ✓ | Wp |  |
| Indonesian | et | ✓ | Wp, Web:banjirembun | a bundar etc. in noise |
| Tagalog | at (English, in Taglish) | ✓ | M | Wp: @ is written for Tagalog at "and"; no source for the spoken name |
| Hindi | एट [ɛʈ] | ✓ | Wp | hi.wikipedia title एट चिह्न; Indian English also "at the rate" |
| Bengali | হারে "at a rate" (calque); spoken "at the rate" | ✗ (✓ lenient) | Wp, Web:morningside | "at the rate" is a longer form (pattern 3: other consonants) |
| Tamil | வீதக் குறி "rate sign" (calque); spoken "at the rate" | ✗ (✓ lenient) | Wp, Web:morningside | as Bengali |
| Persian | ات [et] | ✓ | Wp | fa.wikipedia title ات ساین |
| Arabic | آت [ʔat] | ✓ | Wt, Wp |  |
| Turkish | et | ✓ | Wp, Web:haberler | "mailadresim et gmail nokta kom"; Wt lists only kuyruklu a, güzel a |
| Russian | собака sobaka "dog" | ✗ | Wt, We, Wp |  |
| Spanish | arroba | ✗ | Wt, We, Wp |  |
| French | arobase (younger speakers "at") | ✗ (✓ lenient) | Wt, We, Wp | Wp's "at" is marked citation needed |
| Swahili | at | ✓ | M |  |
| Hausa | at | ✓ | M |  |
| Yoruba | at | ✓ | M |  |
| Quechua | arroba (Spanish) | ✗ | M |  |

Sourced 8/20 in 4 regions; with memory columns 12/5; lenient 15/6.

#### `dot` (dot)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 点 diǎn | ✗ | Wt |  |
| Japanese | ドット dotto | ✓ | Wt, We |  |
| Korean | 닷 dat (닷컴), also 점 jeom | ✓ | Web:hankook, Wp | Hankook Ilbo 2000: TV ads say both 닷컴 and 쩜콤 (jeom); ko title 닷컴 버블; Wt lists only 점 |
| Vietnamese | chấm | ✗ | Wt |  |
| Thai | ดอท [dɔ́t] | ✓ | Lz, Wp | Leipzig "สนุก ดอท คอม"; th title ...ดอตคอม |
| Indonesian | dot (titik also) | ✓ | Web:banjirembun, Wp | id title Gelembung dot-com |
| Tagalog | dot (tuldok in writing) | ✓ | M | tagaloglang.com gives only the transliteration dát |
| Hindi | डॉट | ✓ | Sub, Web:morningside | Sub 4 tokens |
| Bengali | ডট | ✓ | Sub, Wp | Sub 26; bn title ডট-কম বুদ্বুদ |
| Tamil | டாட் | ✓ | Sub | Sub 2 tokens (thin) |
| Persian | دات | ✓ | Sub, Wp | Sub 136; fa title حباب دات-کام |
| Arabic | دوت | ✓ | Wt, Sub | Wt first-listed; Sub 691 |
| Turkish | nokta | ✗ | Wt, Web:haberler |  |
| Russian | точка tochka | ✗ | Wt | Wt also lists дот; everyday is точка |
| Spanish | punto | ✗ | Wt |  |
| French | point | ✗ | Wt |  |
| Swahili | dot (dotcom) | ✓ | Lz | Leipzig "kizazi cha dotcom" (the word, not an address read aloud; thin) |
| Hausa | dot | ✓ | M |  |
| Yoruba | dot | ✓ | M |  |
| Quechua | punto (Spanish) | ✗ | M |  |

Sourced 10/20 in 5 regions; with memory columns 13/5; lenient 13/5.

#### `.com` (com)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | com (read in English) | ✓ | M |  |
| Japanese | コム (ドットコム) | ✓ | M |  |
| Korean | 컴 (닷컴) | ✓ | Web:hankook, Wp |  |
| Vietnamese | com (chấm com) | ✓ | Wp | vi title Công ty dot-com |
| Thai | คอม | ✓ | Lz, Wp |  |
| Indonesian | com | ✓ | Web:banjirembun, Sub, Wp |  |
| Tagalog | com | ✓ | M |  |
| Hindi | कॉम | ✓ | Sub, Web:morningside |  |
| Bengali | কম | ✓ | Wp | bn.wikipedia title .কম |
| Tamil | காம் | ✓ | Sub | Sub 1 token (thin) |
| Persian | کام | ✓ | Sub, Wp |  |
| Arabic | كوم | ✓ | Sub | Sub 648 (beside دوت 691) |
| Turkish | com [kom] | ✓ | Web:haberler, Sub, Wp | "nokta kom" |
| Russian | ком (точка ком) | ✓ | Wp | ru title Дотком; Пузырь доткомов |
| Spanish | com (punto com) | ✓ | We, Sub | We puntocom /puntoˈkom/ |
| French | com (point com) | ✓ | Wp, Sub | fr title Entreprise point com |
| Swahili | com (dotcom) | ✓ | Lz |  |
| Hausa | com | ✓ | M |  |
| Yoruba | com | ✓ | M |  |
| Quechua | com (punto com) | ✓ | M |  |

Sourced 14/20 in 6 regions; with memory columns 20/7; lenient 20/7.

#### `/` (slash)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 斜杠 xiégàng "slant bar" | ✗ | Wt, We |  |
| Japanese | スラッシュ surasshu | ✓ | Wt, We, Wp |  |
| Korean | 슬래시 seullaesi (빗금 bitgeum) | ✓ | Wt, We |  |
| Vietnamese | gạch chéo; xẹt in house numbers | ✗ | Wt, We |  |
| Thai | ทับ thap "over" | ✗ | Wt, Wp |  |
| Indonesian | garis miring "slanted line" | ✗ | Wp |  |
| Tagalog | slash | ✓ | M |  |
| Hindi | स्लैश | ✓ | Wp | hi.wikipedia title |
| Bengali | স্ল্যাশ | ✓ | M |  |
| Tamil | ஸ்லாஷ் | ✓ | M |  |
| Persian | اسلش eslaš | ✓ | Wp | fa.wikipedia title |
| Arabic | خط مائل "slanted line" | ✗ | Wt, Wp |  |
| Turkish | eğik çizgi "slanted line", bölü | ✗ | Wt, Wp |  |
| Russian | слеш slesh | ✓ | Wt |  |
| Spanish | barra | ✗ (✓ lenient) | Wt | Wt also lists slash |
| French | barre oblique; slash in speech | ✗ (✓ lenient) | Wt, Sub | Sub slash 141 |
| Swahili | mkwaju "stick" | ✗ | Wt, Wp |  |
| Hausa | slash | ✓ | M |  |
| Yoruba | slash | ✓ | M |  |
| Quechua | barra (Spanish) | ✗ | M |  |

Sourced 5/20 in 4 regions; with memory columns 10/6; lenient 12/6.

#### `\` (backslash)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 反斜杠 "reverse slant bar" | ✗ | Wt |  |
| Japanese | バックスラッシュ | ✓ | Wt, Wp |  |
| Korean | 역슬래시 "reverse slash" | ✗ | Wt, Wp | half calque; other consonants |
| Vietnamese | gạch chéo ngược | ✗ | M |  |
| Thai | แบ็กสแลช | ✓ | Wt, Wp |  |
| Indonesian | garis miring terbalik | ✗ | Wp |  |
| Tagalog | backslash | ✓ | M |  |
| Hindi | backslash | ✓ | M |  |
| Bengali | backslash | ✓ | M |  |
| Tamil | backslash | ✓ | M |  |
| Persian | بک‌اسلش | ✓ | Wp | fa.wikipedia title |
| Arabic | مائلة معاكسة "reverse slant" | ✗ | Wt, Wp |  |
| Turkish | ters bölü | ✗ | Wt |  |
| Russian | обратная косая (бэкслэш) | ✗ (✓ lenient) | Wt |  |
| Spanish | barra invertida | ✗ | Wt |  |
| French | antislash, barre oblique inversée | ✗ (✓ lenient) | Wt |  |
| Swahili | (no data) | ✗ | M |  |
| Hausa | backslash | ✓ | M |  |
| Yoruba | backslash | ✓ | M |  |
| Quechua | barra invertida (Spanish) | ✗ | M |  |

Sourced 3/20 in 3 regions; with memory columns 9/5; lenient 11/6.

#### `_` (underscore)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 下划线 "under line" | ✗ | Wt, We |  |
| Japanese | アンダーバー andābā "under bar" (アンダースコア) | ✗ (✓ lenient) | Wt, We | underbar is another shape |
| Korean | 언더바 eondeoba "under bar", 밑줄 | ✗ | Wt |  |
| Vietnamese | gạch dưới "under stroke" | ✗ | M |  |
| Thai | เส้นใต้ "under line" | ✗ | Wp |  |
| Indonesian | underscore | ✓ | Wt |  |
| Tagalog | underscore | ✓ | M |  |
| Hindi | underscore | ✓ | M |  |
| Bengali | underscore | ✓ | M |  |
| Tamil | அடிக்கோடு "bottom line" | ✗ | Wt, We |  |
| Persian | زیرخط "under line" | ✗ | Wp |  |
| Arabic | شرطة سفلية "low dash" | ✗ | Wp |  |
| Turkish | alt çizgi "bottom line" | ✗ | Wt |  |
| Russian | подчёркивание | ✗ | Wt |  |
| Spanish | guion bajo "low dash" | ✗ | Wt, We |  |
| French | tiret bas "low dash" | ✗ | Wt, We |  |
| Swahili | (no data) | ✗ | M |  |
| Hausa | underscore | ✓ | M |  |
| Yoruba | underscore | ✓ | M |  |
| Quechua | guion bajo (Spanish) | ✗ | M |  |

Sourced 1/20 in 1 regions; with memory columns 6/3; lenient 7/4.

#### `-` (dash)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 横杠 "cross bar", 减号 | ✗ | M | Wt 連字號 for hyphen |
| Japanese | ハイフン haifun (hyphen) | ✗ | Wt | hyphen shape |
| Korean | 하이픈 haipeun (hyphen) | ✗ | Wt | hyphen shape |
| Vietnamese | gạch ngang "cross stroke" | ✗ | Wt |  |
| Thai | ขีด khìit "stroke" | ✗ | Wt |  |
| Indonesian | strip, tanda hubung | ✗ | Wt, M | strip from Dutch streep |
| Tagalog | dash (gitling in writing) | ✓ | M |  |
| Hindi | डैश (हैफ़ेन) | ✓ | Wt |  |
| Bengali | ড্যাশ (হাইফেন) | ✓ | Wt, Sub | Sub 22 |
| Tamil | dash | ✓ | M |  |
| Persian | خط تیره xatt-e tire | ✗ | Wt | tire shape (French tiret) |
| Arabic | شرطة šarṭa | ✗ | Wt |  |
| Turkish | tire, kısa çizgi | ✗ | Wt | tire shape |
| Russian | дефис, тире | ✗ | Wt | tire shape (тире) |
| Spanish | guion | ✗ | Wt |  |
| French | tiret | ✗ | Wt | tire shape |
| Swahili | kistari | ✗ | Wt |  |
| Hausa | dash | ✓ | M |  |
| Yoruba | dash | ✓ | M |  |
| Quechua | guion (Spanish) | ✗ | M |  |

Sourced 2/20 in 1 regions; with memory columns 6/3; lenient 6/3.

#### `#` (hash)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 井号 jǐnghào "well sign" | ✗ | Wt, Wp |  |
| Japanese | シャープ shāpu "sharp" (ハッシュ listed) | ✗ (✓ lenient) | Wt, M | sharp is another shape |
| Korean | 샵 syap "sharp", 우물 정 | ✗ | M | Wp title 번호 기호 |
| Vietnamese | dấu thăng "sharp sign" | ✗ | Wt |  |
| Thai | แฮช hɛ́ch | ✓ | Wt |  |
| Indonesian | tanda pagar "fence sign" | ✗ | Wt, Wp |  |
| Tagalog | hash | ✓ | M |  |
| Hindi | hash (संख्या चिह्न) | ✓ | M |  |
| Bengali | hash | ✓ | M |  |
| Tamil | hash | ✓ | M |  |
| Persian | مربع "square" | ✗ | Wt, Wp |  |
| Arabic | شباك "window" | ✗ | Wt |  |
| Turkish | kare "square" | ✗ | Wt |  |
| Russian | решётка "grid" (хэш listed) | ✗ (✓ lenient) | Wt, Wp |  |
| Spanish | almohadilla, numeral, gato | ✗ | Wt, Wp |  |
| French | dièse, croisillon | ✗ | Wt, Wp |  |
| Swahili | (no data) | ✗ | M |  |
| Hausa | (no data) | ✗ | M |  |
| Yoruba | (no data) | ✗ | M |  |
| Quechua | (Spanish) | ✗ | M |  |

Sourced 1/20 in 1 regions; with memory columns 5/2; lenient 7/4.

#### `hashtag` (hashtag)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 话题标签, 井号标签 | ✗ | Wt, Wp |  |
| Japanese | ハッシュタグ | ✓ | Wt, Wp |  |
| Korean | 해시태그 | ✓ | Wt, Wp |  |
| Vietnamese | hashtag | ✓ | Wp, Sub | vi title Hashtag; Sub 12 |
| Thai | แฮชแท็ก | ✓ | Wt, Wp, Sub |  |
| Indonesian | hashtag (tagar official) | ✓ | Sub, Wt | Sub hashtag 34, tagar 0 |
| Tagalog | hashtag | ✓ | Wp | tl title Hashtag |
| Hindi | हैशटैग | ✓ | M |  |
| Bengali | হ্যাশট্যাগ | ✓ | Wp | bn title |
| Tamil | hashtag | ✓ | M |  |
| Persian | هشتگ haštag | ✓ | Wt, Wp, Sub | Sub 57 |
| Arabic | هاشتاق, هاشتاغ (وسم first) | ✓ | Wt, M* |  |
| Turkish | hashtag (etiket) | ✓ | Wp, Wt | tr title Hashtag; Wt lists only etiket "label" (broad) |
| Russian | хештег, хэштег | ✓ | Wt, Wp, Sub | Sub 198; метка "mark" is broad |
| Spanish | hashtag | ✓ | Wt, Wp, Sub | Sub 380; etiqueta "label" is broad |
| French | hashtag (mot-dièse official) | ✓ | Wt, Wp, Sub | Sub 290 |
| Swahili | hashtag | ✓ | M |  |
| Hausa | hashtag | ✓ | M |  |
| Yoruba | hashtag | ✓ | M |  |
| Quechua | hashtag (Spanish) | ✓ | M |  |

Sourced 13/20 in 5 regions; with memory columns 19/7; lenient 19/7.

#### `*` (asterisk)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 星号 xīnghào "star sign" | ✗ | Wt, Wp |  |
| Japanese | アスタリスク asutarisuku (米印, 星印) | ✓ | Wt, Wp |  |
| Korean | 별표 byeolpyo "star mark" (애스터리스크) | ✗ (✓ lenient) | Wt, Wp |  |
| Vietnamese | dấu sao "star sign" | ✗ | Wt |  |
| Thai | ดอกจัน "flower" | ✗ | Wt, Wp |  |
| Indonesian | tanda bintang "star sign" (asteris) | ✗ (✓ lenient) | Wt, Wp |  |
| Tagalog | talantanda; star | ✗ | Wt |  |
| Hindi | तारक "star" | ✗ | Wt |  |
| Bengali | তারকা "star" | ✗ | M |  |
| Tamil | உடுக்குறி "star mark" | ✗ | Wt, Wp |  |
| Persian | ستاره "star" | ✗ | Wt, Wp |  |
| Arabic | نجيمة "little star" | ✗ | Wt, Wp |  |
| Turkish | yıldız "star" (asterisk first-listed) | ✗ (✓ lenient) | Wt, M* |  |
| Russian | звёздочка "little star" (астериск) | ✗ (✓ lenient) | Wt, Wp |  |
| Spanish | asterisco | ✓ | Wt, Wp |  |
| French | astérisque; étoile on phone keys | ✓ | Wt, Wp |  |
| Swahili | nyota "star" | ✗ | M |  |
| Hausa | (no data) | ✗ | M |  |
| Yoruba | (no data) | ✗ | M |  |
| Quechua | asterisco (Spanish) | ✓ | M |  |

Sourced 3/20 in 2 regions; with memory columns 4/3; lenient 8/5.

#### `&` (ampersand)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 和号 "and sign" | ✗ | Wt |  |
| Japanese | アンパサンド; アンド ando "and" in speech | ✓ | Wt | dictionary name; everyday reading is "and" |
| Korean | 앰퍼샌드 | ✓ | Wt | dictionary name |
| Vietnamese | ký hiệu "và" "and sign" | ✗ | Wt |  |
| Thai | แอมเพอร์แซนด์ | ✓ | Wt | dictionary name |
| Indonesian | ampersan (tanda dan "and sign") | ✓ | Wt |  |
| Tagalog | (no data) | ✗ | M |  |
| Hindi | ऐंपरसैंड | ✓ | Wt | dictionary name |
| Bengali | (no data) | ✗ | M |  |
| Tamil | உம்மைக் குறி "and mark" | ✗ | Wt, We |  |
| Persian | امپرسند | ✓ | Wt | dictionary name |
| Arabic | واو لاتينية "Latin and" | ✗ | Wt |  |
| Turkish | ampersand (ve imi "and sign") | ✓ | Wt |  |
| Russian | амперсанд | ✓ | Wt, We |  |
| Spanish | ampersand (y comercial "commercial and") | ✓ | Wt, We |  |
| French | esperluette, et commercial | ✗ | Wt, We |  |
| Swahili | ampasendi | ✓ | Wt |  |
| Hausa | (no data) | ✗ | M |  |
| Yoruba | (no data) | ✗ | M |  |
| Quechua | (no data) | ✗ | M |  |

Sourced 10/20 in 6 regions; with memory columns 10/6; lenient 10/6.

#### `+` (plus)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 加 jiā "add" | ✗ | Wt |  |
| Japanese | プラス purasu, 足す tasu "add" | ✓ | Wt |  |
| Korean | 플러스, 더하기 "adding" | ✓ | Wt, Sub | Sub 플러스 19 = 더하기 19 |
| Vietnamese | cộng "add" | ✗ | Wt |  |
| Thai | บวก bùak "add" | ✗ | Wt |  |
| Indonesian | tambah "add" (plus) | ✗ (✓ lenient) | Wt, Sub | Sub plus 560, tambah 1623 (broad) |
| Tagalog | dagdag "add"; plus in English-medium maths | ✗ (✓ lenient) | Wt, M |  |
| Hindi | प्लस | ✓ | Sub | Sub 6 (thin) |
| Bengali | প্লাস | ✓ | Sub | Sub 12 |
| Tamil | பிளஸ் | ✓ | Sub | Sub 6 (thin) |
| Persian | به علاوه "in addition" (پلاس) | ✗ (✓ lenient) | Wt, Sub |  |
| Arabic | زائد "added" | ✗ | Wt |  |
| Turkish | artı "increased" | ✗ | Wt |  |
| Russian | плюс | ✓ | Wt |  |
| Spanish | más | ✗ | Wt |  |
| French | plus | ✓ | Wt |  |
| Swahili | jumlisha "add" | ✗ | Wt |  |
| Hausa | (no data) | ✗ | M |  |
| Yoruba | (no data) | ✗ | M |  |
| Quechua | (Spanish más) | ✗ | M |  |

Sourced 7/20 in 3 regions; with memory columns 7/3; lenient 10/5.

#### `−` (minus)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 减 jiǎn "reduce" | ✗ | Wt |  |
| Japanese | マイナス mainasu (引く hiku "pull" in sums) | ✓ | Wt |  |
| Korean | 마이너스 (빼기 "taking out" in sums) | ✓ | Wt, Sub |  |
| Vietnamese | trừ "remove" | ✗ | Wt |  |
| Thai | ลบ lóp "erase" | ✗ | Wt |  |
| Indonesian | dikurangi "lessened" (minus) | ✗ (✓ lenient) | Wt, Sub | Sub minus 318 |
| Tagalog | bawas "reduce" (minus) | ✗ (✓ lenient) | Wt, M |  |
| Hindi | कम, घटाना (माइनस) | ✗ (✓ lenient) | Wt, Sub | Sub 1 |
| Bengali | বিয়োগ (মাইনাস) | ✗ (✓ lenient) | Wt, Sub | Sub 11 |
| Tamil | கழி (மைனஸ்) | ✗ (✓ lenient) | Wt, Sub | Sub 2 |
| Persian | منها menhā "from it" | ✗ | Wt |  |
| Arabic | ناقص nāqiṣ "lacking" | ✗ | Wt |  |
| Turkish | eksi "less" | ✗ | Wt |  |
| Russian | минус | ✓ | Wt |  |
| Spanish | menos | ✓ | Wt | same consonants m-n-s (pattern 3) |
| French | moins [mwɛ̃] | ✗ | Wt | m-w-n, apart (pattern 3) |
| Swahili | toa "take out" | ✗ | Wt |  |
| Hausa | (no data) | ✗ | M |  |
| Yoruba | (no data) | ✗ | M |  |
| Quechua | menos (Spanish) | ✗ (✓ lenient) | M |  |

Sourced 4/20 in 2 regions; with memory columns 4/2; lenient 10/5.

#### `×` (times)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 乘 chéng | ✗ | Wt |  |
| Japanese | 掛ける kakeru | ✗ | Wt |  |
| Korean | 곱하기 gopagi | ✗ | Wt |  |
| Vietnamese | nhân | ✗ | Wt |  |
| Thai | คูณ khuun | ✗ | Wt |  |
| Indonesian | kali "times, occasions" | ✗ | Wt |  |
| Tagalog | maka, paramihin ng; times in English-medium maths | ✗ (✓ lenient) | Wt, M |  |
| Hindi | गुणा guṇā | ✗ | Wt |  |
| Bengali | গুণ | ✗ | Wp |  |
| Tamil | பெருக்கல் | ✗ | Wp |  |
| Persian | ضرب در zarb dar | ✗ | Wt |  |
| Arabic | في fī "in" | ✗ | Wt |  |
| Turkish | çarpı, kere "times, occasions" | ✗ | Wt, Sub |  |
| Russian | умножить на | ✗ | Wt |  |
| Spanish | por | ✗ | Wt |  |
| French | fois "times, occasions" | ✗ | Wt |  |
| Swahili | mara "times, occasions" | ✗ | Wt |  |
| Hausa | sau "times, occasions" | ✗ | M |  |
| Yoruba | (no data) | ✗ | M |  |
| Quechua | (no data) | ✗ | M |  |

Sourced 0/20 in 0 regions; with memory columns 0/0; lenient 1/1.

#### `÷` (divided by)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 除以 chú yǐ | ✗ | Wt |  |
| Japanese | 割る waru "split" | ✗ | Wt |  |
| Korean | 나누기 nanugi "dividing" | ✗ | Wt |  |
| Vietnamese | chia "divide, share" | ✗ | Wt |  |
| Thai | หาร hǎan | ✗ | Wt |  |
| Indonesian | bagi "divide, share" | ✗ | M |  |
| Tagalog | hati "split" | ✗ | Wt |  |
| Hindi | भाग bhāg | ✗ | M |  |
| Bengali | ভাগ bhag | ✗ | M |  |
| Tamil | வகு | ✗ | M |  |
| Persian | تقسیم بر | ✗ | Wp |  |
| Arabic | على, قسمة | ✗ | Wt |  |
| Turkish | bölü "divided" | ✗ | Wt, Sub |  |
| Russian | разделить на | ✗ | Wt |  |
| Spanish | dividido por, entre | ✓ | Wt | divide family (2) |
| French | divisé par | ✓ | Wt | divide family (2) |
| Swahili | gawanya "divide, share" | ✗ | Wt |  |
| Hausa | (no data) | ✗ | M |  |
| Yoruba | (no data) | ✗ | M |  |
| Quechua | rakiy "divide" | ✗ | Wt |  |

Sourced 2/20 in 1 regions; with memory columns 2/1; lenient 2/1.

#### `=` (equals)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 等于 děngyú "equal to" | ✗ | Wt |  |
| Japanese | は wa; イコール ikōru | ✗ (✓ lenient) | Wt, M |  |
| Korean | 는 neun (topic); 같다 "same" | ✗ | M |  |
| Vietnamese | bằng "equal" | ✗ | Wt |  |
| Thai | เท่ากับ "equal with" | ✗ | Wt |  |
| Indonesian | sama dengan "same as" | ✗ | Wp |  |
| Tagalog | ay; equals in English-medium maths | ✗ (✓ lenient) | M |  |
| Hindi | बराबर barābar | ✗ | Wt, Sub |  |
| Bengali | সমান | ✗ | M |  |
| Tamil | சமம் | ✗ | M |  |
| Persian | مساوی | ✗ | Wt |  |
| Arabic | يساوي | ✗ | Wt |  |
| Turkish | eşittir | ✗ | Wt, Sub |  |
| Russian | равно | ✗ | Wt, Sub |  |
| Spanish | igual a | ✓ | Wt |  |
| French | égale | ✓ | Wt |  |
| Swahili | ni sawa na "is same as" | ✗ | M |  |
| Hausa | (no data) | ✗ | M |  |
| Yoruba | (no data) | ✗ | M |  |
| Quechua | (Spanish igual) | ✗ (✓ lenient) | M |  |

Sourced 2/20 in 1 regions; with memory columns 2/1; lenient 5/4.

#### `%` (percent)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 百分之 "hundred-part-of" (趴 pā, Taiwan slang) | ✗ (✓ lenient) | Wt |  |
| Japanese | パーセント | ✓ | Wt |  |
| Korean | 퍼센트, 프로 | ✓ | Wt, Sub |  |
| Vietnamese | phần trăm "part hundred" | ✗ | Wt |  |
| Thai | เปอร์เซ็นต์ | ✓ | Wt, Sub |  |
| Indonesian | persen | ✓ | Wt, Sub |  |
| Tagalog | porsiyento | ✓ | Wt |  |
| Hindi | प्रतिशत (परसेंट not in Sub) | ✗ | Wt, Sub | rival rule: प्रतिशत 32, परसेंट 0 |
| Bengali | শতাংশ, শতকরা (পার্সেন্ট) | ✗ | Wt, Sub | rival rule: native 59, loan 6 |
| Tamil | சதவீதம் | ✗ | Wt, Sub | rival rule: native 27, loan 0 |
| Persian | درصد "in hundred" | ✗ | Wt |  |
| Arabic | في المئة "in the hundred" | ✗ | Wt |  |
| Turkish | yüzde "in hundred" | ✗ | Wt |  |
| Russian | процент | ✓ | Wt, Sub |  |
| Spanish | por ciento | ✓ | Wt |  |
| French | pour cent | ✓ | Wt |  |
| Swahili | asilimia | ✗ | Wt, Lz | rival rule: asilimia 2759, pasenti 3 |
| Hausa | kashi (cikin ɗari) | ✗ | M, Lz | no loan form in Leipzig |
| Yoruba | ìdá-ọgọ́rùn-ún | ✗ | M |  |
| Quechua | porsiyentu (Spanish) | ✓ | M | Leipzig writes only %; porcentaje twice |

Sourced 8/20 in 3 regions; with memory columns 9/4; lenient 10/4.

#### `www` (double-u)

| Lang | Everyday word | Shared | src | Note |
|---|---|---|---|---|
| Mandarin | 三W sān dǎbùliù | ✓ | We | We "www": /sän tä bu liou/ |
| Japanese | ダブリュー | ✓ | Wt, We |  |
| Korean | 더블유 | ✓ | Wt, We |  |
| Vietnamese | vê kép, đúp lờ vê "double v" | ✗ | We |  |
| Thai | ดับเบิลยู | ✓ | Wt, We |  |
| Indonesian | we we we | ✗ | Wt, We |  |
| Tagalog | dobolyu | ✓ | We |  |
| Hindi | डब्ल्यू | ✓ | Wt |  |
| Bengali | ডব্লিউ | ✓ | Wt |  |
| Tamil | டபிள்யூ | ✓ | M |  |
| Persian | دابلیو | ✓ | M |  |
| Arabic | دابليو | ✓ | Wt |  |
| Turkish | ve ve ve, çift ve | ✗ | M |  |
| Russian | вэ-вэ-вэ (дабл-ю listed) | ✗ (✓ lenient) | Wt, We |  |
| Spanish | uve doble, doble ve | ✗ | Wt, We |  |
| French | double vé | ✗ | Wt, We |  |
| Swahili | dabliu | ✓ | M |  |
| Hausa | dabliu | ✓ | M |  |
| Yoruba | wí (Yoruba letter name); double-u in English | ✗ (✓ lenient) | We |  |
| Quechua | doble ve (Spanish) | ✗ | M |  |

Sourced 8/20 in 4 regions; with memory columns 12/5; lenient 14/6.

