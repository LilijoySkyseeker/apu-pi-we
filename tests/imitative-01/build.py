"""Write panel.tsv (imitative-01) from the judgments below plus the Wiktionary translation tables.

Rows not listed in a concept's overrides take their everyday word from the Wiktionary table (first three
entries), shared = n, src = Wt. Listed rows give: everyday, kind, ipa, shared (y / n / l = lenient), src, note.
"""
import csv, os, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, f"{REPO}/tests/lexicon-ladder-01")
sys.path.insert(0, f"{REPO}/tools")
import panel as P
import names as N

LANGS = ["zh", "ja", "ko", "vi", "th", "id", "tl", "hi", "bn", "ta", "fa", "ar", "tr", "ru", "es", "fr", "sw", "ha", "yo", "qu"]
WTCODE = {"zh": "cmn"}

# concept: (tested IPA, Wiktionary page#block for the everyday word, candidate source, overrides)
C = {}


def c(name, ipa, wt, why, rows):
    C[(name, ipa)] = (wt, why, rows)


R = lambda *a: a  # (lang, everyday, kind, ipa, shared, src, note)

c("mother", "mama", "mother#female (human)", "prompt; Globasa row 53 (mama, 12 languages)", [
    R("zh", "媽媽 māma; 母親 mǔqīn (formal)", "E+N", "mama", "y", "Wt, We", "We: informal 'mum, mama'"),
    R("ja", "お母さん okāsan; ママ mama", "N", "mama", "y", "Wt, We", "We: childish 'mama'"),
    R("ko", "엄마 eomma (what children say); 어머니 eomeoni", "N", "ʌmːa", "l", "Wt, We", "adapted ama: one m"),
    R("vi", "mẹ; má (Southern)", "E", "mɛ", "l", "Wt, We", "one syllable, the base of mama"),
    R("th", "แม่ mɛ̂ɛ", "E", "mɛː", "l", "Wt", "one syllable"),
    R("id", "ibu; mama", "E", "mama", "y", "Wt, We", "We: mama 'mother (female parent)', no register label; ibu is the standard word"),
    R("tl", "nanay; mama", "N", "mama", "y", "We", "We: childish, familiar 'mum, mom'; Tagalog mama is also 'mister' (M)"),
    R("hi", "माँ mā̃; मम्मी mammī", "N", "məmːiː", "y", "We", "We: mammī childish, colloquial 'mom, mommy' (from English mummy); māmā = maternal uncle (We)"),
    R("bn", "মা ma; মাম্মি mammi", "N", "mamːi", "y", "We", "We: mammi childish, colloquial 'mother'; mama = maternal uncle (We)"),
    R("ta", "அம்மா ammā", "E", "amːaː", "l", "Wt, We", "adapted ama: one m"),
    R("fa", "مادر mādar; مامان māmān (spoken)", "N", "mɒːmɒːn", "l", "Wt, We", "adapted momon: extra n; We also lists مام mām 'childish' (would be mamu), not counted"),
    R("ar", "أمّ umm; ماما māmā", "N", "maːmaː", "y", "Wt, We", "We: childish, familiar 'mum, mummy, mama'"),
    R("tr", "anne", "E", "", "n", "Wt", "Turkish mama = baby food (We)"),
    R("ru", "мама mama; мать mat'", "E", "mama", "y", "Wt, We", ""),
    R("es", "madre; mamá", "N", "mama", "y", "Wt, We", "We: mamá familiar 'mum, mom'"),
    R("fr", "mère; maman", "N", "mamɑ̃", "l", "Wt, We", "adapted maman: extra n"),
    R("sw", "mama", "E", "mama", "y", "Wt, We", ""),
    R("ha", "uwa, inna; mama", "E", "maːma", "y", "We", "We: mama 'mother'; Wt lists uwa, inna"),
    R("yo", "ìyá; màmá", "E", "mama", "y", "We", "We: mama 'mother'; Wt grandmother table has màmá màmá"),
    R("qu", "mama", "E", "mama", "y", "Wt, We", "native word"),
])

FATHER_P = {"ja": ("お父さん otōsan; パパ papa", "N", "papa", "y", "Wt, We", "We: childish"),
            "ko": ("아빠 appa (what children say); 아버지", "N", "apːa", "l", "Wt, We", "adapted apa: one p"),
            "th": ("พ่อ phɔ̂ɔ; ป๊า páa", "N", "paː", "l", "Wt, We", "We: colloquial; one syllable"),
            "id": ("ayah, bapak; papa", "N", "papa", "y", "We", "We: colloquial 'father'"),
            "tl": ("tatay; papa", "N", "papa", "y", "Wt, We", "We: childish, familiar"),
            "hi": ("पिता pitā; पापा pāpā", "N", "paːpaː", "y", "Wt, We", "We: 'dad, daddy'; Hindi also bābā"),
            "ta": ("அப்பா appā", "E", "apːaː", "l", "Wt, We", "adapted apa: one p"),
            "ru": ("папа papa; отец otec", "E", "papa", "y", "Wt, We", ""),
            "es": ("padre; papá", "N", "papa", "y", "Wt, We", "We: familiar"),
            "fr": ("père; papa", "N", "papa", "y", "Wt, We", "We: childish"),
            "sw": ("baba", "E", "", "n", "Wt, We", "the baba form; Swahili papa = shark (M)"),
            "qu": ("tayta, tata", "E", "", "n", "Wt, We", "Quechua papa = potato (M)")}
FATHER_B = {"zh": ("爸爸 bàba; 父親 fùqīn", "E+N", "baba", "y", "Wt, We", ""),
            "vi": ("bố; ba (Southern)", "E", "ba", "l", "Wt, We", "one syllable"),
            "id": ("ayah, bapak; baba", "E", "baba", "l", "Wt, We", "We lists baba 'father' (no label); used in Arab- and Chinese-descent families (M); bapak has b-p-k"),
            "hi": ("पिता pitā; बाबा bābā", "E", "baːbaː", "y", "Wt, We", "We: 'dad, papa'; also 'paternal grandfather', 'a male elder'"),
            "bn": ("বাবা baba", "E", "baba", "y", "Wt, We", ""),
            "fa": ("پدر pedar; بابا bābā", "E", "baːbaː", "y", "Wt, We", "We: colloquial"),
            "ar": ("أب ab; بابا bābā", "N", "baːbaː", "y", "Wt, We", "We: childish"),
            "tr": ("baba", "E", "baba", "y", "Wt, We", ""),
            "sw": ("baba", "E", "baba", "y", "Wt, We", ""),
            "ha": ("ùbā; bā̀ba", "E", "baːba", "y", "Wt, We", ""),
            "yo": ("bàbá", "E", "baba", "y", "Wt, We", ""),
            "ru": ("папа papa; батя bátja", "E", "", "n", "Wt, We", "the papa form"),
            "ja": ("パパ papa", "N", "", "n", "Wt, We", "the papa form"),
            "es": ("papá", "N", "", "n", "Wt, We", "the papa form"),
            "fr": ("papa", "N", "", "n", "Wt, We", "the papa form"),
            "tl": ("tatay; papa", "N", "", "n", "Wt, We", "the papa form"),
            "ko": ("아빠 appa", "N", "", "n", "Wt, We", "the papa form (one p)"),
            "ta": ("அப்பா appā", "E", "", "n", "Wt, We", "the papa form (one p)"),
            "th": ("พ่อ phɔ̂ɔ; ป๊า páa", "N", "", "n", "Wt, We", "p"),
            "qu": ("tayta, tata", "E", "", "n", "Wt, We", "")}
c("father", "papa", "father#male parent", "prompt; Globasa row 53 (papa)", [R(k, *v) for k, v in FATHER_P.items()])
c("father", "baba", "father#male parent", "the other half of the panel's nursery word (Wt dad, daddy tables)", [R(k, *v) for k, v in FATHER_B.items()])

c("grandmother", "nana", "grandmother#mother of", "prompt (grandma nursery forms); the widest shape in the tables", [
    R("zh", "奶奶 nǎinai", "E", "nainai", "l", "Wt", "adapted nayinayi"),
    R("ja", "お婆ちゃん obāchan; バーバ bāba (nursery)", "N", "", "n", "Wt, Wb", "Wordbank JA sounds item バーバ"),
    R("id", "nenek", "E", "nenek", "l", "Wt", "adapted neneku: extra k"),
    R("hi", "नानी nānī (mother's mother); दादी dādī (father's mother)", "E", "naːniː", "y", "Wt, We", "nānā = maternal grandfather"),
    R("bn", "নানী nani (mother's mother); দাদি dadi", "E", "naniː", "y", "Wt, We", "nana = maternal grandfather (We)"),
    R("fa", "مادربزرگ mādarbozorg; ننه nane", "E", "nane", "y", "Wt", "nane is also 'mother' in speech (M)"),
    R("tr", "nine, babaanne/anneanne", "E", "nine", "y", "Wt", ""),
    R("ru", "бабушка babushka, баба", "E", "", "n", "Wt", "the baba shape (ru, ja bāba, sw bibi)"),
    R("sw", "bibi; nyanya (Kenya)", "E", "ɲaɲa", "l", "Wt, We", "nyanya adapts to nana; regional, second word"),
    R("ar", "جدّة jadda; تيتة tēta", "E", "", "n", "Wt", ""),
    R("fr", "grand-mère; mamie, mémé", "N", "", "n", "Wt", ""),
])
c("grandfather", "dada", "grandfather#from either", "prompt (grandpa nursery forms); the widest shape in the tables", [
    R("ja", "お爺ちゃん ojiichan; ジージ jīji (nursery)", "N", "dʑiːdʑi", "y", "Wb, We", "Wordbank JA sounds item ジージ・ジジ（祖父）; We 爺 jī 'grandfather'"),
    R("hi", "दादा dādā (father's father); नाना nānā", "E", "daːdaː", "y", "Wt, We", ""),
    R("bn", "দাদা dada, দাদু dadu; নানা nana", "E", "dadu", "y", "Wt, We", "dada also 'elder brother'"),
    R("ar", "جدّ jadd; جدّو jiddo, سيدو sido (Levantine)", "E", "dʒadː", "y", "Wt", "adapted dadu"),
    R("tr", "dede, büyükbaba", "E", "dede", "y", "Wt", ""),
    R("ru", "дедушка dedushka, дед ded", "E", "dʲet", "l", "Wt", "ded adapts to detu (final devoicing); dedushka to dedusuka"),
    R("ta", "தாத்தா tāttā", "E", "", "n", "Wt", "t-t"),
    R("fa", "پدربزرگ pedarbozorg", "E", "", "n", "Wt", "dādā is Tajik 'father' (We)"),
])
c("baby", "bebe", "baby#very young", "prompt; Wordbank (baby is a first word)", [
    R("vi", "em bé, bé", "E", "bɛ", "l", "Wt", "one syllable"),
    R("tl", "sanggol; bebe, beybi (colloquial)", "E", "bebe", "y", "Wt, We", "We: bebe colloquial, alternative form of beybi"),
    R("ar", "رضيع raḍīʿ; بيبي bēbī (spoken)", "E", "beːbiː", "y", "M", "spoken Levantine and Egyptian, from memory"),
    R("tr", "bebek", "E", "bebek", "l", "Wt", "adapted bebeku: extra k"),
    R("es", "bebé", "E", "bebe", "y", "Wt", ""),
    R("fr", "bébé", "E", "bebe", "y", "Wt", ""),
    R("qu", "wawa", "E", "", "n", "We", "the wawa shape: qu wawa, zh 娃娃 wáwa (Wt), es guagua (Wt, Andean)"),
    R("sw", "mtoto mchanga", "E", "", "n", "Wt", ""),
    R("yo", "ọmọ ọwọ", "E", "", "n", "M", ""),
    R("ta", "குழந்தை kuḻantai; பாப்பா pāppā", "E", "", "n", "Wt, M", ""),
])

c("cat", "mau", "cat#domestic species", "Globasa myaw; Wordbank sounds 'meow' (29 of 37 lists)", [
    R("zh", "貓 māo", "E", "mau", "y", "Wt, We", ""),
    R("ja", "猫 neko; ニャンニャン nyannyan (nursery)", "N", "", "n", "Wt, Wb", ""),
    R("ko", "고양이 goyangi; 야옹이 yaongi (childish)", "N", "", "n", "Wt, We", ""),
    R("vi", "mèo", "E", "mɛw", "y", "Wt, We", "adapted mewu (m-w)"),
    R("th", "แมว mɛɛw", "E", "mɛːw", "y", "Wt, We", ""),
    R("id", "kucing; meong (informal)", "N", "meoŋ", "l", "Wt, We", "adapted meyon"),
    R("fa", "گربه gorbe; پیشی piši, میو miyaw (childish)", "N", "mijaw", "l", "Wt, We", "adapted miyawu (m-y-w)"),
    R("tl", "pusa", "E", "", "n", "Wt", "the pus shape: tl pusa, tr pisi (childish), fa piši"),
    R("qu", "misi", "E", "", "n", "Wt, We", "the mis shape: qu misi, yo músù (We), ha mussa (We)"),
    R("sw", "paka; nyau", "E", "", "n", "Wt, We", "nyau adapts to nawu"),
])
c("dog", "wau", "dog#animal", "prompt (check only: totu exists); Globasa bwaw", [
    R("ja", "犬 inu; ワンワン wanwan (childish)", "N", "wanwan", "l", "Wt, We", "adapted wanwan (w-n-w-n)"),
    R("tl", "aso; aw-aw (childish)", "N", "ʔawʔaw", "y", "Wt, We", "adapted awawu"),
    R("ko", "개 gae; 멍멍이 meongmeongi (childish)", "N", "", "n", "Wt, We", ""),
    R("fr", "chien; toutou (childish)", "N", "", "n", "Wt, We", "toutou is close to totu, by chance"),
    R("fa", "سگ sag; هاپو hāpu (childish)", "N", "", "n", "Wt, We", ""),
    R("sw", "mbwa", "E", "", "n", "M", "missing from Wt"),
])
c("cow", "muːmuː", "cow#adult female", "Globasa mumu; Wordbank sounds 'moo' (23)", [
    R("ja", "牛 ushi; もうもう mōmō (childish)", "N", "moːmoː", "y", "Wt, We", "adapted momo"),
    R("zh", "母牛 mǔniú; 牛牛 niúniu (childish)", "N", "", "n", "Wt, We", ""),
    R("es", "vaca", "E", "", "n", "Wt", "the vaca shape: es vaca, tl baka, qu waka (not imitative)"),
])
c("sheep", "meme", "sheep#animal", "Globasa meme; Wordbank sounds 'baa' (29)", [
    R("hi", "भेड़ bheṛ; मेमना memnā 'lamb'", "E", "", "n", "Wt, We", ""),
])
c("goat", "meme", "goat#animal", "prompt; Wordbank sounds (ja メーメー is listed for goat)", [
    R("ja", "ヤギ yagi; メーメー mēmē (nursery)", "N", "meːmeː", "y", "Wt, Wb", "Wordbank JA sounds item メーメー (ヤギ)"),
    R("zh", "山羊 shānyáng; 羊咩咩 (childish, southern dialects)", "E", "", "n", "Wt, We", "not Mandarin"),
])
c("duck", "kwak", "duck#aquatic bird", "Globasa kwake; Wordbank sounds 'quack' (29)", [
    R("ha", "agwagwa", "E", "aɡwaɡwa", "l", "Wt", "imitative; adapted aguwaguwa (g-w-g-w)"),
    R("ar", "بطّة baṭṭa", "E", "", "n", "Wt", "not imitative; the bata/pato wanderwort (ar sw bata, es tl pato, vi vịt, th pèt, ta vāttu, hi batakh) splits into several adapted shapes, none above 3"),
])
c("chicken", "kuku", "chicken#bird", "prompt (rooster/chicken); Globasa kuku", [
    R("sw", "kuku", "E", "kuku", "y", "Wt, We", ""),
    R("yo", "adìẹ; àkùkọ 'rooster'", "E", "akuko", "y", "Wt", "counted for rooster (Wt rooster table)"),
    R("bn", "মুরগি murgi; কুঁকড়া kũkṛā", "E", "kukra", "l", "Wt, We", "adapted kukula"),
    R("ja", "鶏 niwatori; コケコッコー kokekokkō (childish)", "N", "kokekokːoː", "l", "Wt, We", "adapted kokekoko"),
    R("hi", "मुर्ग़ा murġā; कुक्कुट kukkuṭ (formal)", "E", "", "n", "Wt", ""),
    R("ha", "kaza", "E", "", "n", "Wt", ""),
])
c("bird", "piu", "bird#animal", "Globasa piu; Wordbank sounds 'tweet' (12)", [
    R("sw", "ndege", "E", "", "n", "Wt", ""),
])
c("cuckoo", "kuku", "cuckoo#the bird", "prompt; Wt 'cuckoo' (the sound)", [
    R("zh", "杜鵑 dùjuān, 布穀鳥 bùgǔniǎo", "E", "", "n", "Wt", ""),
    R("ja", "郭公 kakkō", "E", "kakːoː", "y", "Wt", "adapted kako"),
    R("vi", "chim cu, cu cu", "E", "ku ku", "y", "Wt", ""),
    R("th", "นกกาเหว่า nók-kaa-wàao (koel)", "E", "", "n", "M", "missing from Wt"),
    R("id", "burung kangkok, tekukur (M)", "E", "", "n", "M", "missing from Wt"),
    R("tl", "kakok", "E", "kakok", "l", "Wt", "adapted kakoku"),
    R("hi", "कोयल koyal", "E", "", "n", "Wt", "the koel"),
    R("bn", "কোকিল kokil", "E", "kokil", "l", "We", "adapted kokilu"),
    R("ta", "குயில் kuyil", "E", "", "n", "Wt", ""),
    R("fa", "کوکو kuku", "E", "kuːkuː", "y", "Wt", ""),
    R("ar", "وقواق waqwāq", "E", "", "n", "Wt", ""),
    R("tr", "guguk", "E", "", "n", "Wt", "g, not k"),
    R("ru", "кукушка kukushka", "E", "kukuʂka", "l", "Wt, We", "adapted kukusuka"),
    R("es", "cuco, cuclillo", "E", "kuko", "y", "Wt, We", ""),
    R("fr", "coucou", "E", "kuku", "y", "Wt, We", ""),
    R("sw", "kekeo", "E", "kekeo", "l", "Wt", "adapted kekeyo"),
    R("ha", "(no entry)", "E", "", "n", "M", "missing from Wt and We; not looked up further"),
    R("yo", "(no entry)", "E", "", "n", "M", "missing from Wt and We; not looked up further"),
    R("qu", "(no entry)", "E", "", "n", "M", "missing from Wt and We; not looked up further"),
])
c("crow", "kaka", "crow#any bird", "added: Globasa §4.5 kraw; Wordbank sounds 'caw'", [
    R("bn", "কাক kāk", "E", "kaːk", "y", "Wt", "adapted kaku"),
    R("ta", "காக்கை kākkai, காக்கா kākkā (colloquial)", "E", "kaːkːaː", "y", "Wt, We", ""),
    R("hi", "कौआ kauā; काक kāk (formal)", "E", "kaːk", "l", "Wt", "kāk is listed (M*), kauā is the everyday word"),
    R("th", "กา kaa", "E", "kaː", "l", "Wt", "one syllable"),
    R("ha", "hankaka", "E", "hankaka", "l", "Wt", "adapted ankaka"),
    R("id", "gagak", "E", "", "n", "Wt", "g-g-k"),
    R("sw", "kunguru", "E", "", "n", "Wt", ""),
    R("qu", "(no entry)", "E", "", "n", "M", "missing from Wt"),
])
c("owl", "huhu", "owl#bird", "Globasa huhu", [])
c("frog", "kroa", "frog#amphibian", "Globasa kroa; Wordbank sounds 'ribbit'", [
    R("sw", "chura", "E", "", "n", "Wt", ""),
])
c("bee", "beze", "bee#insect", "Globasa beze; Wordbank sounds 'buzz'", [])
c("wolf", "lobo", "wolf#animal", "prompt; no imitative name found in the panel, so the widest shape is tested", [
    R("tl", "lobo", "E", "lobo", "y", "Wt", "from Spanish"),
    R("es", "lobo", "E", "lobo", "y", "Wt", ""),
    R("ha", "kyarkeci", "E", "", "n", "M", "missing from Wt"),
    R("yo", "ìkòokò", "E", "", "n", "M", "missing from Wt"),
])
c("pig", "buːbuː", "pig#mammal", "added: Wordbank sounds 'oink'; Globasa none", [
    R("ja", "豚 buta; ブーブー būbū (childish)", "N", "buːbuː", "y", "Wt, We", ""),
    R("id", "babi", "E", "babi", "y", "Wt", ""),
    R("tl", "baboy", "E", "baboj", "l", "Wt", "adapted baboyu"),
])
c("horse", "dada", "horse#members", "added: Wordbank sounds 'neigh', 'clip clop'", [
    R("fr", "cheval; dada (childish)", "N", "dada", "y", "Wt, We", ""),
])
c("donkey", "hiha", "donkey#a domestic", "added: Wordbank sounds 'hee haw'", [])
c("mouse", "tʃuːtʃuː", "mouse#rodent", "added: Wordbank sounds 'squeak'", [
    R("ja", "鼠 nezumi; チューチュー chūchū (nursery)", "N", "tʃuːtʃuː", "y", "Wt, Wb", "Wordbank JA sounds item チューチュー（ねずみ）"),
])

c("kiss", "busu", "kiss#a touch with the lips", "prompt; Globasa mwa; the widest shape is not imitative", [
    R("ja", "キス kisu; チュー chū (colloquial)", "E", "", "n", "Wt", "chū is the imitative word; ko 뽀뽀 ppoppo; no two share one"),
    R("bn", "চুম্বন chumbon; চুমু chumu; বুসা busa", "E", "busa", "l", "Wt", "Wt lists busa; chumu is the everyday word (M*)"),
    R("fa", "بوسه buse, بوس bus", "E", "buse", "y", "Wt", ""),
    R("ar", "قبلة qubla; بوسة būsa (spoken)", "E", "buːsa", "y", "Wt", ""),
    R("tr", "öpücük; buse (literary)", "E", "buse", "l", "Wt", "buse is literary"),
    R("es", "beso", "E", "beso", "y", "Wt", ""),
    R("fr", "baiser, bisou", "E", "bizu", "y", "Wt", "bisou is the everyday noun"),
    R("sw", "busu", "E", "busu", "y", "Wt", ""),
    R("ha", "sumba", "E", "", "n", "M", "missing from Wt"),
    R("yo", "ìfẹnukonu", "E", "", "n", "M", "missing from Wt"),
])
c("knock", "tok", "knock#to rap", "prompt; Globasa toka; the knocking sound (tok, toc, тук, 똑똑) is widely shared", [
    R("bn", "টোকা ṭokā (দেওয়া)", "E", "ʈoka", "y", "We", "We: 'knock'"),
    R("tl", "katok; tuktok", "E", "tuktok", "l", "We", "adapted tukutoku"),
    R("es", "tocar (a la puerta), llamar", "E", "tokar", "l", "Wt", "adapted tokalu"),
    R("ja", "ノックする nokku suru; 叩く tataku", "E", "", "n", "Wt", "a loan of English knock (ko 노크 too)"),
    R("ta", "தட்டு taṭṭu", "E", "", "n", "M", ""),
    R("sw", "bisha hodi", "E", "", "n", "M", ""),
    R("ha", "ƙwanƙwasa", "E", "", "n", "M", ""),
    R("yo", "kan ilẹ̀kùn", "E", "", "n", "M", ""),
    R("qu", "(no entry)", "E", "", "n", "M", ""),
])
c("laugh", "haha", "laugh#show mirth", "prompt; Globasa haha", [
    R("hi", "हँसना hãsnā", "E", "", "n", "Wt", "the has shape (hi bn) and the tawa shape (id tl) reach 2 each"),
    R("sw", "cheka", "E", "", "n", "M", "missing from Wt"),
])
c("cry", "wawa", "cry#to shed tears", "prompt (wah); Globasa wawa", [
    R("sw", "lia", "E", "", "n", "M", "missing from Wt"),
    R("ha", "kuka", "E", "", "n", "M", "missing from Wt"),
    R("yo", "sọkún", "E", "", "n", "M", "missing from Wt"),
])
c("sneeze", "atʃu", "sneeze#expel air", "prompt; Globasa acum; Wordbank 'achoo'", [
    R("bn", "হাঁচি hā̃ci (দেওয়া)", "E", "hatʃi", "y", "Wt", "adapted ati"),
    R("vi", "hắt hơi, hắt xì", "E", "hat si", "l", "Wt", "adapted atusi"),
    R("qu", "achhiy", "E", "atʃʰij", "l", "Wt", "adapted atiyu"),
    R("fa", "عطسه کردن atse kardan", "E", "", "n", "Wt", "adapted ase"),
    R("ha", "atishawa", "E", "", "n", "M", "adapted atisawa"),
])
c("cough", "kof", "cough#to push air", "prompt; Globasa kof", [
    R("ha", "tari", "E", "", "n", "M", "missing from Wt"),
])
c("hiccup", "hik", "hiccup#spasm", "prompt; Globasa hiku", [
    R("ja", "しゃっくり shakkuri; ヒック hikku (the sound)", "E", "hikːu", "l", "Wt", "Wt lists hikku; it is the sound, not the everyday name (M*)"),
    R("qu", "hik'iy", "E", "hikij", "l", "Wt", "adapted ikiyu"),
    R("ha", "ƙyafta", "E", "", "n", "M", "missing from Wt"),
])
c("burp", "gep", "burp#a softer", "prompt; Globasa gepu", [
    R("ja", "げっぷ geppu", "E", "ɡepːu", "y", "Wt", "adapted gepu"),
    R("tr", "geğirme", "E", "", "n", "Wt", ""),
])
c("vomit", "ʔuak", "vomit#regurgitate the", "prompt (nursery); the only imitative everyday word found (th อ้วก)", [
    R("th", "อาเจียน aa-jian (formal); อ้วก ûak (colloquial)", "E", "ʔuak", "y", "Wt", ""),
])
c("yawn", "hwam", "yawn#open the mouth", "added: Globasa §4.5 hwam", [])
c("snore", "hor", "snore#breathe", "added: Globasa §4.5 hor", [
    R("fa", "خرخر کردن xorxor kardan", "E", "", "n", "Wt", "adapted kolukolu"),
    R("tr", "horlamak", "E", "", "n", "Wt", ""),
])
c("sleep (nursery)", "nene", "sleep#to rest", "prompt; Wordbank JA ネンネ", [
    R("ja", "寝る neru; ネンネ nenne (nursery)", "N", "nenːe", "y", "Wt, Wb", "Wordbank JA sounds item ネンネ"),
    R("fr", "dormir; dodo (childish)", "N", "", "n", "Wt, We", ""),
    R("id", "tidur; bobo (childish)", "N", "", "n", "Wt, We", ""),
    R("fa", "خوابیدن; لالا lālā (childish)", "N", "", "n", "Wt, We", ""),
    R("zh", "睡覺; 覺覺 jiàojiao (childish)", "N", "", "n", "Wt, We", ""),
    R("es", "dormir; mimir (childish)", "N", "", "n", "Wt, We", ""),
])
c("eat, food (nursery)", "mama", "food#any substance", "prompt (mamam, yumyum); Wordbank 'yum yum'", [
    R("ja", "食べ物 tabemono; マンマ manma (food, nursery)", "N", "manma", "l", "Wt, Wb", "Wordbank JA sounds item マンマ（食べ物）; adapted manma (n-m)"),
    R("ko", "음식 eumsik; 맘마 mamma (childish 'meal')", "N", "mamːa", "y", "Wt, We", ""),
    R("vi", "thức ăn; măm (to eat, of a baby)", "N", "mam", "y", "Wt, We", "adapted mamu"),
    R("tr", "yemek; mama (baby food)", "N", "mama", "y", "Wt, We", "We: 'food (in child's language)'"),
    R("ru", "еда; ням-ням nyam-nyam (M)", "N", "", "n", "Wt, M", ""),
])
c("pee (nursery)", "pipi", "urinate#to pass urine", "prompt; Wordbank (JA シーシ)", [
    R("fr", "uriner; pipi (childish)", "N", "pipi", "y", "Wt, We", ""),
    R("es", "orinar; pipí, pis (childish)", "N", "pipi", "y", "Wt, We", ""),
    R("ru", "мочиться; пипи pipi (childish)", "N", "pipi", "y", "Wt", "Wt 'pee' (urine) table"),
    R("id", "kencing; pipis", "N", "pipis", "l", "We", "adapted pipisu"),
    R("ja", "おしっこ oshikko; しーしー shīshī", "N", "", "n", "Wt", "the sisi shape: ja shīshī, hi susū (We)"),
    R("hi", "पेशाब करना; सुसू susū (childish)", "N", "", "n", "We", ""),
    R("tr", "işemek; çiş (childish)", "N", "", "n", "Wt", ""),
    R("fa", "ادرار کردن; جیش jiš (childish)", "N", "", "n", "Wt", ""),
    R("th", "ปัสสาวะ; ฉี่ chìi", "N", "", "n", "We", ""),
    R("tl", "umihi; wiwi (childish)", "N", "", "n", "We", ""),
    R("ko", "오줌 누다; 쉬 swi (childish)", "N", "", "n", "We", ""),
])
c("poo (nursery)", "kaka", "poop#feces", "prompt; Wordbank", [
    R("ar", "براز burāz; كاكا kākā", "N", "kaːkaː", "y", "Wt", ""),
    R("tr", "kaka (childish)", "N", "kaka", "y", "Wt, We", ""),
    R("ru", "кака kaka (childish)", "N", "kaka", "y", "Wt, We", ""),
    R("fr", "caca (childish)", "N", "kaka", "y", "Wt, We", ""),
    R("es", "caca (childish); popó", "N", "kaka", "y", "We", ""),
    R("qu", "aka", "E", "aka", "l", "We", "adapted aka (one k)"),
    R("bn", "হাগু hagu", "N", "", "n", "Wt", "Bengali kaka = paternal uncle (We)"),
    R("tl", "pupu (childish)", "N", "", "n", "Wt, We", "the pupu/popo shape: tl pupu, es popó, fr popo"),
    R("ha", "tutu (childish)", "N", "", "n", "We", ""),
])
c("bang, boom", "bum", "explosion#violent release", "prompt; Globasa bum", [
    R("vi", "nổ; bùm (the sound)", "E", "", "n", "Wt", "the sound word bùm/boum/bum/бум is shared as an interjection (2.10)"),
])

OUT = f"{REPO}/tests/imitative-01/panel.tsv"
cols = ["concept", "form", "ipa_form", "lang", "everyday", "kind", "ipa", "adapted", "shared", "src", "note"]
w = csv.writer(open(OUT, "w"), delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar="\\")
w.writerow(cols)
for (name, ipa), (wt, why, rows) in C.items():
    form = N.adapt(ipa.replace(" ", ""))
    page, _, blk = wt.partition("#")
    table = next((d for nm, d in P.blocks(page) if blk in nm), {})
    over = {}
    for r in rows:
        over[r[0]] = r[1:]
    for lang in LANGS:
        if lang in over:
            ev, kind, ip, sh, src, note = over[lang]
            ad = N.adapt(ip.replace(" ", "")) if ip else ""
        else:
            ws = table.get(WTCODE.get(lang, lang), [])
            if ws:
                ev, kind, ip, ad, sh, src, note = ", ".join(ws[:3]), "E", "", "", "n", "Wt", ""
            else:
                ev, kind, ip, ad, sh, src, note = "(not in Wt; not looked up)", "E", "", "", "n", "—", "cannot change the verdict"
        w.writerow([name, form, ipa, lang, ev, kind, ip, ad, sh, src, note])
print("wrote", OUT)
