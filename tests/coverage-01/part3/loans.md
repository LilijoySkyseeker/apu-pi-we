# Loan candidates from coverage-01 part 3 against the panel

Proposals only; no word was changed. Candidates: the 109 rows of `ladder.tsv` (this folder) with route `loan?`. Results per candidate: `loans.tsv`.

## Method

The same as `tests/lexicon-ladder-01/loans.md` ("How this was done"), unchanged:

- For each candidate I recorded the everyday word in each of the 20 panel languages and whether a speaker would hear it as the same word as the international form. Translations and calques don't count; neither does a distant etymological link.
- Pass rule (goal L4): at least 12 of 20, across at least 4 of the 7 regions EA (zh ja ko), SEA (vi th id tl), SA (hi bn ta), WA (fa ar tr), EU (ru es fr), SSA (sw ha yo), AM (qu).
- Sources: **Wt** the English Wiktionary translation table for the sense in each heading, fetched 2026-10-13 with `tests/lexicon-ladder-01/panel.py`; **We** the Wiktionary entry for the foreign word; **M** from memory; **M\*** Wiktionary lists the word, but my judgment of the everyday word differs from its first-listed one.
- Quechua: where Wiktionary gives a native form I used it; otherwise I assumed the Spanish loan of bilingual speech (M).
- Borderline: where the count depends on M\* or lenient judgments (✗ (✓ lenient) in the tables), both counts are given. A candidate is **borderline** when the strict count fails and the lenient count passes. It is **pass, borderline** (as email was in loans.md) when the strict count passes at exactly 12, or in exactly 4 regions, and at least one counted column is from memory (M or M\*).
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
