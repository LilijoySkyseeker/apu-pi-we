# Stress test 002: the commander

> Vocabulary as at the test date. Since 2026-10-09 the coinage rules rebuilt some compounds: commander **ewo wungu** → **no wungu**, alien **ewo yaye** → **no obu se yaye** (`data/compounds.tsv`). Later word changes (base 10, the offensive-word moves) are listed in `docs/design-log.md`.

Source: a fiction excerpt supplied by the author (2026-10-08): dialogue, narration, inner states.

Revised after back-translation test 01 (`tests/backtranslation-01/`): new roots for panic, offend, disgust, system and answer, reflexive **nen**, and the commander introduced as a woman. Measurements below are from the first version.

Pronouns: Lilith narrates (**lon**). The commander is the main third person (**wan**), so everyone and everything else in the third person is obviative (**yi**): her reaction, the emotions, the parents.

New roots for this text: now **eda**, become **lewe**, face **suku**, apologize **sepi**, again **moti**, teach **tofo**, lead **wungu**, dream **sinun**, dark **buda**, wall **senmo**, calm **fanse**, free **enpa**, glass **degun**.

## Translation

```
lon duko funo pi lon.
I   turn eye  of me    I rolled my eyes.

a          lon sepi      li  wun  lon sepi.
NONLITERAL I   apologize for that I   apologize    "Sorry for saying sorry, then."

yen eda me  kusa  se   kusa.
and now you leave from leave    "And now you retreat from retreating."

lon— me  momu wun  lon oyi yu.
I    you want that I   say what    "I— What do you want me to say?"

suku pi ewo    wungu futa  lewe   buda.
face of person lead  woman become dark    The commander's face darkened.

ba      en lilifu, me  ewo    nuta.
EXCLAIM Lilith  you person fear    "Lilith, you coward!"

lon niba tun nebe, funo tugan pi lon.
I   walk to  back  eye  wide  of me    I stepped back, my eyes wide.

mon muyi fa nin lon lugo wan, ewo wungu agi fanse pi wan.
at time none while I know her, commander lose calm of her
                                                     The commander had never lost her composure in the time I'd known her.

sepi      eni   obu  yobe tun fade  pi lon, un  lon yonnu nen.
apologize other come fast to  mouth of me,  but I   hold  self
                                                     Another apology rushed to my lips, but I held myself back.

banga, mon mala  pi lon.
panic, at  heart of me    Panic in my chest.

wan le      febo   fu   tan  gi      yu.
she ONGOING answer like this because what    Why was she reacting like this?

lon muge bamo yi      fu   yu.
I   make stop it(OBV) like what    How did I make it stop?

ba      nosen lumi. ewo       wungu oyi  fu    dinbu.
EXCLAIM god   fire  commander say   like snake "Godfire,"    the commander hissed.

me  goyu pume  nin    dili nobi fi, en lilifu.
you sit  think during day  7     Lilith    "You meditated for a week, Lilith.

min me  le      sinun nin    muyi minwe.
Q   you ONGOING dream during time whole    Were you daydreaming the whole time?"

mu  sinun, lon—
not dream  I    "No, I—"

ewo wungu miya bonko mon lon, yen tan muge bamo kegu lon mon eda.
commander look angry at me, and this make stop talk me at now
                                                     The commander fixed me with a glare that shut me up immediately.

gun      fu   don musu  in   duko, feme la we  kusa,
there-is like if  thing some turn: feel PL all leave
yen yonnu musu  meli  la pi nen  mon lini.
and keep  thing small PL of self at  far    It was as if a switch flipped—all the emotions drained away, leaving distant remnants of themselves.

banga gun tapi  mon suyon pi lon, lon keya muge upe  tan,
panic is  close at  belly of me,  I   must make good this,
un  lon gun enpa moti.
but I   is  free again    The panic was locked in my stomach, I had to fix this, but I was free again.

miya bonko pi ewo wungu lewe bebu,
look angry of commander become disgust,
yen tan  muge ke   kudu banga mon kemu  eni   pi senmo degun in   man   kuwi yi se   lugo pi lon.
and this make more big  panic at  place other of wall  glass some which keep it from know of me
                                                     The commander's glare turned to disgust, which made the panic swell on the other side of whatever glass wall was keeping it from my consciousness.

ewo wungu, lon oyi fanse, lon mu lugo wun lon muge yu, un lon sepi li wun lon yenwu me.
commander, I say  calm, I not know that I do  what, but I apologize for that I offend you
                                                     "Commander," I spoke evenly, "I don't know what I did, but I apologize for offending you."

me  mu  yenwu  lon, wan oyi ke   fanse.
you not offend me,  she say more calm    "You didn't offend me," she said in a more neutral tone.

me  yenwu  ewo    man tofo  me  banga ben.
you offend person who teach you panic that    "You offended whoever taught you that panic response."

lon lewe   nokun.
I   become ice    I froze up.

banga kubo   yomo, nin   yile   pi lon walo lafi       wun  yu   gefo  le      muwo.
panic change bad,  while system of me  try  understand that what CURSE ONGOING happen
                                                     The panic response warped awkwardly as my system tried to figure out what the fuck was going on.

me  mu  momu gun tiwu  se   eda, ewo       wungu oyi.
you not want be  child from now, commander say   "You    don't want to be a child anymore," said the commander.

gi      tan, tin      gitin mole   yen wede   pi me.
because this INSTRUCT throw mother and father of you    "So get rid of your parents.

yi        la    tofo me, min.
they(OBV) teach you, Q   It    was them, wasn't it?"
```

## Measurements

- **Length:** 414 syllables against about 337 in the English (contractions expanded), so 23% more syllables (001 was 16%). At the syllable rates of languages with simple syllables (about 7.8 per second against English 6.2, from memory), speaking time comes out about equal again: about 53 against 54 seconds.
- **Where the extra length comes from:**
  - Possession: "my" is **pi lon**, two syllables, nine times.
  - Frequent compounds: commander is **ewo wungu**, four syllables, nine times.
  - The explicit causative **muge**.

  Real languages shorten frequent compounds into new roots over time. A story with a commander in every scene would clip **ewo wungu** quickly. That's healthy evolution, not a design flaw, so no fix is adopted.

## What worked

- **Obviation did English's animacy work.** English separates the commander ("she") from her reaction ("it") by animacy. Here the commander is **wan** and everything else is **yi**, with no gender or animacy needed.
- **Echo answers:** "No, I—" is **mu sinun, lon—** ("not dreaming, I—"). The denial says *what* is denied.
- **Reflexives:** first written as a repeated pronoun (**lon yonnu lon**). The back-translation test showed that fails when the subject is a noun, so the reflexive is now **nen** "self".
- **Questions compose from parts:** why = **gi yu** "because what", how = **fu yu** "like what", what = **yu**.
- **An in-world oath grew from the curse system:** "Godfire" is **ba nosen lumi**, EXCLAIM god fire. This is how a taboo vocabulary seeds itself.
- **The hiss** became **oyi fu dinbu**, "say like a snake".

## Findings and fixes

| # | Finding | Fix | Status |
|---|---|---|---|
| 1 | Where do question words go? | In place (**me momu wun lon oyi yu.** "you want me to say what?"). Moving them to the front would break "role from position", the noise-robustness argument for SVO. | adopted |
| 2 | Indirect questions ("I don't know what I did") | **yu** inside a **wun** clause is an indirect question | adopted |
| 3 | Tag questions ("It was them, wasn't it?") | A clause-final **min** = "right?" A clause-initial **min** stays an open question. | adopted |
| 4 | "Standalone **a.**" relied on hearing a pause, which is fragile | **a** = this sentence; **a a** = the whole turn. Doubling widens or strengthens, as with **yo yo**. | adopted, 001 updated |
| 5 | "seven days" or "the seventh day"? The phrase for "day seven" was both | Noun + number = count (**dili nobi fi** seven days, 6 + 1 in base 6). Noun + **pi** + number = label or order (**lite pi po** step zero). | adopted, 001 updated |
| 6 | "You offended [whoever taught you that panic] angry": a relative clause has no end marker, so anything after it gets swallowed | Causative order is **muge** + result + object: **muge bonko me** "make angry you". Heavy phrases go last. | adopted |
| 7 | Passive / resulting state ("was locked") | **gun** + verb = the resulting state: **gun tapi** "is closed" | adopted |
| 8 | **mole wede** would mean "a fatherly mother" | Noun + noun is always modifier; coordinate with **yen**: **mole yen wede** parents | adopted |
| 9 | Dropped subjects | Allowed only for the same subject after **yen** / **un**, and for the addressee of an instruction or request | adopted |
| 10 | "So …" | **gi tan** "because this". No new word. | adopted |
| 11 | "So, get rid of…": a linker before the speech-act particle | A linker to the previous sentence may come first | adopted |
| 12 | Duration ("for a week") | **nin** + noun phrase = during | adopted |
| 13 | A verb after a preposition ("from retreating") | It names the act: **se kusa** | adopted |
| 14 | Names with foreign sounds ("Lilith") | A foreign sound maps to the native sound listeners most often hear it as (Miller & Nicely: th → f). A final consonant gets an echo vowel. Lilith → **LIlifi**. | adopted |
| 15 | Two content verbs in a row ("meditate" = **goyu pume**) | Already covered: any content word can modify the one before it ("sit thinking") | observation |
| 16 | Metaphors (face darkened, froze, glass wall) | Translated literally. Whether they land is culture, not grammar. | observation |
