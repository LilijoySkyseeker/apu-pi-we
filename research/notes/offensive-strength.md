# Offensive words: which are strong and common today

Task: `offensive-strength-prompt.md` (author, 2026-10-15: "can we do proper research into which ones are actually strongly offensive … pee is on the list, and at least in America that is basically not offensive at all any more"). Working note, terse. Words are written in full.

## Progress

- [x] Read prompt, goal C3, design log (last entry), `tools/offensive.py`; ran the 80-form check and listed which `data/offensive.tsv` rows cause each match (script below).
- [x] Sources on strength (step 1)
- [x] Per-language tables, 34 languages (step 2)
- [x] Forms blocked (step 3)
- [x] One-syllable verdicts, all 80 (step 4)
- [x] Method notes (step 5)
- [x] `offensive-hard-draft.tsv`
- Not done / open: the per-word ratings of Sulpizio et al. 2024 (OSF `ecr32`; the OSF API returned 502 on every try, 2026-10-15). Fetching them would grade Mandarin, Cantonese, Thai, Spanish, French, German, Italian and English words from real ratings; retry and update the grades marked M below.

Reproduce the per-form match list: the script `why.py` used here loads `offensive.load()`, keeps rows with `kind == strong`, `primary == yes`, `counts(r)`, and prints, for each form in `words.SYL` that `blocked()` returns true for, every row whose `sounds` matches exactly or by `key()`.

## Summary

- **Recommended one-syllable hard list: 5 forms** — **ku** (Portuguese *cu*), **kun** (Persian *kun*, English *coon*), **lan** and **lun** (Punjabi *lan/lun*, Hindi-Urdu *lund*), **lon** (Vietnamese *lồn*, medium confidence). Today's tool blocks 80; the first draft had 8.
- **Two-syllable forms: 35 of 18,900** two-syllable strings blocked (0.19%), plus 8 longer forms. None is a word in use today (checked against lexicon, grammar, numbers, compounds, senary). For comparison, today's `blocked()` rejects 2,402 two-syllable strings (12.7%), yet still misses 13 of the 43 hard forms: fiken, manko, obo, paki, siki, tonba, yeba, yoba, kanake, omanko, pukima, putana, tewadiya.
- Changed from the first draft: **bi**, **pi**, **go** move from hard to tie-break. **bi** isn't even blocked today (see finding 1).
- Most of the world's strongest words can't be said in Apupiwe at all (they need sounds or final consonants it lacks). The real exposure is two-syllable CVCV words in Indic, Austronesian, Bantu and Romance languages (*puta*, *puki*, *kuma*, *gandu*, *phuddi*). Several of these the tool misses through mapping bugs (findings 1–2).

## Sources (step 1)

Rating studies and regulator research found and used:

| id | source | covers | method | used for |
|---|---|---|---|---|
| OF21 | Ofcom / Ipsos MORI, *Public attitudes towards offensive language on TV and radio: Quick Reference Guide* (2021). Read from the Wayback copy of ofcom.org.uk/__data/assets/pdf_file/0020/225335/offensive-language-quick-reference-guide.pdf | UK, 2021; 186 English words; plus 9 focus groups with Indian, Pakistani and Bangladeshi communities on non-English words | online survey of acceptability before/after the watershed + qualitative groups; each word placed Mild / Moderate / Strong | English grades; a few Hindi-Urdu-Punjabi words |
| J09 | Jay, T. (2009), "The utility and ubiquity of taboo words", *Perspectives on Psychological Science* 4:153 | US, field recordings 1986–2006 | counts of public swearing | which English words are common: *fuck, shit, hell, damn, goddamn, Jesus Christ, ass, oh my god, bitch, sucks* are about 80% of tokens; *fuck* and *shit* alone a third to a half |
| BF07 | Beers Fägersten (2007), cited in Dewaele 2017 | 60 US undergraduates | 10-point offensiveness ratings of 12 words | *nigger* 8.5, *cunt* 6.6, *motherfucker* 5.9, *bitch* 5, *fuck* 5, *asshole* 4.4, *bastard* 4.3, *dick* 4.1, *ass* 3.2, *shit* 3.1, *damn*/*hell* 2.3 |
| D16, D17 | Dewaele, J.-M. (2016) "Thirty shades of offensiveness", *J. Pragmatics*; (2017) "'Cunt': on the perception and handling of verbal dynamite by L1 and LX users of English" (eprints.bbk.ac.uk/18883) | 1,159 L1 + 1,165 L2 English users, online, mostly UK/US | 5-point offensiveness ratings of 30 words | *cunt* the most offensive for both groups (4.6/5); *piss* treated as a medium taboo word |
| BSC00 | Broadcasting Standards Commission et al. survey (2000), via Wikipedia "Cunt" | UK | survey | *cunt* above *motherfucker* and *fuck* |
| S24 | Sulpizio, S. et al. (2024) "Taboo language across the globe: a multi-lab study", *Behavior Research Methods* 56:3794 (PMC11133054); data osf.io/ecr32 | 17 countries, 13 languages (Cantonese, Dutch, English, Finnish, French, German, Italian, Mandarin, Serbian, Setswana, Slovenian, Spanish, Thai) | free production (N=1,046) then best–worst ratings of offensiveness and tabooness (N=455 per dimension) | cross-language pattern: the most offensive words everywhere are words for female genitals and insults to the mother ("son of a bitch", "I fuck your mother"), then race, gender and sexuality slurs, then disability slurs (*retard*, *spastic*); blasphemy almost absent. Per-word data **not retrieved** (OSF down) |
| J08 | Janschewitz, K. (2008) "Taboo, emotionally valenced, and emotionally neutral word norms", *BRM* 40:1065 | 78 US undergraduates, 92 taboo words | 9-point ratings incl. offensiveness | exists; full table not retrieved (Springer blocked). Cited, not used for grades |
| RKN13 | Roskomnadzor ruling 2013 and the 2014 media law, via Wikipedia "Mat (profanity)" | Russia | regulator | the four mat roots (*khuy*, *pizda*, *yebat'*, *blyad'*) "absolutely unacceptable in the mass media" |
| HK | Hong Kong broadcast practice, via Wikipedia "Cantonese profanity" | Hong Kong | broadcast bleeping | the "five" Cantonese vulgarities: *diu*, *gau*, *lan*, *tsat*, *hai* |
| HKY | *Hōsō kinshi yōgo* (Japanese broadcasters' self-censored word list), via Wikipedia "Japanese profanity" | Japan | industry list | *manko*, slurs |
| BR | Bralczyk (Polish linguist), via Wikipedia "Polish profanity" | Poland | expert statement | five basic vulgarisms: *chuj, pizda, pierdolić, jebać, kurwa* |
| WT | Wiktionary via kaikki.org, already in `data/offensive.tsv` | 34 languages | editors' register tags (vulgar, offensive, slur, derogatory) | presence and register for languages without rating studies. Tags don't grade strength |
| WP | Wikipedia usage articles: Mandarin, Cantonese, Japanese, Korean, Hindustani, Portuguese, Polish, Ukrainian, Italian, Filipino profanity; Mat | various | secondary, variably sourced | usage notes |
| VT | Kang, Pham & Storme (2014) and later corpus work on Vietnamese loanword tones (search summaries; papers not read in full) | Vietnamese | loanword corpus | foreign syllables mostly get the level tone *ngang* |
| BS | easybrandcheck.com, tolingo.com naming-check pages (2026-10-15) | brand screening | vendor pages | method and price (step 5) |
| M | Claude's memory | — | — | **memory, not a source**; every grade marked M needs a native check |

No published rating study was found for: Hindi, Urdu, Bengali, Punjabi, Marathi, Gujarati, Telugu, Tamil, Arabic (either variety), Persian, Turkish, Indonesian, Malay, Javanese, Tagalog, Vietnamese, Korean, Japanese, Hausa, Yoruba, Swahili, Amharic, Portuguese, Russian, Ukrainian, Polish. Spanish, French, German, Italian, Mandarin, Cantonese and Thai have S24 data (not yet retrieved). Their grades below rest on WT presence plus WP and M, and carry low-to-medium confidence. Online "ranked swear words" blogs turned up for Vietnamese and Thai; they're too weak to cite.

## Method

1. **Grades.** *strongest*: the words a language's speakers name as the worst (top of a rating study, a regulator's absolute list, the core of a recognised set like the four mat roots or Cantonese's five). *strong*: clearly vulgar or a slur, avoided in public, below the top. *medium*: rude but used casually (OF21 "moderate"). *mild-or-dated*. Common = used in everyday speech today, not just known.
2. **Hard list rule (proposed).** A word is on the hard list if it's graded strongest or strong, it's common today, **and** its speakers would hear an Apupiwe form *as that word*. The last test uses the listener's own contrasts:
   - **Aspiration.** Apupiwe p t k are aspirated word-initially and b d g are voiced (design log 2026-10-13). Listeners who contrast aspiration (Mandarin, Cantonese, Korean, Thai, Hindi-Urdu, Punjabi, Bengali, Marathi, Gujarati) hear our **p t k as their pʰ tʰ kʰ** and our **b d g as their plain p t k** (or their voiced b d g where those exist, as in Indic). So Mandarin *bī* [pi] is our **bi**, not **pi**; Korean 개 [kɛ] is our **ge**, not **ke**; Bengali *khanki* [kʰanki] is our **kanki**; Punjabi *phuddi* [pʰuddi] is our **pudi**.
   - **Voicing listeners** (Spanish, French, Portuguese, Italian, Russian, Polish, Tagalog…) hear p/b and t/d as different; no merge.
   - **Missing final consonants.** Apupiwe ends syllables only in vowels or -n. A word whose identity depends on a final stop or fricative (*fuck*, *cunt*, *shit*, *kos*, *sik*, *chut*) isn't heard from a form that drops it. A final ŋ heard as n counts as a near match only where the language doesn't contrast n/ŋ finally.
   - **Tone.** In Mandarin, Cantonese, Vietnamese and Thai a toneless CV(n) syllable is a homophone of many ordinary morphemes, and listeners assign foreign syllables a default tone (Vietnamese: mostly level *ngang*, VT). A one-syllable match in these languages is hard only where the offensive word is the most salient reading of that syllable alone.
   - **Retroflex and dental stops.** Indian listeners hear English-style alveolar t d as their retroflex ṭ ḍ, so Apupiwe **d** stands for Hindi ḍ (*gāṇḍū* → **gandu**, *lauḍā* → **loda**).
   - **Stress.** Apupiwe content roots carry first-syllable stress; a word stressed elsewhere (Russian *yebát'*) is a weaker match.
3. **Forms.** One-syllable forms, two-syllable CV(n)CV(n), and anything longer the word maps to. A one-syllable hard form blocks only that form, not two-syllable words that contain it (no language here hears a syllable inside a foreign word as a free word, except perhaps Vietnamese; see open questions).
4. **Counts.** Two-syllable string space: every concatenation of two of the 140 syllables in `words.SYL`, deduplicated: 18,900.

## Per-language tables (steps 2–3)

Columns: word, meaning, grade, region, source, forms blocked. "tb" means the form is only a tie-break match. "—" means no Apupiwe form sounds like the word. Speaker counts are rough totals (first + second language), from memory (Ethnologue-style figures): **M**.

### English (~1.5 bn; ~380 m first-language)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| nigger, nigga | Black person (slur) | strongest | all; *nigga* in-group in AAVE | OF21 strong; BF07 top (8.5); S24 slur class | niga, nige |
| cunt | vulva; insult | strongest (UK, US); milder in Australian banter | all | OF21 strong; D16 top; BSC00 top | — (needs -nt) |
| fuck, fucking | sex; intensifier | strong; the most common swear word | all | OF21 strong; J09; BF07 5.0 | faku ("fuck you"), fakin ("fuckin'") |
| motherfucker | | strong | US esp. | OF21 strong; BF07 5.9 | — |
| Paki | South Asian (slur) | strong | UK | OF21 strong; WT | paki |
| coon | Black person (slur) | strong; now less common | US, UK, Australia | OF21 strong; WT | kun |
| faggot / fag | gay man (slur) | strong / medium | US, UK | OF21 strong / moderate | — |
| retard, spastic, mong | disability slurs | strong (UK); *spastic* mild in US | UK | OF21 strong; S24 | mon (tb; needs final ŋ) |
| darky, gippo, sambo, golly | slurs | strong, dated | UK | OF21 strong | daki, gipo, sanbo (tb) |
| cum | semen | strong (OF21), but a homophone of *come* | | OF21 | — |
| shit | | medium; very common | all | OF21 moderate; BF07 3.1; J09 | — |
| pussy, dick, cock, prick, twat, wanker | | medium | | OF21 moderate | pusi (tb) |
| bitch | | mild (UK) / medium (US) | | OF21 mild; BF07 5.0 | — |
| piss, pissed | | mild-to-medium | | D16 medium; OF21 *pissed* mild | — |
| **pee** | urinate | **not offensive**: informal/childish; the author's "comedic" matches the sources | US, Canada, Australia | WT: "informal" (noun), "colloquial" (verb); absent from OF21's 186 words | none (pi = noise for English) |

### Mandarin Chinese (~1.1 bn)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| 肏/操 cào (你妈) | fuck (your mother) | strongest | all | WP; WT; S24 class | — (needs ts-, -ao) |
| 屄 bī; 傻逼 shǎbī; 牛逼 niúbī | cunt; "stupid cunt"; "awesome" | strongest (bī alone, *shǎbī*); mild (*niúbī*) | all | WP; WT | bi (tb: the syllable bi is dozens of everyday words, 比 笔 必 鼻; bī mostly occurs in compounds); sabi (tb; southern s/sh merger) |
| 批 pī (Sichuanese 瓜批) | = 屄 | strong | Southwest Mandarin | WT; M | pi (tb) |
| 鸡巴 jība | dick | strong | | WT; M | — |
| 他妈的 tāmāde, 妈的 | "fucking", "damn" | medium; very common | | WP; M | tamade (tb) |
| 王八蛋 wángbādàn | bastard | medium | | M | wanbadan (tb) |
| 滚 gǔn | get lost | medium (rude, not obscene) | | M | gun (tb) |
| 干/幹 gàn | "do"; = fuck (Taiwan interjection) | strong in Taiwan as interjection; neutral "do" everywhere | Taiwan | WT; M | gan (tb); kan is heard as 看 kàn "look" (aspiration), noise |
| 黑鬼 hēiguǐ | Black person (slur) | strong | | WP | — |
| 死 sǐ | die | not offensive | | WT topic only | si (noise) |

### Cantonese (~85 m; inside "Chinese" in the tool)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| 屌/𨳒 diu2 | fuck | strongest ("five"; bleeped on HK TV) | HK, Guangdong, diaspora | HK; WP; WT | diu (two syllables di-u; medium confidence) |
| 閪/屄 hai1 | cunt | strongest | | HK; WT | — (needs h-, -ai) |
| 撚 lan2 (n/l-merged nan2) | dick | strongest | | HK; WT | lan (already hard via Punjabi; Cantonese contrasts short ɐ with long aː, but the euphemism 懶 laan shows laan evokes it) |
| 鳩 gau1 | dick | strongest | | HK | — |
| 柒 cat6 | dick; stupid | strong | | HK | — |
| 仆街 puk1 gaai1 | "drop dead" | medium | | M | — |

### Hindi (~600 m) and Urdu (~230 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| मादरचोद/مادرچود mādarchod, बहनचोद behenchod | motherfucker, sisterfucker | strongest | all | OF21 strong (*behnchod*, *machod*); WP | — |
| चूत chūt, चूतिया chūtiyā | cunt; idiot | strongest / strong, very common | | WT; M | — (needs ch-) |
| भोसड़ी bhosḍī | cunt | strongest | | WT; M | — |
| लंड/لنڈ laṇḍ, lund | dick | strong | | WT | lan, lun |
| लौड़ा/لوڑا lauḍā, lodā | dick | strong, very common | | WT; M | loda |
| गांडू gāṇḍū / गांड gāṇḍ | "faggot", asshole / ass | strong, very common | pan-Indian | WT (also English loan entry) | gandu; gan (tb) |
| रंडी randī | whore | strong | | WP; OF21 context | — (r ≠ l) |
| फुद्दी/پھدی phuddī | cunt | strongest | Urdu, Punjab | WT; M | pudi |
| चमार chamār, भंगी bhangī | caste slurs | strong; legally actionable (SC/ST Act) | India | OF21 strong (*chamaar*, *chooray*); WP | bangi (tb: b ≠ bʰ) |
| कुत्ता kuttā, कमीना kamīnā, साला sālā | dog; scoundrel; brother-in-law | mild-to-medium | | OF21 mild (*kutta*) | kuta, kamina, sala (tb) |

### Spanish (~560 m; Spain 48 m, Mexico 130 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| (hijo de) puta | whore; son of a whore | strongest as insult; *¡puta!* strong | all | WT; S24 class; M | puta |
| puto | male prostitute; slur (MX); intensifier (ES) | strong (MX) / medium (ES) | | WT; M | puto |
| concha (de tu madre) | cunt | strongest | Argentina, Chile, Peru | M | — |
| coño | cunt; interjection | medium (Spain, everyday) / strong elsewhere | | M | konyo (tb) |
| polla | cock (Spain); hen, betting pool (LatAm) | strong in Spain only | Spain | WT; M | poya (tb) |
| chingar, verga, pendejo, cabrón, joder, maricón, gilipollas | | strong/medium | regional | M | — |
| culo, mierda | ass, shit | medium | | M | kulo (tb) |
| sudaca | South American (slur) | strong | Spain | M | sudaka (tb) |
| huevón/weón | idiot; "dude" | medium-mild, very common | Chile | M | weon (tb) |

### French (~310 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| nique ta mère, fils de pute | | strongest | | M; S24 class | — |
| enculé, salope, pute | | strong | | WT; M | — |
| pédé | gay man (slur) | strong, common | France | WT | pede |
| nègre, bougnoule, bicot, youpin | slurs | strong; the last three dated | | WT; M | biko, yupin (tb) |
| putain | whore; interjection | medium as interjection (the commonest swear word); strong as insult | | M | — (French /y/ isn't our u or i) |
| con, conne, connard | idiot (genital sense dated) | medium, very common | | WT ("dated" genital sense); M | ko (tb) |
| merde, cul, bite, chatte, couilles | | medium | | M | ki (noise: = *qui*) |
| pine | dick | dated | | WT | pin (tb) |
| ken | = *niquer* (slang) | strong but niche | banlieue slang | WT | ken (tb) |

### Arabic (~370 m incl. second-language) and Egyptian Arabic (~110 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| كس kuss (ummak) | cunt (your mother's) | strongest | all | WT; M | — (needs -ss; *kusa* = zucchini) |
| زب zubb/zebb, أير ayr | dick | strong | Levant, Egypt | WT; M | — |
| شرموطة sharmūṭa | whore | strongest | | WT; M | — |
| خول khawal | gay man (slur) | strong | Egypt | WT; M | — |
| عبد ʿabd / عبيد ʿabīd | slave (anti-Black slur) | strong | Gulf, Maghreb | M | — |
| كلب kalb, حمار ḥmār | dog, donkey | medium | | M | — |
| خرا khara | shit | medium | | M | — |
Arabic's strongest words need sounds Apupiwe lacks (ʕ ħ x q z ʃ r, final clusters). Nothing blocked.

### Bengali (~270 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| খানকি khānki | whore | strongest, common | Bangladesh, West Bengal | WT | kanki (aspiration match) |
| মাগী māgī | whore; woman (derogatory) | strong, common | | WT | magi |
| চোদ chod-, চুদি | fuck | strongest | | WT; M | — |
| বাল bāl | pubic hair; "damn" | medium, very common | | M | — |
| ধোন dhon | dick | strong | | WT; M | don (tb: d ≠ dʰ) |
| শুয়োরের বাচ্চা | son of a pig | strong | | M | — |
| মাং māng | vagina | strong, regional | | WT | man (tb, weak) |

### Portuguese (~265 m; Brazil 215 m, Portugal 10 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| caralho | cock; interjection | strongest (PT), strong (BR) | | WP; WT | — |
| foda, foder, foda-se | fuck | strong, very common | both | WT; WP | foda, fode |
| cu | ass(hole) | strong (BR: *vai tomar no cu*), medium (PT) | both | WT; M | ku |
| buceta | cunt | strongest | Brazil | WT; M | buseta |
| puta, filho da puta | whore | strongest as insult | both | WP; WT | puta |
| porra | cum; "damn" | medium (BR, everyday) | | M | — |
| viado | gay man (slur) | strong | Brazil | M | — |
| pica | dick | strong (PT), medium (BR) | | M | pika (tb) |
| cacete, merda | | medium | | WP; M | — |

### Russian (~255 m) and Ukrainian (~39 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| хуй khuy | dick | strongest (mat) | | RKN13 | — (x ≠ k, no final j) |
| пизда pizda | cunt | strongest (mat) | | RKN13 | — |
| ебать yebat' / ёбаный yobanyy; Ukr. їбати | fuck / fucking | strongest (mat; the top mat word in surveys, WP) | | RKN13; WP | yeba, yoba |
| блядь blyad' | whore; "fuck" | strongest (mat) | | RKN13 | — |
| сука suka | bitch; "fuck!" | strong (not mat), very common | both | WT; WP | suka |
| пидор/пидар pidor | gay man (slur) | strong, common | | WT; M | pida (tb; final r lost) |
| мудак mudak | asshole | strong | | WT; M | — |
| гандон gandon | condom; jerk | medium | | M | gandon (tb) |
| жид zhid, хохол khokhol, кацап katsap, чурка churka | slurs | strong | | M | — |
| пан pan | lord, gentleman | not offensive | | (tool noise) | — |

### Indonesian (~200 m incl. second-language) and Malay (~80 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| puki; pukimak | cunt; "your mother's cunt" | strongest | Malaysia, Riau, eastern Indonesia | WT | puki; pukima |
| kontol | dick | strongest | Indonesia | WT | — (final l); kontolu not a form |
| memek | cunt | strongest | Indonesia | WT | meme (tb: final glottal stop lost) |
| ngentot / entot | fuck | strongest | Indonesia | WT; M | — |
| anjing, bangsat, babi | dog, bastard, pig | strong as curses; *anjing* very common | | WT; M | babi (tb: = "pig") |
| tai, taik | shit | medium | | M | tai (tb) |
| bego, goblok, bodoh | stupid | medium | | M | bego, bodo (tb) |
| keling | Indian (slur) | strong | Malaysia | M | kelin (tb) |
| butoh | dick | strong | Malaysia | M | buto (tb) |

### German (~135 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| Fotze | cunt | strongest | | WT; S24 class; M | — |
| ficken, fick dich | fuck | strong, very common | | WT; M | fiken |
| Hurensohn | son of a whore | strongest | | M | — |
| Neger | Black person (slur) | strong | | WT | nega (already in REJECTED) |
| Kanake | immigrant, esp. Turkish/Arab (slur; partly reclaimed) | strong | | WT; M | kanake |
| Schwuchtel, Spast, Mongo | slurs | strong/medium | | M | mongo (tb) |
| Arschloch, Wichser, Schlampe, Scheiße | | medium | | M | — |
| Nutte | whore | strong | | M | nute (tb; = *Nute* "groove") |

### Japanese (~125 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| まんこ manko, おまんこ omanko (Kansai おめこ omeko) | cunt | strongest (broadcast-banned); known to all, said rarely | | HKY; WT | manko, omanko; omeko (tb) |
| 気違い kichigai, 支那 shina, チョン chon, 穢多 eta | slurs | strong (broadcast-banned) | | HKY; WP | sina (tb: = 品 "goods"), eta (tb: rare in speech) |
| 死ね shine | die! | medium-strong | | WP; M | sine (tb: Japanese hears si as shi) |
| くそ kuso, ばか baka, あほ aho, ブス busu, かす kasu | shit, idiot, ugly, scum | mild-to-medium, very common | | WP | kuso, baka, busu, kasu (tb) |
| ヤリマン yariman | slut | medium | | M | yaliman (tb: Japanese hears l as r) |
| うんこ unko | poo | mild (childish) | | M | — |
Japanese swearing is weak overall (WP); the strongest words are slurs and genital words.

### Marathi (~99 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| झवाड्या zhavāḍyā, आईघाल्या | fuck(er), motherfucker | strongest | | WT; M | — |
| लवडा lavḍā | dick | strong | | WT; M | lauda (tb, three syllables) |
| गांडू gāṇḍū | as Hindi | strong | | WT | gandu |
| भडवा bhaḍvā, रांड rāṇḍ | pimp, whore | strong | | M | — |

### Telugu (~96 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| లంజ lanja | whore | strongest, very common | | WT; M | — |
| పూకు pūku | cunt | strongest | | WT | puku |
| దెంగు deṅgu | fuck | strongest | | WT | dengu |
| మొడ్డ moḍḍa | dick | strong | | WT; M | moda (tb: geminate lost) |
| గుద్ద gudda | ass | medium | | M | guda (tb) |

### Turkish (~90 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| amına koyayım (amk), am | cunt; "fuck your cunt" | strongest | | WT; M | — (final m; *amina* is a common name) |
| sik, siktir, sikerim | dick; fuck off; fuck | strongest | | WT | siki ("the dick", accusative; medium confidence) |
| orospu (çocuğu) | whore (son of a) | strongest | | WT; M | — (r) |
| piç, göt, ibne, yarrak, pezevenk, kahpe | bastard, ass, gay (slur), dick, pimp, slut | strong | | WT; M | — |

### Tamil (~86 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| புண்டை puṇḍai (colloquial punda) | cunt | strongest, very common | Tamil Nadu, Sri Lanka | WT | punda, pundai |
| தேவடியா tēvaḍiyā | whore | strongest | | WT; M | tewadiya |
| ஓத்தா ōttā, ஓம்மாள ommāḷa | fuck; your mother's… | strongest, very common | Chennai | M | ota, omala (tb: dental t, geminates) |
| சுன்னி sunni | dick | strong | | WT; M | suni (tb) |
| கூதி kūti | ass/cunt | strong | | M | kuti (tb) |
| பாடு bāḍu | bastard | medium | | M | badu (tb) |
| பீ pī | shit, faeces | medium (everyday colloquial, also to children) | | WT; M | pi (tb) |

### Vietnamese (~86 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| địt (mẹ), đụ (má) | fuck (your mother) | strongest; *địt* North, *đụ* South | | WT; M | du (tb: toneless du is heard as đu "swing" / the euphemism đù) |
| lồn | cunt; intensifier | strongest, very common (alone, *vãi lồn*) | all | WT | lon (**hard, medium confidence**: toneless lon = *lon* "can", *lớn* "big"; but the toneless spellings *lol*, *loz*, *l* are themselves euphemisms for lồn (M), so the segmental shape alone evokes it) |
| cặc | dick | strongest | | WT | — (final k) |
| đéo | fuck; "not" | strong, very common | | WT; M | deo (tb) |
| đĩ | whore | strong | | WT | di (noise: = đi "go") |
| thằng | derogatory classifier for a man | mild | | WT | tan (noise: ăng ≠ an) |
| mẹ / má | mother (in the curses) | not offensive alone | | (tool noise) | — |
| nứng, lọ, dê | horny, wank, lewd | medium | | WT | lo (tb, weak) |

### Tagalog / Filipino (~83 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| putang ina (mo) / puta | "son of a whore"; whore | strongest; very common (WP: Duterte; Supreme Court called it a common expression of anger) | | WP; WT | puta; putan (tb) |
| puke / puki | cunt | strong | | WT | puke, puki |
| tite | dick | strong | | WT | tite |
| kantot | fuck | strong | | WT | kanto (tb: = "street corner") |
| gago, tarantado, ulol | idiot | medium, very common | | WT | gago (tb) |
| bobo | stupid | mild | | M | bobo (tb) |

### Korean (~82 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| 씨발 ssibal | fuck | strongest, very common | | WP | siba (tb: = the euphemism 시바) |
| 개새끼 gaesaekki | son of a bitch | strong, very common | | WP | keseki (three syllables; medium confidence) |
| 좆 jot, 존나 jonna | dick; "fucking" | strong / medium, very common | | WP | — (ㅈ ≠ t, d) |
| 보지 boji, 씹 ssip | cunt | strong | | WP | — |
| 병신 byeongsin | "retard" | strong, very common | | WP | — |
| 년 nyeon, 놈 nom | bitch, bastard | medium | | WP | — |
| 개 gae- | dog; "fucking" prefix | mild-medium | | WT | ge (tb); ke is heard as 케 (aspiration), noise |
| 깜둥이 kkamdungi, 짱깨 jjangkkae, 쪽바리 jjokbari | slurs | strong | | M | kandungi (tb) |

### Persian (~80–110 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| کس kos (-e nanat) | cunt (your mother's) | strongest | | WT; M | — (final s) |
| کیر kir | dick | strongest | | WT; M | — (r ≠ l) |
| کون kun | ass | strong, very common | Iran, Afghanistan | WT | kun |
| کونی kuni | gay man (slur); "asshole" | strong | | WT | kuni |
| جنده jende | whore | strong | | WT; M | — |
| گه goh | shit | medium (like English *shit*; *goh nakhor*) | | WT; M | go (tb; h lost) |
| جاکش jākesh | pimp | strong | | M | — |
| ان an | poo (childish) | mild | | WT | an (noise) |

### Hausa (~80 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| ɓurar uwarka | your mother's cunt | strongest | | M (low) | — |
| shege | bastard | strong, very common | | M | — (sh) |
| karuwa | prostitute | strong | | M | — (r) |
| gindi (in *gindin uwarka*) | buttocks | medium alone | | M | gindi (tb) |
| wawa | fool | mild | | M | — |
Only 22 WT rows; confidence low.

### Swahili (~70–100 m, mostly second-language)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| kuma, kumamako | cunt, your mother's cunt | strongest | East Africa | WT | kuma |
| (ku)tomba | fuck | strongest | | WT; M | tonba (n assimilates to m before b) |
| mboo | dick | strong | | WT | — (mb-) |
| msenge | gay man (slur) | strong | | M | senge (tb) |
| malaya | prostitute | medium-strong | | M | malaya (tb) |
| mavi, matako, fala | shit, buttocks, fool | mild-medium | | M | fala, matako (tb) |

### Javanese (~68 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| jancuk / cuk | (fuck) | strong, very common (East Java) | | WT; M | — (c) |
| asu | dog (curse) | strong as curse; neutral "dog" in ngoko | | WT | asu (tb) |
| tempik, turuk | cunt | strongest | | M | — |
| kontol, ngentot | as Indonesian | strongest | | M | — |
| bajingan, matamu | scoundrel, "your eyes" | medium | | M | — |

### Italian (~68 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| bestemmie (*porco dio*, *dio cane*) | blasphemy | strongest in Italy (WP); S24 found blasphemy rare in "worst word" lists overall | | WP; M | — |
| cazzo | dick; "fuck" | strong, the commonest | | WP | — |
| fica / figa | cunt; "cool" (North) | strong, common | North Italy (*figa*) | WT | fika, figa |
| puttana, figlio di puttana, troia | whore, slut | strong | | WT; M | putana |
| vaffanculo, stronzo, coglione | | medium-strong | | WP | — |
| frocio, negro | slurs | strong | | M | — |
| minchia | dick | strong | Sicily | M | minkiya (tb) |
| culo, merda | | medium | | M | kulo (tb) |

### Punjabi (~150 m, Pakistan + India)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| ਲੰਨ/لن lan, lun | dick | strong, very common | | WT | lan, lun |
| ਫੁੱਦੀ phuddī | cunt | strongest | | WT; M | pudi |
| ਭੈਣਚੋਦ bhainchod | sisterfucker | strongest | | OF21 strong; M | — |
| ਕੰਜਰ kanjar | pimp | strong | | WT; M | — |
| ਕੁੱਤੀ kuttī | bitch | strong | | M | kuti (tb) |
| ਚਮਾਰ chamār, ਚੂੜ੍ਹਾ chūṛhā | caste slurs | strong | | OF21 strong | — |

### Gujarati (~62 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| ભોસડી bhosḍī, બેનચોદ | cunt, sisterfucker | strongest | | WT; M | — |
| લોડો loḍo / લોડા | dick | strong | | WT; M | loda (via Hindi); lodo (tb) |
| ગાંડુ gāṇḍu | mad (not vulgar in Gujarati) | mild | | M | gandu (hard via Hindi) |
| રાંડ rāṇḍ | whore | strong | | M | — |

### Thai (~61 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| หี hǐi | cunt | strongest | | WT; M | — (h) |
| ควย khuay | dick | strongest | | WT; M | — |
| เย็ด yét | fuck | strongest | | WT; M | — (final t) |
| เหี้ย hîa | monitor lizard; "bastard" | strong, very common | | WT; blog sources | — |
| สัตว์ sàt | animal (insult) | strong | | M | — |
| มึง mʉng / กู kuu | rude "you" / "I" | medium; very common among friends | | WT | mon, mun (tb: ʉ ≠ o, u); gu (tb) |
| แม่ง mɛ̂ng | "fucking" | medium-strong, very common | | WT | men (tb) |
| ขี้ khîi | shit; also an everyday prefix (*khîi-kìat* "lazy") | mild-medium | | WT | ki (tb) |
| ค (khɔɔ) | letter standing for ควย | mild euphemism | | WT | ko (noise for Thai) |
| particles วะ wá, เอ็ง, หมา, โหล | | not offensive or mild | | (tool noise) | — |

### Polish (~41 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| kurwa | whore; "fuck" | strongest, the commonest | | BR; WP | — (r) |
| chuj, pizda, pierdolić | dick, cunt, fuck | strongest | | BR | — |
| jebać, jebany | fuck, fucking | strongest | | BR | yeba |
| skurwysyn | son of a whore | strong | | M | — |
| pedał, ciota | gay man (slurs) | strong | | WT; M | peda (tb) |
| suka | bitch | strong | | WT | suka |
| dupa | ass | mild, very common | | M | dupa (tb) |

### Yoruba (~46 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| òbò | vagina/cunt | strong | Nigeria, Benin | WT (the tool maps it to "b": a bug) | obo (medium confidence; tones LL) |
| okó | penis | strong | | WT | oko (tb: = *oko* "farm", *ọkọ* "husband") |
| dó | fuck | strong | | WT; M | do (noise: many homophones) |
| ashawo | prostitute | medium-strong, Nigeria-wide | | M | asawo (tb) |
| wèrè, ọ̀dẹ̀, yeye | mad, fool, useless | mild-medium | | M | yeye (tb) |
| ìdí | buttocks; also "reason" | mild | | M | idi (noise) |

### Amharic (~58 m)
| word | meaning | grade | region | source | forms |
|---|---|---|---|---|---|
| ሸርሙጣ sharmuṭa | whore | strongest | | WT; M | — |
| ቁላ q'ula | dick | strong | | WT; M | kula (tb: ejective q' ≠ k) |
| ቂጥ q'iṭ | ass | medium | | M | — |
| ጋላ gala | Oromo (ethnic slur) | strong, declining | Ethiopia | M | gala (tb) |
| ባሪያ bariya | slave (slur) | strong | | M | — |
Only 12 WT rows; confidence low.

### Egyptian Arabic: see Arabic. Malay: see Indonesian.

## One-syllable verdicts (step 4)

`blocked()` matches 80 of 140 forms. Verdicts: **hard 5**, **tie-break 16** (pi, pin, ki, ken, gan, ko, du, ge, go, gu, gun, men, mon, mun, man, lo), **noise 59**. "Near" = matched only through `key()` (voicing, e/i, o/u merged), which no listener group here actually merges in these words.

| form | what the tool matched | verdict | reason |
|---|---|---|---|
| en | Thai เอ็ง (rude "you") | noise | mild pronoun |
| an | English *-hon*; Persian ان (poo, childish) | noise | rare / childish |
| on | English *hon*; Vietnamese bóng (onset dropped) | noise | rare slur; mapping bug |
| **pi** | English *pee*; Mandarin 屄 /pi/; 批; Tamil *pī*; Thai ปี้ | tie-break | *pee* isn't offensive (WT informal; not in OF21). Tamil *pī* medium. Mandarin 屄 is **bi** for Mandarin ears (unaspirated), not pi; 批 pī strong only in Southwest compounds |
| pin | French *pine* | tie-break | exact for French ears; dated |
| pen, bin, ben | French *pine* (near) | noise | French contrasts i/e and p/b |
| pa | Korean 빠 (fanboy) | noise | not offensive |
| pan, ban | Russian пан; English *bong* | noise | "lord"; rare slur |
| pon | Thai พ่อง, English *poon*, *bong* | noise | rude "your father" ≠ pon; *poon* rare |
| pun, bon, bun | same (near) | noise | |
| ti | Chinese "D"; Quebec *cul* | noise | mapping artefacts |
| tin, ten, din, den | English *gin*, *ding*, *Chen* | noise | rare or dated slurs, wrong consonant |
| te | French *'tain* | noise | |
| tan, dan | English *tang*; Vietnamese thằng | noise | *tang* rare; thằng mild, vowel differs |
| ton, tun, don, dun | Korean 존 jon- | noise | ㅈ ≠ t, d |
| ki | Thai ขี้; French *cul* | tie-break | Thai khîi exact (our k is aspirated) but mild-medium and an everyday prefix |
| kin, gin, gen | French *ken* (near) | noise | |
| ken | French *ken* (= *niquer*) | tie-break | exact, strong, but niche slang |
| ke | Korean 개; Thai เข้ | noise | aspirated ke is Korean 케, not 개 |
| kan | Cantonese 姦 | noise | written word; Mandarin hears 看 "look" |
| gan | same (near); Mandarin 干/幹 | tie-break | neutral "do"; Taiwan interjection; Hindi *gāṇḍ* without its final |
| ko | French *con*; Thai ค | tie-break | medium, very common |
| kon, gon | *coon*, Persian *kun* (near) | noise | both languages contrast o/u |
| **ku** | Portuguese *cu* | **hard** | strong, very common, exact |
| **kun** | Persian *kun*, *kuni*; English *coon* | **hard** | strong, common (Persian), exact |
| fi, fa, fo, fu | English initialisms FY, FA, FO, FU | noise | nobody says initialisms as one syllable |
| si | English *she-he*; Chinese 死 | noise | mapping bug; "die" isn't offensive |
| sin, sen | Japanese 非人 *hinin* | noise | mapping bug (ç → s) |
| se | Vietnamese dê | noise | onset wrong |
| san | English *San* (people) | noise | ethnonym |
| bu | English *buh* | noise | spelling |
| di | Thai ดี้ | noise | slang, not a slur; Vietnamese đĩ is heard as đi "go" |
| de | German *Hundescheiße* (fragment) | noise | mapping bug |
| da | English *they* /ðə/; Persian جق | noise | mapping bug (ð → d) |
| du | English *Jew* | tie-break | *Jew* isn't a slur by itself (OF21 mild) and dʒ ≠ d; but Vietnamese đụ (strongest, South), toneless |
| ge | French *gueux* | tie-break | *gueux* archaic; but Korean 개 gae (mild-medium) is heard here |
| **go** | Persian گه *goh* | tie-break | medium (≈ *shit*), final h lost. Draft had it hard |
| gu | Japanese グエン | tie-break | Thai กู (rude "I", medium); the tool's Japanese match is noise |
| gun | *coon*, *kun* (near) | tie-break | Mandarin 滚 gǔn "get lost" (medium) |
| min | Thai แม่ง (near) | noise | |
| men | Thai แม่ง | tie-break | medium-strong intensifier, ŋ → n |
| mon, mun | English *mong*; Thai มึง; หม่อง | tie-break | *mong* strong (UK) but needs final ŋ; มึง medium |
| me | Vietnamese mẹ | noise | "mother" |
| ma | Thai หมา | noise | "dog" |
| man | Bengali মাং | tie-break | weak: regional word, final ŋ; = English *man* |
| mo | Thai โมะ | noise | rare slang |
| nin, nen | Vietnamese nứng | noise | ư ≠ i, e |
| na | English *nuh* | noise | spelling |
| nan | Korean 년; Thai นาง, งั่ง | noise | wrong vowel/onset; Cantonese 撚 nan2 has short ɐ |
| **lan** | Hindi-Urdu *laṇḍ*; Punjabi *lan*; English *langer* | **hard** | strong, very common (Punjabi exact); Cantonese 撚 near |
| lo | Vietnamese lọ; Thai โหล | tie-break | weak: lọ "jar" first |
| **lon** | Vietnamese lồn; Thai โล้น "bald" | **hard** (medium) | strongest; tone mismatch (see table) |
| **lun** | Vietnamese lồn (near) | **hard** (medium) | via Punjabi/Urdu *lun*, not via lồn (Vietnamese contrasts o/u) |
| wa | Thai particles | noise | |
| yin, yen | Punjabi یہنا (fragment) | noise | mapping bug |
| yon, yun | Thai ยุ่น | noise | mild |
| yu | Turkish *yuh* | noise | surprise interjection |

First draft, row by row:

| draft | verdict | why |
|---|---|---|
| lồn → lon | keep hard (medium) | strongest, common alone; toneless spellings are its euphemisms. Native check on tone |
| lund / lan → lan, lun | keep both hard | Punjabi *lan/lun* exact; Hindi *laṇḍ* near |
| 屄 bī → bi | **tie-break** | bi = 比 笔 必 鼻 first; bī is mostly heard in compounds. Note the tool blocks **pi** for it, not bi |
| Tamil pī → pi, bi | **tie-break** (pi only) | medium word; bi not a match |
| cu → ku | keep hard | |
| kun, coon → kun | keep hard | |
| goh → go | **tie-break** | medium, final h lost |
| con (ko), khî (ki), gàn (gan, kan), 개 (ke), mʉng (mon, mun), pee (pi) | tie-break, except **kan** and **ke** → noise (aspiration makes them 看 and 케), **pee** → not offensive | |

## Recommended hard list

One-syllable (5): **ku, kun, lan, lun, lon**.

Two-syllable (35): dengu, diu, fakin, faku, figa, fika, fiken, foda, fode, gandu, kanki, kuma, kuni, loda, magi, manko, nega, niga, nige, obo, paki, pede, pudi, puke, puki, puku, punda, puta, puto, siki, suka, tite, tonba, yeba, yoba.

Longer (8): buseta, kanake, keseki, omanko, pukima, pundai, putana, tewadiya.

Medium-confidence entries, for the native check first: lon, lun, diu, obo, siki, keseki, faku, fakin, yoba.

All are in `offensive-hard-draft.tsv`. The tie-break forms named above (tb) are the candidates for the graded tie-break list.

## Findings that bear on the decision

1. **The tool maps aspiration the wrong way for about 30% of first-language listeners.** Since p t k became aspirated (2026-10-13), Mandarin, Cantonese, Korean, Thai and Indic listeners hear our p t k as their aspirated stops and our b d g as their plain ones. `segs()` maps IPA [p] → p, so Mandarin 屄 [pi] blocks **pi** (heard as 批/劈) and leaves **bi**; Korean 개 blocks **ke** (heard as 케); 干 blocks **kan** (heard as 看). It also misses real matches: Bengali *khanki* = **kanki**, Punjabi *phuddi* = **pudi**. `key()` merges voicing, the opposite of what these listeners merge.
2. **`segs()` drops vowels with diacritics**: about 1,300 of 32,910 rows lose a vowel (Chinese 485, Spanish 201, Portuguese 160, Japanese 135; Yoruba *òbò* → "b", Japanese *manko* → "mnko", Telugu *deṅgu* → "degu", Hindi *gāṇḍū* → "gndu"). Some of the strongest words never match anything.
3. **`kind()` takes the union of tags across all senses.** *pee* is "strong" because a secondary sense ("to drizzle") is tagged "mildly vulgar", and "primary" because the first gloss mentions urinating. Neutral words (*they*, *San*, *Jew*, *mẹ*) come in the same way. Ungraded tags plus the whole-word Zipf check can't separate strength, as the design log already says.
4. **Tone languages give weak one-syllable matches.** A toneless CV(n) is many ordinary words in Mandarin, Cantonese, Vietnamese and Thai, and loan syllables default to a level tone (VT). Only *lồn* survives as hard, on its standalone frequency.
5. **The hard list costs little.** 5 of 140 one-syllable forms (the tool blocks 80); 35 of 18,900 two-syllable strings. None is a word in use now. A hand-kept list (this TSV) can replace the Wiktionary-tag block, with the tool used only to rank tie-breaks.

## Method notes (step 5)

- **How brand screening is done.** Agencies send candidate names to native speakers living in each market, usually 1–3 per language (tolingo: one specialist per market; easybrandcheck: 3, 5 or 7 linguists). The speakers report meaning, connotation, slang, pronunciation and offensive potential, and rate each name clear / flagged / critical (BS). They mostly judge written names plus a pronunciation; audio isn't standard. Automated lists are a pre-filter only (BS: "automated tools regularly miss").
- **Cost here.** Easybrandcheck lists €75 per language for 3 linguists, about 10 names per check. Screening the 140 syllables plus about 600 roots (around 74 checks of 10) in 34 languages that way would cost about €190,000 at list price: unrealistic. A cheaper design that fits this project: one audio sheet per language (the 140 syllables, spoken with Apupiwe's stress and aspiration, plus the 35 two-syllable hard candidates and the tie-break forms), with one question per item: "Does this sound like a rude or offensive word in your language? Which, and how bad (1–4)?" With 3 speakers per language on a crowd platform at about £9/hour for 30 minutes, that's about 34 × 3 × £4.50 ≈ £460 plus fees (estimate, M). Hausa, Amharic, Yoruba, Javanese and Marathi speakers may be scarce on such platforms.
- **What this desk research can't settle without native speakers:**
  1. Whether a toneless **lon** is heard as lồn (and **bi** as 屄, **du** as đụ, **gan** as 幹) in running speech, especially at the falling end of a sentence.
  2. Whether Russians hear **yeba** / **yoba** as *yebat'* with Apupiwe's first-syllable stress.
  3. Grades marked M, especially Hausa, Amharic, Yoruba, Javanese, Gujarati, Marathi, Telugu and Tamil.
  4. Whether Indian listeners really hear Apupiwe d as retroflex (**gandu**, **loda**, **punda**), and whether **kanki** / **pudi** are heard as aspirated.
  5. Whether a hard one-syllable form inside a two-syllable word (**lon**pa, **kun**ta) is heard as the word, in Vietnamese especially.
  6. Regional strength: *puto* (Mexico vs Spain), *polla*, *cu* (Brazil vs Portugal), *figa* (North vs South Italy), *kun* (Iran vs Afghanistan).
  7. The S24 ratings would settle the Mandarin, Cantonese, Thai, Spanish, French, German and Italian grades once OSF responds.
