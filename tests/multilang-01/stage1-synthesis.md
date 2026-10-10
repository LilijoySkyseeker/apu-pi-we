# Stage 1 synthesis: what 11 languages mark that Apu Pi We doesn't

Each language's inventory was written by a fresh agent prompted in that
language (`inventory/`). The counts below are from the tables (±1 from
parsing). This is desk judgement by AI agents, not measured loss; stage 2
checks it.

| Language | yes | partly | no |
|---|---|---|---|
| English | 96 | 52 | 7 |
| Mandarin | 76 | 44 | 10 |
| Hindi–Urdu | 45 | 44 | 6 |
| Spanish | 74 | 56 | 4 |
| Arabic | 56 | 54 | 4 |
| French | 60 | 45 | 11 |
| Bengali | 44 | 46 | 14 |
| Portuguese | 98 | 49 | 6 |
| Russian | 71 | 58 | 8 |
| Indonesian | 63 | 55 | 6 |
| Vietnamese | 74 | 32 | 9 |
| **All** | **757 (55%)** | **535 (39%)** | **85 (6%)** |

Almost nothing is outright unsayable. The losses are "partly": the content
survives, and something about it is lost: who it's for, how the speaker feels
about it, what the listener is assumed to know.

## Gap themes, by how many languages put them in their top 8

| Theme | Languages (of 11) | What's lost | Kind |
|---|---|---|---|
| **Stance and common-ground particles, discourse markers** (*you know*, *well*, じゃん, 吧/嘛, kan/dong, же/ведь, to/na, *pues*, *bah/quoi*) | 11 + Japanese round trip | as-you-know, obviously, softening, insisting, reminding, hesitating, turn-taking; all collapse into **min**, **ba**, **nun** or nothing | structural slot |
| **Relationship in address** (tu/vous, tū/tum/āp, aku/gue/saya, kin terms as pronouns, titles, endearments) | 11 | a *standing* closeness/distance/rank between speaker and listener; **nun** is per-utterance deference only, and only upward | structural, deliberately designed out |
| **Contrastive focus and topic packaging** (clefts, dislocation, word order, stress) | 10 | *I* did it, not you; as for me… | structural slot (doc: add a focus particle if a test shows loss) |
| **Scalar "even" and concession** (*even*, 连…都, bhī, даже, *aunque*, *although*) | 9 | far end of a scale; "even if" becomes "if" | missing words |
| **Definiteness** (a/the, al-, -nya, -ṭa) | 7 (article languages only) | new vs known referent | deliberate; half the world's languages have no articles |
| **Register-marked vocabulary** (formal vs casual word forms, Latinate/Sanskritic/Sino-Vietnamese layers) | 7 | the signal of formality | Restraint: speakers grow this |
| **Affectedness and volitionality** (被/把, bị/được, accidental *se*, dative, compound verbs, "it happened to me") | 6 | whether an event helped or hurt someone; accident vs intent | structural |
| **Counter-expectation and surprise** (竟然, ternyata, hóa ra, naki, вдруг) | 6 | "it turned out", "surprisingly", "suddenly" | missing words / particle |
| **Affective morphology** (diminutives, augmentatives, contempt) | 6 | tenderness, minimising a request, scorn | Restraint: speakers grow this |
| **Habitual and finer aspect** (used to, imperfect, resultatives 看完, recent past) | 5 | habit vs one-off; result reached | structural (aspect words exist; no habitual, no stacking) |
| **Respect for a third person** (uni/tini, 您/位, honorific plural) | 5 | deference to someone talked *about* | structural; **nun** only faces the listener |
| **Interjections and emotion words** (ouch, 哎呀, nossa) | 5 | which feeling | lexical |
| **Gender of referents** | 4 | the addressee's or a character's sex | deliberate (gender is a modifier) |
| **Passive / patient as topic** | 3 | news and instruction framing | structural |
| **Religious-social formulas and wishes** (in šāʾ aḷḷāh, blessings) | 1 (Arabic, 335M speakers) | the social act | partly cultural |

**Missing everyday words named along the way:** even, almost, each,
suddenly, hungry, tired, expensive, late, love, miss, disappointed, "sorry"
as sympathy.

## Reading

1. **The pattern Japanese showed is universal.** Every language flagged
   stance particles. Apu Pi We was designed around fidelity of *content*
   (confidence, source, speech act), and it does that well. What it lacks is
   the layer where speakers manage the *relationship and the shared ground*.
2. **Two of the big themes were designed out on purpose:** standing
   relationship pronouns (to protect against politeness drift) and gender.
   Stage 1 shows they're near-universal, so the reasoning deserves a second
   look. That's not the same as a verdict that it was wrong.
3. **Some gaps are cheap:** "even", "almost", "each", "suddenly" and the
   emotion words are vocabulary, and the language's normal process adds them.
4. **Some gaps the language may *block* speakers from fixing:** stance
   particles and focus markers are exactly what native speakers grow, but the
   one-syllable grammar space is full, so any they grow costs two syllables.
   That's a Restraint question: designing the slot, not the content.
