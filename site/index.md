# Apupiwe

Apupiwe is a constructed language. Say it **AH-poo-pee-weh** ([ˈapupiwe]): stress only the first syllable, and say the last one like "wet" without the t. In the language itself it's **apu pi we**, "everyone's language".

It starts from a question. The world's languages have each worked out many of the same answers on their own, so what would you get if you took those shared answers and built one language from them, for children to grow up speaking? It's also a real language, and you can learn it here.

It is still being designed, so words and rules change from time to time. It's designed by its author together with Claude, an AI assistant: Claude does most of the research, drafting and testing, and the author decides the questions that shape the language.

## A first look

Article 1 of the Universal Declaration of Human Rights:

**ewo we tuko nume gan enpa, yen ibe bawe kige yen sogan kige. wan la lenu pume, yen lenu lugo musu upe yen musu yomo. wan la keya muge nen nen fu faba la.**

    ewo     we   tuko   nume  gan   enpa,  yen  ibe   bawe        kige  yen  sogan  kige.
    person  all  start  live  with  free   and  have  importance  same  and  right  same

    wan  la  lenu  pume,  yen  lenu  lugo  musu   upe   yen  musu   yomo.
    3    PL  can   think  and  can   know  thing  good  and  thing  bad

    wan  la  keya  muge  nen nen     fu    faba     la.
    3    PL  must  do    each.other  like  sibling  PL

"All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood." The [whole declaration](example-01-udhr.md) is on the Examples page, with the English under each paragraph.

## Where to go

- [Learn it](learn.md) in fourteen short lessons written for English speakers.
- The [reference](language.md) has every rule, with examples.
- The [dictionary](dictionary.md) lists every word. Type in it to filter, or press / anywhere on the site to search.
- [Examples](examples.md): longer texts, where you can tap any word to see its meaning.
- [The goal](goal.md) says what the language is for. [Why is it like this?](why.md) answers the questions people ask first. The [design notes](rationale.md) explain every decision, and the [changelog](design-log.md) records when each was made.

## How it's built

Apupiwe is designed as [the best language for people who would grow up speaking it, while staying learnable for any adult](rationale.md#11-what-the-project-is). [One rule shapes it](rationale.md#12-how-decisions-get-made). Where unrelated languages agree on what a language needs, it has it. Where they disagree on how to do it, it takes the simplest way. [Agreement is counted by language family](https://github.com/LilijoySkyseeker/apupiwe/blob/main/docs/vocabulary-plan.md#decisions), not by number of speakers, so a solution found independently on different continents counts for more than one that is merely widespread.

[The basic meanings](https://github.com/LilijoySkyseeker/apupiwe/blob/main/docs/vocabulary-method.md#1-which-concepts-in-what-order) come from that rule. A database of over 3,000 languages shows which meanings the most families have a word for. It also shows [where they draw the lines between meanings](https://github.com/LilijoySkyseeker/apupiwe/blob/main/docs/vocabulary-method.md#3-where-boundaries-go-lump-or-split), such as whether "moon" and "month" share a word; in most families they do, and here they do too. [Meanings that modern life uses constantly](https://github.com/LilijoySkyseeker/apupiwe/blob/main/docs/vocabulary-plan.md#decisions), like "country", get words as well.

[The sounds](rationale.md#2-sounds) are the ones most languages share: five vowels and thirteen consonants, in simple syllables almost anyone can say. Each word's sound is then chosen by [a model of how speech gets misheard](rationale.md#32-the-mishearing-model-toolsconfusionpy), so that words likely to be confused sound far apart, and every word is [checked against swear words in 34 languages](rationale.md#36-offensive-word-filter-toolsoffensivepy-dataoffensivetsv). [The meanings people use most get the shortest words](https://github.com/LilijoySkyseeker/apupiwe/blob/main/docs/grammar-rebuild-spec.md#goal), with frequency measured across 15 languages.

[The grammar](rationale.md#4-grammar) comes from the same rule: the features unrelated languages keep arriving at, each in the simplest form any of them uses.

[Native speakers always change their language](https://github.com/LilijoySkyseeker/apupiwe/blob/main/docs/drift.md#whats-already-drift-resistant), so this one is built for it. The most-used words are already short, nothing is irregular, and words are chosen to stay distinct even after the sound changes speakers are likely to make. It also has to [live alongside the world's cultures](design-log.md#coexisting-with-existing-cultures-author-2026-10-10). It carries local conventions such as clocks, calendars, units and names, and where they conflict it follows the international standard.

Underneath it all is one aim: getting meaning across correctly, at a cost speakers will actually pay. Some things are guarantees that must always hold, such as a precise way to say anything, even when everyday speech doesn't use it. Everything else is a cost, kept as low as possible for someone who speaks it all their life. [The goal](goal.md) sets this out in full.
