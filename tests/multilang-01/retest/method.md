# Retest of the interpersonal layer (2026-10-10)

Written before running. Checks the three rooms added after multilanguage
test 01: address and titles (**lanno**), focus (**fule**, **genfo**), stance
(**iwun**, **buni**, **donon**).

- **Same sources as before**, for a direct comparison: Japanese casual
  (roundtrip-01, 42/44), Hindi–Urdu hierarchical + narrative (stage 2,
  40/44; 0 of ~10 third-person respect carried), Spanish written +
  persuasive (stage 2, 39/44; contrast lost).
- **Fresh agents, all prompted in the target language:** translator,
  back-translator (never sees the source), judge.
- **Neutral placeholders:** a word with no Apu Pi We form is written [X1],
  [X2]… and glossed only in the translator's notes, which the
  back-translator doesn't get. Fixes stage 2's leak.
- **Doc leak removed first:** the **lanno** example used "Gupta" from the
  Hindi source; it now uses a name from no test.
- **The judge scores** 0–2 per line with causes L/T/B/E, and checks the
  targets for its language: Japanese stance particles (じゃん, ね, でしょ,
  っけ); Hindi–Urdu respect for people talked about, and address; Spanish
  contrast and emphasis (*yo*, *sí tenemos*, clefts) and formal address.
