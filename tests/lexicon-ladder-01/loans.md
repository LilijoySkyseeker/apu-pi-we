# Loans against Ladder 2 (lexicon-ladder-01, part 1)

Proposals only; no word was changed. Task: `~/work/apupiwe-review/prompts/LX.md`. Ladders: `docs/vocabulary-method.md` §0.

## How this was done

- **Loans checked:** all 22 rows with field `loan` in `data/lexicon.tsv`. I checked the other 461 roots and the compounds for words that look borrowed. None is a loan; see "Other words" at the end.
- **Rung 1 (standard):** is there an international standard term, and does the standard fix a *spoken* form? For units it doesn't. The SI fixes the definition and the symbol, but "unit symbols are mathematical entities", while "unit names … are treated like ordinary nouns" of each language (SI Brochure 9th ed. §5.2–5.3, [NIST SP 330 §5](https://www.nist.gov/pml/special-publication-330/sp-330-section-5)). So for hour, minute, second, km, % and °, rung 1 settles the boundary and the written symbol, but not the word. The spoken form falls to rung 2. Currencies are the exception: the issuer fixes the name.
- **Rung 2 (panel):** I recorded the everyday word in each of the 20 languages and whether it is a recognisably cognate form of the loan. Recognisably means a speaker would hear the two as the same word. Translations and calques don't count: Arabic *ṯāniya* "second" is a calque. Neither does a distant etymological link, such as Russian *gradus* against *diguli*.
  - Pass rule: at least 12 of 20, across at least 4 of these 7 regions: EA (zh ja ko), SEA (vi th id tl), SA (hi bn ta), WA (fa ar tr), EU (ru es fr), SSA (sw ha yo), AM (qu).
  - Regions are counted as written in the task. Note that the Americas has one panel language, Quechua.
- **Sources** (column *src*):
  - **Wt**: the English Wiktionary translation table for the sense named in each section's heading, fetched 2026-10-12 with `panel.py` (in this folder, re-runnable: `direnv exec <repo> python3 panel.py 'police#local'`).
  - **We**: the Wiktionary entry for the foreign word itself.
  - **M**: from memory.
  - **M\***: Wiktionary lists the word, but my judgment of which word is the *everyday* one differs from Wiktionary's first-listed word. This is where the uncertainty is; borderline verdicts give both counts.
- **Quechua:** Wiktionary rarely covers modern Quechua vocabulary. Where it gives a native form I used it. Otherwise I assumed the Spanish loan that bilingual speakers use, marked M. This is the weakest column.
- **Median pronunciation:** for each sound position, the majority among the cognate forms only, in broad IPA. Run through `tools/names.py`. The adapted forms are not yet checked for collisions or offensiveness (`words.py`/`offensive.py`); do that before adopting any.

## Summary

| Loan | Today | Rung 1: standard? | Panel (cognate/20; regions) | Verdict | Proposed form |
|---|---|---|---|---|---|
| dollar | dola | ISO 4217 codes (USD, CAD, AUD…); name is each issuer's | 19; all 7 | **pass** | median [dolar] → **dolalu**; today's *dola* is the non-rhotic English/Swahili form (13 of 19 cognates keep the r) |
| internet | intalunetu | no | 16; 6 (all but AM) | **pass** | median [internet] → **intelunetu** (today's *-ta-* is the English schwa) |
| hour | awuwa | SI-accepted unit, symbol h; name per language | 5 (tl es fr ha qu); 4 regions | **fail** | rung 4: **new root, tier 4** |
| minute, of time | minitu | SI-accepted unit, symbol min | 9; 5 | **fail** | rung 4: **new root, tier 4** |
| second, of time | sekandu | SI base unit, symbol s | 8; 4 | **fail** | rung 4: **new root, tier 3** |
| kilometre | kilamita | SI: prefix k + metre, symbol km | 19; all 7 | **pass** | median [kilometr] → **kilometulu** (5 syllables; today's 4-syllable *kilamita* is English) |
| percent | pasentu | ISO 80000-1 symbol %; name per language | 9; 4 | **fail** | rung 3: **N pi loki** "N of a hundred", the existing part construction (§5.2.5: *fi pi ka* "one of three"): *ka yawu pi loki* 30% |
| email | imeyilu | no | 12 everyday (≈9 counting only Wiktionary's first-listed words); 5 | **pass, borderline** | median [imeil]/[imel] tie → **imeyilu** (today) or *imelu* |
| photo | foto | no | 9; 5 | **fail** | rung 4: **new root "picture, image", tier 3**, which also covers photo (the panel mostly uses its picture word). Interim rung 3: *ge pi kamela* "thing of the camera". The compound *screenshot* (*foto pi du wuye*) follows. |
| train | tuleyin | no | 8; 5 | **fail** | rung 3: **siwa netu** "long cart" (built like *kima netu* "stick") |
| licence | layisansu | no | 9 (10 with French *licence*); 5 | **fail** | rung 3: **du efon** "thing for allowing" (like zh 许可证, vi *giấy phép*, yo *ìwé-àṣẹ*) |
| electricity | ilekutulisiti | IEC 60050 defines the term; no form | 5 (id tr ru es fr); 3 | **fail** | rung 3: **lula pi mufin** "lightning's power" when precise; **lula** "power" alone in context (as English "the power's out"). Option: lump with **mufin** "lightning", as hi *bijlī*, bn, fa *barq*, sw *umeme* do |
| degree (°) | diguli | SI: °C, ° (angle); name per language | 6 (hi bn ta fr sw ha); 3 | **fail** | rung 4: **new root, tier 2** ("degree, step on a scale"); option: say the number alone where the unit is obvious (weather) |
| hospital | osupitalu | no | 8; 4 | **fail** | rung 3: **pu yema simi** "place for helping the sick", the same base as the doctor phrase *no yema simi* (backtranslation-03) |
| bicycle | bayisikalu | no | 8 (9 if Hausa *basukur*); 5 | **fail** | rung 3: **siwa pi pifo** "foot cart" (Hindi *pairgāṛī* "foot cart", vi *xe đạp* "pedal vehicle") |
| battery | batali | IEC 60050 term; no form | 17; all 7 | **pass** | median [batari] → **batali** (= today) |
| euro | yulo | EU: one name in all EU languages, "taking into account the existence of different alphabets" (Madrid European Council 1995); ISO 4217 EUR | 19; all 7 | **pass** | median [juro] → **yulo** (= today) |
| yuan | yuwan | ISO 4217 CNY; issuer's name 元 *yuán* [ɥɛn] | 18; all 7 | **pass** | median [juan] → **yuwan** (= today); issuer's own pronunciation would give *wenu* |
| rupee | lupi | ISO 4217 INR, PKR, LKR, NPR…; issuer's name (Hindi *rupayā*) | 19; all 7 | **pass** | median tie [rupi] 10 / [rupija] 9 → **lupi** (= today); issuer's form → *lupaya* |
| police | polisu | no | 11 strict, 12–13 counting Egyptian colloquial *būlīs* and Spanish-loan Quechua; 6 | **borderline**; fails by one on the strict count | if kept: median [polis] → **polisu** (= today). If failed: rung 3 **no kuwi** "one who protects" (ta *kāval*, qu *chapaq* "guard") |
| camera | kamela | no | 14; all 7 | **pass** | median [kamera] → **kamela** (= today) |
| contact, address-book entry | kontakutu | no | 5 (id tl ru es fr); 3 | **fail** | rung 3: **suso pi liga** "name in the phone"; the list is *suso la* (Thai *rāi chûe* "name list", Turkish *kişiler* "persons") |

**Count:** 9 pass (email only just, at exactly 12), 1 borderline (police, 11 strict / 12–13 lenient), 12 fail.
- Of the 12 failures:
  - 7 can be built from existing words (percent, train, licence, electricity, hospital, bicycle, contact).
  - 5 need new roots: hour, minute, second, degree, and "picture" for photo.
- Of the passes, five keep today's form exactly: battery, euro, yuan, rupee, camera. Police and email also keep it if they pass.
- Three passes would change form if the median rule is applied literally: dollar → *dolalu*, internet → *intelunetu*, kilometre → *kilometulu*. All three are longer, by one syllable (dollar, kilometre) or a vowel change (internet).
  - Today's forms came from English pronunciation, which the method no longer allows ("adapted from the panel's median pronunciation, not from English").
  - Whether one extra syllable is worth it is a C1 cost question for the author.

**Patterns worth a decision rather than case by case:**
1. **The time units all fail.** Hour, minute and second are tier 3–4 words, and the panel splits into three unrelated families:
   - Chinese 時/分/秒 (zh ja ko vi);
   - Arabic *sāʿa*/*daqīqa*/*ṯāniya* (ar fa tr sw, partly ha);
   - Latin *hora*/*minuta*/*secunda* (es fr ru tl qu, plus South Asian loans).

   None reaches 12. Under L4 they need native roots. The upside: at tier 4, `words.py` would likely give two-syllable forms, shorter than *awuwa* and *minitu* (three) and *sekandu* (three). §8.2.5 ("Hours, minutes and seconds are borrowed") would change.
2. **Currencies may be names, not loans.** Rung 1 points to the issuer's name: ISO 4217 codes in writing, EU law for "euro". By that reading they belong under §11.1 (names keep their owner's form) more than under §11.3. All four pass the panel anyway, so the open point is only the form:
   - yuan: issuer *wenu* vs panel *yuwan*;
   - rupee: issuer *lupaya* vs panel *lupi*;
   - dollar: no single issuer; the panel gives *dolalu*.
3. **SI units.** §9.3 says measurements use "borrowed international unit names". Kilometre passes easily, and metre, gram, litre and kilogram would too (not tested here). Hour, minute, second, degree and percent don't. So the blanket statement in §9.3/§8.2.5 is too broad: only the metric names are shared.
4. **The panel's own lumps.** For three failures the panel prefers a broader native word:
   - photo = "picture" (ar *ṣūra*, fa *aks*, sw *picha*, th *rûup*, vi *ảnh*, yo *àwòrán*);
   - electricity = "lightning" or "fire/power" (hi *bijlī*, fa *barq*, sw *umeme*; ha *wuta* and yo *iná* "fire"; th *fai fáa* "sky-fire");
   - licence = "permission paper".

   The proposals follow those lumps.

## Full panel data

Legend: ✓ cognate with the loan's international form, ✗ not. Romanisation is mine where Wiktionary gives none.

### dollar (Wt: [dollar](https://en.wiktionary.org/wiki/dollar#Translations), "designation for specific currency")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 美元 měiyuán (US$); 元/块 generic | ✗ | Wt (元, 块); M (美元) |
| Japanese | ドル doru | ✓ | Wt |
| Korean | 달러 dalleo | ✓ | Wt |
| Vietnamese | đô la | ✓ | Wt |
| Thai | ดอลลาร์ dɔnlaa | ✓ | Wt |
| Indonesian | dolar | ✓ | Wt |
| Tagalog | dolyar | ✓ | Wt |
| Hindi | डॉलर ḍālar | ✓ | Wt |
| Bengali | ডলার ḍɔlar | ✓ | Wt |
| Tamil | டாலர் ṭālar | ✓ | Wt |
| Persian | دلار dolâr | ✓ | Wt |
| Arabic | دولار dūlār | ✓ | Wt |
| Turkish | dolar | ✓ | Wt |
| Russian | доллар dollar | ✓ | Wt |
| Spanish | dólar | ✓ | Wt |
| French | dollar | ✓ | Wt |
| Swahili | dola | ✓ | Wt |
| Hausa | dala | ✓ | Wt |
| Yoruba | dọ́là | ✓ | Wt |
| Quechua | dólar (Spanish loan) | ✓ | M |

### internet (Wt: [Internet](https://en.wiktionary.org/wiki/Internet#Translations))
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 互联网 hùliánwǎng, 网 wǎng | ✗ | Wt |
| Japanese | インターネット intānetto, ネット | ✓ | Wt |
| Korean | 인터넷 inteonet | ✓ | Wt |
| Vietnamese | internet / in-tơ-nét; also mạng | ✓ | Wt |
| Thai | อินเทอร์เน็ต inthəənet | ✓ | Wt |
| Indonesian | internet | ✓ | Wt |
| Tagalog | internet | ✓ | Wt |
| Hindi | इंटरनेट iṇṭarneṭ (formal अंतर्जाल) | ✓ | Wt, M\* |
| Bengali | ইন্টারনেট | ✓ | Wt |
| Tamil | இணையம் iṇaiyam in writing; spoken "internet" | ✓ | Wt, M\* |
| Persian | اینترنت internet | ✓ | Wt |
| Arabic | إنترنت internet | ✓ | Wt |
| Turkish | internet | ✓ | Wt |
| Russian | интернет | ✓ | Wt |
| Spanish | internet | ✓ | Wt |
| French | internet | ✓ | Wt |
| Swahili | intaneti | ✓ | Wt |
| Hausa | yanar gizo | ✗ | Wt |
| Yoruba | ayélujára | ✗ | M |
| Quechua | (neologism; Spanish "internet" in speech) | ✗ | Wt |

### hour (Wt: [hour](https://en.wiktionary.org/wiki/hour#Translations), "time period of sixty minutes")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 小时 xiǎoshí | ✗ | Wt |
| Japanese | 時間 jikan | ✗ | Wt |
| Korean | 시간 sigan | ✗ | Wt |
| Vietnamese | giờ, tiếng | ✗ | Wt |
| Thai | ชั่วโมง chûamoong | ✗ | Wt |
| Indonesian | jam | ✗ | Wt |
| Tagalog | oras | ✓ | Wt |
| Hindi | घंटा ghaṇṭā | ✗ | Wt |
| Bengali | ঘণ্টা ghaṇṭā | ✗ | Wt |
| Tamil | மணி நேரம் maṇi nēram | ✗ | Wt |
| Persian | ساعت sâʿat | ✗ | Wt |
| Arabic | ساعة sāʿa | ✗ | Wt |
| Turkish | saat | ✗ | Wt |
| Russian | час čas | ✗ | Wt |
| Spanish | hora | ✓ | Wt |
| French | heure | ✓ | Wt |
| Swahili | saa | ✗ | Wt |
| Hausa | awa (from English *hour*), sa'a | ✓ | Wt, [We awa](https://en.wiktionary.org/wiki/awa#Hausa) |
| Yoruba | wákàtí | ✗ | [We wakati](https://en.wiktionary.org/wiki/wakati) |
| Quechua | ura (from Spanish *hora*) | ✓ | M |

The Arabic *sāʿa* family (ar fa tr sw ha) has 5 members in 2 regions, so it fails too.

### minute, of time (Wt: [minute](https://en.wiktionary.org/wiki/minute#Translations), "unit of time")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 分钟 fēnzhōng | ✗ | Wt |
| Japanese | 分 fun | ✗ | Wt |
| Korean | 분 bun | ✗ | Wt |
| Vietnamese | phút | ✗ | Wt |
| Thai | นาที naathii | ✗ | Wt |
| Indonesian | menit | ✓ | Wt |
| Tagalog | minuto | ✓ | Wt |
| Hindi | मिनट minaṭ | ✓ | Wt |
| Bengali | মিনিট miniṭ | ✓ | Wt |
| Tamil | நிமிடம் nimiṭam (from Sanskrit *nimiṣa* "blink", not *minute*) | ✗ | Wt; etymology M |
| Persian | دقیقه daqiqe | ✗ | Wt |
| Arabic | دقيقة daqīqa | ✗ | Wt |
| Turkish | dakika | ✗ | Wt |
| Russian | минута minuta | ✓ | Wt |
| Spanish | minuto | ✓ | Wt |
| French | minute | ✓ | Wt |
| Swahili | dakika | ✗ | Wt |
| Hausa | minti | ✓ | Wt, [We minti](https://en.wiktionary.org/wiki/minti) |
| Yoruba | ìṣẹ́jú | ✗ | M |
| Quechua | minutu (Spanish loan); Wt gives *chinini* | ✓ | M\* |

The total is 9 even if Tamil is counted, which would make it 10.

### second, of time (Wt: [second](https://en.wiktionary.org/wiki/second#Translations), "one-sixtieth of a minute; SI unit of time")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 秒 miǎo | ✗ | Wt |
| Japanese | 秒 byō | ✗ | Wt |
| Korean | 초 cho | ✗ | Wt |
| Vietnamese | giây | ✗ | Wt |
| Thai | วินาที winaathii | ✗ | Wt |
| Indonesian | detik (sekon technical) | ✗ | Wt |
| Tagalog | segundo | ✓ | Wt |
| Hindi | सेकंड sekaṇḍ | ✓ | Wt |
| Bengali | সেকেন্ড sekenḍ | ✓ | Wt |
| Tamil | நொடி noḍi, வினாடி | ✗ | Wt |
| Persian | ثانیه sâniye | ✗ | Wt |
| Arabic | ثانية ṯāniya (calque) | ✗ | Wt |
| Turkish | saniye | ✗ | Wt |
| Russian | секунда sekunda | ✓ | Wt |
| Spanish | segundo | ✓ | Wt |
| French | seconde | ✓ | Wt |
| Swahili | sekunde | ✓ | Wt |
| Hausa | daƙiƙa | ✗ | M |
| Yoruba | ìṣẹ́jú-àáyá | ✗ | M |
| Quechua | sigundu (Spanish loan) | ✓ | M |

Rejected rung-3 option: reuse **foke** "moment". Indonesian *detik* and Tamil *noḍi* do lump second with moment, but "5 seconds" needs an exact unit (B3).

### kilometre (Wt: [kilometre](https://en.wiktionary.org/wiki/kilometre#Translations), "unit of measure")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 公里 gōnglǐ | ✗ | Wt |
| Japanese | キロメートル kiromētoru, キロ | ✓ | Wt |
| Korean | 킬로미터 killomiteo | ✓ | Wt |
| Vietnamese | ki-lô-mét; also cây số | ✓ | Wt |
| Thai | กิโลเมตร kilomet | ✓ | Wt |
| Indonesian | kilometer | ✓ | Wt |
| Tagalog | kilometro | ✓ | Wt |
| Hindi | किलोमीटर | ✓ | Wt |
| Bengali | কিলোমিটার | ✓ | Wt |
| Tamil | கிலோமீட்டர் | ✓ | Wt |
| Persian | کیلومتر kilometr | ✓ | Wt |
| Arabic | كيلومتر kīlomitr | ✓ | Wt |
| Turkish | kilometre | ✓ | Wt |
| Russian | километр | ✓ | Wt |
| Spanish | kilómetro | ✓ | Wt |
| French | kilomètre | ✓ | Wt |
| Swahili | kilomita / kilometa | ✓ | Wt |
| Hausa | kilomita | ✓ | M |
| Yoruba | kìlómítà | ✓ | Wt |
| Quechua | kilometro (Spanish loan) | ✓ | M |

Median: third vowel e (9) over i (8). The r is kept in 14 of 19 forms. That gives [kilometr], which `names.py` adapts as *kilometulu*; [kilometər] gives *kilometalu*. Side note: since SI prefixes are productive, the author may prefer to borrow *kilo* and *metre* as parts rather than each composite unit.

### percent (Wt: [percent](https://en.wiktionary.org/wiki/percent#Translations))
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 百分之 bǎifēnzhī "hundred-parts-of" | ✗ | Wt |
| Japanese | パーセント pāsento | ✓ | Wt |
| Korean | 퍼센트 peosenteu, 프로 | ✓ | Wt |
| Vietnamese | phần trăm "part hundred" | ✗ | Wt |
| Thai | เปอร์เซ็นต์ poesen | ✓ | Wt |
| Indonesian | persen | ✓ | Wt |
| Tagalog | porsiyento | ✓ | Wt |
| Hindi | प्रतिशत pratiśat "per hundred" (spoken *parsenṭ* common) | ✗ | Wt, M |
| Bengali | শতাংশ śatāṃśa "hundred-part" | ✗ | Wt |
| Tamil | சதவீதம் catavītam | ✗ | Wt |
| Persian | درصد darsad "in hundred" | ✗ | Wt |
| Arabic | في المئة fī l-miʾa "in the hundred" | ✗ | Wt |
| Turkish | yüzde "hundred-in" | ✗ | Wt |
| Russian | процент procent | ✓ | Wt |
| Spanish | por ciento | ✓ | Wt |
| French | pour cent | ✓ | Wt |
| Swahili | asilimia | ✗ | Wt |
| Hausa | kashi (cikin ɗari) | ✗ | M |
| Yoruba | ìdá-ọgọ́rùn-ún | ✗ | M |
| Quechua | porsiyentu (Spanish loan) | ✓ | M |

Counting spoken Hindi and Bengali *parsenṭ* gives 11, still a fail. Almost every panel language builds the word as "N per/in/of a hundred", so rung 3 fits. The grammar already says it: a number before **pi** makes a part (*fi pi ka* "one of three"), so *ka yawu pi loki* is "30 of 100". It has the same syllable count as *pasentu* + number, and `%` still passes through in writing (§3.4).

### email (Wt: [email](https://en.wiktionary.org/wiki/email#Translations), "message sent through an electronic system")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 邮件 yóujiàn, 电邮 diànyóu | ✗ | Wt |
| Japanese | メール mēru | ✓ | Wt |
| Korean | 이메일 imeil, 메일 | ✓ | Wt |
| Vietnamese | email (formal thư điện tử) | ✓ | Wt, M\* |
| Thai | อีเมล iimeew | ✓ | Wt |
| Indonesian | email (official coinage *surel*) | ✓ | Wt (system sense), M\* |
| Tagalog | email | ✓ | M |
| Hindi | ईमेल īmel | ✓ | Wt |
| Bengali | ইমেইল imeil | ✓ | Wt |
| Tamil | மின்னஞ்சல் miṉṉañcal | ✗ | Wt |
| Persian | ایمیل imeyl | ✓ | Wt |
| Arabic | إيميل īmēl (formal بريد إلكتروني) | ✓ | Wt |
| Turkish | e-posta (also mail) | ✗ | Wt |
| Russian | имейл imejl / мейл; often почта "mail" | ✓ | Wt, M\* |
| Spanish | correo (electrónico) | ✗ | Wt |
| French | mail / e-mail (Quebec courriel) | ✓ | Wt |
| Swahili | barua pepe | ✗ | Wt, [We](https://en.wiktionary.org/wiki/barua_pepe) |
| Hausa | (no data; *saƙon imel* in media) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | (no data) | ✗ | M |

Everyday count: 12 in 5 regions, an exact pass. It rests on four M\* judgments (vi, id, ru, and colloquial ar). Counting only Wiktionary's first-listed words gives about 9, a fail. If the author counts it as a fail, rung 3: **ge sege** "what is sent" (short; context gives "email" on a computer or phone). The compound *spam* (*imeyilu bekin*) depends on this word.

### photo (Wt: [photograph](https://en.wiktionary.org/wiki/photograph#Translations), "picture|photo")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 照片 zhàopiàn | ✗ | Wt |
| Japanese | 写真 shashin | ✗ | Wt |
| Korean | 사진 sajin | ✗ | Wt |
| Vietnamese | ảnh, hình | ✗ | Wt |
| Thai | รูป(ถ่าย) rûup(thàai) | ✗ | Wt |
| Indonesian | foto | ✓ | Wt |
| Tagalog | litrato | ✗ | Wt |
| Hindi | फ़ोटो foṭo, तस्वीर | ✓ | Wt |
| Bengali | ফটো phaṭo | ✓ | Wt |
| Tamil | புகைப்படம் pukaippaṭam (spoken "photo" common) | ✗ | M |
| Persian | عکس aks | ✗ | Wt |
| Arabic | صورة ṣūra | ✗ | Wt |
| Turkish | fotoğraf | ✓ | Wt |
| Russian | фото, фотография | ✓ | Wt |
| Spanish | foto | ✓ | Wt |
| French | photo | ✓ | Wt |
| Swahili | picha | ✗ | Wt |
| Hausa | hoto | ✓ | [We hoto](https://en.wiktionary.org/wiki/hoto) |
| Yoruba | àwòrán | ✗ | M |
| Quechua | foto (Spanish loan) | ✓ | M |

The picture-word lump is the majority pattern: zh 片, vi, th, fa, ar, sw, yo, and tl *litrato* < *retrato*. The lexicon has no "picture, image" root. That gap, more than photo itself, is the finding.

### train (Wt: [train](https://en.wiktionary.org/wiki/train#Translations), "line of connected cars or carriages")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 火车 huǒchē | ✗ | Wt |
| Japanese | 電車 densha, 列車 | ✗ | Wt |
| Korean | 기차 gicha | ✗ | Wt |
| Vietnamese | tàu hỏa, xe lửa | ✗ | Wt |
| Thai | รถไฟ rót fai | ✗ | Wt |
| Indonesian | kereta (api) | ✗ | Wt |
| Tagalog | tren | ✓ | Wt |
| Hindi | ट्रेन ṭren, रेलगाड़ी | ✓ | Wt |
| Bengali | ট্রেন ṭren | ✓ | Wt |
| Tamil | ரயில் rayil (from *rail*) | ✗ | Wt |
| Persian | قطار qatâr | ✗ | Wt |
| Arabic | قطار qiṭār | ✗ | Wt |
| Turkish | tren | ✓ | Wt |
| Russian | поезд poezd | ✗ | Wt |
| Spanish | tren | ✓ | Wt |
| French | train | ✓ | Wt |
| Swahili | treni, garimoshi | ✓ | Wt |
| Hausa | jirgin ƙasa | ✗ | M |
| Yoruba | ọkọ̀ ojú irin | ✗ | [We](https://en.wiktionary.org/wiki/%E1%BB%8Dk%E1%BB%8D_oju_irin) |
| Quechua | tren (Spanish loan) | ✓ | M |

The most common built pattern is "fire cart" (zh vi th id), which describes steam. That isn't a known-wrong belief, but it is out of date, so it isn't proposed.

### licence (Wt: [license](https://en.wiktionary.org/wiki/license#Translations), "legal document giving official permission")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 执照 zhízhào, 许可证 | ✗ | Wt |
| Japanese | 免許 menkyo | ✗ | Wt |
| Korean | 면허 myeonheo | ✗ | Wt |
| Vietnamese | giấy phép | ✗ | Wt |
| Thai | ใบอนุญาต bai anuyâat | ✗ | Wt |
| Indonesian | lisensi (everyday *izin*) | ✓ | Wt |
| Tagalog | lisensya | ✓ | M |
| Hindi | लाइसेंस lāisens | ✓ | Wt |
| Bengali | লাইসেন্স | ✓ | Wt |
| Tamil | உரிமம் urimam | ✗ | Wt |
| Persian | مجوز mojavvez | ✗ | Wt |
| Arabic | رخصة ruxṣa | ✗ | Wt |
| Turkish | ruhsat, ehliyet (driving) | ✗ | Wt, M |
| Russian | лицензия licenzija (driving: права) | ✓ | Wt |
| Spanish | licencia | ✓ | Wt |
| French | permis everyday; licence for software and sport | ✗ | Wt, M\* |
| Swahili | leseni | ✓ | [We leseni](https://en.wiktionary.org/wiki/leseni) |
| Hausa | lasisi | ✓ | [We lasisi](https://en.wiktionary.org/wiki/lasisi) |
| Yoruba | ìwé-àṣẹ | ✗ | M |
| Quechua | licencia (Spanish loan) | ✓ | M |

### electricity (Wt: [electricity](https://en.wiktionary.org/wiki/electricity#Translations), "form of energy")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 电 diàn (orig. "lightning") | ✗ | Wt |
| Japanese | 電気 denki | ✗ | Wt |
| Korean | 전기 jeongi | ✗ | Wt |
| Vietnamese | điện | ✗ | Wt |
| Thai | ไฟฟ้า fai fáa "sky-fire" | ✗ | Wt |
| Indonesian | listrik (< Dutch *elektrisch*; recognisable only weakly) | ✓ | Wt |
| Tagalog | kuryente (< Spanish *corriente*) | ✗ | Wt |
| Hindi | बिजली bijlī "lightning" | ✗ | Wt |
| Bengali | বিজলি / বিদ্যুৎ | ✗ | Wt |
| Tamil | மின்சாரம் miṉcāram (*min* "lightning") | ✗ | Wt |
| Persian | برق barq "lightning" | ✗ | Wt |
| Arabic | كهرباء kahrabāʾ | ✗ | Wt |
| Turkish | elektrik | ✓ | Wt |
| Russian | электричество | ✓ | Wt |
| Spanish | electricidad (everyday also *luz*) | ✓ | Wt |
| French | électricité | ✓ | Wt |
| Swahili | umeme "lightning" | ✗ | Wt |
| Hausa | wuta "fire", (wutar) lantarki | ✗ | Wt, M |
| Yoruba | iná (mànàmáná) "fire/light" | ✗ | [We ina](https://en.wiktionary.org/wiki/ina) |
| Quechua | pinchikilla | ✗ | Wt |

### degree (°) (Wt: [degree](https://en.wiktionary.org/wiki/degree#Translations), "unit of measurement of temperature")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 度 dù | ✗ | Wt |
| Japanese | 度 do | ✗ | Wt |
| Korean | 도 do | ✗ | Wt |
| Vietnamese | độ | ✗ | Wt |
| Thai | องศา ongsǎa | ✗ | Wt |
| Indonesian | derajat | ✗ | Wt |
| Tagalog | antas (Taglish "degrees" common) | ✗ | Wt |
| Hindi | डिग्री ḍigrī | ✓ | Wt |
| Bengali | ডিগ্রি ḍigri | ✓ | Wt |
| Tamil | டிகிரி ṭikiri | ✓ | M |
| Persian | درجه daraje | ✗ | Wt |
| Arabic | درجة daraja | ✗ | Wt |
| Turkish | derece | ✗ | Wt |
| Russian | градус gradus | ✗ | Wt |
| Spanish | grado | ✗ | Wt |
| French | degré | ✓ | Wt |
| Swahili | digrii | ✓ | [We digrii](https://en.wiktionary.org/wiki/digrii) |
| Hausa | digiri | ✓ | M |
| Yoruba | ìwọ̀n | ✗ | M |
| Quechua | grado (Spanish loan) | ✗ | M |

There are three families of four (度; *daraja*; *gradus*) and the English family of six. None passes.

### hospital (Wt: [hospital](https://en.wiktionary.org/wiki/hospital#Translations), "large medical facility")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 医院 yīyuàn | ✗ | Wt |
| Japanese | 病院 byōin "sick-house" | ✗ | Wt |
| Korean | 병원 byeongwon | ✗ | Wt |
| Vietnamese | bệnh viện | ✗ | Wt |
| Thai | โรงพยาบาล roong phayaabaan | ✗ | Wt |
| Indonesian | rumah sakit "sick-house" | ✗ | Wt |
| Tagalog | ospital | ✓ | Wt |
| Hindi | अस्पताल aspatāl | ✓ | Wt |
| Bengali | হাসপাতাল hāspātāl | ✓ | Wt |
| Tamil | ஆஸ்பத்திரி āspattiri (formal மருத்துவமனை) | ✓ | Wt, M\* |
| Persian | بیمارستان bimârestân "sick-place" | ✗ | Wt |
| Arabic | مستشفى mustašfā | ✗ | Wt |
| Turkish | hastane "sick-house" | ✗ | Wt |
| Russian | больница bol'nica | ✗ | Wt |
| Spanish | hospital | ✓ | Wt |
| French | hôpital | ✓ | Wt |
| Swahili | hospitali | ✓ | Wt |
| Hausa | asibiti | ✓ | [We asibiti](https://en.wiktionary.org/wiki/asibiti) |
| Yoruba | ilé-ìwòsàn "healing house" | ✗ | Wt |
| Quechua | hampina wasi "healing house" | ✗ | Wt |

### bicycle (Wt: [bicycle](https://en.wiktionary.org/wiki/bicycle#Translations), "vehicle")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 自行车 zìxíngchē | ✗ | Wt |
| Japanese | 自転車 jitensha | ✗ | Wt |
| Korean | 자전거 jajeongeo | ✗ | Wt |
| Vietnamese | xe đạp | ✗ | Wt |
| Thai | จักรยาน jàkkràyaan | ✗ | Wt |
| Indonesian | sepeda | ✗ | Wt |
| Tagalog | bisikleta | ✓ | Wt |
| Hindi | साइकिल sāikil | ✓ | Wt |
| Bengali | সাইকেল sāikel | ✓ | Wt |
| Tamil | சைக்கிள் saikkiḷ | ✓ | Wt |
| Persian | دوچرخه dočarxe "two-wheel" (Dari bāysikl) | ✗ | Wt |
| Arabic | دراجة darrāja | ✗ | Wt |
| Turkish | bisiklet | ✓ | Wt |
| Russian | велосипед velosiped | ✗ | Wt |
| Spanish | bicicleta, bici | ✓ | Wt |
| French | vélo (bicyclette dated) | ✗ | Wt |
| Swahili | baisikeli | ✓ | Wt |
| Hausa | keke; basukur (< *bicycle*) | ✗ (✓ if *basukur* counts) | Wt, [We basukur](https://en.wiktionary.org/wiki/basukur), M\* |
| Yoruba | kẹ̀kẹ́ | ✗ | Wt |
| Quechua | bicicleta (Spanish loan) | ✓ | M |

### battery (Wt: [battery](https://en.wiktionary.org/wiki/battery#Translations), "device storing electricity")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 电池 diànchí | ✗ | Wt |
| Japanese | バッテリー batterī (dry cell 電池) | ✓ | Wt |
| Korean | 배터리 baeteori | ✓ | Wt |
| Vietnamese | pin (< French *pile*) | ✗ | Wt |
| Thai | แบตเตอรี่ bɛ̀ttəərîi | ✓ | Wt |
| Indonesian | baterai | ✓ | Wt |
| Tagalog | baterya | ✓ | Wt |
| Hindi | बैटरी bɛṭrī | ✓ | Wt |
| Bengali | ব্যাটারি bæṭari | ✓ | Wt |
| Tamil | பேட்டரி pēṭṭari | ✓ | Wt |
| Persian | باتری bâtri | ✓ | Wt |
| Arabic | بطارية baṭṭāriyya | ✓ | Wt |
| Turkish | pil (car: akü) | ✗ | Wt |
| Russian | батарейка batarejka | ✓ | Wt |
| Spanish | batería (dry cell pila) | ✓ | Wt |
| French | batterie (dry cell pile) | ✓ | Wt |
| Swahili | betri | ✓ | [We betri](https://en.wiktionary.org/wiki/betri) |
| Hausa | batir | ✓ | [We batir](https://en.wiktionary.org/wiki/batir) |
| Yoruba | bátìrì | ✓ | M |
| Quechua | batería (Spanish loan) | ✓ | M |

Median second vowel: a 6 (ko th bn ta ar ru), e 4, none 4, i 2. That gives [batari], which is *batali*, today's form.

### euro (Wt: [euro](https://en.wiktionary.org/wiki/euro#Translations), "currency unit of the EMU")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 欧元 ōuyuán | ✗ | Wt |
| Japanese | ユーロ yūro | ✓ | Wt |
| Korean | 유로 yuro | ✓ | Wt |
| Vietnamese | euro | ✓ | Wt |
| Thai | ยูโร yuuroo | ✓ | Wt |
| Indonesian | euro | ✓ | Wt |
| Tagalog | euro | ✓ | Wt |
| Hindi | यूरो yūro | ✓ | Wt |
| Bengali | ইউরো iuro | ✓ | Wt |
| Tamil | யூரோ yūrō | ✓ | M |
| Persian | یورو yuro | ✓ | Wt |
| Arabic | يورو yūrū | ✓ | Wt |
| Turkish | avro / euro | ✓ | Wt |
| Russian | евро jevro | ✓ | Wt |
| Spanish | euro | ✓ | Wt |
| French | euro | ✓ | Wt |
| Swahili | yuro | ✓ | M |
| Hausa | yuro | ✓ | M |
| Yoruba | yúrò | ✓ | Wt |
| Quechua | euro | ✓ | M |

Median [juro] (11 forms with y-) gives *yulo*.

### yuan (Wt: [yuan](https://en.wiktionary.org/wiki/yuan#Translations))
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 元 yuán (spoken 块 kuài) | ✓ | Wt |
| Japanese | 人民元 jinmingen, 元 gen | ✗ | Wt |
| Korean | 위안 wian | ✓ | Wt |
| Vietnamese | nhân dân tệ (Wt nguyên) | ✗ | Wt, M |
| Thai | หยวน yǔan | ✓ | Wt |
| Indonesian | yuan | ✓ | M |
| Tagalog | yuan | ✓ | M |
| Hindi | युआन yuān | ✓ | Wt |
| Bengali | ইউয়ান | ✓ | M |
| Tamil | யுவான் | ✓ | M |
| Persian | یوان yuân | ✓ | Wt |
| Arabic | يوان yuwān | ✓ | Wt |
| Turkish | yuan | ✓ | M |
| Russian | юань juan' | ✓ | Wt |
| Spanish | yuan | ✓ | Wt |
| French | yuan | ✓ | Wt |
| Swahili | yuan | ✓ | M |
| Hausa | yuan | ✓ | M |
| Yoruba | yuan | ✓ | M |
| Quechua | yuan | ✓ | M |

### rupee (Wt: [rupee](https://en.wiktionary.org/wiki/rupee#Translations))
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 卢比 lúbǐ | ✓ | Wt |
| Japanese | ルピー rupī | ✓ | Wt |
| Korean | 루피 rupi | ✓ | Wt |
| Vietnamese | rupi | ✓ | M |
| Thai | รูปี ruupii | ✓ | Wt |
| Indonesian | rupee (cf. own *rupiah*) | ✓ | Wt |
| Tagalog | rupya | ✓ | Wt |
| Hindi | रुपया rupayā | ✓ | Wt |
| Bengali | টাকা ṭākā (everyday for money/rupee) | ✗ | Wt |
| Tamil | ரூபாய் rūpāy | ✓ | Wt |
| Persian | روپیه rupiye | ✓ | Wt |
| Arabic | روبية rūbiyya | ✓ | Wt |
| Turkish | rupi | ✓ | Wt |
| Russian | рупия rupija | ✓ | Wt |
| Spanish | rupia | ✓ | Wt |
| French | roupie | ✓ | Wt |
| Swahili | rupia | ✓ | Wt |
| Hausa | rupi | ✓ | M |
| Yoruba | rúpì | ✓ | M |
| Quechua | rupia | ✓ | M |

### police (Wt: [police](https://en.wiktionary.org/wiki/police#Translations), "local or general law enforcement agency")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 警察 jǐngchá | ✗ | Wt |
| Japanese | 警察 keisatsu | ✗ | Wt |
| Korean | 경찰 gyeongchal | ✗ | Wt |
| Vietnamese | cảnh sát, công an | ✗ | Wt |
| Thai | ตำรวจ tamrùat | ✗ | Wt |
| Indonesian | polisi | ✓ | Wt |
| Tagalog | pulis | ✓ | Wt |
| Hindi | पुलिस pulis | ✓ | Wt |
| Bengali | পুলিশ puliś | ✓ | Wt |
| Tamil | போலீஸ் pōlīs (formal காவல்) | ✓ | Wt, M\* |
| Persian | پلیس polis | ✓ | Wt |
| Arabic | شرطة šurṭa (Egyptian colloquial بوليس būlīs) | ✗ (✓ lenient) | Wt |
| Turkish | polis | ✓ | Wt |
| Russian | полиция policija | ✓ | Wt |
| Spanish | policía | ✓ | Wt |
| French | police | ✓ | Wt |
| Swahili | polisi | ✓ | Wt |
| Hausa | ɗan sanda / 'yan sanda | ✗ | M |
| Yoruba | ọlọ́pàá | ✗ | [We](https://en.wiktionary.org/wiki/%E1%BB%8Dl%E1%BB%8Dpaa) |
| Quechua | chapaq "guard" (Wt); policía in bilingual speech | ✗ (✓ lenient) | Wt, M |

### camera (Wt: [camera](https://en.wiktionary.org/wiki/camera#Translations), "still camera")
| Lang | Everyday word | Shared | src |
|---|---|---|---|
| Mandarin | 相机 xiàngjī | ✗ | Wt |
| Japanese | カメラ kamera | ✓ | Wt |
| Korean | 카메라 kamera | ✓ | Wt |
| Vietnamese | máy ảnh | ✗ | Wt |
| Thai | กล้อง klɔ̂ng | ✗ | Wt |
| Indonesian | kamera | ✓ | Wt |
| Tagalog | kamera | ✓ | Wt |
| Hindi | कैमरा kæmrā | ✓ | Wt |
| Bengali | ক্যামেরা kyāmerā | ✓ | Wt |
| Tamil | கேமரா kēmarā | ✓ | Wt |
| Persian | دوربین durbin (Dari کمره kamra) | ✗ | Wt |
| Arabic | كاميرا kāmērā | ✓ | Wt |
| Turkish | fotoğraf makinesi (phone/video: kamera) | ✗ | Wt |
| Russian | камера / фотоаппарат | ✓ | Wt |
| Spanish | cámara | ✓ | Wt |
| French | appareil photo (caméra = video) | ✗ | Wt |
| Swahili | kamera | ✓ | Wt |
| Hausa | kyamara | ✓ | Wt |
| Yoruba | kámẹ́rà | ✓ | [We kamẹra](https://en.wiktionary.org/wiki/kam%E1%BA%B9ra) |
| Quechua | cámara (Spanish loan) | ✓ | M |

### contact, address-book entry (Wt: [contact](https://en.wiktionary.org/wiki/contact#Translations), "someone with whom one is in communication"; phone-interface labels from memory)
| Lang | Everyday word (phone UI) | Shared | src |
|---|---|---|---|
| Mandarin | 联系人 liánxìrén | ✗ | Wt, M |
| Japanese | 連絡先 renrakusaki | ✗ | Wt |
| Korean | 연락처 yeollakcheo | ✗ | M |
| Vietnamese | danh bạ | ✗ | M |
| Thai | รายชื่อ rāi chûe "name list" | ✗ | M |
| Indonesian | kontak | ✓ | M |
| Tagalog | contact / kontak | ✓ | M |
| Hindi | संपर्क sampark | ✗ | M |
| Bengali | পরিচিতি paricit | ✗ | M |
| Tamil | தொடர்புகள் toṭarpukaḷ | ✗ | M |
| Persian | مخاطبین moxâtabin | ✗ | Wt, M |
| Arabic | جهات الاتصال jihāt al-ittiṣāl | ✗ | M |
| Turkish | kişiler "persons" | ✗ | M |
| Russian | контакты kontakty | ✓ | Wt |
| Spanish | contactos | ✓ | M |
| French | contacts | ✓ | Wt |
| Swahili | anwani | ✗ | M |
| Hausa | (no data) | ✗ | M |
| Yoruba | (no data) | ✗ | M |
| Quechua | (no data) | ✗ | M |

## Other words that look borrowed

- **No native root is a loan.** Some look like other languages' words by accident:
  - *lemon* "brain" and *mole* "mother" look English;
  - *batu* "problem" is Malay "stone";
  - *liga* "phone" is Spanish "league".

  Only *mole* matters. If the SI unit *mole* is ever borrowed, its adapted form *mole* collides with "mother".
- **Compounds that depend on failing loans:** *screenshot* = *foto pi du wuye*; *spam* = *imeyilu bekin* (email is borderline).
- **Outside the brief, but rung 2 applies to every form:** "mother" and "father" would very likely pass the panel test as *mama*/*papa* (zh *māma*, ru, es, sw, ha, qu *mama*…, from memory, not tested). The method deliberately left out baby words (§1.4). Whether *mama* counts as a "form the world shares" under L4 is a question for the author, not a finding.
