# Stress test 001: the alien and the stick

> Vocabulary as at the test date. Since 2026-10-09 the coinage rules rebuilt some compounds: commander **ewo wungu** → **no wungu**, alien **ewo yaye** → **no obu se yaye** (`data/compounds.tsv`). Later word changes (base 10, the offensive-word moves) are listed in `docs/design-log.md`.

Source paragraph, supplied by the author (2026-10-08):

> If I'm being honest, I think hitting an alien intruder in the head with a stick is a pretty good idea and making sure the alien is not your daughter first requires a pretty basic level of stick expertise. More to the point I'm trying to make, fuck you, alien sympathizer. Step zero in surviving an alien abduction is at least trying to cave in their bitch ass moon heads while they're beaming into your bedroom.

Capitals mark the stressed syllable (see "Writing" in docs/language.md). Normal writing would drop them.

## Translation

```
a          a.
NONLITERAL NONLITERAL
(This whole turn is a bit.)

lon oyi feko,
I   say true
"Honestly:"

lon pume  wun  gun      gason to     upe  wun  go  payon lukan pi ewo    yaye inwa  gan  kima netu,
I   think that there-is idea  rather good that one hit   head  of person sky  enter with wood long
"I think it's a pretty good idea to hit an intruding alien in the head with a stick,"

yen go  wupi lugo to     meli  pi kima, li  lugo ya     wun  ewo    yaye gun mu  tiwu  futa  pi go.
and one need know rather small of wood  for know before that person sky  is  not child woman of one
"and you need only fairly basic stick-knowledge to first make sure the alien isn't your daughter."

ke   bawe      li  gason pi lon, ba      gefo  me,  sonu   pi ewo    yaye la.
more important for idea  of me:  EXCLAIM CURSE you, friend of person sky  PL
"More to my point: fuck you, alien sympathizer!"

lite pi po li  nume wo    ewo    yaye la yidu go,
way  of 0   for live after person sky  PL take one
"Step zero in surviving an alien abduction"

gun wun  go  pa       walo alun  lukan dunan gefo  pi wan la,
is  that one at-least try  break head  moon  CURSE of it  PL
"is at least trying to cave in their fucking moon heads"

nin   wan la kobi gan  wino  tun kemu  soti pi go.
while it  PL move with light to  place bed  of one
"while they're beaming into your bedroom."
```

## Measurements

- **Length:** 131 syllables, against about 113 in the English. That's 16% more syllables, but they are simple consonant-vowel syllables. Languages with simple syllables (Spanish, Japanese) are spoken at roughly 7.8 syllables per second, against about 6.2 for English (Pellegrino et al. 2011, from memory). At those rates the two versions take about the same time to say.
- **Vocabulary:** 266 roots plus compounds covered everything. New concepts were all built as phrases: alien (*person sky*), intruder (*entering*), stick (*wood long*), daughter (*child woman*), sympathizer (*friend of*), expertise (*knowledge of*), abduction (*sky-people take one*), bedroom (*place bed*), beaming (*move with light*).

## What the translation says that the English doesn't

- **Two different "you"s.** The English uses "you" for the person being insulted ("fuck you") and also for anyone at all ("your daughter", "your bedroom"). The translation must choose: **me** is the listener, **go** is anyone.
- **The tone.** "san san." at the start marks the whole turn as a bit, so a reader can't take the call for violence literally.
- **"I think" is opinion, not probability.** It's the verb *think* (**pume**), not the confidence particle. The confidence particle is for chance of truth, and "is a good idea" isn't that kind of claim.

## What got lost

- **Swearing is flat.** "fuck you" and "bitch ass" both became the one curse root **gefo**. Real languages grow rich taboo vocabularies culturally. That can't be designed from first principles, only seeded.
- **Nuance in compounds.** "cave in" became *break*, and "expertise" became *knowledge*. More roots will fix this as the lexicon grows.

## Findings and fixes

| # | Finding | Fix | Status |
|---|---|---|---|
| 1 | No way to say generic "you" / "one" | GENERIC pronoun **go** | adopted |
| 2 | No "pretty/fairly", "only", "at least" | **to** RATHER, **na** ONLY, **pa** AT.LEAST; they scope over what follows, like all operators | adopted |
| 3 | No "while" | **nin** WHILE | adopted |
| 4 | No exclamations, insults or swearing | **ba** EXCLAIM speech act; one all-purpose curse root **gefo**, made with no l/w/y (swear words across languages tend to avoid these sounds: Lev-Ari & McKay 2023, from memory, to verify) | adopted |
| 5 | Tone needs to cover more than one sentence | **a a** covers the speaker's whole turn (revised in 002; first a standalone **a.**). It ends with the turn, so no closing marker can go missing. | adopted |
| 6 | "alien entering with a stick" or "hit with a stick"? | A prepositional phrase attaches to its clause's main verb, never to a modifier | adopted |
| 7 | "knowledge of [small stick]" or "[small knowledge] of stick"? | A noun's own modifiers come before its "of" phrase: **lugo to meli pi kima** | adopted |
| 8 | "Intruder" without a relative clause | Verbs can modify nouns directly: **ewo yaye inwa** "intruding alien" | adopted |
| 9 | Heavy clause subjects ("hitting an alien… is a good idea") | Clause subjects move to the end ("there's a good idea: that one hits…"). Head-first order makes this the natural phrasing. | observation |
| 10 | Grammar-syllable reserve almost used up: 4 free syllables left | Options: reshuffle content words (breaks stability) or allow two-syllable grammar words | open |
| 11 | "today/tomorrow/yesterday" were too long as phrases | Roots **mefa** today, **wuma** tomorrow, **afe** yesterday | adopted |
