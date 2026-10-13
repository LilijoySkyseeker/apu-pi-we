# Loan candidates from coverage-01 part 3 against the panel

Proposals only; no word was changed. Candidates: the 109 rows of `ladder.tsv` (this folder) with route `loan?`. Results per candidate: `loans.tsv`.

## Method

The same as `tests/lexicon-ladder-01/loans.md` ("How this was done"), unchanged:

- For each candidate I recorded the everyday word in each of the 20 panel languages and whether a speaker would hear it as the same word as the international form. Translations and calques don't count; neither does a distant etymological link.
- Pass rule (goal L4): at least 12 of 20, across at least 4 of the 7 regions EA (zh ja ko), SEA (vi th id tl), SA (hi bn ta), WA (fa ar tr), EU (ru es fr), SSA (sw ha yo), AM (qu).
- Sources: **Wt** the English Wiktionary translation table for the sense in each heading, fetched 2026-10-13 with `tests/lexicon-ladder-01/panel.py`; **We** the Wiktionary entry for the foreign word; **M** from memory; **M\*** Wiktionary lists the word, but my judgment of the everyday word differs from its first-listed one.
- Quechua: where Wiktionary gives a native form I used it; otherwise I assumed the Spanish loan of bilingual speech (M).
- Borderline: where the count depends on M\* or lenient judgments (✗ (✓ lenient) in the tables), both counts are given. A candidate is **borderline** when the strict count fails and the lenient count passes.
- Median pronunciation: for each sound position, the majority among the cognate forms only, in broad IPA, run through `tools/names.py`. Given for passes and borderlines. The adapted forms are not checked for collisions or offensiveness (`words.py`/`offensive.py`).
- One tool fix: `panel.py` skipped `{{trans-top-also}}` blocks, which Wiktionary uses for some main senses (sandwich, biscuit, toilet). It now reads them; earlier results are unaffected (only blocks were added).

## Summary

(Filled in when all chunks are done.)

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

**12/20 (14 lenient); regions 6 (no SSA) → pass.** Median [moto] → *moto*.
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
