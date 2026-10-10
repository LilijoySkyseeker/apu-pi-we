# Round-trip test 01 (Japanese): analysis

Method fixed in advance: `method.md`. The source was written directly in
Japanese by a blind agent (`source.ja.txt`), translated into Apu Pi We by a
second (`translation.md`), and translated back into Japanese by a third who
never saw the source (`back.ja.md`). A judge, instructed in Japanese, compared
source and back-translation (`scores.md`).

## Result

- **Meaning: 42/44.** No line scored 0.
- **English leaks (E): none caused a loss.** One candidate with no loss: "what
  time" was asked as **muyi yu** "time what", which mirrors English. Japanese
  (何時), Spanish (*qué hora*), German (*wie viel Uhr*) and Mandarin (几点) ask
  with "hour" or "point". The fixed leaks (**muyi** duration, **gimu**
  occasion) were used correctly.
- **Survived:**
  - hearsay (らしい, って → **fen**, all three times);
  - favour direction (くれる/もらう: "help him", "get"; the judge found all six
    cases intact in the back-translation);
  - dropped subjects;
  - confidence (たぶん → **kon oma**, 絶対 → **kon mape**).

## Losses and their causes

Deviation from the method: the judge scored and listed losses but didn't label
causes. Claude labelled them (L = language has no way, T = translator, E =
English leak).

| Turn | Lost | Cause |
|---|---|---|
| 4 | もう "already" surprise weakened; 来月 "next month" read as "a month from now" | L: **wo dunan fi** "after one month" is documented as "next month", but a reader can take it as a duration. The anchor+offset rule doesn't separate the calendar period from the span |
| 18 | さすが "as expected of you" became "you're kind" | L/T: no word or idiom; the translator chose "you are good" |
| 9, 17 | 俺 (casual male "I") → neutral | L, by design: pronouns carry no gender or register |
| 11 | あいつ (rough "that guy") → name | L, by design |
| 15 | めんどい (slang) → standard | L: no register |
| 3, 14 | じゃん / ね / でしょ / っけ all became the one tag **min** | L: one tag covers assuming shared knowledge, inviting agreement and checking a half-memory |

The translator also noted: no way to stack aspect (嘆いてた "was lamenting"
needs **sin** + **le**); only two interjections.

## Reading

- The fixes held, and the round trip didn't surface a new English pun.
- The real gaps are **stance and register**: sentence-final particles,
  pronoun register, slang, interjections. English barely marks these either,
  which is likely why English-sourced tests never found them.
- "Next month" vs "a month from now" is a genuine ambiguity in the time rule.

## Caveats

- One conversation, AI agents throughout.
- The translator and back-translator were instructed in English; the judge in
  Japanese. The dictionary glosses are English whatever the prompt language,
  which is the channel this test was built to probe.
- Back-translating into the source language lets world knowledge fill gaps:
  a plausible Japanese reading can hide a loss.
