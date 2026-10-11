# UDHR terminology pass

Before translating the Universal Declaration of Human Rights (`source.md`), this pass settles how to say each recurring or tricky concept. It uses only the words in `lexicon.tsv`, `grammar.tsv` and `compounds.tsv`, following `vocabulary-method.md` section 5.

How to read the table:
- **Times** is a rough count in `source.md`, including derived forms (free/freedom/freely).
- **Syl** is the syllable count of the main form. It is one syllable per vowel, since this phonology has no diphthongs.
- **Clarity** is a guess at how a reader with only the dictionary would do. *Clear* means they get it right. *Guessable* means they get it from context. *Unclear* means they would likely miss it.
- **R** is a placeholder for the proposed root "respect, honour" (row 7). Its form is left to `tools/words.py`.
- The international-form check for possible loans used these eight languages: Mandarin, Hindi, Arabic, Spanish, Russian, Indonesian, Swahili and Japanese (written zh, hi, ar, es, ru, id, sw, ja).

## Terms

| # | English concept | Times | Best expression with existing words (literal gloss) | Syl | Clarity | Recommendation |
|---|---|---|---|---|---|---|
| 1 | right(s); is entitled to | ~55 | **sogan** "a right" | 2 | clear | Keep (root exists). |
| 2 | human rights | ~10 | **sogan pi ewo** "rights of a person" | 5 | clear | Keep phrase. |
| 3 | Universal Declaration of Human Rights; this Declaration | ~8 | **kemin pi sogan pi ewo we** "document of the rights of all people"; afterwards **kemin tan** "this document" | 9 | clear | Keep phrase. |
| 4 | freedom, free, freely, liberty | ~30 | **enpa** "free, not held or controlled", a noun by position (4.2). "Freely" is **enpa** after the verb: **waka enpa** "choose freely". | 2 | clear | Keep (root exists). |
| 5 | free of charge ("education shall be free") | 1 | **go mu unfu** "anyone not pay" (compounds.tsv) | 4 | clear | Keep. Don't use **enpa** here: it means unconstrained, not gratis. |
| 6 | dignity; worth | 6 | **bawe pi ewo** "a person's importance". "Equal in dignity" is **gun bawe kige** "are equally important". | 5 | guessable | Build on R if R is adopted: **R pi ewo** "a person's honour". Otherwise keep **bawe pi ewo**. |
| 7 | respect (for persons, for rights) | 4 (plus dignity, honour, reputation: ~12 in all) | For rights: **kuwi** "keep". For persons: **pume wun wan gun bawe** "think that they are important". | 2 / 7 | rights: clear; persons: unclear | **New root "respect, honour".** The reasons are in "Why one root" below. |
| 8 | honour, reputation | 2 | **suso upe** "good name". This is the same calque as id *nama baik*, ru *доброе имя*, es *buen nombre*, zh 名誉. | 4 | clear | Keep phrase. Use R for "honour" only where respect is meant. |
| 9 | equal, equality, equally | 13 | **kige** "same"; equality is **gun kige** "being the same" | 2 | clear | Keep. |
| 10 | law; by law, according to law | 9 | **wabun** "rule, law"; **fu wabun** "like the law (says)" | 2 / 3 | clear | Keep (law and rule are already one word, design log 2026-10-10). |
| 11 | before the law; protection of the law | 3 | **kige li wabun** "the same for the law"; **kuwi pi wabun** "the law's keeping" | 5 | guessable | Keep phrase. |
| 12 | rule of law | 1 | **lula pi wabun** "power of law" | 5 | guessable | Keep phrase. |
| 13 | constitution | 1 | **wabun bawe pi fowo** "a country's important law" | 7 | guessable | Keep phrase. Not a loan: only es, ru and id share *constitución/конституция/konstitusi*. zh 宪法, hi संविधान, ar دستور, sw *katiba* and ja 憲法 all differ. |
| 14 | country, State (the polity), nation, territory | ~28 | **fowo pi funti** "land of a people"; then **fowo** alone where context allows (4.5) | 5 / 2 | guessable | **Keep phrase, but this is the strongest candidate for a second root.** The reasoning and add-back trigger are below. Not a loan: 国 *guo/kuni*, देश, بلد/دولة, país, страна, negara, nchi all differ. |
| 15 | national; international | ~10 | **pi fowo** "of the country"; **pi fowo la** "of the countries" (international law: **wabun pi fowo la**) | 3 / 4 | guessable | Keep phrase. |
| 16 | people(s) (a nation as people) | ~6 | **funti** "group"; **ewo la pi fowo** "the country's people" | 2 | guessable | Keep. |
| 17 | United Nations; Member States; Charter; General Assembly | ~8 | **funti pi fowo la** "group of countries"; **fowo la pi bu** "its countries"; **kemin pi funti pi fowo la** "the UN's document"; **fanmu pi funti pi fowo la** "the UN's gathering" | 6 | guessable | Calque. All eight check languages translate the name: 联合国, संयुक्त राष्ट्र, الأمم المتحدة, Naciones Unidas, ООН, PBB, Umoja wa Mataifa, 国際連合. |
| 18 | government; the State as authority; public service | ~6 | **no wungu la** "the leaders" (worked in vocabulary-02); public service is **doku pi no wungu la** "work of the leaders" | 4 | guessable | Keep phrase. |
| 19 | sovereignty, self-governing, trust territory, jurisdiction | 3 | **fowo man wungu nen** "a land that leads itself"; **fowo man fowo eni wungu** "a land another land leads" | 6 | guessable | Keep phrase. |
| 20 | political | 4 | **pi wungu** "of leading" | 3 | guessable | Keep. Not a loan, because there are three competing forms: *politik* (es, ru, id), 政治 *zhengzhi/seiji* (zh, ja) and *siyasa/siasa* (ar, sw); hi has राजनीति. |
| 21 | democracy, democratic | 1 | **lite man ewo we waka no wungu** "a way where all people choose the leaders" | 11 | clear | Keep phrase here. It is the closest loan candidate, **demokulasi** (from `names.py`). ar, es, ru, id and sw share it; zh 民主, hi लोकतंत्र and ja 民主主義 don't. That is the same 5/8 as **polisu**, but there's only 1 use. Revisit if news texts need it. |
| 22 | vote, election, suffrage, representatives, secret ballot | 6 | **waka** "choose"; election is **waka pi no wungu** "choosing of leaders"; suffrage is **sogan li waka**; representatives are **no wungu man go waka** "leaders whom people choose"; secret vote is **waka kunsu** "choose privately" | 2 / 6 | clear | Keep. Election literally means "choosing" in hi *chunav*, ar *intikhab*, es *elección*, ru *выборы*, id *pemilihan* and sw *uchaguzi*. |
| 23 | justice, just, fair | 5 | **denku** "correct" | 2 | guessable | Keep. The correct~just link is wide: zh 正/公正, ja 正しい, ru *справедливый* from *правда*, es *justo* "exact". Add-back: a blind reader takes **denku** as "accurate" and loses the moral sense. |
| 24 | peace, peaceful | 3 | **bonwi**; peaceful is **gan bonwi** "with peace" | 2 | clear | Keep. |
| 25 | religion, religious | 6 | **lite pi nosen** "way of god(s)" | 5 | guessable | Keep phrase. Not a loan: 宗教, धर्म, دين, religión, религия, agama, dini differ. It is weak for non-theistic religions. Add-back: a test reads it as "magic" or excludes Buddhism. |
| 26 | belief; faith (in rights) | 4 | belief is **ge pume feko** "what is thought true"; faith is **gewan** "trust" | 5 / 2 | guessable | Keep phrase. |
| 27 | thought; opinion | 5 | **pume** "think"; opinion is **ge pume** "what is thought" | 2 / 3 | clear | Keep. |
| 28 | conscience; morality | 4 | **lugo pi upe yen yomo** "knowing of good and bad"; morality is **lite upe** "good ways" | 8 | guessable | Keep phrase. es *conciencia* and ru *совесть* are also "co-knowing". |
| 29 | reason (the faculty, Art 1) | 1 | **lenu pume** "can think" | 4 | clear | Keep phrase. **ukun** is "reason" as in *cause*, so don't use it here. |
| 30 | expression; manifest; impart | 4 | **oyi** "say", **wuye** "show", **iko** "tell" | 2 | clear | Keep. |
| 31 | information, ideas, media | 3 | **ge iko** "what is told"; **gason** "idea"; media is **du iko** "things for telling" | 3 | guessable | Keep. Not a loan: only es, ru and id share *información*; zh 信息, hi सूचना, ar معلومات, sw *taarifa* and ja 情報 differ. |
| 32 | worship, practice, (religious) observance, teaching | 4 | worship is **oyi tun nosen** "talk to god(s)"; practice is **muge** "do"; observance is **kuwi** "keep"; teaching is **tofo** | 5 | guessable | Keep. |
| 33 | marriage, marry, spouses, dissolution, wedlock | 6 | **bedan** "marry, wedding"; **ofin** "spouse"; dissolution is **fugi pi bedan** "end of the marriage"; born out of wedlock is **mole yen wede mu gun ofin** "parents are not spouses" | 2 / 5 | clear | Keep (roots exist). |
| 34 | consent | 1 | **tayu** "agree" | 2 | clear | Keep. |
| 35 | family; human family | 6 | **yonyo**; **yonyo pi ewo we** "family of all people" | 2 / 6 | clear | Keep. |
| 36 | men and women of full age (adult) | 1 | **lowu yen futa man sin guge** "men and women who have grown" | 9 | guessable | Keep phrase. There is no "adult" root; watch for it in other texts. |
| 37 | motherhood, childhood, children, parents | 5 | **gun mole** "being a mother"; **gun tiwu** "being a child"; **tiwu**; **mole yen wede** (compounds.tsv) | 3 | clear | Keep. |
| 38 | born, birth | 3 | **tuko nume** "start living" | 4 | guessable | Keep phrase here. BE BORN is a basic concept (CLICS rank 540, 76 families, 6 areas, but past the data-backed 300) and every check language has a simple verb for it. Add-back: a narrative or biography test loses meaning on births or birthdays. |
| 39 | property; own | 3 | own is **ibe** "have" (HAVE/OWN lumped in 29 CLICS families); property is **musu pi nen** "one's own things" | 2 / 4 | clear | Keep. |
| 40 | education | 8 | **tofo** "teach", a noun by position; to be educated is **gun tofo**; school is **pu yesa** (vocabulary-04) | 2 | clear | Keep. |
| 41 | elementary, higher, technical and professional education; compulsory; merit | 5 | **tofo pi tiwu** "children's teaching"; **tofo tisan** "high teaching" (the "high" metaphor is in all eight languages); **tofo li doku** "teaching for work"; compulsory is **keya**; merit is **lenu** "ability" | 4-5 | guessable | Keep phrase. |
| 42 | work, employment, unemployment | 8 | **doku**; unemployment is **mu ibe doku** "not having work" | 2 / 5 | clear | Keep. |
| 43 | pay, remuneration, equal pay | 3 | **nimo pi doku** "money of work"; equal pay for equal work is **nimo kige li doku kige** | 5 | clear | Keep. |
| 44 | trade union | 1 | **funti pi no doku** "group of workers" | 6 | clear | Keep phrase. |
| 45 | rest, leisure, holidays with pay, working hours | 4 | rest is **bamo doku** "stop working"; leisure is **muyi enpa** "free time" (same calque in es, ru, id, zh, ja); holidays are **dili enpa gan nimo** "free days with money"; **awuwa pi doku** | 4 | clear | Keep. |
| 46 | standard of living, well-being, general welfare | 4 | **lite pi nume** "way of living"; **pata upe** "good life"; **upe pi ewo we** "the good of all people" | 4-6 | guessable | Keep. |
| 47 | health, medical care, sickness, disability | 4 | health is **gawo upe** "good body"; medical care is **yema li ewo simi** "help for sick people"; **simi**; disability is **mu lenu doku** "cannot work" | 4 / 7 | guessable | Keep. **osupitalu** is there if needed. |
| 48 | old age, widowhood, lack of livelihood | 3 | **gun pani** "being old"; **ofin sin kono** "spouse has died"; **mu ibe tonya** "not having enough" | 3-5 | clear | Keep. |
| 49 | food, clothing, housing | 1 each | **pasu**, **lonne**, **guyi** | 2 | clear | Keep. |
| 50 | fear and want | 1 | **nuta** "fear"; want (poverty) is **mu ibe tonya** "not having enough" | 5 | clear | Keep. |
| 51 | torture | 1 | **muge wekun bi gan momu** "cause great pain on purpose" | 8 | guessable | Keep phrase. Not a loan: 酷刑, यातना, تعذيب, tortura, пытка, penyiksaan, mateso, 拷問 differ. |
| 52 | cruel, inhuman, degrading treatment | 1 | cruel is **bi yomo** "very bad"; inhuman is **mu fu ewo** "not like a person"; degrading is **muge meli ewo** "make a person small" | 6 | guessable | Keep phrase. |
| 53 | punishment, penalty | 3 | **wekun pi wabun** "pain of the law" (cf. Latin *poena*, es *pena*); heavier penalty is **wekun ke gogo** | 5 | guessable | Keep phrase. |
| 54 | crime, penal offence, criminal, violation | ~12 | **alun wabun** "break the law"; criminal is **no alun wabun**; violating rights is **alun sogan** | 4 | clear | Keep. "Break the law" is the idiom in hi, ar, ru *нарушить*, sw *kuvunja sheria* and ja 法を破る. |
| 55 | charge, accused, prosecution | 3 | **oyi wun wan alun wabun** "say that he broke the law" | 8 | guessable | Keep phrase. Keep it apart from persecution (row 66). |
| 56 | guilty, innocent, presumed, proved | 4 | guilty is **sin alun wabun** "has broken the law"; innocent is past frame + **mu alun wabun**; presumed is **pume** "think"; proved is **wuye wun … feko** "show that … is true" | 4-5 | guessable | Keep. **mu sin** means "not yet" (8.1), so it can't express "innocent". |
| 57 | court, tribunal; trial, hearing; competent | 5 | **pu pi wabun** "place of law" (like zh 法院 "law court"); hearing is **doma pi pu pi wabun** "the court's listening" (ru *слушание*, es *audiencia*); deciding a case is **waka fu wabun** "choose by law" | 4 / 7 | guessable | Keep phrase. A root "judge, decide a case" is a candidate (the decide~judge lump is in sw *amua*, ar *ḥakama*, ru *решать*, zh 判). Add-back: a reader takes **waka** for voting. |
| 58 | independent, impartial | 2 | **enpa** "free"; impartial is **kige li we** "the same for all" | 2 / 4 | guessable | Keep. |
| 59 | remedy; defence | 2 | remedy is **muge upe** "make good" (= fix, 4.2); defence is **kuwi nen** "keep oneself" | 4 / 3 | guessable | Keep. |
| 60 | arrest, detention, exile | 3 | arrest is **yidu** "take"; detention is **yonnu** "hold"; prison is **pu yonnu**; exile is **muge kusa** … **se fowo pi nen** "make leave own country" | 2 / 4 | guessable | Keep. Don't use **kuwi** for detention, because here **kuwi** is "protect". |
| 61 | arbitrary, arbitrarily | 4 | **gan ukun fa** "with no reason" | 4 | clear | Keep. |
| 62 | deprive of | 2 | **yidu** … **se** "take … from" | 3 | clear | Keep. |
| 63 | slavery, slave, servitude, slave trade | 4 | slave is **ewo man ewo eni ibe** "a person another person owns"; slavery is **ibe ewo** "owning people"; servitude is **doku man mu enpa** "unfree work"; slave trade is **bika yen koda ewo** "buying and selling people" | 4-9 | clear | Keep phrase. |
| 64 | asylum | 1 | **pu sonli mon fowo eni** "a safe place in another land" | 8 | clear | Keep phrase. Not a loan: 庇护, शरण, لجوء, asilo, убежище, suaka, hifadhi, 庇護 differ. |
| 65 | nationality, citizen | 4 | **gun ewo pi fowo** "being a person of a country"; citizen is **ewo pi fowo** | 6 | guessable | Keep phrase. Not a loan: 国籍, राष्ट्रीयता, جنسية, nacionalidad, гражданство, kewarganegaraan, uraia differ. |
| 66 | persecution | 1 | **fesun** "hunt" (de *Verfolgung*, es *persecución* and ru *преследование* are all "pursuit") | 2 | guessable | Keep. |
| 67 | movement and residence; borders, frontiers | 4 | **isi yen nume** "go and live"; border is **lifin pi fowo la** "the between of countries"; regardless of frontiers is **tun fowo mesun** "to every country" | 6 | guessable | Keep phrase. |
| 68 | limitation, limit | 4 | Depends on context: **mu ke se** "at most" (9.3), **bamo** "stop", **na wabun** "only the law" | 3 | guessable | Keep. A root "boundary, limit" would cover row 67 too (hi सीमा, ar حد, id *batas* and sw *mpaka* lump them). Add-back: other texts keep needing "limit" or "border". |
| 69 | society, social, community | ~15 | society is **ewo we** "all people"; social is **pi ewo we**; community is **funti** "group"; social origin is **funti man go obu se** "the group one comes from" | 3 / 4 | guessable | Keep phrase. Not a loan: 社会, समाज, مجتمع, sociedad, общество, masyarakat, jamii differ. |
| 70 | security (of person); social security | 5 | **gun sonli** "being safe"; social security is **yema se ewo we** "help from all people" | 3 / 6 | guessable | Keep. |
| 71 | protection, protect; observance (of rights) | ~12 | **kuwi** "keep". The reference already uses it this way: **so nosen kuwi me** "may God keep you" (7.1). ja 守る, zh 守, es *guardar* and id *menjaga* lump keep, protect and observe in the same way. | 2 | clear | Keep. |
| 72 | discrimination, distinction | 6 | without discrimination is **kige li we** "the same for all"; discriminate is **mu muge go kige** "not treat everyone the same" | 4 / 6 | guessable | Keep phrase. |
| 73 | race, colour, sex (as grounds of discrimination) | 3 | race is **niki pi ewo** "kind of person" (zh 人种 and ja 人種 are "person-kind"); colour is **niki pi unne** "kind of skin"; sex is **lowu lu futa** "man or woman" | 5 | guessable | Keep. The lexicon has no general "colour" word (CLICS rank 1238), which is fine here. |
| 74 | privacy, home, correspondence | 3 | **musu kunsu pi wan** "his private things"; **guyi**; correspondence is **ge sege** "what is sent" | 4 / 3 | guessable | Keep. |
| 75 | interference; attacks (on honour) | 3 | **inwa** "enter (into)"; attack on reputation is **oyi yomo fu suso pi wan** "speak badly about his name" | 2 | guessable | Keep. |
| 76 | culture, cultural life | 2 | **lite pi nume pi funti** "a group's way of living" | 8 | guessable | Keep phrase. Not a loan: 文化, संस्कृति, ثقافة, cultura, культура, budaya, utamaduni differ. |
| 77 | art(s), artistic, literary | 3 | arts are **ge muge li sesa** "things made for beauty"; literary works are **ge tusi** "what is written"; author is **no muge** "maker" | 6 | guessable | Keep phrase. Not a loan: 艺术, कला, فن, arte, искусство, seni, sanaa, 芸術 differ. |
| 78 | science, scientific advancement | 2 | **guge pi lugo** "growth of knowledge"; science itself is **lugo** "knowledge" | 5 | guessable | Keep phrase (3b gives science no special status). Not a loan: 科学, विज्ञान, علم, ciencia, наука, ilmu/sains, sayansi differ. |
| 79 | moral and material interests | 1 | **upe pi wan** "his good"; material is **pi nimo** "of money" | 4 | guessable | Keep. |
| 80 | economic, resources | 2 | **pi nimo** "of money"; resources are **musu yen nimo** "things and money" | 3 | guessable | Keep. |
| 81 | development, progress, advancement, personality | 10 | **guge** "grow"; development of his personality is **guge pi nen** "growth of oneself" | 2 / 4 | guessable | Keep. |
| 82 | friendship, friendly relations, spirit of brotherhood | 4 | **gun sonu** "being friends"; **fu faba la** "like siblings" | 3 / 4 | clear | Keep. |
| 83 | tolerance | 1 | **efon wun eni pume eni** "allow that others think otherwise" | 9 | unclear | Keep phrase (1 use). Add-back: other texts need it often. |
| 84 | duties, obligations | 2 | **ge keya** "what must (be done)" | 3 | guessable | Keep. |
| 85 | public (vs private); public order | 6 | **mu kunsu** "not private"; public order is **bonwi pi ewo we** "everyone's peace" | 3 | clear | Keep. |
| 86 | assembly, association; join | 4 | **fanmu** "gather"; **funti** "group"; join is **inwa funti** "enter a group" (id *masuk*, ja 入る) | 2 / 4 | clear | Keep. |
| 87 | recognition, recognise as | 4 | **tayu wun** "agree that"; recognised as a person is **wabun pume wan fu ewo** "the law thinks of him as a person" | 3 | guessable | Keep. |
| 88 | proclaim, pledge | 4 | **iko tun ewo we** "tell all people"; pledge is a quote with **de** (G4) | 6 | guessable | Keep. |
| 89 | tyranny, oppression, rebellion | 1 | **lula yomo pi no wungu** "bad power of leaders"; rebellion is **migi no wungu** "fight the leaders" | 8 | guessable | Keep phrase. |
| 90 | everyone, all human beings, mankind, person, member | ~50 | everyone is **go** (10.3); all people are **ewo we**; person is **ewo**; member is **fi pi** "one of" | 1 / 3 | clear | Keep (G1, G7). |
| 91 | world | 2 | **fowo minwe** "the whole earth" | 4 | clear | Keep. |
| 92 | Article N; Preamble (headings) | 31 | **ge oyi pi N** "statement N"; **ge oyi ya** "what is said beforehand" | 5 | guessable | Keep. Avoid **wabun pi N**, since the Declaration isn't law. |

## Why one root

**R "respect, honour"** is the only new root I'd recommend. The case for it:
- **The phrase fails.** The lexicon has no word for respect. The only respect words, **lanno** and **nun**, are a title and a politeness particle. The workarounds split into three phrases depending on context (**kuwi**, **pume wun … gun bawe**, **suso upe**), and none of them carries respect as behaviour. **pume wun wan gun bawe** is 7 syllables and only says what someone thinks.
- **Languages converge on it.** All eight check languages have a simple, everyday word for it: 尊重/尊敬, सम्मान/इज़्ज़त, احترام, respeto, уважение, hormat, heshima, 敬意. Several lump respect, honour and dignity under one word: sw *heshima*, hi *izzat*, id *hormat/kehormatan*. So one root covers respect, honour and dignity (**R pi ewo**).
- **It is frequent.** There are about 12 uses in this text, and it is common in everyday speech in many cultures ("respect your elders").

The method's evidence is thin here, because RESPECT is not a CLICS concept at all, so this rests on the phrase failing and on the eight-language check. **Add-back trigger** (for deleting R): a blind reading of a UDHR draft that uses the row 6-8 phrases gets dignity and respect right. If you'd rather start with zero new roots, run that test first.

**Not recommended for now, in order of strength:**
1. **country** (row 14). This one is close. COUNTRY~LAND is lumped in 30 CLICS families and COUNTRY~EARTH (SOIL) in 24, out of about 70 that attest COUNTRY. That falls in the method's 20–50% band, which calls for building it from the land word, as I did. Against that, it is about 28 uses here at 5 syllables, and it's frequent in modern speech ("which country are you from?"). Add-back trigger: blind readers take **fowo** as soil or ground, or the draft shows **fowo pi funti** as a real length cost. Note that the gloss of **fowo** ("ground, earth or soil") would need "land" added to it.
2. **be born** (row 38). It's a basic concept, but **tuko nume** is clear.
3. **judge, decide a case** (row 57).
4. **boundary, limit** (rows 67-68).

**Loans: none recommended.** No concept in the text has a form shared by all eight languages. The nearest is **demokulasi** (row 21), at 5/8. The lexicon already took **polisu** at the same ratio, so the de facto bar is looser than "the world shares the form". It might be worth settling a number.

## Grammar the text needs

**G1. "Everyone has the right to X" / "is entitled to X"** is **go ibe sogan li X**. **li** takes a noun ("for X"), a verb phrase ("to do X") or a clause (4.4, 12): **go ibe sogan li kusa se fowo mesun** "everyone has the right to leave any country". By 4.4, **li** attaches to the verb **ibe**, not to **sogan** ("has a right, for leaving"). The meaning survives, but the reference has no noun complement ("a right *to*"). With a bare noun, **sogan pi pata** "right to life" is also fine. *Question:* should 4.4 allow **noun + li** inside a noun phrase, or is the clause-level reading the intended one?

**G2. "No one shall be V-ed"** is **go keya mu gun V** "anyone must not be V-ed". This uses **keya** (12), **mu** scoping over what follows (6.2), **gun** after another verb (4.7) and **gun** + action as a resulting state (4.7). An example is **go keya mu gun yonnu fu ewo man ewo eni ibe** "no one shall be held as a slave". Some forms to avoid:
- **ewo fa keya …** means "no person is obliged to …", a scope trap.
- **mu keya** means "need not" (6.2). That is exactly right for Art 20.2 ("No one may be compelled to belong to an association"): **go mu keya inwa funti**.

When V is a long phrase (torture), use the generic agent instead: **go mu gun efon muge wekun bi gan momu tun go** "no one may torture anyone" (efon, 12). The second **go** can't be the subject by 10.3. *Gap:* the reference never says that **gun** + verb works as a general passive. 4.7 calls it a resulting state and the rationale points to the topic opener. It works here, but it's worth stating.

**G3. "shall" generally.**
- Obligation is **keya**. "should act" (Art 1) is **wupi**. "may / may not" is **gun efon / mu gun efon** (12).
- Norm-statements like "All are equal before the law" stay as plain statements (1.1), as most translations do (zh 人人生而自由).
- *Gap:* the reference doesn't say whether an unmarked statement may express a norm. **de** isn't usable, since it is only the speaker's own commitment (7.1).

**G4. Reported commitment ("Member States have pledged …").** 7.1 says someone else's intention is reported. The clearest form is a quote with **de**: **fowo la sin oyi: "de din …"** "the countries said: 'we will …'". This also gives "promise" without a root.

**G5. Agentless passives** ("rights set forth in this Declaration", "granted him by the constitution", "education shall be directed to …"). Use an active relative clause with the agent as subject: **sogan la man kemin tan oyi** "the rights this document states" (5.3). For an unknown doer use **ewo bo** (10.3), and the topic opener **pi X,** keeps the patient first (4.3).

**G6. A relative clause after a coordination** ("the rights and freedoms set forth in this Declaration", ~6 times). By 5.3 the clause attaches to the nearest noun, so **sogan yen enpa man kemin tan oyi** reads as "rights, and freedoms that this document states". *Gap:* the reference doesn't say whether a relative clause after **X yen Y** can cover both nouns. Workaround: drop "freedoms" and write **sogan la man …**, since each freedom here is a right anyway.

**G7. Referring back to generic "everyone".**
- In the same clause, "his own" is **pi nen** (10.3): **kusa se fowo mesun, wi fowo pi nen** "leave any country, even his own".
- In a later clause ("…at which **he** has had all the guarantees"), repeating **go** would mean a new "anyone". So use **wan**, the topic person.
- *Gap:* 10.3 doesn't say whether **wan** can pick up a generic **go**. I propose that it can.

**G8. The "Whereas" chain.** The preamble is seven "whereas" clauses before one main clause, which is too heavy for one sentence. 4.3 allows one if/because opener, and 1.4 says heavy material goes last. Translate each "Whereas …" as its own statement, then open the main sentence with the linker **gi tan,** "so," (4.1 slot 2). **tan** stands for the situation (10.3).

**G9. Causatives.** "make (someone) leave" is **muge kusa wan** (4.2, muge + result + object; compare **muge sigo** "undo"). *Gap:* if the result verb has its own object ("make him join a group"), **muge inwa funti wan** is ambiguous. The UDHR avoids this with **keya** (G2), but the reference should say how a causee and a second object are ordered.

**G10. Words the grammar lacks, with workarounds.**
- *without* is **gan X fa** "with no X" (fa is a determiner, 5.2): **gan ukun fa** "arbitrarily".
- *against* is **se** for protection (**kuwi se** "protect from"). A fight takes a direct object (**migi no wungu**).
- *until* is **ya** + clause "before" (4.3): **… ya wabun wuye wun wan alun wabun** "until the law shows he broke it".
- *as* (a person, a member) is **fu** (13).
- *equal in X* is restructured as "X are the same": **R yen sogan pi ewo we gun kige** "everyone's dignity and rights are the same".
- *innocent* needs past frame + **mu** + verb, never **mu sin**, which means "not yet" (8.1).
