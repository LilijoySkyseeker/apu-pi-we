# Loan candidates from coverage-01 part 3 against the panel

Proposals only; no word was changed. Candidates: the 109 rows of `ladder.tsv` (this folder) with route `loan?`. Results per candidate: `loans.tsv`.

## Author's decisions

- **Pattern 1 (2026-10-13): count everyday loans beside a formal native word.** A column counts when the loan is what speakers say every day, even where a formal native word exists, with a source for the column; occasional code-switching doesn't count. Verdicts are recomputed after the evidence question (pattern 2).
- **Pattern 2 (2026-10-13): memory columns need a source** (frequency lists, the foreign word's Wiktionary entry, a dictionary); only deciding columns are checked; no blanket Quechua assumption.
- **Pattern 3 (2026-10-13): two shapes are one form when their adapted forms keep the same consonants** (pope/papa together; channel/kanal, mosque/masjid apart).

- **The rest (2026-10-13):** thin deciding columns fail (project, campaign, sofa, platform); the five-times rival rule is accepted; median ties by region count, then length; shared short forms tested and preferred; loans keep their forms and roots move; mile not core; pound a currency loan; pope and mosque each tradition's own word. Final list: `loans-final.tsv` (62 pass, plus pound as a currency).

## Method

The same as `tests/lexicon-ladder-01/loans.md` ("How this was done"), unchanged:

- For each candidate I recorded the everyday word in each of the 20 panel languages and whether a speaker would hear it as the same word as the international form. Translations and calques don't count; neither does a distant etymological link.
- Pass rule (goal L4): at least 12 of 20, across at least 4 of the 7 regions EA (zh ja ko), SEA (vi th id tl), SA (hi bn ta), WA (fa ar tr), EU (ru es fr), SSA (sw ha yo), AM (qu).
- Sources: **Wt** the English Wiktionary translation table for the sense in each heading, fetched 2026-10-13 with `tests/lexicon-ladder-01/panel.py`; **We** the Wiktionary entry for the foreign word; **M** from memory; **M\*** Wiktionary lists the word, but my judgment of the everyday word differs from its first-listed one.
- Quechua: where Wiktionary gives a native form I used it; otherwise I assumed the Spanish loan of bilingual speech (M).
- Borderline: where the count depends on M\* or lenient judgments (✗ (✓ lenient) in the tables), both counts are given. A candidate is **borderline** when the strict count fails and the lenient count passes. It is **pass, borderline** (as email was in loans.md) when the strict count passes at exactly 12, or in exactly 4 regions, and at least one counted column is from memory (M or M\*).
- Median pronunciation: for each sound position, the majority among the cognate forms only (the strict ones, unless the entry says otherwise), in broad IPA, run through `tools/names.py`. Given for passes and borderlines; ties are reported in the entry. I checked the adapted forms against `data/lexicon.tsv` (same form or same content key, as `names.py` does); not against `offensive.py`.
- One tool fix: `panel.py` skipped `{{trans-top-also}}` blocks, which Wiktionary uses for some main senses (sandwich, biscuit, toilet). It now reads them; earlier results are unaffected (only blocks were added).

## Summary

**Counts (109):** 43 pass, 11 pass-borderline (exactly 12, resting on a column from memory), 27 borderline (strict count fails, lenient count passes), 28 fail.

| Verdict | Candidates (adapted form) |
|---|---|
| pass (43) | chocolate *tokolatu*, television *telebisuyon*, coffee *kafe*, pajamas *pidama*, radio *ladiyo*, helicopter *elikoputelu*, tractor *tulakutalu*, penguin *penguwin*, tea *tayu*, cookie (biscuit) *bisukuwitu*, sandwich *sanduwitu*, pizza *pisa*, balcony *balukon*, circus *silukasu*, video *bideyo*, bank *banki*, program *pulogulamu*, computer *konpuyutalu*, hotel *otelu*, beer *biyalu*, code *kodu*, bomb *bonba*, captain *kaputan*, model *modelu*, virus *bilusu*, league *liga*, album *alubumu*, robot *lobotu*, mile *milu*, cigarette *sigaletu*, club *kulabu*, taxi *takusi*, gas *gasu*, chemistry *kimiya*, guitar *gitalu*, gene *denu*, plastic *pulasutiku*, bar *balu*, cinema *sinema*, passport *pasupolutu*, studio *sutudiyo*, profile *pulofilu*, piano *piyano* |
| pass, borderline (11) | giraffe *silafa*, motorcycle *moto*, sweater *suwetalu*, sofa *sofa*, sauce *sosu*, technology *tekunolodi*, machine *masina*, platform *pulatufolumu*, engineer *indiniyalu*, vaccine *bakusin*, mask *masuka* |
| borderline (27) | ice cream, doctor, lamp, tomato, garage, sugar, toast, T-shirt, office, energy, professor, project, website, democracy, design, station, restaurant, philosophy, channel, pound, campaign, pilot, cream, pope, physics, mosque, medal (forms in `loans.tsv`) |
| fail (28) | soup, banana, yogurt, park, pasta, zebra, shorts, party (political), soda, film, music, university, business, sport, president, data, ticket, budget, museum, alcohol, engine, metal, climate, fashion, version, fuel, tunnel, toilet |

**Patterns worth a decision rather than case by case:**

1. **One judgment decides most of the 27 borderlines: does a loan count when it lives beside a formal native word?** The lenient columns are mostly spoken English in South Asia (Tamil 10 borderlines, Hindi 6, Bengali 4: "spoken TV, doctor, office" beside tolaikkāṭci, maruttuvar, kāryālay), colloquial Arabic (5), a katakana/hangul loan beside a Sino word in ja/ko (5 each), and Quechua via Spanish (8). loans.md counted spoken Tamil *internet* but not spoken Tamil *photo*; this run marks all such cases lenient. The rest of the lenient columns are the shape question in pattern 3. Counting every lenient column passes all 27; counting none fails all 27. The strict column already follows a middle rule: the loan counts when Wiktionary lists it for the sense (M\* when not first-listed), or when Wiktionary has no entry and the loan is the clear everyday word.
2. **Half the passes rest on memory.** 27 of the 54 passes fail the rule if only Wiktionary-sourced columns count. The thinnest: profile (4 Wiktionary columns), platform (7), sweater and model (8). Hausa, Yoruba and Quechua are the usual memory columns. 9 of the 11 pass-borderlines need the assumed Spanish loan in Quechua to reach 12 (giraffe, motorcycle, sofa, technology, machine, platform, engineer, vaccine, mask). The Quechua rule from loans.md ("assume the Spanish loan when Wiktionary has nothing") effectively gives Spanish two votes on every Spanish-shared word.
3. **Two shapes of one etymon: same word or not?** I counted shapes together when the consonant skeleton survives (falsafa/filosofia, site [sait]/[sit], dizain/diseño, ʃimi/kimia, cha/chai/šāy) and apart when it doesn't (channel/kanal, masjid/mosque, qahwa/kafe, salsa/sos, pope/papa, engine/motor). channel, mosque and pope are borderline only because of this; coffee and sauce pass on either reading. A stated rule would settle it.
4. **Competing international forms split the panel.** ticket (10) vs billet (5); benzin (5–6) vs petrol (6) vs gasoline (4–5); engine (8) vs motor (5); fashion (6) vs moda (10); tea passes only as *cha* (14) against *te* (6). Where neither form reaches 12, L4 sends the word to rung 3 or 4 even though most of the panel does borrow something.
5. **Where it fails, the panel's own build is usually ready for rung 3:** "striped horse/donkey" for zebra (9 languages), "people-rule" for democracy (all of Asia but id tl), "food house" for restaurant, "short trousers" for shorts, "big school" for university, "film house" for cinema, "grilled bread" for toast, euphemisms ("hand-washing room", "water room") for toilet, "power" words for energy.
6. **East Asia is the usual missing region.** 10 passes lack EA (Sino 銀行, 機械, 化学, 爆弾…), and Sino forms cause most failures in science, institutions and abstract words (university, music, metal, climate, physics, philosophy, president, data, budget). South Asia does the same with Sanskrit coinages, but its spoken English loans mostly rescue it (pattern 1).
7. **Sense matters more than the word.** cream passes as the cosmetic (15 in Wiktionary's own table) but not as dairy cream (7 strict); alcohol fails as a drink but would likely pass as the chemical; hotel means "restaurant" in hi ta sw; machine means "car" in fa ru. Each loan should be fixed to the sense that passed.
8. **Median ties and long forms.** Ties (coffee e/i, tea tʃa/tʃaj, helicopter, video, computer, motorcycle, professor, tomato, project) need a rule; loans.md left them to the author. Clusters make some forms long: *pulatufolumu* (6 syllables), *konpuyutalu*, *bisukuwitu*, *elikoputelu*, *tulakutalu*; the C1 cost question loans.md raised for *kilometulu* applies here at larger scale.
9. **Collisions with existing words:** tea *tayu* = "agree", league *liga* = "phone" (loans.md already noted *liga*), gas *gasu* = "idea", lamp *lanpa* = "cloud" (borderline). Each needs a variant or a decision before adoption.
10. **Not a word question:** mile passes (18) but is outside the metric standard (L3); pound and pope are arguably names (the issuer's currency, a community's own title, loans.md pattern 2); pope's *papa* is also the baby word for "father", the open mama/papa question from loans.md.

## Per-candidate evidence

Legend: ✓ cognate with the international form, ✗ not. Romanisation is mine where Wiktionary gives none.

### ice cream (Wt: [ice cream](https://en.wiktionary.org/wiki/ice_cream#Translations), "dessert")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 冰淇淋 bīngqílín ("ice" + partial sound loan) | ✗ | Wt |
| Japanese | アイスクリーム aisukurīmu, アイス | ✓ | Wt |
| Korean | 아이스크림 aiseukeurim | ✓ | Wt |
| Vietnamese | kem (< French crème) | ✗ | Wt |
| Thai | ไอศกรีม aisakhriim, ไอติม | ✓ | Wt |
| Indonesian | es krim | ✓ | Wt |
| Tagalog | sorbetes (street ice cream); ayskrim also common | ✗ (✓ lenient) | Wt, M* |
| Hindi | आइसक्रीम āiskrīm | ✓ | Wt |
| Bengali | আইসক্রীম āiskrīm | ✓ | Wt |
| Tamil | ஐஸ் கிரீம் ais kirīm | ✓ | Wt |
| Persian | بستنی bastani (āys kerim exists) | ✗ | Wt |
| Arabic | بوظة būẓa (Levant), آيس كريم āys krīm (Egypt, Gulf) | ✗ (✓ lenient) | Wt, M* |
| Turkish | dondurma | ✗ | Wt |
| Russian | мороженое moroženoe | ✗ | Wt |
| Spanish | helado | ✗ | Wt |
| French | glace, crème glacée | ✗ | Wt |
| Swahili | aiskrimu | ✓ | Wt |
| Hausa | (no data; aiskirim likely) | ✗ (✓ lenient) | M |
| Yoruba | áísìkiriìmù | ✓ | Wt |
| Quechua | helado (Spanish loan) | ✗ | M |

**9/20 (12 lenient); regions 4 (no WA EU AM) (5 lenient) → borderline.** Median [aiskrim] → *ayisukulimu*.
The lenient count rests on three uncertain columns (Tagalog, Arabic dialects, Hausa); on Wiktionary's first-listed words alone the count is 9. Europe is the gap: helado, glace, moroženoe.

### soup (Wt: [soup](https://en.wiktionary.org/wiki/soup#Translations), "dish|stew")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 湯 tāng | ✗ | Wt |
| Japanese | スープ sūpu (Western soup; 汁 shiru for miso soup) | ✓ | Wt, M* |
| Korean | 국 guk (수프 for Western soup) | ✗ | Wt |
| Vietnamese | canh (súp for Western soup) | ✗ | Wt |
| Thai | ซุป súp | ✓ | Wt |
| Indonesian | sup, sop | ✓ | Wt |
| Tagalog | sabaw | ✗ | Wt |
| Hindi | सूप sūp, शोरबा šorbā | ✓ | Wt |
| Bengali | ঝোল jhol; স্যুপ syup for Western soup | ✗ (✓ lenient) | M* |
| Tamil | சூப் sūp | ✓ | Wt |
| Persian | سوپ sup (also āš, šurbā) | ✓ | Wt, M* |
| Arabic | شوربة šurba, حساء ḥasāʾ | ✗ | Wt |
| Turkish | çorba | ✗ | Wt |
| Russian | суп sup | ✓ | Wt |
| Spanish | sopa | ✓ | Wt |
| French | soupe, potage | ✓ | Wt |
| Swahili | supu | ✓ | Wt |
| Hausa | miya | ✗ | Wt |
| Yoruba | ọbẹ̀ | ✗ | M |
| Quechua | lawa | ✗ | Wt |

**10/20 (11 lenient); regions 6 (no AM) → fail.**
Two families compete: soup/sopa (10, 11 with Bengali) and the Persian–Arabic šorba (ar tr, plus doublets in fa hi). Neither reaches 12. Many languages keep a native word for their own soups and use the loan only for Western soup (ja ko vi bn).

### chocolate (Wt: [chocolate](https://en.wiktionary.org/wiki/chocolate#Translations), "food made from ground roasted cocoa beans")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 巧克力 qiǎokèlì | ✓ | Wt |
| Japanese | チョコレート chokorēto, チョコ | ✓ | Wt |
| Korean | 초콜릿 chokollit | ✓ | Wt |
| Vietnamese | sô-cô-la | ✓ | Wt |
| Thai | ช็อกโกแลต chɔ́kkoolɛ́ɛt | ✓ | Wt |
| Indonesian | cokelat, coklat | ✓ | Wt |
| Tagalog | tsokolate | ✓ | Wt |
| Hindi | चॉकलेट cŏkleṭ | ✓ | Wt |
| Bengali | চকলেট cɔkleṭ | ✓ | Wt |
| Tamil | சாக்கலேட் cākkalēṭ | ✓ | Wt |
| Persian | شکلات šokolāt | ✓ | Wt |
| Arabic | شوكولاتة šūkūlāta | ✓ | Wt |
| Turkish | çikolata | ✓ | Wt |
| Russian | шоколад šokolad | ✓ | Wt |
| Spanish | chocolate | ✓ | Wt |
| French | chocolat | ✓ | Wt |
| Swahili | chokoleti | ✓ | Wt |
| Hausa | cakulan | ✓ | M |
| Yoruba | ṣokoléètì | ✓ | M |
| Quechua | chocolate (Spanish loan) | ✓ | M |

**20/20; regions all 7 → pass.** Median [tʃokolat] → *tokolatu*.
Initial tʃ 14 against ʃ 6 (fa ar ru fr yo, vi s). Third vowel a (vi id tl fa ar tr ru es fr) over e (ja hi bn ta sw yo, th ɛ).

### doctor (Wt: [physician](https://en.wiktionary.org/wiki/physician#Translations), "medical doctor")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 医生 yīshēng | ✗ | Wt |
| Japanese | 医者 isha | ✗ | Wt |
| Korean | 의사 uisa | ✗ | Wt |
| Vietnamese | bác sĩ (đốc-tờ dated) | ✗ | Wt |
| Thai | หมอ mɔ̌ɔ, แพทย์ phɛ̂ɛt | ✗ | Wt |
| Indonesian | dokter | ✓ | Wt |
| Tagalog | doktor | ✓ | Wt |
| Hindi | डॉक्टर ḍŏkṭar | ✓ | Wt |
| Bengali | ডাক্তার ḍāktār | ✓ | Wt |
| Tamil | டாக்டர் ṭākṭar in speech (formal மருத்துவர் maruttuvar) | ✓ | Wt, M* |
| Persian | دکتر doktor in speech (formal پزشک pezešk) | ✓ | Wt, M* |
| Arabic | دكتور duktōr in all dialects (formal طبيب ṭabīb) | ✓ | Wt, M* |
| Turkish | doktor | ✓ | Wt |
| Russian | врач vrač; доктор doktor in address and colloquially | ✗ (✓ lenient) | Wt |
| Spanish | médico; doctor in address and much of Latin America | ✗ (✓ lenient) | Wt, M |
| French | médecin; docteur in address | ✗ (✓ lenient) | Wt |
| Swahili | daktari | ✓ | Wt |
| Hausa | likita | ✗ | M |
| Yoruba | dókítà | ✓ | M |
| Quechua | jampiq | ✗ | Wt |

**10/20 (13 lenient); regions 4 (no EA EU AM) (5 lenient) → borderline.** Median [doktor] → *dokutolu*.
The strict count rests on spoken Tamil, Persian and Arabic, where the formal word is native. Europe uses doktor/doctor/docteur as a title and colloquially, beside native vrač, médico, médecin; that is the lenient count. Median second vowel: o (tl fa ar tr, and the lenient ru es) against a (hi bn ta sw); [doktor].

### banana (Wt: [banana](https://en.wiktionary.org/wiki/banana#Translations), "fruit")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 香蕉 xiāngjiāo | ✗ | Wt |
| Japanese | バナナ banana | ✓ | Wt |
| Korean | 바나나 banana | ✓ | Wt |
| Vietnamese | chuối | ✗ | Wt |
| Thai | กล้วย klûay | ✗ | Wt |
| Indonesian | pisang | ✗ | Wt |
| Tagalog | saging | ✗ | Wt |
| Hindi | केला kelā | ✗ | Wt |
| Bengali | কলা kɔlā | ✗ | Wt |
| Tamil | வாழைப்பழம் vāḻaippaḻam | ✗ | Wt |
| Persian | موز mowz | ✗ | Wt |
| Arabic | موز mawz | ✗ | Wt |
| Turkish | muz | ✗ | Wt |
| Russian | банан banan | ✓ | Wt |
| Spanish | banana, plátano | ✓ | Wt |
| French | banane | ✓ | Wt |
| Swahili | ndizi | ✗ | Wt |
| Hausa | ayaba | ✗ | Wt |
| Yoruba | ọ̀gẹ̀dẹ̀ | ✗ | Wt |
| Quechua | latanu (< plátano) | ✗ | Wt |

**5/20; regions 2 (EA EU) → fail.**

### giraffe (Wt: [giraffe](https://en.wiktionary.org/wiki/giraffe#Translations), "mammal")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 长颈鹿 chángjǐnglù "long-neck deer" | ✗ | Wt |
| Japanese | キリン kirin | ✗ | Wt |
| Korean | 기린 girin | ✗ | Wt |
| Vietnamese | hươu cao cổ | ✗ | Wt |
| Thai | ยีราฟ yiiráap | ✓ | Wt |
| Indonesian | jerapah | ✓ | Wt |
| Tagalog | hirapa | ✓ | Wt |
| Hindi | जिराफ़ jirāf | ✓ | Wt |
| Bengali | জিরাফ jirāf | ✓ | M* |
| Tamil | ஒட்டகச்சிவிங்கி oṭṭakaccivingi | ✗ | Wt |
| Persian | زرافه zarrāfe | ✓ | Wt |
| Arabic | زرافة zarāfa | ✓ | Wt |
| Turkish | zürafa | ✓ | Wt |
| Russian | жираф žiraf | ✓ | Wt |
| Spanish | jirafa | ✓ | Wt |
| French | girafe | ✓ | Wt |
| Swahili | twiga | ✗ | Wt |
| Hausa | raƙumin dawa "bush camel" | ✗ | M |
| Yoruba | àgùnfọn | ✗ | Wt |
| Quechua | jirafa (Spanish loan) | ✓ | M |

**12/20; regions 5 (no EA SSA) → pass, borderline.** Median [ʒirafa] → *silafa*.
Exactly 12, and two of the twelve are soft (Bengali's Wiktionary form জরৈফ looks garbled, the usual spelling being জিরাফ; Quechua assumed). Initial consonant has no majority in IPA (dʒ 3, z 3, h/x 3, ʒ 2, j 1); the sibilants z/ʒ together are 5 and names.py maps all of them to s. Final vowel a (ar tr tl es qu, id before h) 6 against consonant-final 5.

### motorcycle (Wt: [motorcycle](https://en.wiktionary.org/wiki/motorcycle#Translations), "open-seated motor vehicle with handlebars instead of a steering wheel")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 摩托车 mótuōchē, 摩托 mótuō | ✓ | Wt |
| Japanese | バイク baiku, オートバイ ōtobai | ✗ | Wt |
| Korean | 오토바이 otobai | ✗ | Wt |
| Vietnamese | xe máy (mô tô formal) | ✗ | Wt |
| Thai | มอเตอร์ไซค์ mɔɔtəəsai, มอไซค์ | ✓ | Wt, M* |
| Indonesian | sepeda motor, motor | ✓ | Wt |
| Tagalog | motorsiklo, motor | ✓ | Wt |
| Hindi | मोटरसाइकिल moṭarsāikil | ✓ | Wt |
| Bengali | মোটরসাইকেল moṭarsāikel | ✓ | Wt |
| Tamil | விசையுந்து visaiyundu (formal); spoken moṭṭār saikkiḷ, bike | ✗ (✓ lenient) | Wt, M* |
| Persian | موتور motor, موتورسیکلت motorsiklet | ✓ | Wt |
| Arabic | دراجة نارية darrāja nāriyya; spoken mōtōsīkl | ✗ (✓ lenient) | Wt, M* |
| Turkish | motosiklet | ✓ | Wt |
| Russian | мотоцикл mototsikl | ✓ | Wt |
| Spanish | moto, motocicleta | ✓ | Wt |
| French | moto | ✓ | Wt |
| Swahili | pikipiki | ✗ | Wt |
| Hausa | babur | ✗ | Wt |
| Yoruba | ọ̀kadà, alùpùpù | ✗ | Wt |
| Quechua | moto (Spanish loan) | ✓ | M |

**12/20 (14 lenient); regions 6 (no SSA) → pass, borderline.** Median [moto] → *moto*.
The shared element is moto(r)-; Japanese and Korean ōtobai shares "auto", not "moto", so it is ✗. Mandarin mótuō is a sound loan used alone ("骑摩托"), so it counts. The r after moto is kept in 5 of 12 forms (id tl hi bn fa), so [moto]; after that 6 forms continue with -saikil/-siklet/-tsikl and 6 stop, a tie; I took the shorter. The long form would be [motosaikil].

### television (Wt: [television](https://en.wiktionary.org/wiki/television#Translations), "device for receiving television signals|television set|idiot box")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 电视(机) diànshì(jī) | ✗ | Wt |
| Japanese | テレビ terebi | ✓ | Wt |
| Korean | 텔레비전 tellebijeon, 티비 tibi | ✓ | Wt |
| Vietnamese | ti-vi, TV (máy thu hình formal) | ✓ | Wt, M* |
| Thai | โทรทัศน์ thoorathát; spoken ทีวี thiiwii very common | ✗ (✓ lenient) | Wt, M* |
| Indonesian | televisi, TV | ✓ | Wt |
| Tagalog | telebisyon, TV | ✓ | Wt |
| Hindi | टीवी ṭīvī, टेलीविज़न (formal दूरदर्शन dūrdarśan) | ✓ | Wt, M* |
| Bengali | টেলিভিশন ṭelibhiśan | ✓ | Wt |
| Tamil | தொலைக்காட்சி tolaikkāṭci; spoken TV | ✗ (✓ lenient) | Wt, M* |
| Persian | تلویزیون televizyon | ✓ | Wt |
| Arabic | تلفزيون tilifizyōn, تلفاز tilfāz | ✓ | Wt |
| Turkish | televizyon | ✓ | Wt |
| Russian | телевизор televizor | ✓ | Wt |
| Spanish | televisión, tele | ✓ | Wt |
| French | télévision, télé | ✓ | Wt |
| Swahili | televisheni (runinga coinage) | ✓ | Wt, M* |
| Hausa | talabijin | ✓ | M |
| Yoruba | tẹlifíṣọ̀n | ✓ | Wt |
| Quechua | televisión (Spanish loan) | ✓ | M |

**17/20 (19 lenient); regions all 7 → pass.** Median [televizjon] → *telebisuyon*.
The abbreviation TV/tivi is counted as the same word: it is the international form's own abbreviation, not a translation. Median of the full forms [televizjon]; the panel's everyday short forms (ja terebi, es/fr tele, hi/vi/th/ta TV) would give a shorter word if the author prefers one.

### coffee (Wt: [coffee](https://en.wiktionary.org/wiki/coffee#Translations), "beverage")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 咖啡 kāfēi | ✓ | Wt |
| Japanese | コーヒー kōhī | ✓ | Wt |
| Korean | 커피 keopi | ✓ | Wt |
| Vietnamese | cà phê | ✓ | Wt |
| Thai | กาแฟ kaafɛɛ | ✓ | Wt |
| Indonesian | kopi | ✓ | Wt |
| Tagalog | kape | ✓ | Wt |
| Hindi | कॉफ़ी kŏfī | ✓ | Wt |
| Bengali | কফি kɔphi | ✓ | Wt |
| Tamil | காபி kāpi | ✓ | Wt |
| Persian | قهوه qahve | ✗ (✓ lenient) | Wt |
| Arabic | قهوة qahwa | ✗ (✓ lenient) | Wt |
| Turkish | kahve | ✗ (✓ lenient) | Wt |
| Russian | кофе kofe | ✓ | Wt |
| Spanish | café | ✓ | Wt |
| French | café | ✓ | Wt |
| Swahili | kahawa | ✗ (✓ lenient) | Wt |
| Hausa | kofi | ✓ | Wt |
| Yoruba | kọfí | ✓ | Wt |
| Quechua | kaphiy, café | ✓ | Wt |

**16/20 (20 lenient); regions 6 (no WA) (7 lenient) → pass.** Median [kafe] → *kafe*.
The qahwa/kahve/kahawa family is the source of "coffee", but k-h-w against k-f is a distant link, so it counts only leniently. First vowel a 8 against o 7; second vowel e (zh vi th tl ru es fr qu) 8 against i (ja ko id hi bn ta ha yo) 8, a tie: [kafe] → *kafe* or [kafi] → *kafi*. The lenient forms (qahve, qahwa, kahve, kahawa) all side with the vowel e/a, not i.

### sweater (Wt: [sweater](https://en.wiktionary.org/wiki/sweater#Translations), "similar garment worn for warmth")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 毛衣 máoyī | ✗ | Wt |
| Japanese | セーター sētā | ✓ | Wt |
| Korean | 스웨터 seuweteo | ✓ | Wt |
| Vietnamese | áo len | ✗ | Wt |
| Thai | เสื้อกันหนาว sʉ̂a kan nǎaw | ✗ | M |
| Indonesian | switer | ✓ | Wt |
| Tagalog | sweter | ✓ | M |
| Hindi | स्वेटर sveṭar | ✓ | Wt |
| Bengali | সোয়েটার soeṭār | ✓ | Wt |
| Tamil | ஸ்வெட்டர் sveṭṭar | ✓ | M |
| Persian | ژاکت žāket, پلیور poliver | ✗ | Wt |
| Arabic | سويتر swītar (Wt); also بلوفر | ✓ | Wt |
| Turkish | kazak (süveter less common) | ✗ (✓ lenient) | Wt, M* |
| Russian | свитер sviter | ✓ | Wt |
| Spanish | suéter (Mexico, Central America); jersey, buzo, chompa elsewhere | ✗ (✓ lenient) | Wt, M |
| French | pull | ✗ | Wt |
| Swahili | sweta | ✓ | Wt |
| Hausa | suwaita | ✓ | M |
| Yoruba | súwẹ́tà | ✓ | M |
| Quechua | chompa (Peru Spanish) | ✗ | M |

**12/20 (14 lenient); regions 6 (no AM) → pass, borderline.** Median [swetar] → *suwetalu*.
Exactly 12, with four columns from memory (tl ta ha yo). Spanish splits by country (suéter, jersey, buzo, chompa), so it counts only leniently. Median: first vowel e over i, second a, final r in 7 of 12 (id tl hi bn ta ar ru).

### pajamas (Wt: [pajamas](https://en.wiktionary.org/wiki/pajamas#Translations), "clothes for wearing to bed and sleeping in")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 睡衣 shuìyī | ✗ | Wt |
| Japanese | パジャマ pajama | ✓ | Wt |
| Korean | 잠옷 jamot; 파자마 pajama also | ✗ (✓ lenient) | Wt, M* |
| Vietnamese | đồ ngủ; pijama also | ✗ (✓ lenient) | Wt |
| Thai | ชุดนอน chút nɔɔn | ✗ | Wt |
| Indonesian | piyama | ✓ | Wt |
| Tagalog | padyama, pandiyama | ✓ | Wt |
| Hindi | पाजामा pājāmā | ✓ | Wt |
| Bengali | পায়জামা pāyjāmā | ✓ | Wt |
| Tamil | பைஜாமா paijāmā | ✓ | M |
| Persian | پیژامه pižāme | ✓ | Wt |
| Arabic | بيجاما bījāma (formal منامة manāma) | ✓ | Wt, M* |
| Turkish | pijama | ✓ | Wt |
| Russian | пижама pižama | ✓ | Wt |
| Spanish | pijama | ✓ | Wt |
| French | pyjama | ✓ | Wt |
| Swahili | (no data; pajama likely) | ✗ (✓ lenient) | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | pijama (Spanish loan) | ✓ | M |

**13/20 (16 lenient); regions 6 (no SSA) (7 lenient) → pass.** Median [pidʒama] → *pidama*.
First vowel i (id fa ar tr ru es fr qu) 8 against a (ja tl hi bn ta) 5. Middle consonant dʒ (ja tl hi bn ta ar) 6, ʒ (fa tr ru fr) 4, x (es qu) 2, j (id) 1.

### radio (Wt: [radio](https://en.wiktionary.org/wiki/radio#Translations), "receiver|radioreceptor")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 收音机 shōuyīnjī | ✗ | Wt |
| Japanese | ラジオ rajio | ✓ | Wt |
| Korean | 라디오 radio | ✓ | Wt |
| Vietnamese | ra-đi-ô | ✓ | Wt |
| Thai | วิทยุ witthayú | ✗ | M |
| Indonesian | radio | ✓ | Wt |
| Tagalog | radyo | ✓ | Wt |
| Hindi | रेडियो reḍiyo | ✓ | Wt |
| Bengali | রেডিও reḍio | ✓ | M |
| Tamil | வானொலி vāṉoli; spoken "radio" | ✗ (✓ lenient) | Wt, M |
| Persian | رادیو rādiyo | ✓ | Wt |
| Arabic | راديو rādyū (formal مذياع miḏyāʿ) | ✓ | Wt |
| Turkish | radyo | ✓ | Wt |
| Russian | радио radio | ✓ | Wt |
| Spanish | radio | ✓ | Wt |
| French | radio | ✓ | Wt |
| Swahili | redio | ✓ | Wt |
| Hausa | rediyo | ✓ | Wt |
| Yoruba | rédíò | ✓ | M |
| Quechua | radio (Spanish loan) | ✓ | M |

**17/20 (18 lenient); regions all 7 → pass.** Median [radio] → *ladiyo*.
First vowel a (ja ko vi id tl fa ar tr ru es fr qu) against e (hi bn sw ha yo).

### helicopter (Wt: [helicopter](https://en.wiktionary.org/wiki/helicopter#Translations), "aircraft")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 直升机 zhíshēngjī | ✗ | Wt |
| Japanese | ヘリコプター herikoputā, ヘリ | ✓ | Wt |
| Korean | 헬리콥터 hellikopteo, 헬기 | ✓ | Wt |
| Vietnamese | trực thăng | ✗ | Wt |
| Thai | เฮลิคอปเตอร์ helikhɔ́ptəə | ✓ | Wt |
| Indonesian | helikopter | ✓ | Wt |
| Tagalog | helikopter | ✓ | Wt |
| Hindi | हेलिकॉप्टर helikŏpṭar | ✓ | Wt |
| Bengali | হেলিকপ্টার helikɔpṭār | ✓ | Wt |
| Tamil | உலங்கு வானூர்தி ulangu vāṉūrti (coinage); spoken helicopter | ✗ (✓ lenient) | Wt, M |
| Persian | هلی‌کوپتر helikopter (official بالگرد bālgard) | ✓ | Wt |
| Arabic | مروحية marwaḥiyya; هليكوبتر helikobtar also | ✗ (✓ lenient) | Wt |
| Turkish | helikopter | ✓ | Wt |
| Russian | вертолёт vertolët | ✗ | Wt |
| Spanish | helicóptero | ✓ | Wt |
| French | hélicoptère | ✓ | Wt |
| Swahili | helikopta | ✓ | Wt |
| Hausa | jirgi mai saukar ungulu | ✗ | M |
| Yoruba | (no data; hẹlikópítà likely) | ✗ (✓ lenient) | M |
| Quechua | pillwinkumpa (Wt); helicóptero in bilingual speech | ✗ (✓ lenient) | Wt, M |

**12/20 (16 lenient); regions 6 (no AM) (7 lenient) → pass.** Median [helikopter] → *elikoputelu*.
Second-to-last vowel ties: e (id tl fa tr es fr) 6 against a/ə (ja ko th hi bn sw) 6; [helikoptar] would give *elikoputalu*. names.py drops h, as for every name.

### tractor (Wt: [tractor](https://en.wiktionary.org/wiki/tractor#Translations), "farm vehicle")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 拖拉机 tuōlājī (sound-and-meaning loan, "drag-pull machine") | ✗ (✓ lenient) | Wt |
| Japanese | トラクター torakutā | ✓ | Wt |
| Korean | 트랙터 teuraekteo | ✓ | Wt |
| Vietnamese | máy kéo "pulling machine" | ✗ | Wt |
| Thai | แทรกเตอร์ thrɛ́ktəə | ✓ | Wt |
| Indonesian | traktor | ✓ | Wt |
| Tagalog | guyod (Wt); traktora | ✗ (✓ lenient) | Wt, M |
| Hindi | ट्रैक्टर ṭraikṭar | ✓ | Wt |
| Bengali | ট্র্যাক্টর ṭryākṭar | ✓ | Wt |
| Tamil | டிராக்டர் ṭirākṭar | ✓ | M |
| Persian | تراکتور terāktor | ✓ | Wt |
| Arabic | جرار jarrār; تراكتور tarāktūr | ✗ (✓ lenient) | Wt |
| Turkish | traktör | ✓ | Wt |
| Russian | трактор traktor | ✓ | Wt |
| Spanish | tractor | ✓ | Wt |
| French | tracteur | ✓ | Wt |
| Swahili | trekta | ✓ | Wt |
| Hausa | tarakta | ✓ | M |
| Yoruba | katakata | ✗ | Wt |
| Quechua | tractor (Spanish loan) | ✓ | M |

**15/20 (18 lenient); regions all 7 → pass.** Median [traktar] → *tulakutalu*.
Second vowel a/ə (ja ko th hi bn ta sw ha) 8 against o (id fa ru es qu) 5, with tr ø and fr œ apart; final r in 10 of 15.

### yogurt (Wt: [yogurt](https://en.wiktionary.org/wiki/yogurt#Translations), "a milk-based product thickened by a bacterium-aided curdling process|yoghurt|yogourt|yoghourt")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 酸奶 suānnǎi | ✗ | Wt |
| Japanese | ヨーグルト yōguruto | ✓ | Wt |
| Korean | 요구르트 yogureuteu, 요거트 | ✓ | Wt |
| Vietnamese | sữa chua (north); da ua (south, < French yaourt) | ✗ (✓ lenient) | Wt |
| Thai | โยเกิร์ต yookə̀ət | ✓ | Wt |
| Indonesian | yoghurt | ✓ | Wt |
| Tagalog | yogart | ✓ | Wt |
| Hindi | दही dahī | ✗ | Wt |
| Bengali | দই dôi | ✗ | Wt |
| Tamil | தயிர் tayir | ✗ | Wt |
| Persian | ماست māst | ✗ | Wt |
| Arabic | لبن laban, زبادي zabādī | ✗ | Wt |
| Turkish | yoğurt | ✓ | Wt |
| Russian | йогурт jogurt | ✓ | Wt |
| Spanish | yogur | ✓ | Wt |
| French | yaourt | ✓ | Wt |
| Swahili | maziwa ya mgando "curdled milk" | ✗ | Wt |
| Hausa | kindirmo | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | yugur | ✓ | Wt |

**10/20 (11 lenient); regions 5 (no SA SSA) → fail.**

### sofa (Wt: [sofa](https://en.wiktionary.org/wiki/sofa#Translations), "upholstered seat")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 沙发 shāfā | ✓ | Wt |
| Japanese | ソファー sofā | ✓ | Wt |
| Korean | 소파 sopa | ✓ | Wt |
| Vietnamese | xô-pha | ✓ | Wt |
| Thai | โซฟา soofaa | ✓ | Wt |
| Indonesian | sofa | ✓ | Wt |
| Tagalog | sopa | ✓ | Wt |
| Hindi | सोफ़ा sofā | ✓ | Wt |
| Bengali | সোফা sofā | ✓ | Wt |
| Tamil | சோபா sōpā | ✓ | M |
| Persian | مبل mobl, کاناپه kānāpe | ✗ | Wt, M |
| Arabic | كنبة kanaba, أريكة arīka | ✗ | Wt |
| Turkish | kanepe | ✗ | Wt |
| Russian | диван divan (софа a type) | ✗ | Wt |
| Spanish | sofá | ✓ | Wt |
| French | canapé (sofa less common) | ✗ (✓ lenient) | Wt |
| Swahili | (no data; sofa, kochi in speech) | ✗ (✓ lenient) | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | sofá (Spanish loan) | ✓ | M |

**12/20 (14 lenient); regions 5 (no WA SSA) (6 lenient) → pass, borderline.** Median [sofa] → *sofa*.
Asia is solid; West Asia and France use the kanape/canapé family instead (4 languages in 2 regions, so it does not compete). Median [sofa] unambiguous.

### park (Wt: [park](https://en.wiktionary.org/wiki/park#Translations), "ground for recreation")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 公园 gōngyuán | ✗ | Wt |
| Japanese | 公園 kōen | ✗ | Wt |
| Korean | 공원 gongwon | ✗ | Wt |
| Vietnamese | công viên | ✗ | Wt |
| Thai | สวน(สาธารณะ) sǔan | ✗ | Wt |
| Indonesian | taman | ✗ | Wt |
| Tagalog | parke | ✓ | Wt |
| Hindi | उद्यान udyān (formal); spoken पार्क pārk | ✗ (✓ lenient) | Wt, M |
| Bengali | পার্ক pārk | ✓ | Wt |
| Tamil | பூங்கா pūngā; spoken "park" | ✗ (✓ lenient) | Wt, M |
| Persian | پارک pārk | ✓ | Wt |
| Arabic | حديقة ḥadīqa | ✗ | Wt |
| Turkish | park | ✓ | Wt |
| Russian | парк park | ✓ | Wt |
| Spanish | parque | ✓ | Wt |
| French | parc | ✓ | Wt |
| Swahili | bustani (mbuga = game park) | ✗ | Wt, M |
| Hausa | wurin shaƙatawa | ✗ | M |
| Yoruba | ọgbà | ✗ | M |
| Quechua | parque (Spanish loan) | ✓ | M |

**8/20 (10 lenient); regions 5 (no EA SSA) → fail.**

### pasta (Wt: [pasta](https://en.wiktionary.org/wiki/pasta#Translations), "dough")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 意大利面 yìdàlì miàn "Italian noodles" | ✗ | Wt |
| Japanese | パスタ pasuta | ✓ | Wt |
| Korean | 파스타 paseuta | ✓ | Wt |
| Vietnamese | mì ống | ✗ | Wt |
| Thai | พาสตา phaastaa | ✓ | Wt |
| Indonesian | pasta | ✓ | Wt |
| Tagalog | pasta | ✓ | Wt |
| Hindi | पास्ता pāstā | ✓ | Wt |
| Bengali | পাস্তা pāstā | ✓ | Wt |
| Tamil | மாச்சேவை māccēvai (coinage); spoken "pasta" | ✗ (✓ lenient) | Wt, M |
| Persian | پاستا pāstā | ✓ | Wt |
| Arabic | مكرونة makarōna | ✗ | Wt |
| Turkish | makarna | ✗ | Wt |
| Russian | макароны makarony | ✗ | Wt |
| Spanish | pasta | ✓ | Wt |
| French | pâtes | ✗ (✓ lenient) | Wt |
| Swahili | makaroni, tambi | ✗ | M |
| Hausa | taliya | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | fideos (Spanish loan) | ✗ | M |

**9/20 (11 lenient); regions 5 (no SSA AM) → fail.**
The makaroni family (ar tr ru sw) is the everyday word where pasta is old; pasta is the newer, more specific word. French pâtes is the same etymon but [pat] is hard to hear as pasta.

### lamp (Wt: [lamp](https://en.wiktionary.org/wiki/lamp#Translations), "device producing light")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 灯 dēng | ✗ | Wt |
| Japanese | ランプ ranpu (oil or indicator lamp; desk lamp スタンド, ライト) | ✗ (✓ lenient) | Wt, M* |
| Korean | 램프 raempeu; 스탠드, 전등 | ✗ (✓ lenient) | Wt, M* |
| Vietnamese | đèn | ✗ | Wt |
| Thai | โคมไฟ khoom fai | ✗ | Wt |
| Indonesian | lampu | ✓ | Wt |
| Tagalog | lampara | ✓ | Wt |
| Hindi | लैंप laimp (also चिराग़ cirāġ, दीया) | ✓ | Wt, M* |
| Bengali | বাতি bāti; ল্যাম্প lyāmp | ✗ (✓ lenient) | M |
| Tamil | விளக்கு viḷakku | ✗ | M |
| Persian | لامپ lāmp, چراغ čerāġ | ✓ | Wt |
| Arabic | مصباح miṣbāḥ; لمبة lamba (bulb) | ✗ (✓ lenient) | Wt |
| Turkish | lamba | ✓ | Wt |
| Russian | лампа lampa | ✓ | Wt |
| Spanish | lámpara | ✓ | Wt |
| French | lampe | ✓ | Wt |
| Swahili | taa | ✗ | Wt |
| Hausa | fitila | ✗ | Wt |
| Yoruba | àtùpà | ✗ | M |
| Quechua | lámpara (Spanish loan) | ✓ | M |

**9/20 (13 lenient); regions 5 (no EA SSA) (6 lenient) → borderline.** Median [lampa] → *lanpa*.
Several languages have the loan but for a narrower thing (ja ranpu oil lamp, ar lamba bulb) beside a native general word for "light, lamp" (zh dēng, vi đèn, sw taa, ta viḷakku). Median from all 13 cognates: after lamp-, a final a (tr ru ar es tl qu) 6 against none 4; then -ra (es tl qu) 3 against end 3, so [lampa].

### penguin (Wt: [penguin](https://en.wiktionary.org/wiki/penguin#Translations), "flightless sea bird")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 企鹅 qǐ'é | ✗ | Wt |
| Japanese | ペンギン pengin | ✓ | Wt |
| Korean | 펭귄 penggwin | ✓ | Wt |
| Vietnamese | chim cánh cụt "stub-winged bird" | ✗ | Wt |
| Thai | เพนกวิน phenkwin | ✓ | Wt |
| Indonesian | pinguin, penguin (purist angsa gempal) | ✓ | Wt, M* |
| Tagalog | pingguwino | ✓ | Wt |
| Hindi | पेंगुइन penguin | ✓ | Wt |
| Bengali | পেঙ্গুইন penguin | ✓ | Wt |
| Tamil | பென்குயின் penkuyin | ✓ | Wt |
| Persian | پنگوئن panguan | ✓ | Wt |
| Arabic | بطريق biṭrīq | ✗ | Wt |
| Turkish | penguen | ✓ | Wt |
| Russian | пингвин pingvin | ✓ | Wt |
| Spanish | pingüino | ✓ | Wt |
| French | manchot (pingouin "auk", popularly also penguin) | ✗ (✓ lenient) | Wt |
| Swahili | pengwini | ✓ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | pẹ́ńgúìnì | ✓ | Wt |
| Quechua | pingüino (Spanish loan) | ✓ | M |

**15/20 (16 lenient); regions all 7 → pass.** Median [peŋgwin] → *penguwin*.
First vowel e 10 against i 5. Glide w (ko th ru es sw tl qu) and vowel u (id hi bn ta fa tr yo) tie at 7, but both adapt to *penguwin*.

### tomato (Wt: [tomato](https://en.wiktionary.org/wiki/tomato#Translations), "fruit")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 西红柿 xīhóngshì, 番茄 fānqié | ✗ | Wt |
| Japanese | トマト tomato | ✓ | Wt |
| Korean | 토마토 tomato | ✓ | Wt |
| Vietnamese | cà chua | ✗ | Wt |
| Thai | มะเขือเทศ mákhʉ̌a thêet | ✗ | Wt |
| Indonesian | tomat | ✓ | Wt |
| Tagalog | kamatis | ✗ | Wt |
| Hindi | टमाटर ṭamāṭar | ✓ | Wt |
| Bengali | টমেটো ṭomeṭo (older বিলাতী বেগুন) | ✓ | Wt, M* |
| Tamil | தக்காளி takkāḷi | ✗ | Wt |
| Persian | گوجه(فرنگی) gowje(farangi) | ✗ | Wt |
| Arabic | طماطم ṭamāṭim (Egypt, Gulf); بندورة banadūra (Levant) | ✓ | Wt |
| Turkish | domates | ✓ | Wt |
| Russian | помидор pomidor (томат formal) | ✗ | Wt |
| Spanish | tomate, jitomate | ✓ | Wt |
| French | tomate | ✓ | Wt |
| Swahili | nyanya | ✗ | Wt |
| Hausa | tumatir | ✓ | M |
| Yoruba | tòmátì | ✓ | Wt |
| Quechua | chilltu (Wt); tomate in bilingual speech | ✗ (✓ lenient) | Wt, M |

**11/20 (12 lenient); regions 6 (no AM) (7 lenient) → borderline.** Median [tomate] → *tomate*.
The Italian pomodoro family (ru pomidor, Levantine banadūra, tr dialect pamidor) is a second, smaller family. Median: [tomat] then a final vowel in 10 of 12 forms, tied three ways: o (ja ko bn), e (es qu, tr domates), i (ar ha yo). [tomate] → *tomate*; [tomato] → *tomato*.

### zebra (Wt: [zebra](https://en.wiktionary.org/wiki/zebra#Translations), "African animal")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 斑马 bānmǎ "striped horse" | ✗ | Wt |
| Japanese | シマウマ shimauma "striped horse" | ✗ | Wt |
| Korean | 얼룩말 eollungmal "spotted horse" | ✗ | Wt |
| Vietnamese | ngựa vằn "striped horse" | ✗ | Wt |
| Thai | ม้าลาย máa laai "striped horse" | ✗ | Wt |
| Indonesian | zebra | ✓ | Wt |
| Tagalog | sebra | ✓ | Wt |
| Hindi | ज़ेब्रा zebrā | ✓ | Wt |
| Bengali | জেব্রা jebrā | ✓ | Wt |
| Tamil | வரிக்குதிரை varikkudirai "striped horse" | ✗ | Wt |
| Persian | گورخر gurxar "wild ass" (زبرا zebrā rare) | ✗ (✓ lenient) | Wt |
| Arabic | حمار وحشي ḥimār waḥšī "wild ass" | ✗ | Wt |
| Turkish | zebra | ✓ | Wt |
| Russian | зебра zebra | ✓ | Wt |
| Spanish | cebra | ✓ | Wt |
| French | zèbre | ✓ | Wt |
| Swahili | punda milia "striped donkey" | ✗ | Wt |
| Hausa | jakin dawa "bush donkey" | ✗ | M |
| Yoruba | kẹ́tẹ́kẹ́tẹ́ abilà "striped donkey" | ✗ | Wt |
| Quechua | siwra (< cebra) | ✓ | Wt |

**9/20 (10 lenient); regions 5 (no EA SSA) → fail.**
The majority builds the word as "striped horse" or "striped/wild donkey" (9 languages, 5 regions), which is a ready rung-3 compound.

### tea (Wt: [tea](https://en.wiktionary.org/wiki/tea#Translations), "drink made from leaves of tea plant")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 茶 chá | ✓ | Wt |
| Japanese | お茶 o-cha, 紅茶 kōcha | ✓ | Wt |
| Korean | 차 cha | ✓ | Wt |
| Vietnamese | trà, chè | ✓ | Wt |
| Thai | ชา chaa | ✓ | Wt |
| Indonesian | teh | ✗ | Wt |
| Tagalog | tsaa | ✓ | Wt |
| Hindi | चाय cāy | ✓ | Wt |
| Bengali | চা cā | ✓ | Wt |
| Tamil | தேநீர் tēnīr, டீ ṭī | ✗ | Wt |
| Persian | چای čāy | ✓ | Wt |
| Arabic | شاي šāy | ✓ | Wt |
| Turkish | çay | ✓ | Wt |
| Russian | чай čaj | ✓ | Wt |
| Spanish | té | ✗ | Wt |
| French | thé | ✗ | Wt |
| Swahili | chai | ✓ | Wt |
| Hausa | shayi (ti also) | ✓ | Wt |
| Yoruba | tíì | ✗ | Wt |
| Quechua | tiy | ✗ | Wt |

**14/20; regions 6 (no AM) → pass.** Median [tʃaj] → *tayu*.
Shared column = the cha family (chá, chai, čaj, šāy). The te family (teh, tēnīr/ṭī, té, thé, tíì, tiy) has 6 in 5 regions, so the panel decides for cha. Median: tʃ 12 against ʃ 2 (ar ha); final j (hi fa ar tr ru sw ha) 7 against none (zh ja ko vi th tl bn) 7, a tie. [tʃa] gives *tawu* (names.py lengthens one-syllable forms); [tʃaj] gives *tayu*.

### garage (Wt: [garage](https://en.wiktionary.org/wiki/garage#Translations), "building or section of building to store a car, tools etc.")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 车库 chēkù | ✗ | Wt |
| Japanese | 車庫 shako; ガレージ garēji for a house garage | ✗ (✓ lenient) | Wt, M* |
| Korean | 차고 chago | ✗ | Wt |
| Vietnamese | nhà để xe; ga-ra (repair garage) | ✗ (✓ lenient) | Wt |
| Thai | โรงรถ roong rót | ✗ | Wt |
| Indonesian | garasi | ✓ | Wt |
| Tagalog | garahe | ✓ | Wt |
| Hindi | गेराज gerāj | ✓ | Wt |
| Bengali | গ্যারেজ gyārej | ✓ | Wt |
| Tamil | (no Wt; spoken கேரேஜ் kērēj) | ✗ (✓ lenient) | M |
| Persian | گاراژ gārāž | ✓ | Wt |
| Arabic | مرآب mirʾāb; colloquial garāž | ✗ (✓ lenient) | Wt, M |
| Turkish | garaj | ✓ | Wt |
| Russian | гараж garaž | ✓ | Wt |
| Spanish | garaje, cochera | ✓ | Wt |
| French | garage | ✓ | Wt |
| Swahili | gereji | ✓ | M |
| Hausa | (no data; gareji likely) | ✗ (✓ lenient) | M |
| Yoruba | (no data; gáréèjì likely) | ✗ (✓ lenient) | M |
| Quechua | awtu jallch'ana wasi (Wt); garaje in bilingual speech | ✗ (✓ lenient) | Wt, M |

**10/20 (17 lenient); regions 5 (no EA AM) (7 lenient) → borderline.** Median [garaʒ] → *galasu*.
The widest gap between counts in this set: most of the lenient columns are a loan that exists beside a native word (ja shako/garēji, ar mirʾāb/garāž) or an unattested Africa/Quechua column. Median: final ʒ (fa ar tr ru fr) 5 against dʒ (ja hi bn sw) 4.

### cookie (Wt: [biscuit](https://en.wiktionary.org/wiki/biscuit#Translations), "small, flat baked good|cookie|cracker")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 饼干 bǐnggān (曲奇 qūqí for cookies) | ✗ | Wt |
| Japanese | ビスケット bisuketto, クッキー kukkī | ✓ | Wt |
| Korean | 쿠키 kuki, 비스킷 biseukit | ✗ (✓ lenient) | Wt |
| Vietnamese | bánh quy (< bích quy < French biscuit) | ✗ (✓ lenient) | Wt |
| Thai | บิสกิต bìtsakìt, คุกกี้ khúkkîi | ✓ | Wt |
| Indonesian | biskuit | ✓ | Wt |
| Tagalog | biskwit | ✓ | Wt |
| Hindi | बिस्कुट biskuṭ | ✓ | Wt |
| Bengali | বিস্কুট biskuṭ | ✓ | Wt |
| Tamil | பிஸ்கட் biskaṭ | ✓ | Wt |
| Persian | بیسکوئیت biskuit | ✓ | Wt |
| Arabic | بسكويت baskawīt | ✓ | Wt |
| Turkish | bisküvi | ✓ | Wt |
| Russian | печенье pečen'e | ✗ | Wt |
| Spanish | galleta | ✗ | Wt |
| French | biscuit | ✓ | Wt |
| Swahili | biskuti | ✓ | Wt |
| Hausa | biskit, fanke | ✓ | Wt (cookie) |
| Yoruba | bisikíìtì | ✓ | M |
| Quechua | galleta (Spanish loan) | ✗ | M |

**14/20 (16 lenient); regions 6 (no AM) → pass.** Median [biskwit] → *bisukuwitu*.
Tested as "biscuit", per the ladder note; the American "cookie" form is a minority. The adapted form is long (5 syllables) because of the sk and kw clusters; [biskit] (ja th ta ha yo vowels) would give *bisukitu*.

### shorts (Wt: [shorts](https://en.wiktionary.org/wiki/shorts#Translations), "leg garment|hot pants")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 短裤 duǎnkù | ✗ | Wt |
| Japanese | ショートパンツ shōto pantsu, ショーツ | ✓ | Wt |
| Korean | 반바지 banbaji | ✗ | Wt |
| Vietnamese | quần soóc, quần đùi | ✓ | Wt |
| Thai | กางเกงขาสั้น kaangkeeng khǎa sân "short-leg trousers" | ✗ | Wt |
| Indonesian | celana pendek "short trousers" | ✗ | Wt |
| Tagalog | salawal (Wt); shorts in everyday speech | ✗ (✓ lenient) | Wt, M |
| Hindi | शॉर्ट्स śŏrṭs, हाफ़ पैंट | ✓ | Wt |
| Bengali | শর্টস śôrṭs | ✓ | Wt |
| Tamil | டிராயர் ṭirāyar "drawers" | ✗ | Wt |
| Persian | شلوارک šalvārak | ✗ | Wt |
| Arabic | شورت šōrt | ✓ | Wt |
| Turkish | şort | ✓ | Wt |
| Russian | шорты šorty | ✓ | Wt |
| Spanish | pantalón corto; short in much of Latin America | ✗ (✓ lenient) | Wt |
| French | short | ✓ | Wt |
| Swahili | kaptula | ✗ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | (Spanish pantalón corto) | ✗ | M |

**8/20 (10 lenient); regions 5 (no SSA AM) → fail.**

### party (political) (Wt: [political party](https://en.wiktionary.org/wiki/political_party#Translations), "political organization")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 党 dǎng, 政党 | ✗ | Wt |
| Japanese | 政党 seitō | ✗ | Wt |
| Korean | 정당 jeongdang | ✗ | Wt |
| Vietnamese | đảng | ✗ | Wt |
| Thai | พรรค phák | ✗ | Wt |
| Indonesian | partai | ✓ | Wt |
| Tagalog | partido | ✓ | Wt |
| Hindi | पार्टी pārṭī, दल dal | ✓ | Wt |
| Bengali | পার্টি pārṭi, দল dôl | ✓ | Wt |
| Tamil | கட்சி kaṭci | ✗ | Wt |
| Persian | حزب hezb | ✗ | Wt |
| Arabic | حزب ḥizb | ✗ | Wt |
| Turkish | parti | ✓ | Wt |
| Russian | партия partija | ✓ | Wt |
| Spanish | partido | ✓ | Wt |
| French | parti | ✓ | Wt |
| Swahili | chama | ✗ | Wt |
| Hausa | jam'iyya | ✗ | Wt |
| Yoruba | ẹgbẹ́ | ✗ | M |
| Quechua | rakisa (Wt); partido in bilingual speech | ✗ (✓ lenient) | Wt, M |

**8/20 (9 lenient); regions 4 (no EA SSA AM) (5 lenient) → fail.**

### sandwich (Wt: [sandwich](https://en.wiktionary.org/wiki/sandwich#Translations), "dish|open sandwich")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 三明治 sānmíngzhì | ✓ | Wt |
| Japanese | サンドイッチ sandoitchi | ✓ | Wt |
| Korean | 샌드위치 saendeuwichi | ✓ | Wt |
| Vietnamese | bánh mì (kẹp); xăng-uých | ✗ (✓ lenient) | Wt |
| Thai | แซนด์วิช sɛɛnwít | ✓ | Wt |
| Indonesian | roti lapis, roti apit; sandwich also used | ✗ (✓ lenient) | Wt, M |
| Tagalog | sandwich | ✓ | M |
| Hindi | सैंडविच saiṇḍvic | ✓ | Wt |
| Bengali | স্যান্ডউইচ syānḍuic | ✓ | Wt |
| Tamil | சாண்ட்விச் sāṇṭvic | ✓ | M |
| Persian | ساندویچ sāndevič | ✓ | Wt |
| Arabic | ساندويتش sandawitš (formal شطيرة šaṭīra) | ✓ | Wt |
| Turkish | sandviç | ✓ | Wt |
| Russian | бутерброд buterbrod (open); сэндвич sendvič | ✗ (✓ lenient) | Wt |
| Spanish | sándwich, sánguche | ✓ | Wt |
| French | sandwich | ✓ | Wt |
| Swahili | sandwichi | ✓ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | san-wiiṣi | ✓ | Wt |
| Quechua | sánguche (Spanish loan) | ✓ | M |

**16/20 (19 lenient); regions all 7 → pass.** Median [sandwitʃ] → *sanduwitu*.
Median: w/v/u after d is w (th tl es fr sw ar) over v (hi ta tr fa); final consonant-only majority.

### pizza (Wt: [pizza](https://en.wiktionary.org/wiki/pizza#Translations), "Italian dish")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 比萨 bǐsà, 披萨 pīsà | ✓ | Wt |
| Japanese | ピザ piza | ✓ | Wt |
| Korean | 피자 pija | ✓ | Wt |
| Vietnamese | pizza | ✓ | Wt |
| Thai | พิซซ่า phítsâa | ✓ | Wt |
| Indonesian | piza, pizza | ✓ | Wt |
| Tagalog | pitsa | ✓ | Wt |
| Hindi | पिज़्ज़ा pizzā | ✓ | Wt |
| Bengali | পিৎজা pitjā | ✓ | Wt |
| Tamil | பீட்ஸா pīṭsā | ✓ | Wt |
| Persian | پیتزا pitzā | ✓ | Wt |
| Arabic | بيتزا bītzā | ✓ | Wt |
| Turkish | pizza | ✓ | Wt |
| Russian | пицца pitstsa | ✓ | Wt |
| Spanish | pizza | ✓ | Wt |
| French | pizza | ✓ | Wt |
| Swahili | piza | ✓ | M |
| Hausa | fiza | ✓ | M |
| Yoruba | písà | ✓ | M |
| Quechua | pizza (Spanish loan) | ✓ | M |

**20/20; regions all 7 → pass.** Median [pitsa] → *pisa*.

### sauce (Wt: [sauce](https://en.wiktionary.org/wiki/sauce#Translations), "liquid condiment")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 酱 jiàng, 酱汁 jiàngzhī (沙司 shāsī rare) | ✗ | Wt |
| Japanese | ソース sōsu | ✓ | Wt |
| Korean | 소스 soseu | ✓ | Wt |
| Vietnamese | xốt (nước chấm dipping sauce) | ✓ | Wt |
| Thai | ซอส sɔ́ɔt | ✓ | Wt |
| Indonesian | saus | ✓ | Wt |
| Tagalog | sarsa (< Spanish salsa) | ✗ (✓ lenient) | Wt |
| Hindi | सॉस sŏs (चटनी chaṭnī is chutney) | ✓ | Wt, M* |
| Bengali | সস sɔs | ✓ | Wt, M* |
| Tamil | (no Wt; spoken சாஸ் sās) | ✓ | M |
| Persian | سس sos | ✓ | Wt |
| Arabic | صلصة ṣalṣa (< Italian salsa) | ✗ (✓ lenient) | Wt |
| Turkish | sos (salça = paste) | ✓ | Wt |
| Russian | соус sous | ✓ | Wt |
| Spanish | salsa | ✗ (✓ lenient) | Wt |
| French | sauce | ✓ | Wt |
| Swahili | mchuzi | ✗ | M |
| Hausa | miya | ✗ | M |
| Yoruba | ọbẹ̀ | ✗ | M |
| Quechua | salsa, uchu (Spanish loan or native chili sauce) | ✗ (✓ lenient) | M |

**12/20 (16 lenient); regions 5 (no SSA AM) (6 lenient) → pass, borderline.** Median [sos] → *sosu*.
The sos form alone reaches 12, with Tamil from memory and Hindi and Bengali as M\*; hence "pass, borderline". Counting salsa/sarsa/ṣalṣa as the same word gives 16. Median [sos].

### sugar (Wt: [sugar](https://en.wiktionary.org/wiki/sugar#Translations), "sucrose from sugar cane or sugar beet used to sweeten food and drink")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 糖 táng | ✗ | Wt |
| Japanese | 砂糖 satō | ✗ | Wt |
| Korean | 설탕 seoltang | ✗ | Wt |
| Vietnamese | đường | ✗ | Wt |
| Thai | น้ำตาล námtaan | ✗ | Wt |
| Indonesian | gula | ✗ | Wt |
| Tagalog | asukal | ✓ | Wt |
| Hindi | चीनी cīnī; शक्कर šakkar also common | ✗ (✓ lenient) | Wt |
| Bengali | চিনি cini | ✗ | Wt |
| Tamil | சர்க்கரை sarkkarai, சக்கரை | ✓ | Wt |
| Persian | شکر šekar | ✓ | Wt |
| Arabic | سكر sukkar | ✓ | Wt |
| Turkish | şeker | ✓ | Wt |
| Russian | сахар saxar | ✓ | Wt |
| Spanish | azúcar | ✓ | Wt |
| French | sucre | ✓ | Wt |
| Swahili | sukari | ✓ | Wt |
| Hausa | sukari | ✓ | Wt |
| Yoruba | ṣúgà (< English) | ✓ | M |
| Quechua | misk'i (Wt "sweet"); azúcar in bilingual speech | ✗ (✓ lenient) | Wt, M |

**11/20 (13 lenient); regions 5 (no EA AM) (6 lenient) → borderline.** Median [sukar] → *sukalu*.
The whole family goes back to Sanskrit śarkarā, but in South Asia the everyday word is cīnī "the Chinese (sugar)". Median: s over ʃ, u over a and e, final consonant-only majority: [sukar].

### soda (Wt: [soda](https://en.wiktionary.org/wiki/soda#Translations), "sweet, carbonated drink")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 汽水 qìshuǐ | ✗ | Wt |
| Japanese | 炭酸飲料 tansan inryō (ソーダ = soda water) | ✗ | Wt |
| Korean | 탄산음료 tansan eumryo, 사이다 saida | ✗ | Wt, M |
| Vietnamese | nước ngọt | ✗ | Wt |
| Thai | น้ำอัดลม náam àt lom | ✗ | Wt |
| Indonesian | minuman bersoda, soda | ✗ (✓ lenient) | Wt (soft drink), M |
| Tagalog | softdrinks | ✗ | M |
| Hindi | सोडा soḍā; कोल्ड ड्रिंक | ✓ | Wt |
| Bengali | কোল্ড ড্রিংক kold ḍriṅk | ✗ | M |
| Tamil | குளிர்பானம் kuḷirpāṉam | ✗ | Wt |
| Persian | نوشابه nušābe | ✗ | Wt |
| Arabic | مشروب غازي mašrūb ġāzī | ✗ | Wt |
| Turkish | gazoz, gazlı içecek | ✗ | Wt |
| Russian | газировка gazirovka | ✗ | Wt |
| Spanish | refresco, gaseosa (soda in some countries) | ✗ (✓ lenient) | Wt |
| French | soda, boisson gazeuse | ✓ | Wt |
| Swahili | soda | ✓ | Wt |
| Hausa | lemu | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | (no data) | ✗ | M |

**3/20 (5 lenient); regions 3 (SA EU SSA) (4 lenient) → fail.**

### film (Wt: [movie](https://en.wiktionary.org/wiki/movie#Translations), "motion picture")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 电影 diànyǐng | ✗ | Wt |
| Japanese | 映画 eiga | ✗ | Wt |
| Korean | 영화 yeonghwa | ✗ | Wt |
| Vietnamese | phim (< French film) | ✓ | Wt |
| Thai | หนัง nǎng, ภาพยนตร์ | ✗ | Wt |
| Indonesian | film | ✓ | Wt |
| Tagalog | pelikula, sine | ✗ | Wt |
| Hindi | फ़िल्म film, पिक्चर | ✓ | Wt |
| Bengali | ফিল্ম film, ছবি chobi, সিনেমা | ✓ | Wt |
| Tamil | படம் paṭam, திரைப்படம் | ✗ | Wt |
| Persian | فیلم film | ✓ | Wt |
| Arabic | فيلم film | ✓ | Wt |
| Turkish | film | ✓ | Wt |
| Russian | фильм fil'm | ✓ | Wt |
| Spanish | película (filme rare) | ✗ | Wt |
| French | film | ✓ | Wt |
| Swahili | filamu | ✓ | Wt |
| Hausa | sinima | ✗ | Wt |
| Yoruba | fiimu | ✓ | Wt |
| Quechua | película (Spanish loan) | ✗ | M |

**11/20; regions 5 (no EA AM) → fail.**
Fails by one. No column is doubtful in film's favour; the near misses use another loan (tl sine, ha sinima) or Spanish película.

### toast (Wt: [toast](https://en.wiktionary.org/wiki/toast#Translations), "toasted bread")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 烤面包 kǎo miànbāo; 吐司 tǔsī | ✗ (✓ lenient) | Wt |
| Japanese | トースト tōsuto | ✓ | Wt |
| Korean | 토스트 toseuteu | ✓ | Wt |
| Vietnamese | bánh mì nướng | ✗ | Wt |
| Thai | ขนมปังปิ้ง khanǒm pang pîng | ✗ | Wt |
| Indonesian | roti bakar, roti panggang | ✗ | Wt |
| Tagalog | tinapay (toasted bread, no loan) | ✗ | M |
| Hindi | टोस्ट ṭosṭ | ✓ | M |
| Bengali | টোস্ট ṭosṭ | ✓ | M |
| Tamil | (no data; ṭōsṭ likely) | ✗ (✓ lenient) | M |
| Persian | نان تست nān-e tost | ✓ | Wt |
| Arabic | خبز محمص xubz muḥammaṣ; tōst colloquial | ✗ (✓ lenient) | M |
| Turkish | kızarmış ekmek (tost = toasted sandwich) | ✗ (✓ lenient) | Wt |
| Russian | гренки grenki; тост | ✗ (✓ lenient) | Wt |
| Spanish | pan tostado, tostada | ✗ (✓ lenient) | Wt |
| French | pain grillé; toast | ✗ (✓ lenient) | Wt |
| Swahili | tosti | ✓ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | (no data) | ✗ | M |

**6/20 (13 lenient); regions 4 (no SEA EU AM) (5 lenient) → borderline.** Median [tost] → *tosutu*.
The lenient count is high only because many languages have tost beside a native everyday phrase "grilled/roasted bread" (zh, vi, th, id, ar, tr, ru, es, fr). That phrase is the majority build and is ready at rung 3. The low strict count makes this a weak borderline.

### balcony (Wt: [balcony](https://en.wiktionary.org/wiki/balcony#Translations), "structure extending from a building")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 阳台 yángtái | ✗ | Wt |
| Japanese | バルコニー barukonī, ベランダ beranda | ✓ | Wt |
| Korean | 발코니 balkoni | ✓ | Wt |
| Vietnamese | ban công (< French balcon) | ✓ | Wt |
| Thai | ระเบียง rabiang | ✗ | Wt |
| Indonesian | balkon | ✓ | Wt |
| Tagalog | balkonahe | ✓ | Wt |
| Hindi | छज्जा chajjā; spoken बालकनी bālkanī | ✗ (✓ lenient) | Wt, M |
| Bengali | ব্যালকনি byālkani | ✓ | Wt |
| Tamil | பால்கனி pālkaṉi | ✓ | Wt |
| Persian | بالکن bālkon | ✓ | Wt |
| Arabic | شرفة šurfa; colloquial balkōna | ✗ (✓ lenient) | Wt, M |
| Turkish | balkon | ✓ | Wt |
| Russian | балкон balkon | ✓ | Wt |
| Spanish | balcón | ✓ | Wt |
| French | balcon | ✓ | Wt |
| Swahili | roshani | ✗ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | balcón (Spanish loan) | ✓ | M |

**13/20 (15 lenient); regions 6 (no SSA) → pass.** Median [balkon] → *balukon*.
Median: final vowel i (ja ko bn ta) 4 against consonant-final 9.

### circus (Wt: [circus](https://en.wiktionary.org/wiki/circus#Translations), "company that travels")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 马戏团 mǎxìtuán "horse-show troupe" | ✗ | Wt |
| Japanese | サーカス sākasu | ✓ | Wt |
| Korean | 서커스 seokeoseu | ✓ | Wt |
| Vietnamese | xiếc (< French cirque) | ✓ | Wt |
| Thai | ละครสัตว์ lakhɔɔn sàt "animal theatre" | ✗ | Wt |
| Indonesian | sirkus | ✓ | Wt |
| Tagalog | sirko | ✓ | Wt |
| Hindi | सर्कस sarkas | ✓ | Wt |
| Bengali | সার্কাস sārkās | ✓ | Wt |
| Tamil | வட்டரங்கு vaṭṭaraṅku (coinage); spoken sarkas | ✗ (✓ lenient) | Wt, M |
| Persian | سیرک sirk, سرکس serkes | ✓ | Wt |
| Arabic | سيرك sirk | ✓ | Wt |
| Turkish | sirk | ✓ | Wt |
| Russian | цирк tsirk | ✓ | Wt |
| Spanish | circo | ✓ | Wt |
| French | cirque | ✓ | Wt |
| Swahili | sarakasi | ✓ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | circo (Spanish loan) | ✓ | M |

**15/20 (16 lenient); regions all 7 → pass.** Median [sirkas] → *silukasu*.
Two shapes: Romance sirk(o) (vi id tl fa ar tr ru es fr qu) and English sarkas (ja ko hi bn sw). Per position: first vowel i 10 against a 5; then a final vowel in 9 of 15 (a 4, o 3), then s in 6 of 9. The result [sirkas] is a blend nobody says; [sirk] (the Romance shape, majority of whole forms) would give *silku*.

### T-shirt (Wt: [T-shirt](https://en.wiktionary.org/wiki/T-shirt#Translations), "type of shirt")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | T恤(衫) tī-xù(shān) | ✓ | Wt |
| Japanese | Tシャツ tī-shatsu | ✓ | Wt |
| Korean | 티셔츠 tisyeocheu | ✓ | Wt |
| Vietnamese | áo thun | ✗ | Wt |
| Thai | เสื้อยืด sʉ̂a yʉ̂ʉt; ทีเชิร์ต thii-chəət | ✗ (✓ lenient) | Wt |
| Indonesian | kaus | ✗ | Wt |
| Tagalog | t-shirt, kamiseta | ✗ (✓ lenient) | M |
| Hindi | टी-शर्ट ṭī-śarṭ | ✓ | Wt |
| Bengali | টি-শার্ট ṭi-śārṭ | ✓ | Wt |
| Tamil | (coinage கொசுவுசட்டை); spoken T-shirt | ✗ (✓ lenient) | Wt, M |
| Persian | تی‌شرت tišert | ✓ | Wt |
| Arabic | تي شيرت tī šīrt | ✓ | Wt |
| Turkish | tişört | ✓ | Wt |
| Russian | футболка futbolka | ✗ | Wt |
| Spanish | camiseta, playera | ✗ | Wt |
| French | T-shirt | ✓ | Wt |
| Swahili | tisheti | ✓ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | (Spanish polo, camiseta) | ✗ | M |

**10/20 (13 lenient); regions 5 (no SEA AM) (6 lenient) → borderline.** Median [tiʃart] → *tisalutu*.
Median second vowel a (ja hi bn) is only a plurality (e fa sw, ø/œ tr fr); r kept in 6 of 10.

### music (Wt: [music](https://en.wiktionary.org/wiki/music#Translations), "sound, organized in time in a melodious way")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 音乐 yīnyuè | ✗ | Wt |
| Japanese | 音楽 ongaku | ✗ | Wt |
| Korean | 음악 eumak | ✗ | Wt |
| Vietnamese | âm nhạc | ✗ | Wt |
| Thai | ดนตรี dontrii | ✗ | Wt |
| Indonesian | musik | ✓ | Wt |
| Tagalog | musika | ✓ | Wt |
| Hindi | संगीत saṅgīt; मूसीक़ी mūsīqī (Urdu) | ✗ (✓ lenient) | Wt |
| Bengali | সঙ্গীত saṅgīt, গান gān | ✗ | Wt |
| Tamil | இசை isai | ✗ | Wt |
| Persian | موسیقی musiqi | ✓ | Wt |
| Arabic | موسيقى mūsīqā | ✓ | Wt |
| Turkish | müzik | ✓ | Wt |
| Russian | музыка muzyka | ✓ | Wt |
| Spanish | música | ✓ | Wt |
| French | musique | ✓ | Wt |
| Swahili | muziki | ✓ | Wt |
| Hausa | kiɗa | ✗ | M |
| Yoruba | orin | ✗ | Wt |
| Quechua | taki "song"; música in bilingual speech | ✗ (✓ lenient) | M |

**9/20 (11 lenient); regions 4 (no EA SA AM) (6 lenient) → fail.**

### university (Wt: [university](https://en.wiktionary.org/wiki/university#Translations), "institution of higher education")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 大学 dàxué | ✗ | Wt |
| Japanese | 大学 daigaku | ✗ | Wt |
| Korean | 대학(교) daehak(gyo) | ✗ | Wt |
| Vietnamese | đại học | ✗ | Wt |
| Thai | มหาวิทยาลัย mahǎawítthayaalai | ✗ | Wt |
| Indonesian | universitas | ✓ | Wt |
| Tagalog | unibersidad (pamantasan formal) | ✓ | Wt |
| Hindi | विश्वविद्यालय viśvavidyālay; यूनिवर्सिटी yūnivarsiṭī | ✗ (✓ lenient) | Wt |
| Bengali | বিশ্ববিদ্যালয় biśvabidyālay | ✗ | Wt |
| Tamil | பல்கலைக்கழகம் palkalaikkaḻakam | ✗ | Wt |
| Persian | دانشگاه dānešgāh | ✗ | Wt |
| Arabic | جامعة jāmiʿa | ✗ | Wt |
| Turkish | üniversite | ✓ | Wt |
| Russian | университет universitet | ✓ | Wt |
| Spanish | universidad | ✓ | Wt |
| French | université | ✓ | Wt |
| Swahili | chuo kikuu "big school" | ✗ | Wt |
| Hausa | jami'a | ✗ | Wt |
| Yoruba | yunifásítì | ✓ | Wt |
| Quechua | jatun yachay wasi "big learning house" | ✗ (✓ lenient) | Wt |

**7/20 (9 lenient); regions 4 (no EA SA AM) (6 lenient) → fail.**

### video (Wt: [video](https://en.wiktionary.org/wiki/video#Translations), "television show, movie")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 视频 shìpín | ✗ | Wt |
| Japanese | 動画 dōga (online); ビデオ bideo | ✗ (✓ lenient) | Wt |
| Korean | 영상 yeongsang; 비디오 bidio | ✗ (✓ lenient) | Wt |
| Vietnamese | video, vi-đê-ô | ✓ | Wt, M* |
| Thai | วิดีโอ widiioo | ✓ | Wt |
| Indonesian | video | ✓ | Wt |
| Tagalog | video | ✓ | M |
| Hindi | वीडियो vīḍiyo | ✓ | Wt |
| Bengali | ভিডিও bhiḍio | ✓ | Wt |
| Tamil | வீடியோ vīṭiyō | ✓ | M |
| Persian | ویدیو vidiyo | ✓ | Wt |
| Arabic | فيديو fīdyū | ✓ | Wt |
| Turkish | video | ✓ | Wt |
| Russian | видео video | ✓ | Wt |
| Spanish | vídeo, video | ✓ | Wt |
| French | vidéo | ✓ | Wt |
| Swahili | filamu (Wt); video in speech | ✗ (✓ lenient) | Wt, M |
| Hausa | bidiyo | ✓ | M |
| Yoruba | fídíò | ✓ | M |
| Quechua | video (Spanish loan) | ✓ | M |

**16/20 (19 lenient); regions 6 (no EA) (7 lenient) → pass.** Median [video] → *bideyo*.
Second vowel: e (vi id tl tr ru es fr qu) 8 against i/j (th hi bn ta fa ar ha yo) 8; the lenient forms (ja bideo, ko bidio, sw video) favour e. [vidio] would give *bidiyo*.

### bank (Wt: [bank](https://en.wiktionary.org/wiki/bank#Translations), "institution")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 银行 yínháng | ✗ | Wt |
| Japanese | 銀行 ginkō | ✗ | Wt |
| Korean | 은행 eunhaeng | ✗ | Wt |
| Vietnamese | ngân hàng (nhà băng dated) | ✗ | Wt |
| Thai | ธนาคาร thanaakhaan | ✗ | Wt |
| Indonesian | bank | ✓ | Wt |
| Tagalog | bangko | ✓ | Wt |
| Hindi | बैंक baiṅk | ✓ | Wt |
| Bengali | ব্যাংক byāṅk | ✓ | Wt |
| Tamil | வங்கி vaṅki | ✓ | Wt |
| Persian | بانک bānk | ✓ | Wt |
| Arabic | بنك bank, مصرف maṣrif | ✓ | Wt |
| Turkish | banka | ✓ | Wt |
| Russian | банк bank | ✓ | Wt |
| Spanish | banco | ✓ | Wt |
| French | banque | ✓ | Wt |
| Swahili | benki | ✓ | Wt |
| Hausa | banki | ✓ | Wt |
| Yoruba | báńkì | ✓ | M |
| Quechua | banco (Spanish loan) | ✓ | M |

**15/20; regions 6 (no EA) → pass.** Median [banki] → *banki*.
Median: a final vowel in 8 of 15 forms (i: ta sw ha yo 4, o: tl es qu 3, a: tr), so [banki]; the consonant-final forms (id hi bn fa ar ru fr) are 7, so [bank] → *banku* is one vote away.

### office (Wt: [office](https://en.wiktionary.org/wiki/office#Translations), "room(s) or building used for non-manual work")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 办公室 bàngōngshì | ✗ | Wt |
| Japanese | 事務所 jimusho; オフィス ofisu | ✗ (✓ lenient) | Wt |
| Korean | 사무실 samusil; 오피스 opiseu | ✗ (✓ lenient) | Wt |
| Vietnamese | văn phòng | ✗ | Wt |
| Thai | สำนักงาน samnákngaan; spoken ออฟฟิศ ɔ́ɔfít | ✗ (✓ lenient) | Wt |
| Indonesian | kantor | ✗ | Wt |
| Tagalog | opisina | ✓ | Wt |
| Hindi | कार्यालय kāryālay (formal); spoken ऑफ़िस ŏfis | ✗ (✓ lenient) | Wt, M |
| Bengali | অফিস ophis, দপ্তর daptar | ✓ | Wt |
| Tamil | அலுவலகம் aluvalakam; spoken ஆபீஸ் āpīs | ✗ (✓ lenient) | Wt, M |
| Persian | دفتر daftar (آفیس āfis in Afghanistan) | ✗ | Wt |
| Arabic | مكتب maktab | ✗ | Wt |
| Turkish | ofis, büro | ✓ | Wt, M* |
| Russian | офис ofis, контора | ✓ | Wt |
| Spanish | oficina | ✓ | Wt |
| French | bureau | ✗ | Wt |
| Swahili | ofisi, afisi | ✓ | Wt |
| Hausa | ofis | ✓ | M |
| Yoruba | ọ́fíìsì | ✓ | M |
| Quechua | oficina (Spanish loan) | ✓ | M |

**9/20 (14 lenient); regions 6 (no EA) (7 lenient) → borderline.** Median [ofis] → *ofisu*.
Median of all 14 cognates [ofis].

### program (Wt: [program](https://en.wiktionary.org/wiki/program#Translations), "software application")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 程序 chéngxù, 应用 | ✗ | Wt |
| Japanese | プログラム puroguramu | ✓ | Wt |
| Korean | 프로그램 peurogeuraem | ✓ | Wt |
| Vietnamese | chương trình | ✗ | Wt |
| Thai | โปรแกรม proograem | ✓ | Wt |
| Indonesian | program | ✓ | Wt |
| Tagalog | programa | ✓ | M |
| Hindi | प्रोग्राम progrām | ✓ | Wt |
| Bengali | প্রোগ্রাম progrām | ✓ | Wt |
| Tamil | நிரல் niral; spoken program | ✗ (✓ lenient) | M |
| Persian | برنامه barnāme; پروگرام porogrām | ✗ (✓ lenient) | Wt |
| Arabic | برنامج barnāmaj (< Persian barnāme) | ✗ | Wt |
| Turkish | program | ✓ | Wt |
| Russian | программа programma | ✓ | Wt |
| Spanish | programa | ✓ | Wt |
| French | programme | ✓ | Wt |
| Swahili | programu | ✓ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | programa (Spanish loan) | ✓ | M |

**13/20 (15 lenient); regions all 7 → pass.** Median [program] → *pulogulamu*.
Median: consonant-final (th id hi bn tr fr ko) 7 against -a (tl ru es qu) 4 and -u (ja sw) 2.

### technology (Wt: [technology](https://en.wiktionary.org/wiki/technology#Translations), "the study of or a collection of techniques")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 技术 jìshù, 科技 | ✗ | Wt |
| Japanese | 技術 gijutsu; テクノロジー tekunorojī | ✗ (✓ lenient) | Wt |
| Korean | 기술 gisul; 테크놀로지 | ✗ (✓ lenient) | Wt |
| Vietnamese | công nghệ, kỹ thuật | ✗ | Wt |
| Thai | เทคโนโลยี theknooloyii | ✓ | Wt |
| Indonesian | teknologi | ✓ | Wt |
| Tagalog | teknolohiya | ✓ | Wt |
| Hindi | टैक्नोलॉजी ṭaiknolojī (formal प्रौद्योगिकी) | ✓ | Wt |
| Bengali | প্রযুক্তি prajukti; spoken technology | ✗ (✓ lenient) | Wt, M |
| Tamil | தொழில்நுட்பம் toḻilnuṭpam | ✗ | Wt |
| Persian | تکنولوژی teknoloži (official فناوری fanāvari) | ✓ | Wt, M* |
| Arabic | تكنولوجيا teknolōjyā, تقنية taqniya | ✓ | Wt |
| Turkish | teknoloji | ✓ | Wt |
| Russian | технология texnologija | ✓ | Wt |
| Spanish | tecnología | ✓ | Wt |
| French | technologie | ✓ | Wt |
| Swahili | teknolojia | ✓ | Wt |
| Hausa | fasaha | ✗ | M |
| Yoruba | ìmọ̀-ẹ̀rọ | ✗ | M |
| Quechua | tecnología (Spanish loan) | ✓ | M |

**12/20 (15 lenient); regions 6 (no EA) (7 lenient) → pass, borderline.** Median [teknolodʒi] → *tekunolodi*.
Median: the consonant before the last vowel is dʒ (hi ar tr sw) 4, x/h (tl es qu) 3, ʒ (fa fr) 2, g (id ru) 2; the ending -i (th id hi fa tr fr) and -ia (tl ar ru es sw qu) tie 6/6; I took the shorter.

### computer (Wt: [computer](https://en.wiktionary.org/wiki/computer#Translations), "programmable electronic device")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 电脑 diànnǎo | ✗ | Wt |
| Japanese | コンピューター konpyūtā, パソコン | ✓ | Wt |
| Korean | 컴퓨터 keompyuteo | ✓ | Wt |
| Vietnamese | máy tính | ✗ | Wt |
| Thai | คอมพิวเตอร์ khɔmphiwtəə, คอม | ✓ | Wt |
| Indonesian | komputer | ✓ | Wt |
| Tagalog | kompyuter | ✓ | Wt |
| Hindi | कंप्यूटर kampyūṭar (formal संगणक) | ✓ | Wt, M* |
| Bengali | কম্পিউটার kampiuṭār | ✓ | Wt |
| Tamil | கணினி kaṇiṉi, கம்ப்யூட்டர் kampyūṭṭar | ✓ | Wt, M* |
| Persian | کامپیوتر kāmpyuter (official رایانه rāyāne) | ✓ | Wt |
| Arabic | كمبيوتر kambyūtar (formal حاسوب ḥāsūb) | ✓ | Wt, M* |
| Turkish | bilgisayar | ✗ | Wt |
| Russian | компьютер komp'juter | ✓ | Wt |
| Spanish | computadora (Latin America), ordenador (Spain) | ✓ | Wt, M* |
| French | ordinateur | ✗ | Wt |
| Swahili | kompyuta | ✓ | Wt |
| Hausa | kwamfuta (Wt na'ura "machine") | ✓ | M* |
| Yoruba | kọ̀ǹpútà | ✓ | Wt |
| Quechua | antañiqiq (coinage); computadora in bilingual speech | ✗ (✓ lenient) | Wt, M |

**15/20 (16 lenient); regions 6 (no AM) (7 lenient) → pass.** Median [kompjutar] → *konpuyutalu*.
First vowel ties: o (ja th id tl es sw yo) against a (hi bn ta fa ar ru ha); [kampjutar] gives *kanpuyutalu*. Either way 5 syllables, against the existing compound *du sunbu*.

### business (Wt: [business](https://en.wiktionary.org/wiki/business#Translations), "commercial enterprise or establishment")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 企业 qǐyè, 生意 shēngyi | ✗ | Wt |
| Japanese | 事業 jigyō, 企業; ビジネス bijinesu | ✗ (✓ lenient) | Wt, M |
| Korean | 사업 saeop; 비즈니스 bijeuniseu | ✗ (✓ lenient) | Wt, M |
| Vietnamese | doanh nghiệp, kinh doanh | ✗ | Wt |
| Thai | ธุรกิจ thurakìt | ✗ | Wt |
| Indonesian | bisnis, usaha (Wt perusahaan "company") | ✓ | M* |
| Tagalog | negosyo; Taglish bisnes | ✗ (✓ lenient) | Wt, M |
| Hindi | व्यापार vyāpār, व्यवसाय; spoken बिज़नेस | ✗ (✓ lenient) | Wt, M |
| Bengali | ব্যবসা byabsā | ✗ | Wt |
| Tamil | வியாபாரம் viyāpāram | ✗ | M |
| Persian | تجارت tejārat; بیزینس colloquial | ✗ (✓ lenient) | Wt, M |
| Arabic | تجارة tijāra, شركة šarika | ✗ | Wt |
| Turkish | iş, işletme | ✗ | Wt |
| Russian | бизнес biznes | ✓ | Wt |
| Spanish | negocio (bisnes rare) | ✗ | Wt |
| French | affaires, entreprise (le business colloquial) | ✗ | Wt |
| Swahili | biashara | ✗ | Wt |
| Hausa | kasuwanci | ✗ | M |
| Yoruba | òwò | ✗ | M |
| Quechua | (no data) | ✗ | M |

**2/20 (7 lenient); regions 2 (SEA EU) (5 lenient) → fail.**

### hotel (Wt: [hotel](https://en.wiktionary.org/wiki/hotel#Translations), "establishment providing accommodation")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 酒店 jiǔdiàn, 宾馆 bīnguǎn | ✗ | Wt |
| Japanese | ホテル hoteru | ✓ | Wt |
| Korean | 호텔 hotel | ✓ | Wt |
| Vietnamese | khách sạn | ✗ | Wt |
| Thai | โรงแรม roongrɛɛm | ✗ | Wt |
| Indonesian | hotel | ✓ | Wt |
| Tagalog | hotel | ✓ | Wt |
| Hindi | होटल hoṭal | ✓ | Wt |
| Bengali | হোটেল hoṭel | ✓ | Wt |
| Tamil | ஹோட்டல் hōṭṭal | ✓ | Wt |
| Persian | هتل hotel | ✓ | Wt |
| Arabic | فندق funduq; colloquial أوتيل ōtēl | ✗ (✓ lenient) | Wt |
| Turkish | otel | ✓ | Wt |
| Russian | гостиница gostinica; отель otel' | ✗ (✓ lenient) | Wt |
| Spanish | hotel | ✓ | Wt |
| French | hôtel | ✓ | Wt |
| Swahili | hoteli (also "restaurant") | ✓ | Wt |
| Hausa | hotel, otal | ✓ | Wt |
| Yoruba | hòtẹ́ẹ̀lì | ✓ | M |
| Quechua | hotel (Spanish loan) | ✓ | M |

**15/20 (17 lenient); regions all 7 → pass.** Median [hotel] → *otelu*.
In Indian English, Hindi, Tamil and Swahili "hotel/hoteli" commonly means an eating house, so the shared form is broader than the English sense. names.py drops h: [hotel] → *otelu*.

### energy (Wt: [energy](https://en.wiktionary.org/wiki/energy#Translations), "physics")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 能量 néngliàng | ✗ | Wt |
| Japanese | エネルギー enerugī | ✓ | Wt |
| Korean | 에너지 eneoji | ✓ | Wt |
| Vietnamese | năng lượng | ✗ | Wt |
| Thai | พลังงาน phalang-ngaan | ✗ | Wt |
| Indonesian | energi | ✓ | Wt |
| Tagalog | enerhiya | ✓ | M |
| Hindi | ऊर्जा ūrjā; spoken energy | ✗ (✓ lenient) | Wt, M |
| Bengali | শক্তি śakti; spoken energy | ✗ (✓ lenient) | Wt, M |
| Tamil | ஆற்றல் āṟṟal | ✗ | M |
| Persian | انرژی enerži | ✓ | Wt |
| Arabic | طاقة ṭāqa | ✗ | Wt |
| Turkish | enerji | ✓ | Wt |
| Russian | энергия energija | ✓ | Wt |
| Spanish | energía | ✓ | Wt |
| French | énergie | ✓ | Wt |
| Swahili | nishati | ✗ | M |
| Hausa | kuzari | ✗ | Wt |
| Yoruba | agbára | ✗ | M |
| Quechua | energía (Spanish loan) | ✓ | M |

**10/20 (12 lenient); regions 5 (no SA SSA) (6 lenient) → borderline.** Median [enerdʒi] → *eneludi*.
Many languages lump energy with "power, strength" (th phalang, hi śakti, bn śakti, ha kuzari, yo agbára), which the lexicon may already have. Median consonant: dʒ (ko tr hi bn) 4, g (ja id ru) 3, x/h (tl es qu) 3, ʒ (fa fr) 2.

### sport (Wt: [sport](https://en.wiktionary.org/wiki/sport#Translations), "any athletic activity that uses physical skills")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 运动 yùndòng | ✗ | Wt |
| Japanese | スポーツ supōtsu | ✓ | Wt |
| Korean | 스포츠 seupocheu, 운동 undong | ✓ | Wt |
| Vietnamese | thể thao | ✗ | Wt |
| Thai | กีฬา kiilaa | ✗ | Wt |
| Indonesian | olahraga | ✗ | Wt |
| Tagalog | palakasan; Taglish sports | ✗ (✓ lenient) | Wt, M |
| Hindi | खेल khel; spoken sports | ✗ (✓ lenient) | Wt |
| Bengali | খেলা khelā | ✗ | Wt |
| Tamil | விளையாட்டு viḷaiyāṭṭu | ✗ | Wt |
| Persian | ورزش varzeš | ✗ | Wt |
| Arabic | رياضة riyāḍa | ✗ | Wt |
| Turkish | spor | ✓ | Wt |
| Russian | спорт sport | ✓ | Wt |
| Spanish | deporte (same etymon, not heard as the same word) | ✗ | Wt |
| French | sport | ✓ | Wt |
| Swahili | michezo; spoti | ✗ (✓ lenient) | Wt |
| Hausa | wasanni | ✗ | M |
| Yoruba | eré ìdárayá | ✗ | M |
| Quechua | pukllay "game" | ✗ | M |

**5/20 (8 lenient); regions 3 (EA WA EU) (6 lenient) → fail.**

### machine (Wt: [machine](https://en.wiktionary.org/wiki/machine#Translations), "mechanical or electrical device")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 机器 jīqì | ✗ | Wt |
| Japanese | 機械 kikai (マシン mashin specialised) | ✗ | Wt |
| Korean | 기계 gigye | ✗ | Wt |
| Vietnamese | máy | ✗ | Wt |
| Thai | เครื่อง khrʉ̂ang | ✗ | Wt |
| Indonesian | mesin | ✓ | Wt |
| Tagalog | makina | ✓ | Wt |
| Hindi | यंत्र yantra (formal); spoken मशीन mašīn | ✗ (✓ lenient) | Wt, M |
| Bengali | মেশিন mešin | ✓ | Wt |
| Tamil | எந்திரம் enthiram; spoken மெஷின் | ✗ (✓ lenient) | Wt, M |
| Persian | ماشین māšin (also "car") | ✓ | Wt |
| Arabic | آلة āla; ماكينة mākīna | ✓ | Wt |
| Turkish | makine | ✓ | Wt |
| Russian | машина mašina (also "car") | ✓ | Wt |
| Spanish | máquina | ✓ | Wt |
| French | machine | ✓ | Wt |
| Swahili | mashine | ✓ | Wt |
| Hausa | mashin | ✓ | M |
| Yoruba | ẹ̀rọ | ✗ | M |
| Quechua | máquina (Spanish loan) | ✓ | M |

**12/20 (14 lenient); regions 6 (no EA) → pass, borderline.** Median [maʃina] → *masina*.
Median: ʃ (bn fa ru fr sw ha) 6 against k (tl ar tr es qu) 5; a final vowel in 7 of 12 (a 5, e 2), so [maʃina]. In fa and ru the word also or mainly means "car".

### president (Wt: [president](https://en.wiktionary.org/wiki/president#Translations), "the head of state of a republic")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 总统 zǒngtǒng | ✗ | Wt |
| Japanese | 大統領 daitōryō | ✗ | Wt |
| Korean | 대통령 daetongnyeong | ✗ | Wt |
| Vietnamese | tổng thống | ✗ | Wt |
| Thai | ประธานาธิบดี prathaanaathíbɔɔdii | ✗ | Wt |
| Indonesian | presiden | ✓ | Wt |
| Tagalog | pangulo, presidente | ✓ | Wt |
| Hindi | राष्ट्रपति rāṣṭrapati | ✗ | Wt |
| Bengali | রাষ্ট্রপতি rāṣṭrapati | ✗ | Wt |
| Tamil | ஜனாதிபதி janāpati | ✗ | Wt |
| Persian | رئیس‌جمهور ra'is-jomhur; پرزیدنت rare | ✗ (✓ lenient) | Wt |
| Arabic | رئيس raʾīs | ✗ | Wt |
| Turkish | cumhurbaşkanı | ✗ | Wt |
| Russian | президент prezident | ✓ | Wt |
| Spanish | presidente | ✓ | Wt |
| French | président | ✓ | Wt |
| Swahili | rais | ✗ | Wt |
| Hausa | shugaban ƙasa | ✗ | M |
| Yoruba | Ààrẹ | ✗ | Wt |
| Quechua | presidente (Spanish loan) | ✓ | M |

**6/20 (7 lenient); regions 3 (SEA EU AM) (4 lenient) → fail.**

### data (Wt: [data](https://en.wiktionary.org/wiki/data#Translations), "information")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 数据 shùjù | ✗ | Wt |
| Japanese | データ dēta | ✓ | Wt, M* |
| Korean | 데이터 deiteo, 자료 | ✓ | Wt, M* |
| Vietnamese | dữ liệu | ✗ | Wt |
| Thai | ข้อมูล khɔ̂ɔmuun | ✗ | Wt |
| Indonesian | data | ✓ | Wt |
| Tagalog | datos | ✓ | Wt |
| Hindi | डेटा ḍeṭā | ✓ | Wt |
| Bengali | ডেটা ḍeṭā (formal উপাত্ত) | ✓ | Wt, M* |
| Tamil | தரவு taravu | ✗ | Wt |
| Persian | داده dāde (calque "given") | ✗ | Wt |
| Arabic | بيانات bayānāt, معطيات muʿṭayāt (calque) | ✗ | Wt |
| Turkish | veri | ✗ | Wt |
| Russian | данные dannye (calque) | ✗ | Wt |
| Spanish | datos | ✓ | Wt |
| French | données (calque) | ✗ | Wt |
| Swahili | data | ✓ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | datos (Spanish loan) | ✗ (✓ lenient) | M |

**8/20 (9 lenient); regions 5 (no WA AM) (6 lenient) → fail.**

### professor (Wt: [professor](https://en.wiktionary.org/wiki/professor#Translations), "higher ranking for a teacher or faculty member at a college or university")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 教授 jiàoshòu | ✗ | Wt |
| Japanese | 教授 kyōju | ✗ | Wt |
| Korean | 교수 gyosu | ✗ | Wt |
| Vietnamese | giáo sư | ✗ | Wt |
| Thai | ศาสตราจารย์ sàatsatraajaan | ✗ | Wt |
| Indonesian | profesor | ✓ | M |
| Tagalog | propesor | ✓ | Wt |
| Hindi | प्रोफ़ेसर profesar | ✓ | Wt |
| Bengali | প্রফেসর prophesar | ✓ | M |
| Tamil | பேராசிரியர் pērāsiriyar; spoken professor | ✗ (✓ lenient) | M |
| Persian | استاد ostād; پروفسور profesor (title) | ✗ (✓ lenient) | Wt |
| Arabic | أستاذ ustāḏ | ✗ | Wt |
| Turkish | profesör | ✓ | Wt |
| Russian | профессор professor | ✓ | Wt |
| Spanish | profesor (also any teacher) | ✓ | Wt |
| French | professeur (also any teacher) | ✓ | Wt |
| Swahili | profesa | ✓ | Wt |
| Hausa | farfesa | ✓ | M |
| Yoruba | ọ̀jọ̀gbọ́n | ✗ | M |
| Quechua | profesor (Spanish loan) | ✓ | M |

**11/20 (13 lenient); regions 6 (no EA) → borderline.** Median [profesor] → *pulofesolu*.
Last vowel: o (id tl es qu) 4, a (hi bn sw ha) 4, ø/œ/ə (tr fr ru) 3; [profesar] gives *pulofesalu*. In Spanish and French the word means any teacher.

### project (Wt: [project](https://en.wiktionary.org/wiki/project#Translations), "planned endeavor")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 项目 xiàngmù, 计划 | ✗ | Wt |
| Japanese | 計画 keikaku; プロジェクト purojekuto at work | ✗ (✓ lenient) | Wt |
| Korean | 계획 gyehoek; 프로젝트 peurojekteu | ✗ (✓ lenient) | Wt |
| Vietnamese | dự án | ✗ | Wt |
| Thai | โครงการ khroongkaan | ✗ | Wt |
| Indonesian | proyek | ✓ | Wt |
| Tagalog | proyekto | ✓ | Wt |
| Hindi | प्रोजेक्ट projekṭ (formal परियोजना) | ✓ | Wt, M* |
| Bengali | প্রজেক্ট projekṭ | ✓ | Wt |
| Tamil | திட்டம் tiṭṭam; spoken project | ✗ (✓ lenient) | M |
| Persian | پروژه proože | ✓ | Wt |
| Arabic | مشروع mašrūʿ | ✗ | Wt |
| Turkish | proje | ✓ | Wt |
| Russian | проект proekt | ✓ | Wt |
| Spanish | proyecto | ✓ | Wt |
| French | projet | ✓ | Wt |
| Swahili | mradi | ✗ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | proyecto (Spanish loan) | ✓ | M |

**10/20 (13 lenient); regions 5 (no EA SSA) (6 lenient) → borderline.** Median [projekt] → *puloyekutu*.
Median from the strict cognates: j (id tl es qu ru) 5 against ʒ (fa tr fr) 3 and dʒ (hi bn) 2; with the lenient ja ko ta, dʒ ties j at 5, giving [prodʒekt] → *pulodekutu*.

### beer (Wt: [beer](https://en.wiktionary.org/wiki/beer#Translations), "alcoholic drink made of malt")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 啤酒 píjiǔ (sound loan pí + "liquor") | ✗ (✓ lenient) | Wt |
| Japanese | ビール bīru | ✓ | Wt |
| Korean | 맥주 maekju | ✗ | Wt |
| Vietnamese | bia | ✓ | Wt |
| Thai | เบียร์ bia | ✓ | Wt |
| Indonesian | bir | ✓ | Wt |
| Tagalog | serbesa | ✗ | Wt |
| Hindi | बियर biyar | ✓ | Wt |
| Bengali | বিয়ার biyār | ✓ | Wt |
| Tamil | பியர் piyar | ✓ | Wt |
| Persian | آبجو ābjow "barley water" | ✗ | Wt |
| Arabic | بيرة bīra | ✓ | Wt |
| Turkish | bira | ✓ | Wt |
| Russian | пиво pivo | ✗ | Wt |
| Spanish | cerveza | ✗ | Wt |
| French | bière | ✓ | Wt |
| Swahili | bia (pombe = any brew) | ✓ | Wt |
| Hausa | giya | ✗ | Wt |
| Yoruba | bíà | ✓ | Wt |
| Quechua | sirwisa (< cerveza) | ✗ | Wt |

**12/20 (13 lenient); regions 6 (no AM) → pass.** Median [biar] → *biyalu*.
Exactly 12, but every counted column is from Wiktionary, so a plain pass. Median: a after bi in 7 of 12 (vi th hi bn ta sw yo), r present in 8 of 12; [biar]. The r-less [bia] (vi th sw yo) gives *biya*.

### code (Wt: [code](https://en.wiktionary.org/wiki/code#Translations), "instructions for a computer")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 代码 dàimǎ | ✗ | Wt |
| Japanese | コード kōdo | ✓ | Wt |
| Korean | 코드 kodeu | ✓ | Wt |
| Vietnamese | mã | ✗ | Wt |
| Thai | โค้ด khóot | ✓ | Wt |
| Indonesian | kode | ✓ | M |
| Tagalog | code, koda | ✓ | M |
| Hindi | कोड koḍ | ✓ | Wt |
| Bengali | কোড koḍ | ✓ | M |
| Tamil | (no Wt; குறியீடு kuṟiyīṭu; spoken code) | ✗ (✓ lenient) | M |
| Persian | کد kod | ✓ | M |
| Arabic | كود kōd | ✓ | Wt |
| Turkish | kod | ✓ | Wt |
| Russian | код kod | ✓ | Wt |
| Spanish | código | ✓ | Wt |
| French | code | ✓ | Wt |
| Swahili | kodi | ✓ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | código (Spanish loan) | ✓ | M |

**15/20 (16 lenient); regions all 7 → pass.** Median [kod] → *kodu*.

### website (Wt: [website](https://en.wiktionary.org/wiki/website#Translations), "a collection of pages on the World Wide Web")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 网站 wǎngzhàn | ✗ | Wt |
| Japanese | (ウェブ)サイト (webu)saito | ✓ | Wt |
| Korean | 웹사이트 wepsaiteu, 사이트 | ✓ | Wt |
| Vietnamese | trang web "web page" | ✗ (✓ lenient) | Wt |
| Thai | เว็บไซต์ wépsái | ✓ | Wt |
| Indonesian | situs (web) | ✓ | Wt |
| Tagalog | websayt | ✓ | Wt |
| Hindi | वेबसाइट vebsāiṭ (formal जालस्थल) | ✓ | Wt, M* |
| Bengali | ওয়েবসাইট oyebsāiṭ | ✓ | Wt |
| Tamil | வலைத்தளம் valaittaḷam | ✗ | Wt |
| Persian | وبگاه vebgāh (official); colloquial سایت sāyt | ✗ (✓ lenient) | Wt, M |
| Arabic | موقع mawqiʿ "site" (calque) | ✗ | Wt |
| Turkish | web sitesi | ✓ | Wt |
| Russian | сайт sajt | ✓ | Wt |
| Spanish | sitio web | ✓ | Wt |
| French | site (web) | ✓ | Wt |
| Swahili | tovuti | ✗ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | sitio web (Spanish loan) | ✗ (✓ lenient) | M |

**11/20 (14 lenient); regions 5 (no SSA AM) (6 lenient) → borderline.** Median [sait] → *sayitu*.
Tested as the "site" element, per the ladder note. English-pronounced sait (ja ko th tl hi bn ru) 7 against spelling-pronounced sit- (id tr es fr) 4; median [sait].

### democracy (Wt: [democracy](https://en.wiktionary.org/wiki/democracy#Translations), "rule by the people")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 民主 mínzhǔ | ✗ | Wt |
| Japanese | 民主主義 minshushugi | ✗ | Wt |
| Korean | 민주주의 minjujuui | ✗ | Wt |
| Vietnamese | dân chủ | ✗ | Wt |
| Thai | ประชาธิปไตย prachaathíppatai | ✗ | Wt |
| Indonesian | demokrasi | ✓ | Wt |
| Tagalog | demokrasya | ✓ | Wt |
| Hindi | लोकतंत्र loktantra | ✗ | Wt |
| Bengali | গণতন্ত্র gaṇatantra | ✗ | Wt |
| Tamil | மக்களாட்சி makkaḷāṭci, ஜனநாயகம் | ✗ | Wt |
| Persian | دموکراسی demokrāsi (official مردم‌سالاری) | ✓ | Wt |
| Arabic | ديمقراطية dīmuqrāṭiyya | ✓ | Wt |
| Turkish | demokrasi | ✓ | Wt |
| Russian | демократия demokratija | ✓ | Wt |
| Spanish | democracia | ✓ | Wt |
| French | démocratie | ✓ | Wt |
| Swahili | demokrasia | ✓ | Wt |
| Hausa | dimokuraɗiyya | ✓ | Wt |
| Yoruba | ìjọba tiwa-n-tiwa; dẹmọkrasi | ✗ (✓ lenient) | M |
| Quechua | democracia (Spanish loan) | ✓ | M |

**11/20 (12 lenient); regions 5 (no EA SA) → borderline.** Median [demokrasia] → *demokulasiya*.
Every Asian language except id and tl uses a native "people-rule" compound, a ready rung-3 pattern. Median ending: -ia/-ija (tl ar ru es sw ha qu) 7 against -i (id fa tr fr) 4.

### bomb (Wt: [bomb](https://en.wiktionary.org/wiki/bomb#Translations), "device filled with explosives")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 炸弹 zhàdàn | ✗ | Wt |
| Japanese | 爆弾 bakudan | ✗ | Wt |
| Korean | 폭탄 poktan | ✗ | Wt |
| Vietnamese | bom | ✓ | Wt |
| Thai | ระเบิด rabə̀ət; บอมบ์ bɔm | ✗ (✓ lenient) | Wt |
| Indonesian | bom | ✓ | Wt |
| Tagalog | bomba | ✓ | Wt |
| Hindi | बम bam | ✓ | Wt |
| Bengali | বোমা bomā | ✓ | Wt |
| Tamil | வெடிகுண்டு veṭikuṇṭu | ✗ | Wt |
| Persian | بمب bomb | ✓ | Wt |
| Arabic | قنبلة qunbula | ✗ | Wt |
| Turkish | bomba | ✓ | Wt |
| Russian | бомба bomba | ✓ | Wt |
| Spanish | bomba | ✓ | Wt |
| French | bombe | ✓ | Wt |
| Swahili | bomu | ✓ | Wt |
| Hausa | bam | ✓ | M |
| Yoruba | bọ́m̀bù | ✓ | Wt |
| Quechua | bomba (Spanish loan) | ✓ | M |

**14/20 (15 lenient); regions 6 (no EA) → pass.** Median [bomba] → *bonba*.
Median: b after m in 8 of 14; then a (tl tr ru es qu) 5 against u (yo) and none (fa fr).

### design (Wt: [design](https://en.wiktionary.org/wiki/design#Translations), "art of designing")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 设计 shèjì | ✗ | Wt |
| Japanese | デザイン dezain | ✓ | Wt |
| Korean | 디자인 dijain | ✓ | Wt |
| Vietnamese | thiết kế | ✗ | Wt |
| Thai | การออกแบบ kaan ɔ̀ɔk bɛ̀ɛp | ✗ | Wt |
| Indonesian | desain | ✓ | Wt |
| Tagalog | disenyo (Wt coinage antangan) | ✓ | M |
| Hindi | डिज़ाइन dizāin | ✓ | Wt |
| Bengali | ডিজাইন ḍijāin | ✓ | M |
| Tamil | வடிவமைப்பு vaṭivamaippu; spoken design | ✗ (✓ lenient) | M |
| Persian | طراحی tarrāhi; دیزاین dizāyn | ✗ (✓ lenient) | Wt |
| Arabic | تصميم taṣmīm; ديزاين dīzāyn | ✗ (✓ lenient) | Wt |
| Turkish | tasarım; dizayn | ✗ (✓ lenient) | Wt |
| Russian | дизайн dizajn | ✓ | Wt |
| Spanish | diseño | ✓ | Wt |
| French | design (conception) | ✓ | Wt |
| Swahili | usanifu | ✗ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | diseño (Spanish loan) | ✓ | M |

**10/20 (14 lenient); regions 5 (no WA SSA) (6 lenient) → borderline.** Median [dizain] → *disayin*.
Spanish diseño (and Tagalog disenyo from it) are counted as the same word. In fa ar tr the loan dizāyn exists beside native tarrāhi/taṣmīm/tasarım, which carry the everyday weight.

### station (Wt: [station](https://en.wiktionary.org/wiki/station#Translations), "place where a vehicle may stop")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 站 zhàn | ✗ | Wt |
| Japanese | 駅 eki | ✗ | Wt |
| Korean | 역 yeok, 정류장 | ✗ | Wt |
| Vietnamese | ga (< French gare), trạm, bến | ✗ | Wt |
| Thai | สถานี sathǎanii (Sanskrit sthāna) | ✗ | Wt |
| Indonesian | stasiun | ✓ | Wt |
| Tagalog | estasyon | ✓ | Wt |
| Hindi | स्टेशन sṭešan | ✓ | Wt |
| Bengali | স্টেশন sṭešan | ✓ | Wt |
| Tamil | நிலையம் nilaiyam; spoken ṭēšan | ✗ (✓ lenient) | Wt, M |
| Persian | ایستگاه istgāh "stopping place" | ✗ | Wt |
| Arabic | محطة maḥaṭṭa | ✗ | Wt |
| Turkish | istasyon, gar, durak | ✓ | Wt |
| Russian | станция stantsija (вокзал main rail station) | ✓ | Wt |
| Spanish | estación | ✓ | Wt |
| French | gare; station (metro) | ✗ (✓ lenient) | Wt |
| Swahili | kituo; stesheni (railway) | ✗ (✓ lenient) | Wt, M |
| Hausa | tasha | ✓ | M |
| Yoruba | ibùdókọ̀ | ✗ | M |
| Quechua | estación (Spanish loan) | ✓ | M |

**9/20 (12 lenient); regions 6 (no EA) → borderline.** Median [stasjon] → *sutasuyon*.
Median: first vowel a (id tl tr ru es qu) over e (hi bn), s over ʃ, then -jon (tl tr es qu). The prothetic e/i of tl es tr qu is a minority.

### captain (Wt: [captain](https://en.wiktionary.org/wiki/captain#Translations), "the person lawfully in command of a sea-going vessel")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 船长 chuánzhǎng; 队长 duìzhǎng (team) | ✗ | Wt |
| Japanese | 船長 senchō; キャプテン kyaputen (team) | ✗ (✓ lenient) | Wt |
| Korean | 선장 seonjang; 캡틴 kaeptin (team) | ✗ (✓ lenient) | Wt |
| Vietnamese | thuyền trưởng | ✗ | Wt |
| Thai | กัปตัน kàptan | ✓ | Wt |
| Indonesian | kapten | ✓ | Wt |
| Tagalog | kapitan | ✓ | M |
| Hindi | कप्तान kaptān | ✓ | Wt |
| Bengali | ক্যাপ্টেন kyāpṭen | ✓ | Wt |
| Tamil | கேப்டன் kēpṭaṉ | ✓ | M |
| Persian | کاپیتان kāpitān, ناخدا nāxodā | ✓ | Wt |
| Arabic | قبطان qubṭān; كبتن kabtin (team) | ✓ | Wt |
| Turkish | kaptan | ✓ | Wt |
| Russian | капитан kapitan | ✓ | Wt |
| Spanish | capitán | ✓ | Wt |
| French | capitaine | ✓ | Wt |
| Swahili | nahodha (ship); kapteni (team) | ✓ | Wt |
| Hausa | kyaftin | ✓ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | capitán (Spanish loan) | ✓ | M |

**15/20 (17 lenient); regions 6 (no EA) (7 lenient) → pass.** Median [kaptan] → *kaputan*.
East Asia names captains by role (ship-head, team-head). Median: no vowel between p and t in 9 of 15, last vowel a 10 of 15.

### model (Wt: [model](https://en.wiktionary.org/wiki/model#Translations), "simplified representation")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 模型 móxíng; 模特 mótè (fashion) | ✗ | Wt |
| Japanese | モデル moderu (模型 mokei for a physical model) | ✓ | Wt, M* |
| Korean | 모델 model | ✓ | Wt |
| Vietnamese | mô hình; người mẫu (fashion) | ✗ | Wt |
| Thai | แบบจำลอง bɛ̀ɛp jamloong; โมเดล moodeen | ✗ (✓ lenient) | Wt |
| Indonesian | model | ✓ | Wt |
| Tagalog | modelo (Wt coinage hulwaran) | ✓ | M |
| Hindi | मॉडल mŏḍal | ✓ | Wt |
| Bengali | মডেল maḍel | ✓ | M |
| Tamil | மாதிரி mātiri | ✗ | M |
| Persian | مدل model | ✓ | Wt |
| Arabic | نموذج namūḏaj; موديل mūdīl (fashion, car) | ✗ (✓ lenient) | Wt |
| Turkish | model | ✓ | M |
| Russian | модель model' | ✓ | Wt |
| Spanish | modelo | ✓ | Wt |
| French | modèle | ✓ | Wt |
| Swahili | modeli | ✓ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | modelo (Spanish loan) | ✓ | M |

**13/20 (15 lenient); regions all 7 → pass.** Median [model] → *modelu*.
Median: consonant-final (ko id hi bn fa tr ru fr) 8 against -o (tl es qu) and -u/-i.

### virus (Wt: [virus](https://en.wiktionary.org/wiki/virus#Translations), "infectious organism")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 病毒 bìngdú | ✗ | Wt |
| Japanese | ウイルス uirusu | ✓ | Wt |
| Korean | 바이러스 baireoseu | ✓ | Wt |
| Vietnamese | vi-rút | ✓ | Wt |
| Thai | ไวรัส wairát | ✓ | Wt, M* |
| Indonesian | virus | ✓ | Wt |
| Tagalog | birus, virus | ✓ | Wt |
| Hindi | वाइरस vāiras (formal विषाणु) | ✓ | Wt, M* |
| Bengali | ভাইরাস bhāiras | ✓ | Wt |
| Tamil | தீ நுண்மம் (coinage); spoken vairas | ✗ (✓ lenient) | Wt, M |
| Persian | ویروس virus | ✓ | Wt |
| Arabic | فيروس fīrūs | ✓ | Wt |
| Turkish | virüs | ✓ | Wt |
| Russian | вирус virus | ✓ | Wt |
| Spanish | virus | ✓ | Wt |
| French | virus | ✓ | Wt |
| Swahili | virusi | ✓ | Wt |
| Hausa | ƙwayar cuta | ✗ | M |
| Yoruba | kòkòrò àrùn | ✗ | M |
| Quechua | añaw (Wt); virus in bilingual speech | ✗ (✓ lenient) | Wt, M |

**15/20 (17 lenient); regions 6 (no AM) (7 lenient) → pass.** Median [virus] → *bilusu*.
Median: i (Latin pronunciation) 11 against ai (ko th hi bn, from English) 4.

### restaurant (Wt: [restaurant](https://en.wiktionary.org/wiki/restaurant#Translations), "an eating establishment in which diners are served food")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 餐厅 cāntīng, 饭馆 | ✗ | Wt |
| Japanese | レストラン resutoran | ✓ | Wt |
| Korean | 식당 sikdang; 레스토랑 (Western) | ✗ (✓ lenient) | Wt |
| Vietnamese | nhà hàng, quán ăn | ✗ | Wt |
| Thai | ร้านอาหาร ráan aahǎan | ✗ | Wt |
| Indonesian | restoran, rumah makan | ✓ | Wt |
| Tagalog | restawran | ✓ | Wt |
| Hindi | रेस्तरां restarā̃ (formal भोजनालय) | ✓ | Wt, M* |
| Bengali | রেস্টুরেন্ট resṭurenṭ | ✓ | Wt |
| Tamil | உணவகம் uṇavakam, ஓட்டல் ōṭṭal | ✗ | Wt |
| Persian | رستوران restorān | ✓ | Wt |
| Arabic | مطعم maṭʿam | ✗ | Wt |
| Turkish | restoran, lokanta | ✓ | Wt |
| Russian | ресторан restoran | ✓ | Wt |
| Spanish | restaurante | ✓ | Wt |
| French | restaurant | ✓ | Wt |
| Swahili | mkahawa, hoteli | ✗ | Wt |
| Hausa | gidan abinci | ✗ | M |
| Yoruba | ilé-oúnjẹ "food house" | ✗ | Wt |
| Quechua | mikhuna wasi "food house" (Wt); restaurante in bilingual speech | ✗ (✓ lenient) | Wt, M |

**10/20 (12 lenient); regions 5 (no SSA AM) (6 lenient) → borderline.** Median [restoran] → *lesutolan*.
Several languages use the hotel word for an eating place (ta ōṭṭal, sw hoteli), and "food house/shop" is the common native build.

### ticket (Wt: [ticket](https://en.wiktionary.org/wiki/ticket#Translations), "pass for transportation")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 票 piào | ✗ | Wt |
| Japanese | 切符 kippu (train); チケット chiketto (events) | ✓ | Wt |
| Korean | 티켓 tiket, 표 pyo | ✓ | Wt |
| Vietnamese | vé | ✗ | Wt |
| Thai | ตั๋ว tǔa | ✗ | Wt |
| Indonesian | tiket | ✓ | Wt |
| Tagalog | tiket | ✓ | M |
| Hindi | टिकट ṭikaṭ | ✓ | Wt |
| Bengali | টিকেট ṭikeṭ | ✓ | Wt |
| Tamil | டிக்கெட் ṭikkeṭ | ✓ | M |
| Persian | بلیت belit | ✗ | Wt |
| Arabic | تذكرة taḏkira | ✗ | Wt |
| Turkish | bilet | ✗ | Wt |
| Russian | билет bilet | ✗ | Wt |
| Spanish | boleto, billete (tiquete in Colombia) | ✗ | Wt |
| French | billet; ticket (metro, bus) | ✗ (✓ lenient) | Wt |
| Swahili | tiketi | ✓ | Wt |
| Hausa | tikiti | ✓ | M |
| Yoruba | tíkẹ́ẹ̀tì | ✓ | M |
| Quechua | boleto (Spanish loan) | ✗ | M |

**10/20 (11 lenient); regions 4 (no WA EU AM) (5 lenient) → fail.**
The two international forms split the panel: ticket (Asia, Africa) and billet (fa tr ru es fr, plus es boleto). Neither reaches 12, so the panel does not choose; zh piào, vi vé, th tǔa and ar taḏkira are native.

### budget (Wt: [budget](https://en.wiktionary.org/wiki/budget#Translations), "amount of money or resources earmarked for a particular institution, activity or time-frame")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 预算 yùsuàn | ✗ | Wt |
| Japanese | 予算 yosan | ✗ | Wt |
| Korean | 예산 yesan | ✗ | Wt |
| Vietnamese | ngân sách | ✗ | Wt |
| Thai | งบประมาณ ngóp pramaan | ✗ | Wt |
| Indonesian | anggaran; bujet | ✗ (✓ lenient) | Wt |
| Tagalog | badyet | ✓ | M |
| Hindi | बजट bajaṭ | ✓ | Wt |
| Bengali | বাজেট bājeṭ | ✓ | Wt |
| Tamil | வரவு-செலவுத் திட்டம்; spoken bajeṭ | ✗ (✓ lenient) | M |
| Persian | بودجه budje | ✓ | Wt |
| Arabic | ميزانية mīzāniyya | ✗ | Wt |
| Turkish | bütçe | ✓ | Wt |
| Russian | бюджет bjudžet | ✓ | Wt |
| Spanish | presupuesto | ✗ | Wt |
| French | budget | ✓ | Wt |
| Swahili | bajeti | ✓ | Wt |
| Hausa | kasafin kuɗi | ✗ | M |
| Yoruba | ìṣúná | ✗ | M |
| Quechua | presupuesto (Spanish loan) | ✗ | M |

**8/20 (10 lenient); regions 5 (no EA AM) → fail.**

### league (Wt: [league](https://en.wiktionary.org/wiki/league#Translations), "organization of sports teams")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 联赛 liánsài, 联盟 | ✗ | Wt |
| Japanese | リーグ rīgu | ✓ | Wt |
| Korean | 리그 rigeu | ✓ | Wt |
| Vietnamese | giải, hạng | ✗ | Wt |
| Thai | ลีก líik | ✓ | Wt |
| Indonesian | liga | ✓ | Wt |
| Tagalog | liga | ✓ | Wt |
| Hindi | लीग līg | ✓ | Wt |
| Bengali | লিগ lig | ✓ | Wt |
| Tamil | லீக் līk | ✓ | M |
| Persian | لیگ lig | ✓ | Wt |
| Arabic | دوري dawrī | ✗ | Wt |
| Turkish | lig | ✓ | Wt |
| Russian | лига liga | ✓ | Wt |
| Spanish | liga | ✓ | Wt |
| French | ligue | ✓ | Wt |
| Swahili | ligi | ✓ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | liga (Spanish loan) | ✓ | M |

**15/20; regions all 7 → pass.** Median [liga] → *liga*.
Final vowel: present in 8 (a: id tl ru es qu; u: ja ko; i: sw) against 7 consonant-final (th hi bn ta fa tr fr). [lig] would give *ligu*.

### album (Wt: [album](https://en.wiktionary.org/wiki/album#Translations), "book for photographs, stamps, or autographs")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 相册 xiàngcè, 专辑 zhuānjí (music) | ✗ | Wt |
| Japanese | アルバム arubamu | ✓ | Wt |
| Korean | 앨범 aelbeom | ✓ | Wt |
| Vietnamese | an-bom, album | ✓ | Wt |
| Thai | อัลบั้ม anlabâm | ✓ | Wt |
| Indonesian | album | ✓ | Wt |
| Tagalog | album | ✓ | Wt |
| Hindi | अलबम albam | ✓ | Wt |
| Bengali | অ্যালবাম ælbām | ✓ | Wt |
| Tamil | ஆல்பம் ālbam | ✓ | M |
| Persian | آلبوم ālbom | ✓ | Wt |
| Arabic | ألبوم albūm | ✓ | Wt |
| Turkish | albüm | ✓ | Wt |
| Russian | альбом al'bom | ✓ | Wt |
| Spanish | álbum | ✓ | Wt |
| French | album | ✓ | Wt |
| Swahili | albamu | ✓ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | álbum (Spanish loan) | ✓ | M |

**17/20; regions all 7 → pass.** Median [album] → *alubumu*.
Second vowel u (ja id tl ar es fr qu, tr y) 8 against a (ko th hi bn ta sw) 6 and o (vi fa ru) 3.

### philosophy (Wt: [philosophy](https://en.wiktionary.org/wiki/philosophy#Translations), "academic discipline")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 哲学 zhéxué | ✗ | Wt |
| Japanese | 哲学 tetsugaku | ✗ | Wt |
| Korean | 철학 cheolhak | ✗ | Wt |
| Vietnamese | triết học | ✗ | Wt |
| Thai | ปรัชญา pràtyaa | ✗ | Wt |
| Indonesian | filsafat (< Arabic falsafa) | ✓ | Wt |
| Tagalog | pilosopiya | ✓ | Wt |
| Hindi | दर्शन darśan; फ़लसफ़ा falsafā (Urdu) | ✗ (✓ lenient) | Wt |
| Bengali | দর্শন darśan | ✗ | M |
| Tamil | தத்துவம் tattuvam | ✗ | Wt |
| Persian | فلسفه falsafe | ✓ | Wt |
| Arabic | فلسفة falsafa | ✓ | Wt |
| Turkish | felsefe | ✓ | Wt |
| Russian | философия filosofija | ✓ | Wt |
| Spanish | filosofía | ✓ | Wt |
| French | philosophie | ✓ | Wt |
| Swahili | falsafa | ✓ | Wt |
| Hausa | falsafa | ✓ | M |
| Yoruba | ìmọ̀ ọgbọ́n | ✗ | M |
| Quechua | filosofía (Spanish loan) | ✓ | M |

**11/20 (12 lenient); regions 5 (no EA SA) (6 lenient) → borderline.** Median [filsafa] → *filusafa*.
The Arabic-mediated falsafa (id fa ar tr sw ha) and the Greek-Latin filosofia (tl ru es fr qu) share the skeleton f-l-s-f and are counted as one word. The per-position median blends them: [filsafa].

### channel (Wt: [channel](https://en.wiktionary.org/wiki/channel#Translations), "broadcasting: specific radio frequency or band of frequencies used for transmitting television")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 频道 píndào | ✗ | Wt |
| Japanese | チャンネル channeru | ✓ | Wt |
| Korean | 채널 chaeneol | ✓ | Wt |
| Vietnamese | kênh | ✗ | Wt |
| Thai | ช่อง chɔ̂ng | ✗ | Wt |
| Indonesian | saluran; kanal | ✗ (✓ lenient) | M |
| Tagalog | channel (Wt coinage alunan) | ✓ | M |
| Hindi | चैनल cainal | ✓ | Wt |
| Bengali | চ্যানেল cyānel | ✓ | Wt |
| Tamil | சேனல் cēṉal | ✓ | M |
| Persian | کانال kānāl | ✗ (✓ lenient) | Wt |
| Arabic | قناة qanāt | ✗ | Wt |
| Turkish | kanal | ✗ (✓ lenient) | Wt |
| Russian | канал kanal | ✗ (✓ lenient) | Wt |
| Spanish | canal | ✗ (✓ lenient) | Wt |
| French | chaîne | ✗ | Wt |
| Swahili | chaneli | ✓ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | canal (Spanish loan) | ✗ (✓ lenient) | M |

**7/20 (13 lenient); regions 4 (no WA EU AM) (7 lenient) → borderline.** Median [tʃanel] → *tanelu*.
The panel splits between English channel (ja ko tl hi bn ta sw) and Latin-Romance kanal (fa tr ru es qu, id). They share an etymon but tʃanel and kanal are not heard as one word. Neither form passes alone. Median of the channel form [tʃanel]; [kanal] would give *kanalu*.

### robot (Wt: [robot](https://en.wiktionary.org/wiki/robot#Translations), "intelligent mechanical being")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 机器人 jīqìrén "machine person" | ✗ | Wt |
| Japanese | ロボット robotto | ✓ | Wt |
| Korean | 로봇 robot | ✓ | Wt |
| Vietnamese | rô-bốt, người máy | ✓ | Wt, M* |
| Thai | หุ่นยนต์ hùn yon; โรบอต roobɔ̀t | ✗ (✓ lenient) | Wt |
| Indonesian | robot | ✓ | Wt |
| Tagalog | robot | ✓ | Wt |
| Hindi | रोबोट robot | ✓ | Wt |
| Bengali | রোবট robaṭ | ✓ | Wt |
| Tamil | ரோபோ robo | ✓ | Wt |
| Persian | روبات robāt | ✓ | Wt |
| Arabic | روبوت rūbūt | ✓ | Wt |
| Turkish | robot | ✓ | Wt |
| Russian | робот robot | ✓ | Wt |
| Spanish | robot | ✓ | Wt |
| French | robot | ✓ | Wt |
| Swahili | roboti | ✓ | Wt |
| Hausa | saƙago | ✗ | Wt |
| Yoruba | (no data) | ✗ (✓ lenient) | M |
| Quechua | antapunqu (coinage); robot in bilingual speech | ✗ (✓ lenient) | Wt, M |

**15/20 (18 lenient); regions 6 (no AM) (7 lenient) → pass.** Median [robot] → *lobotu*.

### mile (Wt: [mile](https://en.wiktionary.org/wiki/mile#Translations), "measure of length")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 英里 yīnglǐ "English li" | ✗ | Wt |
| Japanese | マイル mairu | ✓ | Wt |
| Korean | 마일 mail | ✓ | Wt |
| Vietnamese | dặm | ✗ | Wt |
| Thai | ไมล์ mai | ✓ | Wt |
| Indonesian | mil | ✓ | Wt |
| Tagalog | milya | ✓ | Wt |
| Hindi | मील mīl | ✓ | Wt |
| Bengali | মাইল māil | ✓ | Wt |
| Tamil | மைல் mail | ✓ | Wt |
| Persian | مایل māyl | ✓ | Wt |
| Arabic | ميل mīl | ✓ | Wt |
| Turkish | mil | ✓ | Wt |
| Russian | миля milja | ✓ | Wt |
| Spanish | milla | ✓ | Wt |
| French | mille | ✓ | Wt |
| Swahili | maili | ✓ | M |
| Hausa | mil | ✓ | M |
| Yoruba | máìlì | ✓ | Wt |
| Quechua | milla (Spanish loan) | ✓ | M |

**18/20; regions all 7 → pass.** Median [mil] → *milu*.
The panel shares the word, but the unit is outside the metric standard the language follows (L3); whether it needs a word at all is for the author. Vowel i (Latin mil-) 9 against ai (English) 8.

### pound (Wt: [pound](https://en.wiktionary.org/wiki/pound#Translations), "unit of currency")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 镑 bàng | ✓ | Wt |
| Japanese | ポンド pondo | ✓ | Wt |
| Korean | 파운드 paundeu | ✓ | Wt |
| Vietnamese | bảng | ✓ | Wt |
| Thai | ปอนด์ pɔn | ✓ | Wt |
| Indonesian | paun | ✓ | Wt |
| Tagalog | libra | ✗ | M |
| Hindi | पाउंड pāuṇḍ | ✓ | Wt |
| Bengali | পাউন্ড pāunḍ | ✓ | Wt |
| Tamil | பவுண்டு pavuṇṭu | ✓ | M |
| Persian | پوند pond | ✓ | Wt |
| Arabic | جنيه junayh (< guinea) | ✗ | Wt |
| Turkish | sterlin, pound | ✗ | M |
| Russian | фунт funt | ✗ (✓ lenient) | Wt |
| Spanish | libra | ✗ | Wt |
| French | livre | ✗ | Wt |
| Swahili | pauni | ✓ | Wt |
| Hausa | fam | ✗ (✓ lenient) | Wt |
| Yoruba | pọ́n-ùn | ✗ (✓ lenient) | M |
| Quechua | libra (Spanish loan) | ✗ | M |

**11/20 (14 lenient); regions 5 (no EU AM) (6 lenient) → borderline.** Median [paund] → *pawundu*.
As a currency, loans.md's pattern 2 applies: the issuer's name (pound sterling) may settle it as a name rather than a loan. Russian funt and Hausa fam come from pound but are hard to hear as it.

### cigarette (Wt: [cigarette](https://en.wiktionary.org/wiki/cigarette#Translations), "thin roll of tobacco made for smoking")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 香烟 xiāngyān | ✗ | Wt |
| Japanese | タバコ tabako | ✗ | Wt |
| Korean | 담배 dambae | ✗ | Wt |
| Vietnamese | thuốc lá | ✗ | Wt |
| Thai | บุหรี่ burìi | ✗ | Wt |
| Indonesian | rokok | ✗ | Wt |
| Tagalog | sigarilyo, yosi | ✓ | Wt |
| Hindi | सिगरेट sigreṭ | ✓ | Wt |
| Bengali | সিগারেট sigāreṭ | ✓ | Wt |
| Tamil | சிகரெட் sikareṭ | ✓ | Wt |
| Persian | سیگار sigār, سیگارت | ✓ | Wt |
| Arabic | سيجارة sījāra | ✓ | Wt |
| Turkish | sigara | ✓ | Wt |
| Russian | сигарета sigareta | ✓ | Wt |
| Spanish | cigarrillo | ✓ | Wt |
| French | cigarette | ✓ | Wt |
| Swahili | sigara | ✓ | Wt |
| Hausa | taba; sigari | ✗ (✓ lenient) | M |
| Yoruba | sìgá | ✓ | M |
| Quechua | cigarro (Spanish loan) | ✓ | M |

**13/20 (14 lenient); regions 6 (no EA) → pass.** Median [sigaret] → *sigaletu*.
Median: after sigar-, e (hi bn ta fa ru fr) 6 is a plurality over a (ar tr sw) 3; then t in 6 against 4 endings.

### club (Wt: [club](https://en.wiktionary.org/wiki/club#Translations), "association of members")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 俱乐部 jùlèbù (sound loan) | ✓ | Wt |
| Japanese | クラブ kurabu | ✓ | Wt |
| Korean | 동아리 dongari, 동호회; 클럽 (nightclub, football club) | ✗ (✓ lenient) | Wt |
| Vietnamese | câu lạc bộ (< 俱樂部) | ✓ | Wt |
| Thai | สโมสร samooson; คลับ khláp | ✗ (✓ lenient) | Wt |
| Indonesian | klub | ✓ | Wt |
| Tagalog | klab | ✓ | M |
| Hindi | क्लब klab | ✓ | Wt |
| Bengali | ক্লাব klāb | ✓ | Wt |
| Tamil | கழகம் kaḻakam; spoken klap | ✗ (✓ lenient) | M |
| Persian | باشگاه bāšgāh | ✗ | Wt |
| Arabic | نادي nādī | ✗ | Wt |
| Turkish | kulüp | ✓ | Wt |
| Russian | клуб klub | ✓ | Wt |
| Spanish | club | ✓ | Wt |
| French | club | ✓ | Wt |
| Swahili | klabu | ✓ | Wt |
| Hausa | kulob | ✓ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | club (Spanish loan) | ✓ | M |

**14/20 (17 lenient); regions all 7 → pass.** Median [klab] → *kulabu*.
Mandarin jùlèbù and Vietnamese câu lạc bộ are sound loans (via Japanese 倶楽部) and count. Main vowel a (ja tl hi bn sw vi) 6 against u (id ru es qu, tr y) 5.

### campaign (Wt: [campaign](https://en.wiktionary.org/wiki/campaign#Translations), "series of operations undertaken to achieve a set goal")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 活动 huódòng | ✗ | Wt |
| Japanese | キャンペーン kyanpēn | ✓ | Wt |
| Korean | 캠페인 kaempein | ✓ | Wt |
| Vietnamese | chiến dịch | ✗ | Wt |
| Thai | การรณรงค์ kaan ronnarong | ✗ | Wt |
| Indonesian | kampanye | ✓ | Wt |
| Tagalog | kampanya | ✓ | Wt |
| Hindi | अभियान abhiyān, मुहिम | ✗ | Wt |
| Bengali | প্রচার pracār | ✗ | Wt |
| Tamil | பிரச்சாரம் piraccāram | ✗ | M |
| Persian | کارزار kārzār; کمپین kampein | ✗ (✓ lenient) | Wt |
| Arabic | حملة ḥamla | ✗ | Wt |
| Turkish | kampanya | ✓ | Wt |
| Russian | кампания kampanija | ✓ | Wt |
| Spanish | campaña | ✓ | Wt |
| French | campagne | ✓ | Wt |
| Swahili | kampeni | ✓ | Wt |
| Hausa | kamfe | ✓ | M |
| Yoruba | ìpolongo | ✗ | M |
| Quechua | campaña (Spanish loan) | ✓ | M |

**11/20 (12 lenient); regions 6 (no SA) → borderline.** Median [kampaɲa] → *kanpana*.
South Asia (abhiyān, pracār) and Arabic ḥamla are native.

### taxi (Wt: [taxi](https://en.wiktionary.org/wiki/taxi#Translations), "vehicle available for public hire")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 出租车 chūzūchē (的士 dīshì in Hong Kong) | ✗ | Wt |
| Japanese | タクシー takushī | ✓ | Wt |
| Korean | 택시 taeksi | ✓ | Wt |
| Vietnamese | tắc-xi | ✓ | Wt |
| Thai | แท็กซี่ thɛ́ksîi | ✓ | Wt |
| Indonesian | taksi | ✓ | Wt |
| Tagalog | taxi | ✓ | Wt |
| Hindi | टैक्सी ṭaiksī | ✓ | Wt |
| Bengali | ট্যাক্সি ṭyāksi | ✓ | Wt |
| Tamil | டாக்ஸி ṭāksi | ✓ | Wt |
| Persian | تاکسی tāksi | ✓ | Wt |
| Arabic | تاكسي tāksī | ✓ | Wt |
| Turkish | taksi | ✓ | Wt |
| Russian | такси taksi | ✓ | Wt |
| Spanish | taxi | ✓ | Wt |
| French | taxi | ✓ | Wt |
| Swahili | teksi | ✓ | Wt |
| Hausa | tasi | ✓ | Wt |
| Yoruba | takisí | ✓ | Wt |
| Quechua | taxi (Spanish loan) | ✓ | M |

**19/20; regions all 7 → pass.** Median [taksi] → *takusi*.

### gas (Wt: [gas](https://en.wiktionary.org/wiki/gas#Translations), "(uncountable, chemistry) state of matter")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 气体 qìtǐ, 气 | ✗ | Wt |
| Japanese | 気体 kitai; ガス gasu (fuel gas) | ✗ (✓ lenient) | Wt |
| Korean | 가스 gaseu, 기체 | ✓ | Wt |
| Vietnamese | khí; ga (fuel gas) | ✗ (✓ lenient) | Wt |
| Thai | ก๊าซ kɛ́ɛt | ✓ | Wt |
| Indonesian | gas | ✓ | Wt |
| Tagalog | gas (Wt coinage buhag) | ✓ | M |
| Hindi | गैस gais | ✓ | Wt |
| Bengali | গ্যাস gyās | ✓ | Wt |
| Tamil | வாயு vāyu; spoken gas | ✗ (✓ lenient) | Wt, M |
| Persian | گاز gāz | ✓ | Wt |
| Arabic | غاز ġāz | ✓ | Wt |
| Turkish | gaz | ✓ | Wt |
| Russian | газ gaz | ✓ | Wt |
| Spanish | gas | ✓ | Wt |
| French | gaz | ✓ | Wt |
| Swahili | gesi | ✓ | Wt |
| Hausa | gas | ✓ | M |
| Yoruba | gáàsì | ✓ | Wt |
| Quechua | gas (Spanish loan) | ✓ | M |

**16/20 (19 lenient); regions all 7 → pass.** Median [gas] → *gasu*.
s (ko th id tl hi bn es sw ha yo qu) against z (fa ar tr ru fr).

### museum (Wt: [museum](https://en.wiktionary.org/wiki/museum#Translations), "building or institution")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 博物馆 bówùguǎn | ✗ | Wt |
| Japanese | 博物館 hakubutsukan | ✗ | Wt |
| Korean | 박물관 bangmulgwan | ✗ | Wt |
| Vietnamese | bảo tàng | ✗ | Wt |
| Thai | พิพิธภัณฑ์ phíphítthaphan | ✗ | Wt |
| Indonesian | museum | ✓ | Wt |
| Tagalog | museo | ✓ | Wt |
| Hindi | संग्रहालय saṅgrahālay; म्यूज़ियम myūziyam | ✗ (✓ lenient) | Wt |
| Bengali | জাদুঘর jādughar "magic house" | ✗ | Wt |
| Tamil | அருங்காட்சியகம் aruṅkāṭciyakam | ✗ | Wt |
| Persian | موزه muze | ✓ | Wt |
| Arabic | متحف matḥaf | ✗ | Wt |
| Turkish | müze | ✓ | Wt |
| Russian | музей muzej | ✓ | Wt |
| Spanish | museo | ✓ | Wt |
| French | musée | ✓ | Wt |
| Swahili | makumbusho | ✗ | Wt |
| Hausa | gidan tarihi "history house" | ✗ | M |
| Yoruba | ilé ìṣẹ̀ǹbáyé | ✗ | M |
| Quechua | museo (Spanish loan) | ✓ | M |

**8/20 (9 lenient); regions 4 (no EA SA SSA) (5 lenient) → fail.**

### alcohol (Wt: [alcohol](https://en.wiktionary.org/wiki/alcohol#Translations), "intoxicating beverage")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 酒 jiǔ | ✗ | Wt |
| Japanese | お酒 osake; アルコール arukōru | ✗ (✓ lenient) | Wt |
| Korean | 술 sul; 알코올 alkool | ✗ (✓ lenient) | Wt |
| Vietnamese | rượu | ✗ | Wt |
| Thai | เหล้า lâo, สุรา | ✗ | Wt |
| Indonesian | alkohol, minuman keras | ✓ | Wt |
| Tagalog | alak (< Arabic ʿaraq) | ✗ | M |
| Hindi | शराब šarāb, दारू | ✗ | Wt |
| Bengali | মদ mad | ✗ | Wt |
| Tamil | மது madhu | ✗ | M |
| Persian | عرق ʿaraq, مشروب | ✗ | Wt |
| Arabic | كحول kuḥūl (the etymon of alcohol) | ✗ (✓ lenient) | Wt |
| Turkish | içki; alkol | ✓ | Wt |
| Russian | алкоголь alkogol', спиртное | ✓ | Wt |
| Spanish | alcohol | ✓ | Wt |
| French | alcool | ✓ | Wt |
| Swahili | pombe | ✗ | M |
| Hausa | giya | ✗ | M |
| Yoruba | ọtí | ✗ | M |
| Quechua | trago (Spanish), aqha (chicha) | ✗ | M |

**5/20 (8 lenient); regions 3 (SEA WA EU) (4 lenient) → fail.**

### engine (Wt: [engine](https://en.wiktionary.org/wiki/engine#Translations), "mechanical device")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 发动机 fādòngjī, 引擎 yǐnqíng (sound loan of engine) | ✗ | Wt |
| Japanese | エンジン enjin (モーター mōtā = electric motor) | ✗ | Wt |
| Korean | 엔진 enjin (모터 = electric motor) | ✗ | Wt |
| Vietnamese | động cơ (mô-tơ = electric motor) | ✗ | Wt |
| Thai | เครื่องยนต์ khrʉ̂ang yon (มอเตอร์ = electric motor) | ✗ | Wt |
| Indonesian | mesin (motor = motorcycle) | ✗ | Wt |
| Tagalog | makina | ✗ | M |
| Hindi | इंजन injan (मोटर = electric motor) | ✗ | Wt |
| Bengali | ইঞ্জিন iñjin (মোটর = electric motor) | ✗ | Wt |
| Tamil | இன்ஜின் injin | ✗ | M |
| Persian | موتور motor | ✓ | Wt |
| Arabic | محرك muḥarrik; colloquial موتور mōtōr | ✗ (✓ lenient) | Wt |
| Turkish | motor | ✓ | Wt |
| Russian | двигатель dvigatel'; мотор motor | ✗ (✓ lenient) | Wt |
| Spanish | motor | ✓ | Wt |
| French | moteur | ✓ | Wt |
| Swahili | injini | ✗ | Wt |
| Hausa | inji | ✗ | M |
| Yoruba | ẹ́ńjìnnì | ✗ | M |
| Quechua | motor (Spanish loan) | ✓ | M |

**5/20 (7 lenient); regions 3 (WA EU AM) → fail.**
Shared column = the motor form proposed in the ladder note. The panel splits between two loans for a car engine: engine (ja ko hi bn ta sw ha yo, 8 in 3 regions, plus zh yǐnqíng) and motor (fa tr es fr qu, plus colloquial ar ru). Where both exist, motor usually means an electric motor. Neither passes.

### chemistry (Wt: [chemistry](https://en.wiktionary.org/wiki/chemistry#Translations), "branch of natural science")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 化学 huàxué | ✗ | Wt |
| Japanese | 化学 kagaku | ✗ | Wt |
| Korean | 화학 hwahak | ✗ | Wt |
| Vietnamese | hóa học | ✗ | Wt |
| Thai | เคมี khemii | ✓ | Wt |
| Indonesian | kimia | ✓ | Wt |
| Tagalog | kimika | ✓ | Wt |
| Hindi | रसायन शास्त्र rasāyan šāstra | ✗ | Wt |
| Bengali | রসায়ন rasāyan | ✗ | Wt |
| Tamil | வேதியியல் vētiyiyal | ✗ | Wt |
| Persian | شیمی šimi (< French chimie) | ✓ | Wt |
| Arabic | كيمياء kīmiyāʾ | ✓ | Wt |
| Turkish | kimya | ✓ | Wt |
| Russian | химия ximija | ✓ | Wt |
| Spanish | química | ✓ | Wt |
| French | chimie | ✓ | Wt |
| Swahili | kemia | ✓ | Wt |
| Hausa | kimiyya | ✓ | M |
| Yoruba | kẹ́mísírì | ✓ | M |
| Quechua | química (Spanish loan) | ✓ | M |

**13/20; regions 5 (no EA SA) → pass.** Median [kimia] → *kimiya*.
EA uses Sino 化学 and SA Sanskrit rasāyan. French and Persian ʃimi are counted with kimia; without them it is 11 and fails. Median: k 10, first vowel i 10, final a.

### guitar (Wt: [guitar](https://en.wiktionary.org/wiki/guitar#Translations), "musical instrument")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 吉他 jítā | ✓ | Wt |
| Japanese | ギター gitā | ✓ | Wt |
| Korean | 기타 gita | ✓ | Wt |
| Vietnamese | ghi-ta | ✓ | Wt |
| Thai | กีตาร์ kiitaa | ✓ | Wt |
| Indonesian | gitar | ✓ | Wt |
| Tagalog | gitara | ✓ | Wt |
| Hindi | गिटार giṭār | ✓ | Wt |
| Bengali | গিটার giṭār | ✓ | Wt |
| Tamil | கித்தார் kittār | ✓ | Wt |
| Persian | گیتار gitār | ✓ | Wt |
| Arabic | جيتار gītār (classical قيثارة qīṯāra) | ✓ | Wt |
| Turkish | gitar | ✓ | Wt |
| Russian | гитара gitara | ✓ | Wt |
| Spanish | guitarra | ✓ | Wt |
| French | guitare | ✓ | Wt |
| Swahili | gitaa | ✓ | Wt |
| Hausa | gita | ✓ | M |
| Yoruba | gìtá | ✓ | M |
| Quechua | guitarra (Spanish loan) | ✓ | M |

**20/20; regions all 7 → pass.** Median [gitar] → *gitalu*.

### metal (Wt: [metal](https://en.wiktionary.org/wiki/metal#Translations), "atomic element or material made of such atoms")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 金属 jīnshǔ | ✗ | Wt |
| Japanese | 金属 kinzoku | ✗ | Wt |
| Korean | 금속 geumsok | ✗ | Wt |
| Vietnamese | kim loại | ✗ | Wt |
| Thai | โลหะ lohà | ✗ | Wt |
| Indonesian | logam | ✗ | Wt |
| Tagalog | metal | ✓ | Wt |
| Hindi | धातु dhātu | ✗ | Wt |
| Bengali | ধাতু dhātu | ✗ | Wt |
| Tamil | உலோகம் ulōkam | ✗ | Wt |
| Persian | فلز felez | ✗ | Wt |
| Arabic | معدن maʿdin, فلز filizz | ✗ | Wt |
| Turkish | metal | ✓ | Wt |
| Russian | металл metall | ✓ | Wt |
| Spanish | metal | ✓ | Wt |
| French | métal | ✓ | Wt |
| Swahili | metali | ✓ | Wt |
| Hausa | ƙarfe | ✗ | M |
| Yoruba | irin | ✗ | M |
| Quechua | chuqi, q'illay | ✗ | Wt |

**6/20; regions 4 (no EA SA AM) → fail.**

### climate (Wt: [climate](https://en.wiktionary.org/wiki/climate#Translations), "long-term atmospheric conditions")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 气候 qìhòu | ✗ | Wt |
| Japanese | 気候 kikō | ✗ | Wt |
| Korean | 기후 gihu | ✗ | Wt |
| Vietnamese | khí hậu | ✗ | Wt |
| Thai | ภูมิอากาศ phuumí-aakàat | ✗ | Wt |
| Indonesian | iklim | ✓ | Wt |
| Tagalog | klima | ✓ | Wt |
| Hindi | जलवायु jalvāyu "water-air" | ✗ | Wt |
| Bengali | জলবায়ু jalbāyu | ✗ | Wt |
| Tamil | காலநிலை kālanilai | ✗ | Wt |
| Persian | آب و هوا āb o havā "water and air"; اقلیم eqlim | ✗ (✓ lenient) | Wt |
| Arabic | مناخ munāx | ✗ | Wt |
| Turkish | iklim | ✓ | Wt |
| Russian | климат klimat | ✓ | Wt |
| Spanish | clima | ✓ | Wt |
| French | climat | ✓ | Wt |
| Swahili | tabianchi | ✗ | Wt |
| Hausa | yanayi | ✗ | M |
| Yoruba | ojú-ọjọ́ | ✗ | M |
| Quechua | clima (Spanish loan) | ✓ | M |

**7/20 (8 lenient); regions 4 (no EA SA SSA) → fail.**

### gene (Wt: [gene](https://en.wiktionary.org/wiki/gene#Translations), "unit of heredity")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 基因 jīyīn (sound loan) | ✓ | Wt |
| Japanese | 遺伝子 idenshi | ✗ | Wt |
| Korean | 유전자 yujeonja | ✗ | Wt |
| Vietnamese | gen | ✓ | Wt |
| Thai | ยีน yiin (Wt gives a coinage) | ✓ | M |
| Indonesian | gen | ✓ | Wt |
| Tagalog | hene | ✓ | Wt |
| Hindi | जीन jīn | ✓ | Wt |
| Bengali | জিন jin | ✓ | Wt |
| Tamil | மரபணு marapaṇu | ✗ | Wt |
| Persian | ژن žen | ✓ | Wt |
| Arabic | جين jīn, مورثة | ✓ | Wt, M* |
| Turkish | gen | ✓ | Wt |
| Russian | ген gen | ✓ | Wt |
| Spanish | gen | ✓ | Wt |
| French | gène | ✓ | Wt |
| Swahili | jeni | ✓ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | gen (Spanish loan) | ✓ | M |

**15/20; regions all 7 → pass.** Median [dʒen] → *denu*.
Initial consonant: dʒ (zh hi bn ar sw) 5, g (id tr ru) 3, ʒ (vi fa fr) 3, x/h (tl es qu) 3. Vowel e 10 against i 5. names.py adds a vowel to reach two syllables.

### pilot (Wt: [pilot](https://en.wiktionary.org/wiki/pilot#Translations), "controller of aircraft|aviator")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 飞行员 fēixíngyuán | ✗ | Wt |
| Japanese | パイロット pairotto | ✓ | Wt |
| Korean | 파일럿 pailleot, 조종사 | ✓ | Wt |
| Vietnamese | phi công | ✗ | Wt |
| Thai | นักบิน nák bin | ✗ | Wt |
| Indonesian | pilot | ✓ | Wt |
| Tagalog | piloto | ✓ | Wt |
| Hindi | पायलट pāylaṭ | ✓ | Wt |
| Bengali | বিমান চালক bimān cālak; spoken pāilaṭ | ✗ (✓ lenient) | Wt, M |
| Tamil | பைலட் pailaṭ, வானோடி | ✓ | Wt |
| Persian | خلبان xalabān (پیلوت rare) | ✗ | Wt |
| Arabic | طيار ṭayyār | ✗ | Wt |
| Turkish | pilot | ✓ | Wt |
| Russian | пилот pilot, лётчик | ✓ | Wt |
| Spanish | piloto | ✓ | Wt |
| French | pilote | ✓ | Wt |
| Swahili | rubani | ✗ | Wt |
| Hausa | matuƙin jirgi | ✗ | M |
| Yoruba | awakọ̀ òfurufú | ✗ | M |
| Quechua | piloto (Spanish loan) | ✓ | M |

**11/20 (12 lenient); regions 6 (no SSA) → borderline.** Median [pilot] → *pilotu*.
Median: i (id tl tr ru es fr qu) 7 against English ai (ja ko hi ta bn) 5.

### fashion (Wt: [fashion](https://en.wiktionary.org/wiki/fashion#Translations), "current (constantly changing) trend, favored for frivolous rather than practical, logical, or intellectual reasons|vogue")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 时尚 shíshàng, 时装 | ✗ | Wt |
| Japanese | ファッション fasshon, 流行 | ✗ | Wt |
| Korean | 패션 paesyeon | ✗ | Wt |
| Vietnamese | mốt (< French mode), thời trang | ✓ | Wt |
| Thai | แฟชั่น fɛɛchân | ✗ | Wt |
| Indonesian | mode | ✓ | Wt |
| Tagalog | moda | ✓ | Wt |
| Hindi | फ़ैशन faišan | ✗ | Wt |
| Bengali | ফ্যাশন fyāšan | ✗ | Wt |
| Tamil | ஃபேஷன் fēšan | ✗ | Wt |
| Persian | مد mod | ✓ | Wt |
| Arabic | موضة mōḍa | ✓ | Wt |
| Turkish | moda | ✓ | Wt |
| Russian | мода moda | ✓ | Wt |
| Spanish | moda | ✓ | Wt |
| French | mode | ✓ | Wt |
| Swahili | mitindo | ✗ | M |
| Hausa | yayi | ✗ | M |
| Yoruba | àṣà | ✗ | M |
| Quechua | moda (Spanish loan) | ✓ | M |

**10/20; regions 4 (no EA SA SSA) → fail.**
Shared column = moda/mode. The English fashion form (ja ko th hi bn ta) is the other half of the panel, 6 in 3 regions.

### plastic (Wt: [plastic](https://en.wiktionary.org/wiki/plastic#Translations), "synthetic thermoplastic polymer")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 塑料 sùliào | ✗ | Wt |
| Japanese | プラスチック purasuchikku | ✓ | Wt |
| Korean | 플라스틱 peullaseutik | ✓ | Wt |
| Vietnamese | nhựa, chất dẻo | ✗ | Wt |
| Thai | พลาสติก phláatsatìk | ✓ | Wt |
| Indonesian | plastik | ✓ | M |
| Tagalog | plastik | ✓ | Wt |
| Hindi | प्लास्टिक plāsṭik | ✓ | Wt |
| Bengali | প্লাস্টিক plāsṭik | ✓ | Wt |
| Tamil | பிளாஸ்டிக் pilāsṭik (coinage நெகிழி) | ✓ | Wt, M* |
| Persian | پلاستیک pelāstik | ✓ | Wt |
| Arabic | بلاستيك blāstīk | ✓ | Wt |
| Turkish | plastik | ✓ | Wt |
| Russian | пластик plastik, пластмасса | ✓ | Wt |
| Spanish | plástico | ✓ | Wt |
| French | plastique | ✓ | Wt |
| Swahili | plastiki | ✓ | Wt |
| Hausa | roba "rubber" | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | plástico (Spanish loan) | ✓ | M |

**16/20; regions all 7 → pass.** Median [plastik] → *pulasutiku*.

### bar (Wt: [bar](https://en.wiktionary.org/wiki/bar#Translations), "business licensed to sell intoxicating beverages")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 酒吧 jiǔbā (bā sound loan + "liquor") | ✗ (✓ lenient) | Wt |
| Japanese | バー bā (居酒屋 izakaya for a pub) | ✓ | Wt |
| Korean | 술집 suljip; 바 ba | ✗ (✓ lenient) | Wt |
| Vietnamese | quán rượu; quán bar in cities | ✗ (✓ lenient) | Wt |
| Thai | บาร์ baa | ✓ | Wt |
| Indonesian | bar | ✓ | Wt |
| Tagalog | bar | ✓ | M |
| Hindi | बार bār | ✓ | Wt |
| Bengali | বার bār | ✓ | Wt |
| Tamil | பார் pār | ✓ | M |
| Persian | بار bār, میخانه meykhāne | ✓ | Wt |
| Arabic | بار bār, حانة ḥāna | ✓ | Wt, M* |
| Turkish | bar, meyhane | ✓ | Wt |
| Russian | бар bar | ✓ | Wt |
| Spanish | bar | ✓ | Wt |
| French | bar | ✓ | Wt |
| Swahili | baa | ✓ | M |
| Hausa | mashaya | ✗ | M |
| Yoruba | ilé ọtí | ✗ | M |
| Quechua | bar (Spanish loan) | ✓ | M |

**15/20 (18 lenient); regions all 7 → pass.** Median [bar] → *balu*.

### version (Wt: [version](https://en.wiktionary.org/wiki/version#Translations), "computing: particular revision")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 版本 bǎnběn | ✗ | Wt |
| Japanese | バージョン bājon | ✓ | Wt |
| Korean | 버전 beojeon | ✓ | Wt |
| Vietnamese | phiên bản | ✗ | Wt |
| Thai | เวอร์ชัน wəəchan | ✓ | Wt, M* |
| Indonesian | versi | ✓ | Wt |
| Tagalog | bersyon | ✓ | M |
| Hindi | संस्करण saṃskaraṇ; spoken varzan | ✗ (✓ lenient) | Wt, M |
| Bengali | সংস্করণ saṃskaraṇ | ✗ | Wt |
| Tamil | பதிப்பு patippu | ✗ | M |
| Persian | نسخه nosxe | ✗ | Wt |
| Arabic | إصدار iṣdār, نسخة nusxa | ✗ | Wt |
| Turkish | sürüm, versiyon | ✓ | Wt |
| Russian | версия versija | ✓ | Wt |
| Spanish | versión | ✓ | Wt |
| French | version | ✓ | Wt |
| Swahili | toleo | ✗ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | versión (Spanish loan) | ✓ | M |

**10/20 (11 lenient); regions 5 (no SA SSA) (6 lenient) → fail.**

### cinema (Wt: [cinema](https://en.wiktionary.org/wiki/cinema#Translations), "a film/movie theatre")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 电影院 diànyǐngyuàn | ✗ | Wt |
| Japanese | 映画館 eigakan | ✗ | Wt |
| Korean | 영화관 yeonghwagwan | ✗ | Wt |
| Vietnamese | rạp chiếu phim; rạp xi-nê | ✗ (✓ lenient) | Wt |
| Thai | โรงหนัง roong nǎng | ✗ | Wt |
| Indonesian | bioskop; sinema | ✗ (✓ lenient) | Wt |
| Tagalog | sinehan | ✓ | Wt |
| Hindi | सिनेमा sinemā | ✓ | Wt |
| Bengali | সিনেমা sinemā | ✓ | Wt |
| Tamil | சினிமா sinimā | ✓ | Wt |
| Persian | سینما sinemā | ✓ | Wt |
| Arabic | سينما sīnimā | ✓ | Wt |
| Turkish | sinema | ✓ | Wt |
| Russian | кинотеатр kinoteatr, кино kino | ✗ (✓ lenient) | Wt |
| Spanish | cine | ✓ | Wt |
| French | cinéma | ✓ | Wt |
| Swahili | sinema | ✓ | Wt |
| Hausa | sinima | ✓ | M |
| Yoruba | sinimá | ✓ | M |
| Quechua | cine (Spanish loan) | ✓ | M |

**13/20 (16 lenient); regions 6 (no EA) → pass.** Median [sinema] → *sinema*.
Russian kino shares the etymon (kinema) but is heard as a different word. Median: second vowel e 9 against i 4.

### fuel (Wt: [gasoline](https://en.wiktionary.org/wiki/gasoline#Translations), "motor fuel")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 汽油 qìyóu | ✗ | Wt |
| Japanese | ガソリン gasorin | ✗ | Wt |
| Korean | 휘발유 hwiballyu; 가솔린 | ✗ | Wt |
| Vietnamese | xăng (< French essence) | ✗ | Wt |
| Thai | น้ำมัน námman; เบนซิน bensin | ✗ (✓ lenient) | Wt |
| Indonesian | bensin | ✓ | Wt |
| Tagalog | gasolina | ✗ | Wt |
| Hindi | पेट्रोल peṭrol | ✗ | Wt |
| Bengali | পেট্রল peṭrol | ✗ | Wt |
| Tamil | பெட்ரோல் peṭrōl | ✗ | Wt |
| Persian | بنزین benzin (Iran; پترول in Afghanistan) | ✓ | Wt |
| Arabic | بنزين banzīn | ✓ | Wt |
| Turkish | benzin | ✓ | Wt |
| Russian | бензин benzin | ✓ | Wt |
| Spanish | gasolina (Chile bencina, Argentina nafta) | ✗ | Wt |
| French | essence | ✗ | Wt |
| Swahili | petroli | ✗ | Wt |
| Hausa | fetur | ✗ | M |
| Yoruba | pẹtiróòlù, bẹntiróò | ✗ | Wt |
| Quechua | gasolina (Spanish loan) | ✗ | M |

**5/20 (6 lenient); regions 3 (SEA WA EU) → fail.**
Shared column = the benzin form. The panel splits three ways: benzin (id fa ar tr ru, th), petrol (hi bn ta sw ha yo) and gasoline (ja ko tl es qu). The largest family has 6. Native "oil" words (zh qìyóu "gas oil", th námman) are the remaining pattern.

### cream (Wt: [cream](https://en.wiktionary.org/wiki/cream#Translations), "fatty part of milk")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 奶油 nǎiyóu | ✗ | Wt |
| Japanese | クリーム kurīmu | ✓ | Wt |
| Korean | 크림 keurim | ✓ | Wt |
| Vietnamese | kem (< French crème) | ✗ (✓ lenient) | Wt |
| Thai | ครีม khriim | ✓ | Wt |
| Indonesian | krim | ✓ | Wt |
| Tagalog | krema (Wt coinage laknip) | ✓ | M |
| Hindi | मलाई malāī | ✗ | Wt |
| Bengali | মালাই mālāi | ✗ | Wt |
| Tamil | ஆடை āṭai; கிரீம் kirīm | ✗ (✓ lenient) | Wt |
| Persian | خامه xāme, سرشیر saršir | ✗ | Wt |
| Arabic | قشطة qišṭa | ✗ | Wt |
| Turkish | kaymak (krema whipped cream) | ✗ (✓ lenient) | Wt |
| Russian | сливки slivki | ✗ | Wt |
| Spanish | nata (Spain), crema (Latin America) | ✓ | Wt |
| French | crème | ✓ | Wt |
| Swahili | (no data; krimu for skin cream) | ✗ (✓ lenient) | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | crema (Spanish loan) | ✗ (✓ lenient) | M |

**7/20 (12 lenient); regions 3 (EA SEA EU) (7 lenient) → borderline.** Median [krim] → *kulimu*.
A weak borderline: the lenient count rests on five soft columns. The finding is the split by sense. For dairy cream most of Asia and Russia keep a native word (malāī, xāme, qišṭa, kaymak, slivki). For skin cream Wiktionary's own table has the loan in 15 languages (ja ko vi th id tl hi bn fa ar tr ru es fr sw), a clear pass. If the language needs the word mainly for the cosmetic, it passes.

### passport (Wt: [passport](https://en.wiktionary.org/wiki/passport#Translations), "official document for foreign travel")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 护照 hùzhào | ✗ | Wt |
| Japanese | パスポート pasupōto (旅券 ryoken formal) | ✓ | Wt |
| Korean | 여권 yeogwon | ✗ | Wt |
| Vietnamese | hộ chiếu | ✗ | Wt |
| Thai | หนังสือเดินทาง nǎngsʉ̌ʉ dəən thaang; พาสปอร์ต colloquial | ✗ (✓ lenient) | Wt |
| Indonesian | paspor | ✓ | Wt |
| Tagalog | pasaporte | ✓ | Wt |
| Hindi | पासपोर्ट pāsporṭ | ✓ | Wt |
| Bengali | পাসপোর্ট pāsporṭ (formal পারপত্র) | ✓ | Wt, M* |
| Tamil | பாஸ்போர்ட் pāsporṭ (formal கடவுச்சீட்டு) | ✓ | Wt, M* |
| Persian | گذرنامه gozarnāme; پاسپورت pāsport | ✗ (✓ lenient) | Wt |
| Arabic | جواز سفر jawāz safar | ✗ | Wt |
| Turkish | pasaport | ✓ | Wt |
| Russian | паспорт pasport | ✓ | Wt |
| Spanish | pasaporte | ✓ | Wt |
| French | passeport | ✓ | Wt |
| Swahili | pasipoti, paspoti | ✓ | Wt |
| Hausa | fasfo | ✓ | Wt |
| Yoruba | ìwé ìrìnnà | ✗ | Wt |
| Quechua | pasaporte (Spanish loan) | ✓ | M |

**13/20 (15 lenient); regions all 7 → pass.** Median [pasport] → *pasupolutu*.
Median: no vowel between s and p in 7 of 13; r kept in 9; consonant-final 7.

### platform (Wt: [platform](https://en.wiktionary.org/wiki/platform#Translations), "computing: a specific operating system or environment; a specific type of computer or microprocessor")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 平台 píngtái | ✗ | Wt |
| Japanese | プラットフォーム purattofōmu | ✓ | Wt |
| Korean | 플랫폼 peullaetpom | ✓ | Wt |
| Vietnamese | nền tảng | ✗ | Wt |
| Thai | แพลตฟอร์ม phlɛ́tfɔɔm | ✓ | M |
| Indonesian | platform (Wt coinage anjungan) | ✓ | M |
| Tagalog | plataporma | ✓ | M |
| Hindi | प्लेटफ़ॉर्म pleṭfŏrm | ✓ | Wt (travel sense) |
| Bengali | প্ল্যাটফর্ম plyāṭfôrm | ✓ | M |
| Tamil | தளம் taḷam; spoken platform | ✗ (✓ lenient) | M |
| Persian | پلتفرم platform; سکو sakku (station) | ✗ (✓ lenient) | M |
| Arabic | منصة minaṣṣa | ✗ | Wt |
| Turkish | platform | ✓ | Wt |
| Russian | платформа platforma | ✓ | Wt |
| Spanish | plataforma | ✓ | Wt |
| French | plateforme | ✓ | Wt |
| Swahili | jukwaa | ✗ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | plataforma (Spanish loan) | ✓ | M |

**12/20 (14 lenient); regions 6 (no SSA) → pass, borderline.** Median [platform] → *pulatufolumu*.
Wiktionary's computing-sense table is thin (10 languages), so five columns come from memory. The adapted form is long (6 syllables) because of the pl, tf and rm clusters.

### engineer (Wt: [engineer](https://en.wiktionary.org/wiki/engineer#Translations), "person engaged in designing, constructing, or maintaining engines or machinery")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 工程师 gōngchéngshī | ✗ | Wt |
| Japanese | エンジニア enjinia, 技師 | ✓ | Wt |
| Korean | 엔지니어 enjinieo, 기사 | ✓ | Wt |
| Vietnamese | kỹ sư | ✗ | Wt |
| Thai | วิศวกร wítsawakɔɔn | ✗ | Wt |
| Indonesian | insinyur (< Dutch ingenieur) | ✓ | Wt |
| Tagalog | inhinyero | ✓ | Wt |
| Hindi | इंजीनियर iñjīniyar (formal अभियंता) | ✓ | Wt, M* |
| Bengali | প্রকৌশলী prakauśalī; spoken iñjiniyār | ✗ (✓ lenient) | Wt, M |
| Tamil | பொறியாளர் poṟiyāḷar; spoken iñjiniyar | ✗ (✓ lenient) | Wt, M |
| Persian | مهندس mohandes (انجنیر Afghan) | ✗ | Wt |
| Arabic | مهندس muhandis | ✗ | Wt |
| Turkish | mühendis | ✗ | Wt |
| Russian | инженер inžener | ✓ | Wt |
| Spanish | ingeniero | ✓ | Wt |
| French | ingénieur | ✓ | Wt |
| Swahili | injinia, mhandisi | ✓ | Wt |
| Hausa | injiniya | ✓ | M |
| Yoruba | ẹn̄jiníà | ✓ | Wt |
| Quechua | ingeniero (Spanish loan) | ✓ | M |

**12/20 (14 lenient); regions 6 (no WA) → pass, borderline.** Median [indʒiniar] → *indiniyalu*.
West Asia uses muhandis (fa ar tr), as does Swahili beside injinia. Median: dʒ (ja ko hi sw ha yo) 6, r kept in 7 of 12, vowel before it a 6.

### vaccine (Wt: [vaccine](https://en.wiktionary.org/wiki/vaccine#Translations), "substance given to stimulate a body’s production of antibodies and provide immunity against a disease")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 疫苗 yìmiáo | ✗ | Wt |
| Japanese | ワクチン wakuchin | ✓ | Wt |
| Korean | 백신 baeksin | ✓ | Wt |
| Vietnamese | vắc-xin | ✓ | Wt |
| Thai | วัคซีน wákkhsiin | ✓ | Wt |
| Indonesian | vaksin | ✓ | Wt |
| Tagalog | bakuna | ✓ | Wt |
| Hindi | टीका ṭīkā; वैक्सीन vaiksīn | ✗ (✓ lenient) | Wt |
| Bengali | ভ্যাক্সিন bhyāksin, টীকা | ✓ | Wt |
| Tamil | தடுப்பூசி taṭuppūci; spoken vaccine | ✗ (✓ lenient) | M |
| Persian | واکسن vāksan | ✓ | Wt |
| Arabic | لقاح laqāḥ | ✗ | Wt |
| Turkish | aşı | ✗ | Wt |
| Russian | вакцина vaktsina | ✓ | Wt |
| Spanish | vacuna | ✓ | Wt |
| French | vaccin | ✓ | Wt |
| Swahili | chanjo | ✗ | Wt |
| Hausa | allurar rigakafi | ✗ | M |
| Yoruba | abẹ́rẹ́ àjẹsára | ✗ | M |
| Quechua | vacuna (Spanish loan) | ✓ | M |

**12/20 (14 lenient); regions 6 (no SSA) → pass, borderline.** Median [vaksin] → *bakusin*.
First consonant v and b tie at 5 (w 2); names.py maps both to b.

### tunnel (Wt: [tunnel](https://en.wiktionary.org/wiki/tunnel#Translations), "an underground or underwater passage")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 隧道 suìdào | ✗ | Wt |
| Japanese | トンネル tonneru | ✓ | Wt |
| Korean | 터널 teoneol | ✓ | Wt |
| Vietnamese | đường hầm | ✗ | Wt |
| Thai | อุโมงค์ ʔumoong | ✗ | Wt |
| Indonesian | terowongan | ✗ | Wt |
| Tagalog | tunel, lagusan | ✓ | M |
| Hindi | सुरंग suraṅg | ✗ | Wt |
| Bengali | সুড়ঙ্গ suṛaṅga | ✗ | Wt |
| Tamil | சுரங்கம் suraṅkam | ✗ | M |
| Persian | تونل tunel | ✓ | Wt |
| Arabic | نفق nafaq | ✗ | Wt |
| Turkish | tünel | ✓ | Wt |
| Russian | тоннель tonnel' | ✓ | Wt |
| Spanish | túnel | ✓ | Wt |
| French | tunnel | ✓ | Wt |
| Swahili | handaki | ✗ | M |
| Hausa | rami | ✗ | M |
| Yoruba | ihò | ✗ | M |
| Quechua | túnel (Spanish loan) | ✓ | M |

**9/20; regions 5 (no SA SSA) → fail.**

### toilet (Wt: [toilet](https://en.wiktionary.org/wiki/toilet#Translations), "room used for urination and defecation")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 厕所 cèsuǒ, 洗手间 | ✗ | Wt |
| Japanese | トイレ toire | ✓ | Wt |
| Korean | 화장실 hwajangsil | ✗ | Wt |
| Vietnamese | nhà vệ sinh | ✗ | Wt |
| Thai | ห้องน้ำ hɔ̂ng náam "water room" | ✗ | Wt |
| Indonesian | toilet, WC, kamar kecil | ✓ | Wt |
| Tagalog | palikuran; CR "comfort room" | ✗ | Wt, M |
| Hindi | टॉयलेट ṭŏyleṭ (formal शौचालय) | ✓ | Wt, M* |
| Bengali | টয়লেট ṭayleṭ, পায়খানা | ✓ | Wt, M* |
| Tamil | கழிவறை kaḻivaṟai; spoken ṭāylaṭ | ✗ (✓ lenient) | Wt, M |
| Persian | دستشویی dastšuyi; توالت tuālet | ✗ (✓ lenient) | Wt |
| Arabic | حمام ḥammām; تواليت twālitt | ✗ (✓ lenient) | Wt |
| Turkish | tuvalet | ✓ | Wt |
| Russian | туалет tualet | ✓ | Wt |
| Spanish | baño | ✗ | Wt |
| French | toilettes | ✓ | Wt |
| Swahili | choo | ✗ | Wt |
| Hausa | bayan gida "behind the house" | ✗ | M |
| Yoruba | ilé ìyàgbẹ́ | ✗ | Wt |
| Quechua | jisp'ana wasi | ✗ | Wt |

**7/20 (10 lenient); regions 5 (no SSA AM) → fail.**
The panel mostly uses euphemisms ("hand-washing room", "water room", "bath", "behind the house"), so no single form is shared.

### studio (Wt: [studio](https://en.wiktionary.org/wiki/studio#Translations), "place where radio or television programs, records or films are made|set")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 演播室 yǎnbōshì | ✗ | Wt |
| Japanese | スタジオ sutajio | ✓ | Wt |
| Korean | 스튜디오 seutyudio | ✓ | Wt |
| Vietnamese | phòng thu; studio (photo studio) | ✗ (✓ lenient) | M |
| Thai | สตูดิโอ satuudio | ✓ | M |
| Indonesian | studio | ✓ | M |
| Tagalog | istudyo | ✓ | M |
| Hindi | स्टूडियो sṭūḍiyo | ✓ | M |
| Bengali | স্টুডিও sṭuḍio | ✓ | M |
| Tamil | ஸ்டுடியோ sṭuṭiyō (Wt gives a coinage) | ✓ | M |
| Persian | استودیو estudiyo | ✓ | Wt |
| Arabic | استوديو istūdiyū | ✓ | Wt |
| Turkish | stüdyo | ✓ | Wt |
| Russian | студия studija | ✓ | Wt |
| Spanish | estudio | ✓ | Wt |
| French | studio | ✓ | Wt |
| Swahili | studio | ✓ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | estudio (Spanish loan) | ✓ | M |

**16/20 (17 lenient); regions all 7 → pass.** Median [studio] → *sutudiyo*.
Prothetic e/i (tl fa ar es qu) is a minority, 5 of 16.

### profile (Wt: [profile](https://en.wiktionary.org/wiki/profile#Translations), "summary or collection of information, especially about a person")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 个人资料 gèrén zīliào | ✗ | M |
| Japanese | プロフィール purofīru | ✓ | Wt |
| Korean | 프로필 peuropil | ✓ | M |
| Vietnamese | hồ sơ; profile also used | ✗ (✓ lenient) | M |
| Thai | โปรไฟล์ proofaai | ✓ | M |
| Indonesian | profil | ✓ | M |
| Tagalog | profile | ✓ | M |
| Hindi | प्रोफ़ाइल profāil | ✓ | M |
| Bengali | প্রোফাইল profāil | ✓ | M |
| Tamil | சுயவிவரம் suyavivaram; spoken profile | ✗ (✓ lenient) | M |
| Persian | پروفایل profāyl | ✓ | M |
| Arabic | ملف شخصي malaff šaxṣī; بروفايل colloquial | ✗ (✓ lenient) | M |
| Turkish | profil | ✓ | M |
| Russian | профиль profil' | ✓ | Wt |
| Spanish | perfil | ✓ | Wt |
| French | profil | ✓ | Wt |
| Swahili | wasifu | ✗ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | perfil (Spanish loan) | ✓ | M |

**13/20 (16 lenient); regions 6 (no SSA) → pass.** Median [profil] → *pulofilu*.
The weakest evidence in this set: Wiktionary's tables for this sense cover only 6 languages. Spanish perfil is counted as the same word. Second vowel i (Latin profil) 8 against English ai 5.

### pope (Wt: [pope](https://en.wiktionary.org/wiki/pope#Translations), "head of the Roman Catholic Church|pontiff")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 教皇 jiàohuáng, 教宗 | ✗ | Wt |
| Japanese | 教皇 kyōkō, 法王 | ✗ | Wt |
| Korean | 교황 gyohwang | ✗ | Wt |
| Vietnamese | giáo hoàng | ✗ | Wt |
| Thai | สันตะปาปา santapaapaa; โป๊ป póop | ✓ | Wt |
| Indonesian | paus (< Dutch paus) | ✗ (✓ lenient) | Wt |
| Tagalog | papa, Santo Papa | ✓ | Wt |
| Hindi | पोप pop | ✗ (✓ lenient) | Wt |
| Bengali | ধর্মযাজক dharmayājak "priest" | ✗ | Wt |
| Tamil | போப் pōp | ✗ (✓ lenient) | M |
| Persian | پاپ pāp | ✓ | Wt |
| Arabic | بابا bābā | ✓ | Wt |
| Turkish | papa | ✓ | Wt |
| Russian | папа (римский) papa | ✓ | Wt |
| Spanish | papa | ✓ | Wt |
| French | pape | ✓ | Wt |
| Swahili | papa | ✓ | Wt |
| Hausa | Fafaroma "Papa Roma" | ✓ | M |
| Yoruba | Póòpù | ✗ (✓ lenient) | M |
| Quechua | papa (Spanish loan) | ✓ | M |

**11/20 (15 lenient); regions 5 (no EA SA) (6 lenient) → borderline.** Median [papa] → *papa*.
The form papa is also the baby word for father in many panel languages, the mama/papa question loans.md left open. A religious title is arguably the community's own term (C2), like a name.

### piano (Wt: [piano](https://en.wiktionary.org/wiki/piano#Translations), "a keyboard musical instrument")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 钢琴 gāngqín "steel zither" | ✗ | Wt |
| Japanese | ピアノ piano | ✓ | Wt |
| Korean | 피아노 piano | ✓ | Wt |
| Vietnamese | dương cầm "Western zither"; đàn piano | ✗ (✓ lenient) | Wt |
| Thai | เปียโน piano | ✓ | Wt |
| Indonesian | piano | ✓ | Wt |
| Tagalog | piyano | ✓ | Wt |
| Hindi | पियानो piyāno | ✓ | Wt |
| Bengali | পিয়ানো piyāno | ✓ | Wt |
| Tamil | பியானோ piyāṉō | ✓ | Wt |
| Persian | پیانو piyāno | ✓ | Wt |
| Arabic | بيانو biyānū | ✓ | Wt |
| Turkish | piyano | ✓ | Wt |
| Russian | пианино pianino, фортепиано | ✓ | Wt |
| Spanish | piano | ✓ | Wt |
| French | piano | ✓ | Wt |
| Swahili | kinanda, piano | ✓ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | dùrù | ✗ | M |
| Quechua | yatana qallwa (coinage); piano in bilingual speech | ✗ (✓ lenient) | Wt, M |

**15/20 (17 lenient); regions 6 (no AM) (7 lenient) → pass.** Median [piano] → *piyano*.

### physics (Wt: [physics](https://en.wiktionary.org/wiki/physics#Translations), "branch of science")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 物理学 wùlǐxué | ✗ | Wt |
| Japanese | 物理学 butsurigaku | ✗ | Wt |
| Korean | 물리학 mullihak | ✗ | Wt |
| Vietnamese | vật lý | ✗ | Wt |
| Thai | ฟิสิกส์ fisìk | ✓ | Wt |
| Indonesian | fisika | ✓ | Wt |
| Tagalog | pisika | ✓ | Wt |
| Hindi | भौतिकी bhautikī | ✗ | Wt |
| Bengali | পদার্থবিজ্ঞান padārthabijñān | ✗ | Wt |
| Tamil | இயற்பியல் iyaṟpiyal | ✗ | Wt |
| Persian | فیزیک fizik | ✓ | Wt |
| Arabic | فيزياء fīziyāʾ | ✓ | Wt |
| Turkish | fizik | ✓ | Wt |
| Russian | физика fizika | ✓ | Wt |
| Spanish | física | ✓ | Wt |
| French | physique | ✓ | Wt |
| Swahili | fizikia | ✓ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | físíìsì | ✗ (✓ lenient) | M |
| Quechua | física (Spanish loan) | ✓ | M |

**11/20 (12 lenient); regions 5 (no EA SA) → borderline.** Median [fizika] → *fisika*.
Same pattern as chemistry, one column weaker: EA (物理) and SA (bhautikī, padārtha-) build their own words.

### mosque (Wt: [mosque](https://en.wiktionary.org/wiki/mosque#Translations), "a place of worship for Muslims")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 清真寺 qīngzhēnsì | ✗ | Wt |
| Japanese | モスク mosuku | ✗ (✓ lenient) | Wt |
| Korean | 모스크 moseukeu | ✗ (✓ lenient) | Wt |
| Vietnamese | nhà thờ Hồi giáo | ✗ | Wt |
| Thai | มัสยิด mátsayít | ✓ | Wt |
| Indonesian | masjid, mesjid | ✓ | Wt |
| Tagalog | moske | ✗ (✓ lenient) | Wt |
| Hindi | मस्जिद masjid | ✓ | Wt |
| Bengali | মসজিদ mosjid | ✓ | Wt |
| Tamil | மசூதி masūti, மஸ்ஜித் | ✓ | Wt |
| Persian | مسجد masjed | ✓ | Wt |
| Arabic | مسجد masjid, جامع jāmiʿ | ✓ | Wt |
| Turkish | cami; mescit (small mosque) | ✗ (✓ lenient) | Wt |
| Russian | мечеть mečet' (< masjid via Turkic) | ✗ (✓ lenient) | Wt |
| Spanish | mezquita | ✗ (✓ lenient) | Wt |
| French | mosquée | ✗ (✓ lenient) | Wt |
| Swahili | msikiti | ✓ | Wt |
| Hausa | masallaci (< muṣallā) | ✗ | Wt |
| Yoruba | mọ́ṣáláṣí (< muṣallā) | ✗ | Wt |
| Quechua | mezquita (Spanish loan) | ✗ (✓ lenient) | M |

**8/20 (16 lenient); regions 4 (no EA EU AM) (7 lenient) → borderline.** Median [masdʒid] → *masudidu*.
Shared column = the Arabic masjid, the community's own word. The European shape mosque/mezquita/mosquée (and ja ko tl from it) goes back to masjid but is not heard as the same word. A religious institution's name arguably follows its community (C2), which would favour masjid regardless of the count.

### medal (Wt: [medal](https://en.wiktionary.org/wiki/medal#Translations), "stamped metal disc")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 奖牌 jiǎngpái | ✗ | Wt |
| Japanese | メダル medaru | ✓ | Wt |
| Korean | 메달 medal | ✓ | Wt |
| Vietnamese | huy chương; mề đay (< French médaille) | ✗ (✓ lenient) | Wt |
| Thai | เหรียญ rǐan | ✗ | Wt |
| Indonesian | medali | ✓ | Wt |
| Tagalog | medalya | ✓ | Wt |
| Hindi | पदक padak; मेडल meḍal | ✗ (✓ lenient) | Wt |
| Bengali | পদক padak; মেডেল meḍel | ✗ (✓ lenient) | Wt |
| Tamil | பதக்கம் patakkam | ✗ | Wt |
| Persian | مدال medāl | ✓ | Wt |
| Arabic | ميدالية mīdāliya | ✓ | Wt |
| Turkish | madalya | ✓ | Wt |
| Russian | медаль medal' | ✓ | Wt |
| Spanish | medalla | ✓ | Wt |
| French | médaille | ✓ | Wt |
| Swahili | nishani | ✗ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | medalla (Spanish loan) | ✓ | M |

**11/20 (14 lenient); regions 5 (no SA SSA) (6 lenient) → borderline.** Median [medaʎa] → *medala*.
Median: a final vowel in 8 of 11 (a: tl ar tr es qu), with a palatal l (ʎ, lj) before it in 5; names.py maps ʎ to l.

### mask (Wt: [mask](https://en.wiktionary.org/wiki/mask#Translations), "cover for the face")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 面具 miànjù; 口罩 kǒuzhào (medical) | ✗ | Wt |
| Japanese | マスク masuku (仮面 kamen for costume) | ✓ | Wt |
| Korean | 마스크 maseukeu (가면 for costume) | ✓ | Wt |
| Vietnamese | mặt nạ; khẩu trang (medical) | ✗ | Wt |
| Thai | หน้ากาก nâakàak | ✗ | Wt |
| Indonesian | masker (topeng costume) | ✓ | Wt |
| Tagalog | maskara | ✓ | M |
| Hindi | मास्क māsk, मुखौटा | ✓ | Wt |
| Bengali | মাস্ক māsk | ✓ | Wt |
| Tamil | முகமூடி mukamūṭi; spoken māsk | ✗ (✓ lenient) | Wt, M |
| Persian | ماسک māsk | ✓ | Wt |
| Arabic | قناع qināʿ, كمامة kimāma (medical); colloquial māsk | ✗ (✓ lenient) | Wt |
| Turkish | maske | ✓ | Wt |
| Russian | маска maska | ✓ | Wt |
| Spanish | máscara; mascarilla (medical) | ✓ | Wt |
| French | masque | ✓ | Wt |
| Swahili | barakoa | ✗ | Wt |
| Hausa | (no data) | ✗ | M |
| Yoruba | ìbòjú | ✗ | M |
| Quechua | máscara (Spanish loan) | ✓ | M |

**12/20 (14 lenient); regions 6 (no SSA) → pass, borderline.** Median [maska] → *masuka*.
Median: a final vowel in 8 of 12, a (ru tl es qu) the plurality; -ra after it ties 4/4 with no ending.

## Older loans re-run (2026-10-13)

The 14 loans in `data/lexicon.tsv` that no 2026-10-13 decision had settled (the metric set and kilo are decided; the seven phrase replacements and percent left the lexicon) were re-run under the rules above: everyday loans beside a formal word count with a source; memory columns count only once sourced, with no Quechua assumption; the five-times rival rule; thin deciding columns fail; median ties by regions, then length; shared short forms tested. Per-column judgments: `loanwork/older.txt`; sources for memory columns: `loanwork/verified.tsv`; results: `loans-rerun.tsv`.

| Loan | Before (lexicon-ladder-01) | Now | Form |
|---|---|---|---|
| email | pass, borderline, 12/5 | **pass, 16/6** | *imeyilu* (unchanged) |
| police | borderline, 11 strict | **fail, 11/5** | *polisu* → native root |
| rupee | pass, 19/7 | pass, 16/6 | ***lupi* → *lupiya*** |
| dollar, internet, battery, euro, yuan, camera | pass | pass (14–19, 6–7 regions) | unchanged |
| hour, minute, second, degree, photo | fail | fail (4–9) | native roots, as before |

- **email** no longer rests on judgment: Tagalog and Hausa are now sourced, and Turkish (*e-mail*/*mail* as often as *e-posta*), Spanish (*email* forms at a third of *correo*, which also means post) and Swahili (*email* about as often as *barua pepe*) count as everyday loans. The short form *mail* reaches 8 languages and fails, so *imeyilu* stays.
- **police** fails by one. Arabic *būlīs* is 1/48 as frequent as *šurṭa* in the subtitles, so it fails the rival rule. Quechua *policía* (2 Leipzig tokens) would be a thin 12th vote. Tamil *pōlīs* counts (more frequent than *kāval*).
- **rupee:** the end of the word ties. Eight languages use the English shape [rupi] (zh ja ko vi th id tr fr), in 4 regions. Eight use the Hindi/Portuguese shape [rupija] (tl hi ta fa ar ru es sw), in 5 regions. The region rule gives [rupija] → *lupiya*. Before, Hausa, Yoruba and Vietnamese *rupi* were counted from memory; now only Vietnamese is sourced, and one sourced Hausa or Yoruba *rupi* would restore *lupi*. **Open for the author:** *lupi* and *lupiya* differ only by the glide y, and y is a consonant (language.md 2.2). Read literally, the shape rule makes them two forms of 8 each, and rupee fails. Here the glide is read out of the comparison, because most glides in adapted loans come from vowels (*piyano*, *ladiyo*). The coverage panel never had to decide this.
- **How the shape rule was applied:** shapes are the source's forms (rupee / rupiya, second / segundo, hour / hora). A borrowing language's own sound changes don't make a new shape. Japanese *doru*, Thai *dɔnlaa* and Arabic *rūbiyya* stay with their source, just as the coverage panel counted Japanese *gitā* with guitar and *konpyūtā* with computer, and as the dollar decision counted *dola* with *dolar*. Applied to each language's adaptation instead, dollar (*dola* vs *dolalu*) and internet (*intanetu* vs *intelunetu*) would split, which no earlier verdict did.
- **Five-times rule with broad rivals:** it was applied only where the rival names the same concept. Where the rival is a broader word (*thư* "letter", *почта* "post", *mạng* "network", *mtandao* "network", Bengali *chhabi* "picture"), its frequency can't be separated, so the column stays as Wiktionary lists it. Wherever a specific compound could be counted (*электронная почта*, *البريد الإلكتروني*), it stayed under 5x.
- **Counts that moved without changing a verdict:** yuan rested on 9 memory columns; Indonesian (KBBI), Turkish, Tagalog, Hausa and Swahili are now sourced, giving 14/6. Hausa "yuan" in Leipzig is mostly names, with about 5 currency sentences. Euro 16/6, camera 16/6 (Vietnamese *camera*, Turkish *kamera* and French *caméra* added), internet 17/7 (Tamil out; Hausa *intanet* in, at 4.9x its rival), battery 17/6 (Turkish *batarya* in). Every passing form except rupee reproduces from the new medians.
- **The failures stay failures.** Under the shape rule, hour (hora 3, hour 1) and second (second 4, segundo 3) fall further. Hausa *digiri* is only the academic degree. Tamil spoken *photo* is sourced (photo 9/5), but that isn't enough. hour, minute, second, degree and photo are still loans in the lexicon, waiting for their native roots in the coverage batch.
