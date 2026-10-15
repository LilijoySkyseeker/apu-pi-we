# Imitative and nursery words through the loan panel (imitative-01)

Proposals only; no word was changed. Task: `PROMPT.md`. Decision behind it: design log 2026-10-15, "Root forms stay invented; shared nursery words are tested as loans" (Globasa review, option C, part 3): run imitative and nursery words through the L4 panel before the ~1,500-root placement, since loans keep their forms and roots move (design log 2026-10-13).

## Question

For imitative words (onomatopoeia and the animal and action names built on it) and nursery words, does the world already share a form (goal L4)? If yes, the concept takes that form as a loan before the placement. The study behind it (`research/notes/globasa.md` §8.3, row 53) found these to be the one core area where the world shares forms.

## Answer in short

**One concept passes: mother, as *mama*** (13 of 20, all 7 regions). It rests on two columns that are sensitive to one reading of mine (below), and it collides with **maman** "suck" by the tool's near-identity rule. Everything else fails, most of it far from 12: **the world shares the sounds, not the names.** Children everywhere say *miau*, *mu*, *kwak*, *haha* and *achoo* (Wordbank), but almost no panel language names the cat, the cow or laughing with them, and the sounds themselves are already free in Apupiwe as interjections (reference 2.10). The nursery kin words share shapes but split: *papa* against *baba* by voicing (7 and 9), and *nana*, *dada*, *mama* mean different relatives or things in different languages.

## Method

The panel method of `tests/coverage-01/part3/loans.md` ("Method" and the author's decisions at its top), unchanged:

- For each concept I recorded the everyday word in each of the 20 panel languages and whether a speaker would hear it as the same word as the tested form.
- **Pass:** at least 12 of 20, across at least 4 of the 7 regions EA (zh ja ko), SEA (vi th id tl), SA (hi bn ta), WA (fa ar tr), EU (ru es fr), SSA (sw ha yo), AM (qu).
- **Author's rules applied** (2026-10-13): an everyday loan beside a formal word counts, with a source (pattern 1); memory columns need a source, so a pass that needs a memory-only column fails (pattern 2; "thin deciding columns fail"); two shapes are one form when their adapted forms keep the same consonants (pattern 3); median ties by regions, then length; shared short forms preferred.
- **Nursery and imitative columns (this task's rule):** "the everyday word" includes the word parents and children actually say (*mama*, *nyan*-type names) when it is an established word in that language, not a one-off sound. The `kind` column says which kind each counted word is: *everyday* (the general word), *nursery* (the child's or familiar word beside a general word), or *both*.
- **Tested form:** for each concept, the imitative or nursery candidate the sources name (Globasa's §4.5 forms, the prompt's list, the Wordbank sound), adapted with `tools/names.py`. Where no imitative name exists anywhere in the panel but a wider shape does, the note says so (wolf tests *lobo*; duck, kiss and laugh name the wider non-imitative shapes in their notes).
- **Counts** come from `emit.py` over `panel.tsv`: *sourced* (the verdict), *with memory* (adds memory-only columns), *lenient* (adds the "✗ (✓ lenient)" columns). `emit.py check` confirms every ✓ has the tested form's adapted consonants.

### Two readings of mine, flagged

Pattern 3 compares adapted consonants, so the result depends on how a form goes into `names.py`:

1. **Geminates are written as length** (Hindi *mammī* [məmːiː], Korean *appa* [apːa], Japanese *kakkō* [kakːoː]). That is broad-IPA practice, and `names.py` drops length marks as it drops vowel length; Apupiwe has no long consonants. Written as two letters instead ([məmmiː]), `names.py` makes *manmi*, *apupa*, *kakuko*. **This decides mother:** with length, Hindi *mammī* and Bengali *mammi* adapt to *mami* and count (13); with two letters they don't (11, borderline). It moves no other verdict (Korean and Tamil *appa* would join *papa*, 9; cuckoo, crow, grandfather, burp, sleep and food would lose one column each).
2. **Lenient columns** ("✗ (✓ lenient)") are near shapes that pattern 3 strictly keeps apart: the one-syllable base of a doubled form (Vietnamese *má*, Thai *mɛ̂ɛ*, Vietnamese *ba*), one consonant added or dropped (French *maman*, Persian *māmān*, Turkish *bebek*, Korean *eomma*), and a few words Wiktionary lists that I judge aren't the everyday word (Turkish literary *buse*, Hindi formal *kāk*). They never decide a verdict here; mother passes on either reading.

### Sources (column `src`)

- **Wt**: English Wiktionary translation tables, fetched 2026-10-15 with `tests/lexicon-ladder-01/panel.py` (pages and blocks in `build.py`: mother, father, grandmother, grandfather, baby, cat, dog, cow, sheep, goat, duck, chicken, rooster, bird, cuckoo, crow, owl, frog, bee, wolf, pig, horse, donkey, mouse, kiss, knock, laugh, cry, sneeze, cough, hiccup, burp, vomit, yawn, snore, sleep, food, urinate, pee, poop, explosion; also dad, daddy, grandma, grandpa, granny and the sound pages meow, moo, quack, baa, bow-wow, oink, cock-a-doodle-doo, cluck, tweet, chirp, boom).
- **We**: the Wiktionary entry for the foreign word, from the kaikki.org extracts cached by the coverage run (`~/work/cache/coverage/kaikki-*.jsonl.gz`, fetched 2026-10-13). `scan.py` lists every sense in the panel languages whose gloss starts with a concept's English words, flagged when tagged childish, informal or colloquial, or when the etymology says onomatopoeic.
- **Wb**: Wordbank CDI Words & Sentences forms, the "sounds" category, from the CSVs cached by the coverage run (`~/work/cache/coverage/wordbank/`, 37 lists). `tests/coverage-01/wordbank.tsv` excludes sounds and routines (its header says so; column 3 has one "sounds2" row, *oink*), so I read the CSVs directly. The Japanese list carries nursery words in that category (ネンネ "sleep", マンマ "food", ジージ "grandfather", バーバ "grandmother", チューチュー "mouse", メーメー "goat").
- **M**: from memory. **M\***: Wiktionary lists the word, but my judgment of the everyday word differs.

Web pages were fetched with a generic User-Agent. No other web source was needed: no verdict turns on an unsourced column.

### Forms

The pass's form is the median pronunciation of its cognate forms in broad IPA, adapted with `tools/names.py`, then checked with `check.py` against `data/lexicon.tsv`, `data/grammar.tsv`, `data/numbers.tsv` (same form or same content key, as `names.py` does), the spelling-alphabet words in `docs/language.md` 11.5, and `tools/offensive.py` (`blocked`, `matches`). The same check is given for every tested form.

### Candidates

From the prompt: cat, cow, duck, sheep, goat, dog (check only), bird, frog, bee, owl, cuckoo, rooster/chicken, wolf, baby, mother, father, grandmother, grandfather, kiss, knock, laugh, cry, sneeze, cough, hiccup, burp, vomit, sleep, eat/food, pee, poo, bang/boom.

**Added** (everyday concepts from the same two sources): **pig**, **horse**, **donkey**, **mouse** (Wordbank sounds *oink*, *neigh*, *hee haw*, *squeak*; all four are on the concept list or in the lexicon), **crow**, **yawn**, **snore** (Globasa §4.5 *kraw*, *hwam*, *hor*). **Not added:** car (*vroom*) and train (*choo choo*), whose panel names are not built on the sound outside Japanese nursery speech (ブーブー, ポッポ) and which the lexicon and ladder already route; Globasa's *glu* "drink" and *tutum* "heart" (no panel language's everyday word for either is imitative).

**Where each concept stands now:** in the lexicon: mother **mole**, father **wede**, dog **totu**, bird **lodi**, cow **dunsa**, goat **elen**, chicken **yiban**, horse **anbo**, food **pasu**, eat **nawi**, sleep **wopo**, laugh **bubo**, cry **nowa**, cough **dowin**, sneeze **tinne**, yawn **ganpa**, snore **nenmu**, vomit **gabu**, urinate **tibin**, defecate **desin**. Queued as new roots in `tests/coverage-01/part3/ladder.tsv`: duck, mouse, sheep, frog, baby, cat, bee, pig, wolf, kiss, donkey, owl, knock. Composed: grandmother **mole pi mole** / **mole pi wede**, grandfather likewise (with the flag "children's first word, add back a root if tests lose meaning"). Not on the concept list: cuckoo, crow, rooster, hiccup, burp, bang/boom.

## Results

| Concept | Tested form | Sourced (verdict) | Lenient | Verdict | Adapted form | Collisions (`check.py`) | Deciding columns, sources |
|---|---|---|---|---|---|---|---|
| mother | mama | 13/20, 7 regions | 19, 7 | **pass** | ***mama*** | same content key as **maman** "suck"; not blocked, no offensive match | hi *mammī*, bn *mammi* (We, childish; the geminate reading); tl, ha, yo, id rest on We alone |
| father | papa | 7/20, 4 | 10, 4 | fail | *papa* | spelling-alphabet word for P | split by voicing with *baba* (below) |
| father | baba | 9/20, 4 | 11, 5 | fail | *baba* | clear | |
| grandmother | nana | 4/20, 2 | 7, 5 | fail | *nana* | clear | hi bn: mother's mother only |
| grandfather | dada | 5/20, 3 | 6, 4 | fail | *dada* | offensive match only | hi bn: father's father only |
| baby | bebe | 3/20, 2 | 6, 3 | fail | *bebe* | offensive match only | |
| cat | mau (Globasa *myaw*) | 3/20, 2 | 5, 3 | fail | *mawu* | same content key as **mawun** "flat" | zh vi th only |
| dog (check) | wau (Globasa *bwaw*) | 1/20, 1 | 2, 2 | fail | *wawu* | clear | **totu** stands |
| cow | mumu | 1/20, 1 | 1, 1 | fail | *mumu* | clear | |
| sheep | meme | 0 | 0 | fail | *meme* | clear | |
| goat | meme | 1/20, 1 | 1, 1 | fail | *meme* | clear | |
| duck | kwak | 0 | 1, 1 | fail | *kuwaku* | clear | |
| chicken, rooster | kuku | 2/20, 1 | 4, 3 | fail | *kuku* | offensive match only | |
| bird | piu | 0 | 0 | fail | *piyu* | offensive match only | |
| cuckoo | kuku | 5/20, 4 | 9, 6 | fail | *kuku* | offensive match only | |
| crow | kaka | 2/20, 1 | 5, 3 | fail | *kaka* | offensive match only | |
| owl | huhu | 0 | 0 | fail | *uwu* | clear | |
| frog | kroa | 0 | 0 | fail | *kulowa* | clear | |
| bee | beze | 0 | 0 | fail | *bese* | same form as **bese** "inside"; offensive match | |
| wolf | lobo | 2/20, 2 | 2, 2 | fail | *lobo* | clear | |
| pig | bubu | 2/20, 2 | 3, 2 | fail | *bubu* | same content key as **bubo** "laugh" | |
| horse | dada | 1/20, 1 | 1, 1 | fail | *dada* | offensive match only | |
| donkey | hiha | 0 | 0 | fail | *iya* | clear | |
| mouse | chuchu | 1/20, 1 | 1, 1 | fail | *tutu* | offensive match only | |
| kiss | busu | 5/20, 3 | 7, 4 | fail | *busu* | offensive match only | |
| knock | tok | 1/20, 1 | 3, 3 | fail | *toku* | same content key as **togun** "breathe" | |
| laugh | haha | 0 | 0 | fail | *awu* | clear | |
| cry | wawa | 0 | 0 | fail | *wawa* | clear | |
| sneeze | achoo | 1/20, 1 | 3, 3 | fail | *atu* | clear | |
| cough | kof | 0 | 0 | fail | *kofu* | clear | |
| hiccup | hik | 0 | 2, 2 | fail | *iku* | same content key as **iko** "tell" | |
| burp | gep | 1/20, 1 | 1, 1 | fail | *gepu* | clear | |
| vomit | ûak (th) | 1/20, 1 | 1, 1 | fail | *uwaku* | clear | |
| yawn | hwam | 0 | 0 | fail | *wamu* | clear | |
| snore | hor | 0 | 0 | fail | *olu* | clear | |
| sleep (nursery) | nene | 1/20, 1 | 1, 1 | fail | *nene* | clear | |
| eat, food (nursery) | mama | 3/20, 3 | 4, 3 | fail | *mama* | as mother | |
| pee (nursery) | pipi | 3/20, 1 | 4, 2 | fail | *pipi* | offensive match only | |
| poo (nursery) | kaka | 5/20, 2 | 6, 3 | fail | *kaka* | offensive match only | |
| bang, boom | bum | 0 | 0 | fail | *bumu* | clear | |

No tested form is `blocked`. "Offensive match" means `offensive.matches` is true (the Wiktionary tie-break list, exact or near; e.g. *kaka* matches Telugu and Portuguese words, *pipi* and *bebe* a Gujarati one); it only matters as a tie-breaker.

**Count:** 1 pass (mother), 39 fail. No borderline: no failure passes even on the lenient count (the closest are father *baba*, 11, and cuckoo, 9).

### The pass: mother → *mama*

- **Columns.** Counted (13): zh *māma*, ja *mama*, id *mama*, tl *mama*, hi *mammī*, bn *mammi*, ar *māmā*, ru *mama*, es *mamá*, sw *mama*, ha *mama*, yo *màmá*, qu *mama*. Lenient (6 more): ko *eomma*, vi *má*/*mẹ*, th *mɛ̂ɛ*, ta *ammā*, fa *māmān*, fr *maman*. Only Turkish (*anne*) has nothing like it. All counted columns are sourced (Wt or We); none is memory.
- **What it rests on.** Hindi and Bengali count through their childish, colloquial *mammī*/*mammi* (from English *mummy*), and only under the geminate-as-length reading; without them the count is 11, all 7 regions, and mother is borderline (19 lenient). Tagalog, Hausa, Yoruba and Indonesian rest on the Wiktionary entry alone (Wt lists *nanay*, *uwa*, *ìyá*, *ibu*). Persian lists a childish *mām* (We) that would adapt to *mamu* and count; I left it out because *māmān* is what Persian children say.
- **Form.** All counted forms agree on *mama* except hi bn *mami*; the median is [mama] → **mama**. No tie.
- **Collisions.** `check.py`: **mama** has the same content key as **maman** "suck" (the key ignores a later syllable's final n), so B2 treats them as one word. By the 2026-10-13 rule (loans keep their forms; roots move), **maman** would be re-placed. Not blocked, no offensive match, no clash with grammar words, numbers or the spelling alphabet.
- **Listener-side clashes** (as *hotel* means "restaurant" in hi ta sw, loans.md pattern 7): *mama* is "maternal uncle" in Hindi and Bengali (and *māmī*, which hears like *mami*, is his wife), "baby food" in Turkish, "breast" in Indonesian and Spanish, and "mister" (a man addressed) in Tagalog (from memory). A speaker of those languages hears another word first, though in context a child's *mama* is unmistakable.

**Question for the author (not a decision): is *mama* the word for "mother" or a second word beside *mole*?**

The panel splits about evenly. In 7 languages *mama* is the general word (sw, qu, ru, ha, yo, id, and zh *māma* beside formal *mǔqīn*). In 6 it is the child's or familiar word beside a general one (ja *okāsan*/*mama*, tl *nanay*/*mama*, hi *mā̃*/*mammī*, bn *ma*/*mammi*, ar *umm*/*māmā*, es *madre*/*mamá*), and most lenient columns are the same split (fr *mère*/*maman*, fa *mādar*/*māmān*, ko *eomeoni*/*eomma*). The options as I see them:

- **(a) *mama* replaces *mole*** as the root "mother". One word, as in Swahili or Quechua; **mole**'s form is freed. The composed kin words follow (**mama pi mama** "grandmother", **mama yen wede** "parents"), beside a father still on the root **wede**, since father fails.
- **(b) *mama* is a second word beside *mole***: "mum, mommy", the familiar word and the term of address, as in Japanese, Spanish or Arabic; **mole** stays the general and formal word. That would be a register pair, which the lexicon doesn't otherwise have, and the cost is a synonym to learn.
- **(c) No loan**: **mole** stays, and *mama* lives only as a child's sound outside the sound system (2.10), as any baby babble does.

What the repo already says: the seed left baby words out (`docs/vocabulary-method.md` §1.4, add-back trigger "tests lose points to missing interjections"); `tests/lexicon-ladder-01/loans.md` raised *mama*/*papa* as "a question for the author, not a finding"; the design log of 2026-10-15 decided to test them. I found nothing recorded on register pairs.

### Near misses and what they show

- **Father splits by voicing.** *papa* (ja id tl hi ru es fr: 7, 4 regions) and *baba* (zh hi bn fa ar tr sw ha yo: 9, 4 regions) are, to the panel, the same nursery word, but Apupiwe distinguishes p and b, so pattern 3 keeps them apart and neither reaches 12. Counted as one form they would pass (15 sourced, 6 regions, all but AM), and the median consonant would be b (*baba*: 9 against 7, Hindi in both). *papa* is also the spelling-alphabet word for P (11.5); *baba* is clear. Only a change to pattern 3 for this pair would flip it, so I list it as a question, not a recommendation.
- **Grandparents split by sense.** *nana*/*nani* is "grandmother" in Persian and Turkish but "mother's mother" (*nānī*) and "mother's father" (*nānā*) in Hindi and Bengali; *dada* is "father's father" in Hindi and Bengali, "elder brother" in Bengali, "father" in Tajik. A shared shape with different referents isn't a shared word. The composed **mole pi mole** stands.
- **Cuckoo** (5 sourced, 9 lenient) and **kiss** (*busu*: fa ar es fr sw, 5) are the widest after the kin words; neither is close. *busu* isn't imitative: it's the Persian–Arabic *bus* spread with Spanish *beso* and French *bisou*.
- **Poo and pee**: *kaka* (ar tr ru es fr) and *pipi* (ru es fr) are the European and Middle Eastern nursery words; Asia uses others (*unchi*, *bianbian*, *shīshī*, *chìi*, *susū*).

### Findings along the way

1. **The world shares the sounds, not the names.** Wordbank's sound items are near-universal (*woof* on 31 of 37 lists, *meow*, *baa*, *quack* 29, *moo* 23, *yum yum* 22), but a name built on the sound is rare: only Mandarin, Vietnamese and Thai call the cat by its *miau* in everyday speech (Indonesian *meong* and Persian *miyaw* in child speech, which adapt to other consonants). Naming animals by their sounds is mostly nursery speech (Japanese *wanwan*, *nyannyan*, *mōmō*, *būbū*, *chūchū*, *mēmē*; Korean *meongmeongi*, *yaongi*, *kkulkkuri*; Tagalog *aw-aw*; French *dada*), and each language hears the animal differently enough that the names don't match. The sounds are already usable: reference 2.10 puts interjections outside the sound system, so a child's *miau* or *haha* needs no word.
2. **Imitative forms don't survive adaptation well.** `names.py` drops h, so *haha* → *awu*, *huhu* → *uwu*, *hik* → *iku*, *hwam* → *wamu*. Even a world-shared laugh word would not be recognisable after the sound system had it.
3. **Nursery kin words are shared shapes with different meanings.** *mama* (mother, maternal uncle, baby food, breast), *nana* (grandmother, maternal grandparent), *dada* (grandfather, elder brother, father), *kaka* (poo, paternal uncle in Bengali), *papa* (father; potato in Quechua and shark in Swahili, from memory). Babies' first syllables (ma, pa, ba, na, da, ka) get attached to whatever is nearest in each culture, so the shapes converge and the meanings don't.
4. **One reading decides the one pass.** How geminates enter `names.py` (length or two letters) moves mother between 13 and 11. Neither the method nor `names.py` says; the author may want to settle it for all loans.
5. **Deciding columns are again Hausa, Yoruba, Tagalog and Indonesian**, as in the coverage run, but here Wiktionary entries cover them; no column was memory-only where it mattered.
6. **To track in `docs/roadmap.md`** (not edited; this test changes nothing outside its folder): the author's decision on *mama* (pass) and the separate-concept question; **maman** "suck" re-placed if *mama* is adopted; whether pattern 3 should treat *papa*/*baba* as one form; the geminate reading in `names.py` input; 2.10 already covers the shared sounds, so nothing else is queued from this test.

## Files

- `panel.tsv`: one row per concept, tested form and language (concept, adapted form, its IPA, language, word, kind, the word's IPA, its adapted form, shared y/n/l, source, note). Written by `build.py`.
- `build.py`: the judgments (one block per concept) plus the Wiktionary tables, written to `panel.tsv`; rows not listed take their word from the table. Edit a judgment there and re-run.
- `emit.py`: counts, the tables below and a pattern-3 consistency check (`counts`, `tables`, `check`).
- `scan.py`: lists kaikki Wiktionary senses in the panel languages that name a tested concept, with childish/onomatopoeic flags.
- `check.py`: checks adapted forms against the language's words, the spelling alphabet and `offensive.py`.

Re-run inside the dev shell: `direnv exec <repo> python3 tests/imitative-01/build.py`, then `... emit.py counts`.

## Per-concept evidence

Legend: ✓ the same form as the tested one (same adapted consonants), ✗ not; "✗ (✓ lenient)" a near shape or a listed word I judge isn't the everyday one (see "Two readings"). The kind in brackets is the counted word's: everyday, nursery, or both. Rows with no note take the first words of the Wiktionary table. Romanisation is mine where the source gives none.

#### mother: *mama* [mama]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 媽媽 māma; 母親 mǔqīn (formal) (both) | mama | ✓ | Wt, We | We: informal 'mum, mama' |
| Japanese | お母さん okāsan; ママ mama (nursery) | mama | ✓ | Wt, We | We: childish 'mama' |
| Korean | 엄마 eomma (what children say); 어머니 eomeoni (nursery) | ama | ✗ (✓ lenient) | Wt, We | adapted ama: one m |
| Vietnamese | mẹ; má (Southern) (everyday) | meyu | ✗ (✓ lenient) | Wt, We | one syllable, the base of mama |
| Thai | แม่ mɛ̂ɛ (everyday) | meyu | ✗ (✓ lenient) | Wt | one syllable |
| Indonesian | ibu; mama (everyday) | mama | ✓ | Wt, We | We: mama 'mother (female parent)', no register label; ibu is the standard word |
| Tagalog | nanay; mama (nursery) | mama | ✓ | We | We: childish, familiar 'mum, mom'; Tagalog mama is also 'mister' (M) |
| Hindi | माँ mā̃; मम्मी mammī (nursery) | mami | ✓ | We | We: mammī childish, colloquial 'mom, mommy' (from English mummy); māmā = maternal uncle (We) |
| Bengali | মা ma; মাম্মি mammi (nursery) | mami | ✓ | We | We: mammi childish, colloquial 'mother'; mama = maternal uncle (We) |
| Tamil | அம்மா ammā (everyday) | ama | ✗ (✓ lenient) | Wt, We | adapted ama: one m |
| Persian | مادر mādar; مامان māmān (spoken) (nursery) | momon | ✗ (✓ lenient) | Wt, We | adapted momon: extra n; We also lists مام mām 'childish' (would be mamu), not counted |
| Arabic | أمّ umm; ماما māmā (nursery) | mama | ✓ | Wt, We | We: childish, familiar 'mum, mummy, mama' |
| Turkish | anne (everyday) |  | ✗ | Wt | Turkish mama = baby food (We) |
| Russian | мама mama; мать mat' (everyday) | mama | ✓ | Wt, We |  |
| Spanish | madre; mamá (nursery) | mama | ✓ | Wt, We | We: mamá familiar 'mum, mom' |
| French | mère; maman (nursery) | maman | ✗ (✓ lenient) | Wt, We | adapted maman: extra n |
| Swahili | mama (everyday) | mama | ✓ | Wt, We |  |
| Hausa | uwa, inna; mama (everyday) | mama | ✓ | We | We: mama 'mother'; Wt lists uwa, inna |
| Yoruba | ìyá; màmá (everyday) | mama | ✓ | We | We: mama 'mother'; Wt grandmother table has màmá màmá |
| Quechua | mama (everyday) | mama | ✓ | Wt, We | native word |

Sourced 13/20 in 7 regions; with memory 13/7; lenient 19/7. **pass.**

#### father: *papa* [papa]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 父親 (fùqīn), 父 (fù), 爸爸 (bàba) (everyday) |  | ✗ | Wt |  |
| Japanese | お父さん otōsan; パパ papa (nursery) | papa | ✓ | Wt, We | We: childish |
| Korean | 아빠 appa (what children say); 아버지 (nursery) | apa | ✗ (✓ lenient) | Wt, We | adapted apa: one p |
| Vietnamese | cha, ba, bố (everyday) |  | ✗ | Wt |  |
| Thai | พ่อ phɔ̂ɔ; ป๊า páa (nursery) | pawu | ✗ (✓ lenient) | Wt, We | We: colloquial; one syllable |
| Indonesian | ayah, bapak; papa (nursery) | papa | ✓ | We | We: colloquial 'father' |
| Tagalog | tatay; papa (nursery) | papa | ✓ | Wt, We | We: childish, familiar |
| Hindi | पिता pitā; पापा pāpā (nursery) | papa | ✓ | Wt, We | We: 'dad, daddy'; Hindi also bābā |
| Bengali | আব্বা, পিতা, বাবা (everyday) |  | ✗ | Wt |  |
| Tamil | அப்பா appā (everyday) | apa | ✗ (✓ lenient) | Wt, We | adapted apa: one p |
| Persian | پَدَر, پِدَر, وَالِد (everyday) |  | ✗ | Wt |  |
| Arabic | أَب, وَالِد, بَابَا (everyday) |  | ✗ | Wt |  |
| Turkish | baba, ata (everyday) |  | ✗ | Wt |  |
| Russian | папа papa; отец otec (everyday) | papa | ✓ | Wt, We |  |
| Spanish | padre; papá (nursery) | papa | ✓ | Wt, We | We: familiar |
| French | père; papa (nursery) | papa | ✓ | Wt, We | We: childish |
| Swahili | baba (everyday) |  | ✗ | Wt, We | the baba form; Swahili papa = shark (M) |
| Hausa | ùbā, bā̀ba (everyday) |  | ✗ | Wt |  |
| Yoruba | bàbá, baba (everyday) |  | ✗ | Wt |  |
| Quechua | tayta, tata (everyday) |  | ✗ | Wt, We | Quechua papa = potato (M) |

Sourced 7/20 in 4 regions; with memory 7/4; lenient 10/4. **fail.**

#### father: *baba* [baba]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 爸爸 bàba; 父親 fùqīn (both) | baba | ✓ | Wt, We |  |
| Japanese | パパ papa (nursery) |  | ✗ | Wt, We | the papa form |
| Korean | 아빠 appa (nursery) |  | ✗ | Wt, We | the papa form (one p) |
| Vietnamese | bố; ba (Southern) (everyday) | bawu | ✗ (✓ lenient) | Wt, We | one syllable |
| Thai | พ่อ phɔ̂ɔ; ป๊า páa (nursery) |  | ✗ | Wt, We | p |
| Indonesian | ayah, bapak; baba (everyday) | baba | ✗ (✓ lenient) | Wt, We | We lists baba 'father' (no label); used in Arab- and Chinese-descent families (M); bapak has b-p-k |
| Tagalog | tatay; papa (nursery) |  | ✗ | Wt, We | the papa form |
| Hindi | पिता pitā; बाबा bābā (everyday) | baba | ✓ | Wt, We | We: 'dad, papa'; also 'paternal grandfather', 'a male elder' |
| Bengali | বাবা baba (everyday) | baba | ✓ | Wt, We |  |
| Tamil | அப்பா appā (everyday) |  | ✗ | Wt, We | the papa form (one p) |
| Persian | پدر pedar; بابا bābā (everyday) | baba | ✓ | Wt, We | We: colloquial |
| Arabic | أب ab; بابا bābā (nursery) | baba | ✓ | Wt, We | We: childish |
| Turkish | baba (everyday) | baba | ✓ | Wt, We |  |
| Russian | папа papa; батя bátja (everyday) |  | ✗ | Wt, We | the papa form |
| Spanish | papá (nursery) |  | ✗ | Wt, We | the papa form |
| French | papa (nursery) |  | ✗ | Wt, We | the papa form |
| Swahili | baba (everyday) | baba | ✓ | Wt, We |  |
| Hausa | ùbā; bā̀ba (everyday) | baba | ✓ | Wt, We |  |
| Yoruba | bàbá (everyday) | baba | ✓ | Wt, We |  |
| Quechua | tayta, tata (everyday) |  | ✗ | Wt, We |  |

Sourced 9/20 in 4 regions; with memory 9/4; lenient 11/5. **fail.**

#### grandmother: *nana* [nana]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 奶奶 nǎinai (everyday) | nayinayi | ✗ (✓ lenient) | Wt | adapted nayinayi |
| Japanese | お婆ちゃん obāchan; バーバ bāba (nursery) (nursery) |  | ✗ | Wt, Wb | Wordbank JA sounds item バーバ |
| Korean | 할머니, 외할머니 (everyday) |  | ✗ | Wt |  |
| Vietnamese | bà, bà ngoại, bà nội (everyday) |  | ✗ | Wt |  |
| Thai | ย่า, ยาย (everyday) |  | ✗ | Wt |  |
| Indonesian | nenek (everyday) | neneku | ✗ (✓ lenient) | Wt | adapted neneku: extra k |
| Tagalog | lola, impo, lelang (everyday) |  | ✗ | Wt |  |
| Hindi | नानी nānī (mother's mother); दादी dādī (father's mother) (everyday) | nani | ✓ | Wt, We | nānā = maternal grandfather |
| Bengali | নানী nani (mother's mother); দাদি dadi (everyday) | nani | ✓ | Wt, We | nana = maternal grandfather (We) |
| Tamil | பாட்டி, ஆயாள், மூதாய் (everyday) |  | ✗ | Wt |  |
| Persian | مادربزرگ mādarbozorg; ننه nane (everyday) | nane | ✓ | Wt | nane is also 'mother' in speech (M) |
| Arabic | جدّة jadda; تيتة tēta (everyday) |  | ✗ | Wt |  |
| Turkish | nine, babaanne/anneanne (everyday) | nine | ✓ | Wt |  |
| Russian | бабушка babushka, баба (everyday) |  | ✗ | Wt | the baba shape (ru, ja bāba, sw bibi) |
| Spanish | abuela (everyday) |  | ✗ | Wt |  |
| French | grand-mère; mamie, mémé (nursery) |  | ✗ | Wt |  |
| Swahili | bibi; nyanya (Kenya) (everyday) | nana | ✗ (✓ lenient) | Wt, We | nyanya adapts to nana; regional, second word |
| Hausa | kaka (everyday) |  | ✗ | Wt |  |
| Yoruba | ìyá ìyá, màmá màmá, ìyá bàbá (everyday) |  | ✗ | Wt |  |
| Quechua | jatun mama (everyday) |  | ✗ | Wt |  |

Sourced 4/20 in 2 regions; with memory 4/2; lenient 7/5. **fail.**

#### grandfather: *dada* [dada]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 爺爺 (yéye), 祖父 (zǔfù), 外祖父 (wàizǔfù) (everyday) |  | ✗ | Wt |  |
| Japanese | お爺ちゃん ojiichan; ジージ jīji (nursery) (nursery) | didi | ✓ | Wb, We | Wordbank JA sounds item ジージ・ジジ（祖父）; We 爺 jī 'grandfather' |
| Korean | 할아버지, 친할아버지, 외할아버지 (everyday) |  | ✗ | Wt |  |
| Vietnamese | ông, ôông (everyday) |  | ✗ | Wt |  |
| Thai | ปู่, ตา, ก๋ง (everyday) |  | ✗ | Wt |  |
| Indonesian | kakek, engkong (everyday) |  | ✗ | Wt |  |
| Tagalog | lolo, ingkong, lelong (everyday) |  | ✗ | Wt |  |
| Hindi | दादा dādā (father's father); नाना nānā (everyday) | dada | ✓ | Wt, We |  |
| Bengali | দাদা dada, দাদু dadu; নানা nana (everyday) | dadu | ✓ | Wt, We | dada also 'elder brother' |
| Tamil | தாத்தா tāttā (everyday) |  | ✗ | Wt | t-t |
| Persian | پدربزرگ pedarbozorg (everyday) |  | ✗ | Wt | dādā is Tajik 'father' (We) |
| Arabic | جدّ jadd; جدّو jiddo, سيدو sido (Levantine) (everyday) | dadu | ✓ | Wt | adapted dadu |
| Turkish | dede, büyükbaba (everyday) | dede | ✓ | Wt |  |
| Russian | дедушка dedushka, дед ded (everyday) | detu | ✗ (✓ lenient) | Wt | ded adapts to detu (final devoicing); dedushka to dedusuka |
| Spanish | abuelo (everyday) |  | ✗ | Wt |  |
| French | grand-père, aïeul (everyday) |  | ✗ | Wt |  |
| Swahili | babu (everyday) |  | ✗ | Wt |  |
| Hausa | kaka (everyday) |  | ✗ | Wt |  |
| Yoruba | bàbá bàbá, bàbá ìyá, bàbá màmá (everyday) |  | ✗ | Wt |  |
| Quechua | awki, jatun tata (everyday) |  | ✗ | Wt |  |

Sourced 5/20 in 3 regions; with memory 5/3; lenient 6/4. **fail.**

#### baby: *bebe* [bebe]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 嬰兒, 娃娃, 小娃娃 (everyday) |  | ✗ | Wt |  |
| Japanese | 赤ちゃん (あかちゃん, akachan), 赤ん坊 (あかんぼう, akanbō), 嬰児 (えいじ, eiji) (everyday) |  | ✗ | Wt |  |
| Korean | 아기, 유아(乳兒), 젖먹이 (everyday) |  | ✗ | Wt |  |
| Vietnamese | em bé, bé (everyday) | beyu | ✗ (✓ lenient) | Wt | one syllable |
| Thai | เด็กอ่อน, เด็กน้อย, ทารก (everyday) |  | ✗ | Wt |  |
| Indonesian | bayi (everyday) |  | ✗ | Wt |  |
| Tagalog | sanggol; bebe, beybi (colloquial) (everyday) | bebe | ✓ | Wt, We | We: bebe colloquial, alternative form of beybi |
| Hindi | शिशु, बच्चा (everyday) |  | ✗ | Wt |  |
| Bengali | শিশু, বাচ্চা (everyday) |  | ✗ | Wt |  |
| Tamil | குழந்தை kuḻantai; பாப்பா pāppā (everyday) |  | ✗ | Wt, M |  |
| Persian | اُشْتُک (uštuk), اُشْتُکَک (uštukak), بچه (bačča) (everyday) |  | ✗ | Wt |  |
| Arabic | رضيع raḍīʿ; بيبي bēbī (spoken) (everyday) | bebi | ✓ | M | spoken Levantine and Egyptian, from memory |
| Turkish | bebek (everyday) | bebeku | ✗ (✓ lenient) | Wt | adapted bebeku: extra k |
| Russian | младе́нец, малы́ш, малы́шка (everyday) |  | ✗ | Wt |  |
| Spanish | bebé (everyday) | bebe | ✓ | Wt |  |
| French | bébé (everyday) | bebe | ✓ | Wt |  |
| Swahili | mtoto mchanga (everyday) |  | ✗ | Wt |  |
| Hausa | jariri (everyday) |  | ✗ | Wt |  |
| Yoruba | ọmọ ọwọ (everyday) |  | ✗ | M |  |
| Quechua | wawa (everyday) |  | ✗ | We | the wawa shape: qu wawa, zh 娃娃 wáwa (Wt), es guagua (Wt, Andean) |

Sourced 3/20 in 2 regions; with memory 4/3; lenient 6/3. **fail.**

#### cat: *mawu* [mau]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 貓 māo (everyday) | mawu | ✓ | Wt, We |  |
| Japanese | 猫 neko; ニャンニャン nyannyan (nursery) (nursery) |  | ✗ | Wt, Wb |  |
| Korean | 고양이 goyangi; 야옹이 yaongi (childish) (nursery) |  | ✗ | Wt, We |  |
| Vietnamese | mèo (everyday) | mewu | ✓ | Wt, We | adapted mewu (m-w) |
| Thai | แมว mɛɛw (everyday) | mewu | ✓ | Wt, We |  |
| Indonesian | kucing; meong (informal) (nursery) | meyon | ✗ (✓ lenient) | Wt, We | adapted meyon |
| Tagalog | pusa (everyday) |  | ✗ | Wt | the pus shape: tl pusa, tr pisi (childish), fa piši |
| Hindi | बिल्ली, बिल्ला (everyday) |  | ✗ | Wt |  |
| Bengali | বিড়াল, বেড়াল, বিলাই (everyday) |  | ✗ | Wt |  |
| Tamil | பூனை, பூசை, பில்லி (everyday) |  | ✗ | Wt |  |
| Persian | گربه gorbe; پیشی piši, میو miyaw (childish) (nursery) | miyawu | ✗ (✓ lenient) | Wt, We | adapted miyawu (m-y-w) |
| Arabic | قِطّ, قِطَّة, هِرّ (everyday) |  | ✗ | Wt |  |
| Turkish | kedi, pisi[[pisi]], enik (everyday) |  | ✗ | Wt |  |
| Russian | ко́шка, кот (everyday) |  | ✗ | Wt |  |
| Spanish | gato, gata, mish (everyday) |  | ✗ | Wt |  |
| French | chat, chatte (everyday) |  | ✗ | Wt |  |
| Swahili | paka; nyau (everyday) |  | ✗ | Wt, We | nyau adapts to nawu |
| Hausa | kyânwā (everyday) |  | ✗ | Wt |  |
| Yoruba | ológìnní, ológbò (everyday) |  | ✗ | Wt |  |
| Quechua | misi (everyday) |  | ✗ | Wt, We | the mis shape: qu misi, yo músù (We), ha mussa (We) |

Sourced 3/20 in 2 regions; with memory 3/2; lenient 5/3. **fail.**

#### dog: *wawu* [wau]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 狗, 犬 (everyday) |  | ✗ | Wt |  |
| Japanese | 犬 inu; ワンワン wanwan (childish) (nursery) | wanwan | ✗ (✓ lenient) | Wt, We | adapted wanwan (w-n-w-n) |
| Korean | 개 gae; 멍멍이 meongmeongi (childish) (nursery) |  | ✗ | Wt, We |  |
| Vietnamese | chó, cẩu, khuyển (everyday) |  | ✗ | Wt |  |
| Thai | หมา, สุนัข (everyday) |  | ✗ | Wt |  |
| Indonesian | anjing, asu (everyday) |  | ✗ | Wt |  |
| Tagalog | aso; aw-aw (childish) (nursery) | awawu | ✓ | Wt, We | adapted awawu |
| Hindi | कुत्ता, कुत्ती, श्वान (everyday) |  | ✗ | Wt |  |
| Bengali | কুকুর, কুত্তা (everyday) |  | ✗ | Wt |  |
| Tamil | நாய், ஞமலி, ஞாளி (everyday) |  | ✗ | Wt |  |
| Persian | سگ sag; هاپو hāpu (childish) (nursery) |  | ✗ | Wt, We |  |
| Arabic | كَلْب (everyday) |  | ✗ | Wt |  |
| Turkish | köpek, it (everyday) |  | ✗ | Wt |  |
| Russian | соба́ка, пёс, пси́на (everyday) |  | ✗ | Wt |  |
| Spanish | perro, can, tuso (everyday) |  | ✗ | Wt |  |
| French | chien; toutou (childish) (nursery) |  | ✗ | Wt, We | toutou is close to totu, by chance |
| Swahili | mbwa (everyday) |  | ✗ | M | missing from Wt |
| Hausa | kàrē (everyday) |  | ✗ | Wt |  |
| Yoruba | ajá (everyday) |  | ✗ | Wt |  |
| Quechua | alkho, allqu, allgo (everyday) |  | ✗ | Wt |  |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 2/2. **fail.**

#### cow: *mumu* [muːmuː]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 母牛 mǔniú; 牛牛 niúniu (childish) (nursery) |  | ✗ | Wt, We |  |
| Japanese | 牛 ushi; もうもう mōmō (childish) (nursery) | momo | ✓ | Wt, We | adapted momo |
| Korean | 암소 (everyday) |  | ✗ | Wt |  |
| Vietnamese | bò cái (everyday) |  | ✗ | Wt |  |
| Thai | วัว, โค (everyday) |  | ✗ | Wt |  |
| Indonesian | sapi (everyday) |  | ✗ | Wt |  |
| Tagalog | baka (everyday) |  | ✗ | Wt |  |
| Hindi | गाय, गो, गऊ (everyday) |  | ✗ | Wt |  |
| Bengali | গাই, গরু (everyday) |  | ✗ | Wt |  |
| Tamil | பசு (everyday) |  | ✗ | Wt |  |
| Persian | مادِه‌گاو, گاو, گُو (everyday) |  | ✗ | Wt |  |
| Arabic | بَقَرَة (everyday) |  | ✗ | Wt |  |
| Turkish | inek, sığır (everyday) |  | ✗ | Wt |  |
| Russian | коро́ва (everyday) |  | ✗ | Wt |  |
| Spanish | vaca (everyday) |  | ✗ | Wt | the vaca shape: es vaca, tl baka, qu waka (not imitative) |
| French | vache (everyday) |  | ✗ | Wt |  |
| Swahili | ng'ombe (everyday) |  | ✗ | Wt |  |
| Hausa | saniya (everyday) |  | ✗ | Wt |  |
| Yoruba | abo màluu (everyday) |  | ✗ | Wt |  |
| Quechua | waka (everyday) |  | ✗ | Wt |  |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 1/1. **fail.**

#### sheep: *meme* [meme]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 綿羊 (miányáng), 羊 (yáng) (everyday) |  | ✗ | Wt |  |
| Japanese | 羊 (ひつじ, hitsují), ヒツジ (hitsuji), 綿羊 (めんよう, men'yō) (everyday) |  | ✗ | Wt |  |
| Korean | 양, 면양 (everyday) |  | ✗ | Wt |  |
| Vietnamese | cừu (everyday) |  | ✗ | Wt |  |
| Thai | แกะ (everyday) |  | ✗ | Wt |  |
| Indonesian | domba, biri-biri (everyday) |  | ✗ | Wt |  |
| Tagalog | tupa, obeha (everyday) |  | ✗ | Wt |  |
| Hindi | भेड़ bheṛ; मेमना memnā 'lamb' (everyday) |  | ✗ | Wt, We |  |
| Bengali | ভেড়া, মেষ (everyday) |  | ✗ | Wt |  |
| Tamil | செம்மறியாடு (everyday) |  | ✗ | Wt |  |
| Persian | گوسْفَنْد, میش, قُوچ (everyday) |  | ✗ | Wt |  |
| Arabic | خَرُوف, شاء, حَمَل (everyday) |  | ✗ | Wt |  |
| Turkish | koyun (everyday) |  | ✗ | Wt |  |
| Russian | овца́, ове́чка (everyday) |  | ✗ | Wt |  |
| Spanish | carnero, oveja (everyday) |  | ✗ | Wt |  |
| French | mouton (everyday) |  | ✗ | Wt |  |
| Swahili | kondoo (everyday) |  | ✗ | Wt |  |
| Hausa | tunkìyā (everyday) |  | ✗ | Wt |  |
| Yoruba | àgùtàn (everyday) |  | ✗ | Wt |  |
| Quechua | uwija (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### goat: *meme* [meme]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 山羊 shānyáng; 羊咩咩 (childish, southern dialects) (everyday) |  | ✗ | Wt, We | not Mandarin |
| Japanese | ヤギ yagi; メーメー mēmē (nursery) (nursery) | meme | ✓ | Wt, Wb | Wordbank JA sounds item メーメー (ヤギ) |
| Korean | 염소, 산양(山羊) (everyday) |  | ✗ | Wt |  |
| Vietnamese | dê, con dê (everyday) |  | ✗ | Wt |  |
| Thai | แพะ (everyday) |  | ✗ | Wt |  |
| Indonesian | kambing (everyday) |  | ✗ | Wt |  |
| Tagalog | kambing (everyday) |  | ✗ | Wt |  |
| Hindi | बकरी, बकरा (everyday) |  | ✗ | Wt |  |
| Bengali | ছাগল, বকরা (everyday) |  | ✗ | Wt |  |
| Tamil | வெள்ளாடு, ஆடு (everyday) |  | ✗ | Wt |  |
| Persian | بُز, بُز (everyday) |  | ✗ | Wt |  |
| Arabic | مَاعِز, عَنْزَة (everyday) |  | ✗ | Wt |  |
| Turkish | keçi (everyday) |  | ✗ | Wt |  |
| Russian | коза́, козёл (everyday) |  | ✗ | Wt |  |
| Spanish | cabra, chivo (everyday) |  | ✗ | Wt |  |
| French | chèvre, bouc, bique (everyday) |  | ✗ | Wt |  |
| Swahili | mbuzi (everyday) |  | ✗ | Wt |  |
| Hausa | bunsuru (everyday) |  | ✗ | Wt |  |
| Yoruba | ewúrẹ́ (everyday) |  | ✗ | Wt |  |
| Quechua | kawra (everyday) |  | ✗ | Wt |  |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 1/1. **fail.**

#### duck: *kuwaku* [kwak]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 鴨 (yā), 鴨子 (yāzi) (everyday) |  | ✗ | Wt |  |
| Japanese | 鴨 (kamo), カモ (kamo), 家鴨 (ahiru) (everyday) |  | ✗ | Wt |  |
| Korean | 오리 (everyday) |  | ✗ | Wt |  |
| Vietnamese | ([[con]]) [[vịt]], vịt (everyday) |  | ✗ | Wt |  |
| Thai | เป็ด (everyday) |  | ✗ | Wt |  |
| Indonesian | bebek (everyday) |  | ✗ | Wt |  |
| Tagalog | itik, bibi, pato (everyday) |  | ✗ | Wt |  |
| Hindi | बतख़, बत्तख, बतख (everyday) |  | ✗ | Wt |  |
| Bengali | পাতিহাঁস, হাঁস (everyday) |  | ✗ | Wt |  |
| Tamil | வாத்து (everyday) |  | ✗ | Wt |  |
| Persian | مرغابی (murġābī), اردک (ordak), مرغابی (morġâbi) (everyday) |  | ✗ | Wt |  |
| Arabic | بطّة baṭṭa (everyday) |  | ✗ | Wt | not imitative; the bata/pato wanderwort (ar sw bata, es tl pato, vi vịt, th pèt, ta vāttu, hi batakh) splits into several adapted shapes, none above 3 |
| Turkish | ördek (everyday) |  | ✗ | Wt |  |
| Russian | у́тка, се́лезень, ка́чка (everyday) |  | ✗ | Wt |  |
| Spanish | pato, ánade, corco (everyday) |  | ✗ | Wt |  |
| French | canard (everyday) |  | ✗ | Wt |  |
| Swahili | bata (everyday) |  | ✗ | Wt |  |
| Hausa | agwagwa (everyday) | aguwaguwa | ✗ (✓ lenient) | Wt | imitative; adapted aguwaguwa (g-w-g-w) |
| Yoruba | pẹ́pẹ́yẹ (everyday) |  | ✗ | Wt |  |
| Quechua | wacwa (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 1/1. **fail.**

#### chicken: *kuku* [kuku]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 雞//鷄//鸡 (jī) (everyday) |  | ✗ | Wt |  |
| Japanese | 鶏 niwatori; コケコッコー kokekokkō (childish) (nursery) | kokekoko | ✗ (✓ lenient) | Wt, We | adapted kokekoko |
| Korean | 닭 (everyday) |  | ✗ | Wt |  |
| Vietnamese | gà (everyday) |  | ✗ | Wt |  |
| Thai | ไก่ (everyday) |  | ✗ | Wt |  |
| Indonesian | ayam, manuk (everyday) |  | ✗ | Wt |  |
| Tagalog | manok (everyday) |  | ✗ | Wt |  |
| Hindi | मुर्ग़ा murġā; कुक्कुट kukkuṭ (formal) (everyday) |  | ✗ | Wt |  |
| Bengali | মুরগি murgi; কুঁকড়া kũkṛā (everyday) | kukula | ✗ (✓ lenient) | Wt, We | adapted kukula |
| Tamil | கோழி (everyday) |  | ✗ | Wt |  |
| Persian | مرغ خانگی (morġ-e xânegi), ماک (mâk), مرغ (morġ) (everyday) |  | ✗ | Wt |  |
| Arabic | دَجَاجَة (everyday) |  | ✗ | Wt |  |
| Turkish | tavuk (everyday) |  | ✗ | Wt |  |
| Russian | цыплёнок, ку́рица, пету́х (everyday) |  | ✗ | Wt |  |
| Spanish | pollo (everyday) |  | ✗ | Wt |  |
| French | poulet (everyday) |  | ✗ | Wt |  |
| Swahili | kuku (everyday) | kuku | ✓ | Wt, We |  |
| Hausa | kaza (everyday) |  | ✗ | Wt |  |
| Yoruba | adìẹ; àkùkọ 'rooster' (everyday) | akuko | ✓ | Wt | counted for rooster (Wt rooster table) |
| Quechua | wallpa (everyday) |  | ✗ | Wt |  |

Sourced 2/20 in 1 regions; with memory 2/1; lenient 4/3. **fail.**

#### bird: *piyu* [piu]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 鳥 (niǎo), 雀 (què) (everyday) |  | ✗ | Wt |  |
| Japanese | 鳥 (とり, tori), 鳥類 (ちょうるい, chōrui) (everyday) |  | ✗ | Wt |  |
| Korean | 새, 조류(鳥類) (everyday) |  | ✗ | Wt |  |
| Vietnamese | chim (everyday) |  | ✗ | Wt |  |
| Thai | นก, ปักษา (everyday) |  | ✗ | Wt |  |
| Indonesian | burung (everyday) |  | ✗ | Wt |  |
| Tagalog | ibon (everyday) |  | ✗ | Wt |  |
| Hindi | चिड़िया, पंछी, पक्षी (everyday) |  | ✗ | Wt |  |
| Bengali | পাখী, পাখি (everyday) |  | ✗ | Wt |  |
| Tamil | பறவை (everyday) |  | ✗ | Wt |  |
| Persian | پَرِنْدَه, مُرْغ, پَرَنْدِه (everyday) |  | ✗ | Wt |  |
| Arabic | طَائِر, عُصْفُور (everyday) |  | ✗ | Wt |  |
| Turkish | kuş (everyday) |  | ✗ | Wt |  |
| Russian | пти́ца, пта́шка, пта́х (everyday) |  | ✗ | Wt |  |
| Spanish | pájaro, ave (everyday) |  | ✗ | Wt |  |
| French | oiseau, oiselle, oiselet (everyday) |  | ✗ | Wt |  |
| Swahili | ndege (everyday) |  | ✗ | Wt |  |
| Hausa | tsuntsu (everyday) |  | ✗ | Wt |  |
| Yoruba | ẹyẹ (everyday) |  | ✗ | Wt |  |
| Quechua | pisqu, pisgo (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### cuckoo: *kuku* [kuku]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 杜鵑 dùjuān, 布穀鳥 bùgǔniǎo (everyday) |  | ✗ | Wt |  |
| Japanese | 郭公 kakkō (everyday) | kako | ✓ | Wt | adapted kako |
| Korean | 뻐꾸기, 두견새 (everyday) |  | ✗ | Wt |  |
| Vietnamese | chim cu, cu cu (everyday) | kuku | ✓ | Wt |  |
| Thai | นกกาเหว่า nók-kaa-wàao (koel) (everyday) |  | ✗ | M | missing from Wt |
| Indonesian | burung kangkok, tekukur (M) (everyday) |  | ✗ | M | missing from Wt |
| Tagalog | kakok (everyday) | kakoku | ✗ (✓ lenient) | Wt | adapted kakoku |
| Hindi | कोयल koyal (everyday) |  | ✗ | Wt | the koel |
| Bengali | কোকিল kokil (everyday) | kokilu | ✗ (✓ lenient) | We | adapted kokilu |
| Tamil | குயில் kuyil (everyday) |  | ✗ | Wt |  |
| Persian | کوکو kuku (everyday) | kuku | ✓ | Wt |  |
| Arabic | وقواق waqwāq (everyday) |  | ✗ | Wt |  |
| Turkish | guguk (everyday) |  | ✗ | Wt | g, not k |
| Russian | кукушка kukushka (everyday) | kukusuka | ✗ (✓ lenient) | Wt, We | adapted kukusuka |
| Spanish | cuco, cuclillo (everyday) | kuko | ✓ | Wt, We |  |
| French | coucou (everyday) | kuku | ✓ | Wt, We |  |
| Swahili | kekeo (everyday) | kekeyo | ✗ (✓ lenient) | Wt | adapted kekeyo |
| Hausa | (no entry) (everyday) |  | ✗ | M | missing from Wt and We; not looked up further |
| Yoruba | (no entry) (everyday) |  | ✗ | M | missing from Wt and We; not looked up further |
| Quechua | (no entry) (everyday) |  | ✗ | M | missing from Wt and We; not looked up further |

Sourced 5/20 in 4 regions; with memory 5/4; lenient 9/6. **fail.**

#### crow: *kaka* [kaka]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 烏鴉 (wūyā) (everyday) |  | ✗ | Wt |  |
| Japanese | 烏 (からす, karasu), 慈鳥 (じちょう, jichō) (everyday) |  | ✗ | Wt |  |
| Korean | 까마귀 (everyday) |  | ✗ | Wt |  |
| Vietnamese | quạ (everyday) |  | ✗ | Wt |  |
| Thai | กา kaa (everyday) | kawu | ✗ (✓ lenient) | Wt | one syllable |
| Indonesian | gagak (everyday) |  | ✗ | Wt | g-g-k |
| Tagalog | uwák (everyday) |  | ✗ | Wt |  |
| Hindi | कौआ kauā; काक kāk (formal) (everyday) | kaku | ✗ (✓ lenient) | Wt | kāk is listed (M*), kauā is the everyday word |
| Bengali | কাক kāk (everyday) | kaku | ✓ | Wt | adapted kaku |
| Tamil | காக்கை kākkai, காக்கா kākkā (colloquial) (everyday) | kaka | ✓ | Wt, We |  |
| Persian | کلاغ (kalâġ), غراب (ġorâb) (everyday) |  | ✗ | Wt |  |
| Arabic | غُرَاب, زَاغ (everyday) |  | ✗ | Wt |  |
| Turkish | karga (everyday) |  | ✗ | Wt |  |
| Russian | воро́на (everyday) |  | ✗ | Wt |  |
| Spanish | corneja, cuervo (everyday) |  | ✗ | Wt |  |
| French | corneille, corbeau (everyday) |  | ✗ | Wt |  |
| Swahili | kunguru (everyday) |  | ✗ | Wt |  |
| Hausa | hankaka (everyday) | ankaka | ✗ (✓ lenient) | Wt | adapted ankaka |
| Yoruba | kanna-kánná (everyday) |  | ✗ | Wt |  |
| Quechua | (no entry) (everyday) |  | ✗ | M | missing from Wt |

Sourced 2/20 in 1 regions; with memory 2/1; lenient 5/3. **fail.**

#### owl: *uwu* [huhu]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 貓頭鷹 (māotóuyīng), 夜貓子 (yèmāozi), 鴞 (xiāo) (everyday) |  | ✗ | Wt |  |
| Japanese | フクロウ (fukurō), 梟 (ふくろう, fukurō) (everyday) |  | ✗ | Wt |  |
| Korean | 올빼미, 부엉이 (everyday) |  | ✗ | Wt |  |
| Vietnamese | cú (everyday) |  | ✗ | Wt |  |
| Thai | นกฮูก (nók hûuk) (everyday) |  | ✗ | Wt |  |
| Indonesian | burung hantu, burung suangi, celepuk (everyday) |  | ✗ | Wt |  |
| Tagalog | kuwago (everyday) |  | ✗ | Wt |  |
| Hindi | उल्लू, पेचक, उलूक (everyday) |  | ✗ | Wt |  |
| Bengali | পেঁচা, উলূক, পেচক (everyday) |  | ✗ | Wt |  |
| Tamil | ஆந்தை, கூகை (everyday) |  | ✗ | Wt |  |
| Persian | جغد (joġd), بوف (buf) (everyday) |  | ✗ | Wt |  |
| Arabic | بُومَة (everyday) |  | ✗ | Wt |  |
| Turkish | baykuş (everyday) |  | ✗ | Wt |  |
| Russian | сова́, фи́лин, сыч (everyday) |  | ✗ | Wt |  |
| Spanish | búho, lechuza, tecolote (everyday) |  | ✗ | Wt |  |
| French | hibou, chouette (everyday) |  | ✗ | Wt |  |
| Swahili | bundi (everyday) |  | ✗ | Wt |  |
| Hausa | mujiya (everyday) |  | ✗ | Wt |  |
| Yoruba | òwìwí (everyday) |  | ✗ | Wt |  |
| Quechua | tuku, paqpaka, ch'usiqa (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### frog: *kulowa* [kroa]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 青蛙 (qīngwā), 田雞 (tiánjī) (everyday) |  | ✗ | Wt |  |
| Japanese | 蛙 (かえる, kaeru, かわず, kawazu), かはづ (kahadzu), カエル (kaeru) (everyday) |  | ✗ | Wt |  |
| Korean | 개구리 (everyday) |  | ✗ | Wt |  |
| Vietnamese | ếch, nhái, ngoé (everyday) |  | ✗ | Wt |  |
| Thai | กบ (gòp) (everyday) |  | ✗ | Wt |  |
| Indonesian | kodok (everyday) |  | ✗ | Wt |  |
| Tagalog | palaka (everyday) |  | ✗ | Wt |  |
| Hindi | मेंढक, मेंढकी, मेंडक (everyday) |  | ✗ | Wt |  |
| Bengali | ব্যাঙ (everyday) |  | ✗ | Wt |  |
| Tamil | தவளை (everyday) |  | ✗ | Wt |  |
| Persian | بَقَه, قُورْبَاغَه, قورْباغِه (everyday) |  | ✗ | Wt |  |
| Arabic | ضِفْدِع, ضَفْدَع, ضِفْدَع (everyday) |  | ✗ | Wt |  |
| Turkish | kurbağa (everyday) |  | ✗ | Wt |  |
| Russian | лягу́шка, жа́ба (everyday) |  | ✗ | Wt |  |
| Spanish | rana (everyday) |  | ✗ | Wt |  |
| French | grenouille (everyday) |  | ✗ | Wt |  |
| Swahili | chura (everyday) |  | ✗ | Wt |  |
| Hausa | kwaɗo (everyday) |  | ✗ | Wt |  |
| Yoruba | àkèré, kọ̀ǹkọ̀, ọ̀pọ̀lọ́ (everyday) |  | ✗ | Wt |  |
| Quechua | kaira, racak, jamp'atu (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### bee: *bese* [beze]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 蜜蜂 (mìfēng), 蠟蜂 (làfēng) (everyday) |  | ✗ | Wt |  |
| Japanese | 蜂 (はち, hachi), 花蜂 (はなばち, hanabachi) (everyday) |  | ✗ | Wt |  |
| Korean | 벌, 밀봉(蜜蜂) (everyday) |  | ✗ | Wt |  |
| Vietnamese | ong (everyday) |  | ✗ | Wt |  |
| Thai | ผึ้ง, ภมร, ภุมรี (everyday) |  | ✗ | Wt |  |
| Indonesian | lebah, tawon (everyday) |  | ✗ | Wt |  |
| Tagalog | bubuyog, pukyot (everyday) |  | ✗ | Wt |  |
| Hindi | मधुमक्खी (everyday) |  | ✗ | Wt |  |
| Bengali | মৌমাছি (everyday) |  | ✗ | Wt |  |
| Tamil | தேனீ (everyday) |  | ✗ | Wt |  |
| Persian | زَنْبور, زَنْبورِ عَسَل, مُنْج (everyday) |  | ✗ | Wt |  |
| Arabic | نَحْلَة, نَحْل (everyday) |  | ✗ | Wt |  |
| Turkish | arı (everyday) |  | ✗ | Wt |  |
| Russian | пчела́ (everyday) |  | ✗ | Wt |  |
| Spanish | abeja (everyday) |  | ✗ | Wt |  |
| French | abeille, mouche à miel (everyday) |  | ✗ | Wt |  |
| Swahili | nyuki (everyday) |  | ✗ | Wt |  |
| Hausa | zuma (everyday) |  | ✗ | Wt |  |
| Yoruba | oyin, kòkòrò oyin (everyday) |  | ✗ | Wt |  |
| Quechua | mapa mama, abiha (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### wolf: *lobo* [lobo]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 狼 (láng) (everyday) |  | ✗ | Wt |  |
| Japanese | 狼 (おおかみ, ōkami), オオカミ (ōkami), ウルフ (urufu) (everyday) |  | ✗ | Wt |  |
| Korean | 늑대, 이리 (everyday) |  | ✗ | Wt |  |
| Vietnamese | sói, chó sói (everyday) |  | ✗ | Wt |  |
| Thai | หมาป่า, สุนัขป่า (everyday) |  | ✗ | Wt |  |
| Indonesian | serigala (everyday) |  | ✗ | Wt |  |
| Tagalog | lobo (everyday) | lobo | ✓ | Wt | from Spanish |
| Hindi | भेड़िया, वृक (everyday) |  | ✗ | Wt |  |
| Bengali | নেকড়ে (everyday) |  | ✗ | Wt |  |
| Tamil | ஓநாய் (everyday) |  | ✗ | Wt |  |
| Persian | گُرْگ, گُرْگ (everyday) |  | ✗ | Wt |  |
| Arabic | ذِئْب (everyday) |  | ✗ | Wt |  |
| Turkish | kurt, börü (everyday) |  | ✗ | Wt |  |
| Russian | волк, волчи́ца (everyday) |  | ✗ | Wt |  |
| Spanish | lobo (everyday) | lobo | ✓ | Wt |  |
| French | loup (everyday) |  | ✗ | Wt |  |
| Swahili | mbwa mwitu (everyday) |  | ✗ | Wt |  |
| Hausa | kyarkeci (everyday) |  | ✗ | M | missing from Wt |
| Yoruba | ìkòokò (everyday) |  | ✗ | M | missing from Wt |
| Quechua | atawka (everyday) |  | ✗ | Wt |  |

Sourced 2/20 in 2 regions; with memory 2/2; lenient 2/2. **fail.**

#### pig: *bubu* [buːbuː]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 豬 (zhū), 豬玀 (zhūluó), 豕 (shǐ) (everyday) |  | ✗ | Wt |  |
| Japanese | 豚 buta; ブーブー būbū (childish) (nursery) | bubu | ✓ | Wt, We |  |
| Korean | 돼지 (everyday) |  | ✗ | Wt |  |
| Vietnamese | heo, lợn, cúi (everyday) |  | ✗ | Wt |  |
| Thai | หมู (everyday) |  | ✗ | Wt |  |
| Indonesian | babi (everyday) | babi | ✓ | Wt |  |
| Tagalog | baboy (everyday) | baboyu | ✗ (✓ lenient) | Wt | adapted baboyu |
| Hindi | सूअर (everyday) |  | ✗ | Wt |  |
| Bengali | শূকর, শুওর, শুয়ার (everyday) |  | ✗ | Wt |  |
| Tamil | பன்றி (everyday) |  | ✗ | Wt |  |
| Persian | خوک (everyday) |  | ✗ | Wt |  |
| Arabic | خِنْزِير, حَلُوف (everyday) |  | ✗ | Wt |  |
| Turkish | domuz, hınzır (everyday) |  | ✗ | Wt |  |
| Russian | свинья́, бо́ров (everyday) |  | ✗ | Wt |  |
| Spanish | cerdo, chancho, chon (everyday) |  | ✗ | Wt |  |
| French | cochon, porc, pourceau (everyday) |  | ✗ | Wt |  |
| Swahili | nguruwe (everyday) |  | ✗ | Wt |  |
| Hausa | alade (everyday) |  | ✗ | Wt |  |
| Yoruba | ẹlẹ́dẹ̀, òdo (everyday) |  | ✗ | Wt |  |
| Quechua | khuchi (everyday) |  | ✗ | Wt |  |

Sourced 2/20 in 2 regions; with memory 2/2; lenient 3/2. **fail.**

#### horse: *dada* [dada]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 馬 (mǎ) (everyday) |  | ✗ | Wt |  |
| Japanese | 馬 (うま, uma), ウマ (uma) (everyday) |  | ✗ | Wt |  |
| Korean | 말 (everyday) |  | ✗ | Wt |  |
| Vietnamese | ngựa (everyday) |  | ✗ | Wt |  |
| Thai | ม้า (everyday) |  | ✗ | Wt |  |
| Indonesian | kuda (everyday) |  | ✗ | Wt |  |
| Tagalog | kabayo (everyday) |  | ✗ | Wt |  |
| Hindi | घोड़ा, अश्व, तुरग (everyday) |  | ✗ | Wt |  |
| Bengali | ঘোড়া (everyday) |  | ✗ | Wt |  |
| Tamil | குதிரை, புரவி (everyday) |  | ✗ | Wt |  |
| Persian | اَسْپ (asp), اَسْب (everyday) |  | ✗ | Wt |  |
| Arabic | حِصَان, فَرَس, خَيْل (everyday) |  | ✗ | Wt |  |
| Turkish | at, deh deh, beygir (everyday) |  | ✗ | Wt |  |
| Russian | ло́шадь, конь (everyday) |  | ✗ | Wt |  |
| Spanish | caballo, arpa, caballuno (everyday) |  | ✗ | Wt |  |
| French | cheval; dada (childish) (nursery) | dada | ✓ | Wt, We |  |
| Swahili | farasi (everyday) |  | ✗ | Wt |  |
| Hausa | doki (everyday) |  | ✗ | Wt |  |
| Yoruba | ẹṣin (everyday) |  | ✗ | Wt |  |
| Quechua | kawallu (everyday) |  | ✗ | Wt |  |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 1/1. **fail.**

#### donkey: *iya* [hiha]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 驢 (lǘ), 驢子 (lǘzi) (everyday) |  | ✗ | Wt |  |
| Japanese | 驢馬 (ろば, roba), ロバ (roba) (everyday) |  | ✗ | Wt |  |
| Korean | 당나귀, 나귀 (everyday) |  | ✗ | Wt |  |
| Vietnamese | lừa (everyday) |  | ✗ | Wt |  |
| Thai | ลา (everyday) |  | ✗ | Wt |  |
| Indonesian | keledai (everyday) |  | ✗ | Wt |  |
| Tagalog | asno, buriko (everyday) |  | ✗ | Wt |  |
| Hindi | गधा, हिमार (everyday) |  | ✗ | Wt |  |
| Bengali | গাধা (everyday) |  | ✗ | Wt |  |
| Tamil | கழுதை (everyday) |  | ✗ | Wt |  |
| Persian | خَر, حِمَار, خَر (everyday) |  | ✗ | Wt |  |
| Arabic | حِمَار (everyday) |  | ✗ | Wt |  |
| Turkish | eşek, merkep, himar (everyday) |  | ✗ | Wt |  |
| Russian | осёл, осли́ца, иша́к (everyday) |  | ✗ | Wt |  |
| Spanish | asno, burro, jumento (everyday) |  | ✗ | Wt |  |
| French | âne (everyday) |  | ✗ | Wt |  |
| Swahili | punda (everyday) |  | ✗ | Wt |  |
| Hausa | jaki (everyday) |  | ✗ | Wt |  |
| Yoruba | kẹ́tẹ́kẹ́tẹ́ (everyday) |  | ✗ | Wt |  |
| Quechua | wuru, asnu (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### mouse: *tutu* [tʃuːtʃuː]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 老鼠, 鼠, 耗子 (everyday) |  | ✗ | Wt |  |
| Japanese | 鼠 nezumi; チューチュー chūchū (nursery) (nursery) | tutu | ✓ | Wt, Wb | Wordbank JA sounds item チューチュー（ねずみ） |
| Korean | 생쥐, 쥐 (everyday) |  | ✗ | Wt |  |
| Vietnamese | chuột (everyday) |  | ✗ | Wt |  |
| Thai | หนู (everyday) |  | ✗ | Wt |  |
| Indonesian | tikus (everyday) |  | ✗ | Wt |  |
| Tagalog | daga (everyday) |  | ✗ | Wt |  |
| Hindi | चूहा (everyday) |  | ✗ | Wt |  |
| Bengali | ইঁদুর (everyday) |  | ✗ | Wt |  |
| Tamil | சுண்டெலி (everyday) |  | ✗ | Wt |  |
| Persian | مُوش, موش, مُشْک (everyday) |  | ✗ | Wt |  |
| Arabic | فَأْرَة, فَأْر (everyday) |  | ✗ | Wt |  |
| Turkish | fare, sıçan (everyday) |  | ✗ | Wt |  |
| Russian | мышь, мы́шка (everyday) |  | ✗ | Wt |  |
| Spanish | ratón, laucha, pericote (everyday) |  | ✗ | Wt |  |
| French | souris (everyday) |  | ✗ | Wt |  |
| Swahili | kipanya (everyday) |  | ✗ | Wt |  |
| Hausa | ɓera (everyday) |  | ✗ | Wt |  |
| Yoruba | èkúté, eliri (everyday) |  | ✗ | Wt |  |
| Quechua | ukuca, ukuş, juk'ucha (everyday) |  | ✗ | Wt |  |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 1/1. **fail.**

#### kiss: *busu* [busu]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 吻 (wěn), 親 (qīn), 親吻 (qīnwěn) (everyday) |  | ✗ | Wt |  |
| Japanese | キス kisu; チュー chū (colloquial) (everyday) |  | ✗ | Wt | chū is the imitative word; ko 뽀뽀 ppoppo; no two share one |
| Korean | 입맞춤, 키스, 뽀뽀 (everyday) |  | ✗ | Wt |  |
| Vietnamese | [[nụ]] [[hôn]], [[cái]] [[hôn]] (everyday) |  | ✗ | Wt |  |
| Thai | การจูบ, จูบ (everyday) |  | ✗ | Wt |  |
| Indonesian | ciuman (everyday) |  | ✗ | Wt |  |
| Tagalog | halik, humalik, maghalikan (everyday) |  | ✗ | Wt |  |
| Hindi | चुम्बन, पप्पी, चुम्मा (everyday) |  | ✗ | Wt |  |
| Bengali | চুম্বন chumbon; চুমু chumu; বুসা busa (everyday) | busa | ✗ (✓ lenient) | Wt | Wt lists busa; chumu is the everyday word (M*) |
| Tamil | முத்தம் (everyday) |  | ✗ | Wt |  |
| Persian | بوسه buse, بوس bus (everyday) | buse | ✓ | Wt |  |
| Arabic | قبلة qubla; بوسة būsa (spoken) (everyday) | busa | ✓ | Wt |  |
| Turkish | öpücük; buse (literary) (everyday) | buse | ✗ (✓ lenient) | Wt | buse is literary |
| Russian | поцелу́й (everyday) |  | ✗ | Wt |  |
| Spanish | beso (everyday) | beso | ✓ | Wt |  |
| French | baiser, bisou (everyday) | bisu | ✓ | Wt | bisou is the everyday noun |
| Swahili | busu (everyday) | busu | ✓ | Wt |  |
| Hausa | sumba (everyday) |  | ✗ | M | missing from Wt |
| Yoruba | ìfẹnukonu (everyday) |  | ✗ | M | missing from Wt |
| Quechua | much'a (everyday) |  | ✗ | Wt |  |

Sourced 5/20 in 3 regions; with memory 5/3; lenient 7/4. **fail.**

#### knock: *toku* [tok]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 敲 (qiāo) (everyday) |  | ✗ | Wt |  |
| Japanese | ノックする nokku suru; 叩く tataku (everyday) |  | ✗ | Wt | a loan of English knock (ko 노크 too) |
| Korean | 노크하다, 두드리다 (everyday) |  | ✗ | Wt |  |
| Vietnamese | gõ (everyday) |  | ✗ | Wt |  |
| Thai | เคาะ (everyday) |  | ✗ | Wt |  |
| Indonesian | ketuk, ketok (everyday) |  | ✗ | Wt |  |
| Tagalog | katok; tuktok (everyday) | tukutoku | ✗ (✓ lenient) | We | adapted tukutoku |
| Hindi | खटखटाना (everyday) |  | ✗ | Wt |  |
| Bengali | টোকা ṭokā (দেওয়া) (everyday) | toka | ✓ | We | We: 'knock' |
| Tamil | தட்டு taṭṭu (everyday) |  | ✗ | M |  |
| Persian | زدن (zadan), کوبیدن (kubidan) (everyday) |  | ✗ | Wt |  |
| Arabic | خَبَطَ, دَقَّ, طَرَقَ (everyday) |  | ✗ | Wt |  |
| Turkish | çalmak, tıklatmak, vurmak (everyday) |  | ✗ | Wt |  |
| Russian | стуча́ть, сту́кнуть, постуча́ть (everyday) |  | ✗ | Wt |  |
| Spanish | tocar (a la puerta), llamar (everyday) | tokalu | ✗ (✓ lenient) | Wt | adapted tokalu |
| French | frapper (everyday) |  | ✗ | Wt |  |
| Swahili | bisha hodi (everyday) |  | ✗ | M |  |
| Hausa | ƙwanƙwasa (everyday) |  | ✗ | M |  |
| Yoruba | kan ilẹ̀kùn (everyday) |  | ✗ | M |  |
| Quechua | (no entry) (everyday) |  | ✗ | M |  |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 3/3. **fail.**

#### laugh: *awu* [haha]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 笑 (xiào), 發笑 (fāxiào) (everyday) |  | ✗ | Wt |  |
| Japanese | 笑う (warau) (everyday) |  | ✗ | Wt |  |
| Korean | 웃다 (everyday) |  | ✗ | Wt |  |
| Vietnamese | cười (everyday) |  | ✗ | Wt |  |
| Thai | ขำ, หัวเราะ (everyday) |  | ✗ | Wt |  |
| Indonesian | tertawa (everyday) |  | ✗ | Wt |  |
| Tagalog | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Hindi | हँसना hãsnā (everyday) |  | ✗ | Wt | the has shape (hi bn) and the tawa shape (id tl) reach 2 each |
| Bengali | উপহাস করা, হাসা (everyday) |  | ✗ | Wt |  |
| Tamil | சிரி (everyday) |  | ✗ | Wt |  |
| Persian | خندیدن (xandidan) (everyday) |  | ✗ | Wt |  |
| Arabic | ضَحِكَ (everyday) |  | ✗ | Wt |  |
| Turkish | gülmek (everyday) |  | ✗ | Wt |  |
| Russian | смея́ться, рассмея́ться, хохота́ть (everyday) |  | ✗ | Wt |  |
| Spanish | reír (everyday) |  | ✗ | Wt |  |
| French | rire (everyday) |  | ✗ | Wt |  |
| Swahili | cheka (everyday) |  | ✗ | M | missing from Wt |
| Hausa | dāra (everyday) |  | ✗ | Wt |  |
| Yoruba | rẹ́rìn-ín (everyday) |  | ✗ | Wt |  |
| Quechua | asiy (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### cry: *wawa* [wawa]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 哭 (kū), 流眼淚 (liú yǎnlèi), 流淚 (liúlèi) (everyday) |  | ✗ | Wt |  |
| Japanese | 泣く (なく, naku) (everyday) |  | ✗ | Wt |  |
| Korean | 울다, 흐느끼다 (everyday) |  | ✗ | Wt |  |
| Vietnamese | khóc (everyday) |  | ✗ | Wt |  |
| Thai | ร้องไห้, ร่ำไห้ (everyday) |  | ✗ | Wt |  |
| Indonesian | tangis, menangis (everyday) |  | ✗ | Wt |  |
| Tagalog | lumuha, umiyak, hikbi (everyday) |  | ✗ | Wt |  |
| Hindi | रोना (everyday) |  | ✗ | Wt |  |
| Bengali | কাঁদা, কান্দা, ক্রন্দন করা (everyday) |  | ✗ | Wt |  |
| Tamil | அழு (everyday) |  | ✗ | Wt |  |
| Persian | گریستن (geristan), گریه کردن (gerye kardan) (everyday) |  | ✗ | Wt |  |
| Arabic | بَكَى (everyday) |  | ✗ | Wt |  |
| Turkish | ağlamak (everyday) |  | ✗ | Wt |  |
| Russian | пла́кать, рыда́ть (everyday) |  | ✗ | Wt |  |
| Spanish | llorar, plorar (everyday) |  | ✗ | Wt |  |
| French | pleurer (everyday) |  | ✗ | Wt |  |
| Swahili | lia (everyday) |  | ✗ | M | missing from Wt |
| Hausa | kuka (everyday) |  | ✗ | M | missing from Wt |
| Yoruba | sọkún (everyday) |  | ✗ | M | missing from Wt |
| Quechua | waqay, wagai (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### sneeze: *atu* [atʃu]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 打噴嚏 (everyday) |  | ✗ | Wt |  |
| Japanese | くしゃみ (kushami o suru), しゃみ (shami o suru) (everyday) |  | ✗ | Wt |  |
| Korean | 재채기하다 (everyday) |  | ✗ | Wt |  |
| Vietnamese | hắt hơi, hắt xì (everyday) | asi | ✗ (✓ lenient) | Wt | adapted atusi |
| Thai | จาม (everyday) |  | ✗ | Wt |  |
| Indonesian | bersin (everyday) |  | ✗ | Wt |  |
| Tagalog | bumahin, humatsing (everyday) |  | ✗ | Wt |  |
| Hindi | छींकना (everyday) |  | ✗ | Wt |  |
| Bengali | হাঁচি hā̃ci (দেওয়া) (everyday) | ati | ✓ | Wt | adapted ati |
| Tamil | தும்மு (everyday) |  | ✗ | Wt |  |
| Persian | عطسه کردن atse kardan (everyday) |  | ✗ | Wt | adapted ase |
| Arabic | عَطَسَ (everyday) |  | ✗ | Wt |  |
| Turkish | hapşırmak, aksırmak (everyday) |  | ✗ | Wt |  |
| Russian | чиха́ть, чихну́ть (everyday) |  | ✗ | Wt |  |
| Spanish | estornudar (everyday) |  | ✗ | Wt |  |
| French | éternuer (everyday) |  | ✗ | Wt |  |
| Swahili | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Hausa | atishawa (everyday) |  | ✗ | M | adapted atisawa |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | achhiy (everyday) | atiyu | ✗ (✓ lenient) | Wt | adapted atiyu |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 3/3. **fail.**

#### cough: *kofu* [kof]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 咳嗽 (késou) (everyday) |  | ✗ | Wt |  |
| Japanese | [[咳]]を[[する]] (せきをする, seki o suru) (everyday) |  | ✗ | Wt |  |
| Korean | 기침하다 (everyday) |  | ✗ | Wt |  |
| Vietnamese | ho (everyday) |  | ✗ | Wt |  |
| Thai | ไอ (everyday) |  | ✗ | Wt |  |
| Indonesian | batuk (everyday) |  | ✗ | Wt |  |
| Tagalog | umubo (everyday) |  | ✗ | Wt |  |
| Hindi | खांसना, खाँसना (everyday) |  | ✗ | Wt |  |
| Bengali | কাশা (everyday) |  | ✗ | Wt |  |
| Tamil | இருமு (everyday) |  | ✗ | Wt |  |
| Persian | کهیدن (kohidan), سرفیدن (sorfidan), سرفه کردن (sorfe kardan) (everyday) |  | ✗ | Wt |  |
| Arabic | سَعَلَ (everyday) |  | ✗ | Wt |  |
| Turkish | öksürmek (everyday) |  | ✗ | Wt |  |
| Russian | ка́шлять, кашляну́ть (everyday) |  | ✗ | Wt |  |
| Spanish | toser (everyday) |  | ✗ | Wt |  |
| French | tousser (everyday) |  | ✗ | Wt |  |
| Swahili | kohoa (everyday) |  | ✗ | Wt |  |
| Hausa | tari (everyday) |  | ✗ | M | missing from Wt |
| Yoruba | húkọ́ (everyday) |  | ✗ | Wt |  |
| Quechua | uhuy (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### hiccup: *iku* [hik]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 打嗝 (dǎgé[r]), 呃逆 (ènì) (everyday) |  | ✗ | Wt |  |
| Japanese | しゃっくり shakkuri; ヒック hikku (the sound) (everyday) | iku | ✗ (✓ lenient) | Wt | Wt lists hikku; it is the sound, not the everyday name (M*) |
| Korean | 딸꾹질 (everyday) |  | ✗ | Wt |  |
| Vietnamese | cái nấc (everyday) |  | ✗ | Wt |  |
| Thai | สะอึก (sà-ʉ̀k) (everyday) |  | ✗ | Wt |  |
| Indonesian | cegukan (everyday) |  | ✗ | Wt |  |
| Tagalog | sinok, sigok, siyok (everyday) |  | ✗ | Wt |  |
| Hindi | हिचकी (everyday) |  | ✗ | Wt |  |
| Bengali | হেঁচকা (hẽcka), হেঁচকি (hẽcki) (everyday) |  | ✗ | Wt |  |
| Tamil | விக்கல் (everyday) |  | ✗ | Wt |  |
| Persian | سکسکه (sekseke), هکه (hokke), هکک (hekkak) (everyday) |  | ✗ | Wt |  |
| Arabic | حَازُوقَة, فُوَاق (everyday) |  | ✗ | Wt |  |
| Turkish | hıçkırık (everyday) |  | ✗ | Wt |  |
| Russian | ико́та (everyday) |  | ✗ | Wt |  |
| Spanish | hipo, singulto, hipido (everyday) |  | ✗ | Wt |  |
| French | hoquet (everyday) |  | ✗ | Wt |  |
| Swahili | kwikwi (everyday) |  | ✗ | Wt |  |
| Hausa | ƙyafta (everyday) |  | ✗ | M | missing from Wt |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | hik'iy (everyday) | ikiyu | ✗ (✓ lenient) | Wt | adapted ikiyu |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 2/2. **fail.**

#### burp: *gepu* [gep]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 飽嗝 (bǎogé), 噯氣 (ǎiqì) (everyday) |  | ✗ | Wt |  |
| Japanese | げっぷ geppu (everyday) | gepu | ✓ | Wt | adapted gepu |
| Korean | 트림, 애기 (everyday) |  | ✗ | Wt |  |
| Vietnamese | ợ (everyday) |  | ✗ | Wt |  |
| Thai | เรอ (everyday) |  | ✗ | Wt |  |
| Indonesian | serdawa, sendawa, antop (everyday) |  | ✗ | Wt |  |
| Tagalog | dighay (everyday) |  | ✗ | Wt |  |
| Hindi | डकार (everyday) |  | ✗ | Wt |  |
| Bengali | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Tamil | ஏப்பம் (everyday) |  | ✗ | Wt |  |
| Persian | آروغ (âruġ) (everyday) |  | ✗ | Wt |  |
| Arabic | تَجَشُّؤ (everyday) |  | ✗ | Wt |  |
| Turkish | geğirme (everyday) |  | ✗ | Wt |  |
| Russian | отры́жка, рыга́ние (everyday) |  | ✗ | Wt |  |
| Spanish | eructo, regüeldo (everyday) |  | ✗ | Wt |  |
| French | rot, renvoi, éructation (everyday) |  | ✗ | Wt |  |
| Swahili | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Hausa | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 1/1. **fail.**

#### vomit: *uwaku* [ʔuak]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 嘔吐 (ǒutù), 嘔 (ǒu), 吐 (tù) (everyday) |  | ✗ | Wt |  |
| Japanese | 吐く ([[はく]], haku), 嘔吐 (おうとする, ōto suru), 戻す (もどす, modosu) (everyday) |  | ✗ | Wt |  |
| Korean | 게우다, 토하다 (everyday) |  | ✗ | Wt |  |
| Vietnamese | nôn, mửa, ói (everyday) |  | ✗ | Wt |  |
| Thai | อาเจียน aa-jian (formal); อ้วก ûak (colloquial) (everyday) | uwaku | ✓ | Wt |  |
| Indonesian | memuntahkan, muntah (everyday) |  | ✗ | Wt |  |
| Tagalog | sumuka (everyday) |  | ✗ | Wt |  |
| Hindi | उल्टी करना, वमन करना, उल्टी (everyday) |  | ✗ | Wt |  |
| Bengali | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Tamil | குமட்டு, உவட்டு, உவாந்தி (everyday) |  | ✗ | Wt |  |
| Persian | قی کردن (qay kardan), بالا آوردن (bâlâ âvordan) (everyday) |  | ✗ | Wt |  |
| Arabic | تَقَيَّأَ, قَاءَ, اِسْتَفْرَغَ (everyday) |  | ✗ | Wt |  |
| Turkish | kusmak, istifra etmek (everyday) |  | ✗ | Wt |  |
| Russian | блева́ть, рвать, тошни́ть (everyday) |  | ✗ | Wt |  |
| Spanish | vomitar, devolver, arrojar (everyday) |  | ✗ | Wt |  |
| French | vomir (everyday) |  | ✗ | Wt |  |
| Swahili | tapika (everyday) |  | ✗ | Wt |  |
| Hausa | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | aqtuy (everyday) |  | ✗ | Wt |  |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 1/1. **fail.**

#### yawn: *wamu* [hwam]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 打哈欠 (dǎ hāqian), 打呵欠 (dǎ hēqiàn), 打阿老 (dǎ ālǎo) (everyday) |  | ✗ | Wt |  |
| Japanese | 欠伸 (あくびする, akubi suru) (everyday) |  | ✗ | Wt |  |
| Korean | 하품하다 (everyday) |  | ✗ | Wt |  |
| Vietnamese | ngáp (everyday) |  | ✗ | Wt |  |
| Thai | หาว (everyday) |  | ✗ | Wt |  |
| Indonesian | menguap (everyday) |  | ✗ | Wt |  |
| Tagalog | maghikab (everyday) |  | ✗ | Wt |  |
| Hindi | जंभना, जँभाई लेना, अंगड़ाई लेना (everyday) |  | ✗ | Wt |  |
| Bengali | হাই তোলা (everyday) |  | ✗ | Wt |  |
| Tamil | கொட்டாவி (everyday) |  | ✗ | Wt |  |
| Persian | خمیازه کشیدن (xamyâze kešidan), فاژیدن (fâžidan), دهان‌دره کردن (dahân-darre kardan) (everyday) |  | ✗ | Wt |  |
| Arabic | تَثَاءَبَ (everyday) |  | ✗ | Wt |  |
| Turkish | esnemek (everyday) |  | ✗ | Wt |  |
| Russian | зева́ть, зевну́ть (everyday) |  | ✗ | Wt |  |
| Spanish | bostezar (everyday) |  | ✗ | Wt |  |
| French | bâiller (everyday) |  | ✗ | Wt |  |
| Swahili | piga miayo, enda miayo (everyday) |  | ✗ | Wt |  |
| Hausa | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | hanyay (everyday) |  | ✗ | Wt |  |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### snore: *olu* [hor]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 打鼾 (everyday) |  | ✗ | Wt |  |
| Japanese | [[鼾]][[を]][[かく]] (いびきをかく, ibiki o kaku), [[鼾]][[を]][[立てる]] (いびきをたてる, ibiki o tateru) (everyday) |  | ✗ | Wt |  |
| Korean | [[코]][[-를]] [[골다]] (everyday) |  | ✗ | Wt |  |
| Vietnamese | ngáy (everyday) |  | ✗ | Wt |  |
| Thai | กรน (everyday) |  | ✗ | Wt |  |
| Indonesian | mendengkur, berdengkur (everyday) |  | ✗ | Wt |  |
| Tagalog | humilik (everyday) |  | ✗ | Wt |  |
| Hindi | खर्राटा लेना (everyday) |  | ✗ | Wt |  |
| Bengali | নাক ডাকা (everyday) |  | ✗ | Wt |  |
| Tamil | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Persian | خرخر کردن xorxor kardan (everyday) |  | ✗ | Wt | adapted kolukolu |
| Arabic | شَخَرَ (everyday) |  | ✗ | Wt |  |
| Turkish | horlamak (everyday) |  | ✗ | Wt |  |
| Russian | храпе́ть (everyday) |  | ✗ | Wt |  |
| Spanish | roncar (everyday) |  | ✗ | Wt |  |
| French | ronfler (everyday) |  | ✗ | Wt |  |
| Swahili | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Hausa | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

#### sleep (nursery): *nene* [nene]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 睡覺; 覺覺 jiàojiao (childish) (nursery) |  | ✗ | Wt, We |  |
| Japanese | 寝る neru; ネンネ nenne (nursery) (nursery) | nene | ✓ | Wt, Wb | Wordbank JA sounds item ネンネ |
| Korean | 자다, 잠자다, 주무시다 (everyday) |  | ✗ | Wt |  |
| Vietnamese | ngủ, ngủ gục (everyday) |  | ✗ | Wt |  |
| Thai | นอน, หลับ (everyday) |  | ✗ | Wt |  |
| Indonesian | tidur; bobo (childish) (nursery) |  | ✗ | Wt, We |  |
| Tagalog | matulog (everyday) |  | ✗ | Wt |  |
| Hindi | सोना (everyday) |  | ✗ | Wt |  |
| Bengali | শোয়া, ঘুমানো (everyday) |  | ✗ | Wt |  |
| Tamil | தூங்கு, உறங்கு (everyday) |  | ✗ | Wt |  |
| Persian | خوابیدن; لالا lālā (childish) (nursery) |  | ✗ | Wt, We |  |
| Arabic | نَامَ, رَقَدَ (everyday) |  | ✗ | Wt |  |
| Turkish | uyumak (everyday) |  | ✗ | Wt |  |
| Russian | спать, поспа́ть (everyday) |  | ✗ | Wt |  |
| Spanish | dormir; mimir (childish) (nursery) |  | ✗ | Wt, We |  |
| French | dormir; dodo (childish) (nursery) |  | ✗ | Wt, We |  |
| Swahili | kulala, lala (everyday) |  | ✗ | Wt |  |
| Hausa | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | puñuy, puñui (everyday) |  | ✗ | Wt |  |

Sourced 1/20 in 1 regions; with memory 1/1; lenient 1/1. **fail.**

#### eat, food (nursery): *mama* [mama]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 食物 (shíwù), 食品 (shípǐn), 吃食 (chīshi) (everyday) |  | ✗ | Wt |  |
| Japanese | 食べ物 tabemono; マンマ manma (food, nursery) (nursery) | manma | ✗ (✓ lenient) | Wt, Wb | Wordbank JA sounds item マンマ（食べ物）; adapted manma (n-m) |
| Korean | 음식 eumsik; 맘마 mamma (childish 'meal') (nursery) | mama | ✓ | Wt, We |  |
| Vietnamese | thức ăn; măm (to eat, of a baby) (nursery) | mamu | ✓ | Wt, We | adapted mamu |
| Thai | อาหาร, ของกิน (everyday) |  | ✗ | Wt |  |
| Indonesian | makanan, pangan (everyday) |  | ✗ | Wt |  |
| Tagalog | pagkain (everyday) |  | ✗ | Wt |  |
| Hindi | खाना, भोजन, ग़िज़ा (everyday) |  | ✗ | Wt |  |
| Bengali | খাদ্য, খাবার (khabar) (everyday) |  | ✗ | Wt |  |
| Tamil | சாப்பாடு, உணவு (everyday) |  | ✗ | Wt |  |
| Persian | غِذَا, خوراک (xōrāk, xurāk), نَان (everyday) |  | ✗ | Wt |  |
| Arabic | طَعَام, أَكْل, غِذَاء (everyday) |  | ✗ | Wt |  |
| Turkish | yemek; mama (baby food) (nursery) | mama | ✓ | Wt, We | We: 'food (in child's language)' |
| Russian | еда; ням-ням nyam-nyam (M) (nursery) |  | ✗ | Wt, M |  |
| Spanish | alimento, comida, víveres (everyday) |  | ✗ | Wt |  |
| French | nourriture, alimentation, manger (everyday) |  | ✗ | Wt |  |
| Swahili | chakula (everyday) |  | ✗ | Wt |  |
| Hausa | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Yoruba | oúnjẹ (everyday) |  | ✗ | Wt |  |
| Quechua | mikhuna (everyday) |  | ✗ | Wt |  |

Sourced 3/20 in 3 regions; with memory 3/3; lenient 4/3. **fail.**

#### pee (nursery): *pipi* [pipi]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 尿 (niào), 排尿, 撒尿 (everyday) |  | ✗ | Wt |  |
| Japanese | おしっこ oshikko; しーしー shīshī (nursery) |  | ✗ | Wt | the sisi shape: ja shīshī, hi susū (We) |
| Korean | 오줌 누다; 쉬 swi (childish) (nursery) |  | ✗ | We |  |
| Vietnamese | tiểu, tiểu tiện (everyday) |  | ✗ | Wt |  |
| Thai | ปัสสาวะ; ฉี่ chìi (nursery) |  | ✗ | We |  |
| Indonesian | kencing; pipis (nursery) | pipisu | ✗ (✓ lenient) | We | adapted pipisu |
| Tagalog | umihi; wiwi (childish) (nursery) |  | ✗ | We |  |
| Hindi | पेशाब करना; सुसू susū (childish) (nursery) |  | ✗ | We |  |
| Bengali | মুতা (everyday) |  | ✗ | Wt |  |
| Tamil | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Persian | ادرار کردن; جیش jiš (childish) (nursery) |  | ✗ | Wt |  |
| Arabic | تَبَوَّلَ, بَالَ (everyday) |  | ✗ | Wt |  |
| Turkish | işemek; çiş (childish) (nursery) |  | ✗ | Wt |  |
| Russian | мочиться; пипи pipi (childish) (nursery) | pipi | ✓ | Wt | Wt 'pee' (urine) table |
| Spanish | orinar; pipí, pis (childish) (nursery) | pipi | ✓ | Wt, We |  |
| French | uriner; pipi (childish) (nursery) | pipi | ✓ | Wt, We |  |
| Swahili | kojoa, tabawali (everyday) |  | ✗ | Wt |  |
| Hausa | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | ispay, jisp'ay (everyday) |  | ✗ | Wt |  |

Sourced 3/20 in 1 regions; with memory 3/1; lenient 4/2. **fail.**

#### poo (nursery): *kaka* [kaka]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 大便 (dàbiàn), 便便 (biānbiān) (everyday) |  | ✗ | Wt |  |
| Japanese | うんち (unchi), うんこ (unko) (everyday) |  | ✗ | Wt |  |
| Korean | 응가, 똥 (everyday) |  | ✗ | Wt |  |
| Vietnamese | phân (everyday) |  | ✗ | Wt |  |
| Thai | อุจจาระ (everyday) |  | ✗ | Wt |  |
| Indonesian | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Tagalog | pupu (childish) (nursery) |  | ✗ | Wt, We | the pupu/popo shape: tl pupu, es popó, fr popo |
| Hindi | टट्टी, मल, गू (everyday) |  | ✗ | Wt |  |
| Bengali | হাগু hagu (nursery) |  | ✗ | Wt | Bengali kaka = paternal uncle (We) |
| Tamil | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Persian | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Arabic | براز burāz; كاكا kākā (nursery) | kaka | ✓ | Wt |  |
| Turkish | kaka (childish) (nursery) | kaka | ✓ | Wt, We |  |
| Russian | кака kaka (childish) (nursery) | kaka | ✓ | Wt, We |  |
| Spanish | caca (childish); popó (nursery) | kaka | ✓ | We |  |
| French | caca (childish) (nursery) | kaka | ✓ | Wt, We |  |
| Swahili | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Hausa | tutu (childish) (nursery) |  | ✗ | We |  |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | aka (everyday) | aka | ✗ (✓ lenient) | We | adapted aka (one k) |

Sourced 5/20 in 2 regions; with memory 5/2; lenient 6/3. **fail.**

#### bang, boom: *bumu* [bum]

| Lang | Word (kind) | Adapted | Shared | src | Note |
|---|---|---|---|---|---|
| Mandarin | 爆炸, 爆發 (everyday) |  | ✗ | Wt |  |
| Japanese | 爆発 (ばくはつ bakuhatsu) (everyday) |  | ✗ | Wt |  |
| Korean | 폭발(爆發) (everyday) |  | ✗ | Wt |  |
| Vietnamese | nổ; bùm (the sound) (everyday) |  | ✗ | Wt | the sound word bùm/boum/bum/бум is shared as an interjection (2.10) |
| Thai | การระเบิด, ภัยการระเบิด (everyday) |  | ✗ | Wt |  |
| Indonesian | ledakan, letupan, eksplosi (everyday) |  | ✗ | Wt |  |
| Tagalog | pagsabog (everyday) |  | ✗ | Wt |  |
| Hindi | विस्फोट (everyday) |  | ✗ | Wt |  |
| Bengali | বিস্ফোরণ (everyday) |  | ✗ | Wt |  |
| Tamil | வெடி (everyday) |  | ✗ | Wt |  |
| Persian | اِنْفِجار (enfejâr), ترکش (tarkeš) (everyday) |  | ✗ | Wt |  |
| Arabic | اِنْفِجَار, تَفْجِير (everyday) |  | ✗ | Wt |  |
| Turkish | patlama (everyday) |  | ✗ | Wt |  |
| Russian | взрыв (everyday) |  | ✗ | Wt |  |
| Spanish | explosión (everyday) |  | ✗ | Wt |  |
| French | explosion (everyday) |  | ✗ | Wt |  |
| Swahili | mlipuko (everyday) |  | ✗ | Wt |  |
| Hausa | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Yoruba | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |
| Quechua | (not in Wt; not looked up) (everyday) |  | ✗ | — | cannot change the verdict |

Sourced 0/20 in 0 regions; with memory 0/0; lenient 0/0. **fail.**

