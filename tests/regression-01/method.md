# Regression test 01: today's changes together (2026-10-10)

Written before running. Every change made on 2026-10-10 was tested alone;
this checks them together, on fresh texts (no doc example can leak).

- **English:** a group chat between friends making plans (casual register,
  American culture: 12-hour clock).
- **Indonesian:** a workplace chat between a junior employee, a manager and a
  colleague (hierarchical and casual; titles, pronoun register, particles).
  This language hasn't been round-tripped before.

Pipeline per text, all fresh agents prompted in the text's language:
writer → translator (current docs; neutral [X1] placeholders) → blind
back-translator → judge.

**The judge scores** 0–2 per line with causes L/T/B/E, then checks every
place where one of the day's changes was used or should have been:
- stance **a**, **buni**, **donon**; focus **o**; also **fe**; even **wi**;
- **lanno** and the address position; topic **pi X,**; habitual **manni**;
- intent **gan momu**; confidence in sixths; the 12-hour/24-hour clock;
- names in their own spelling; computer words; **to** "I"; omission
  (rule 11); **gun** "there is".

Pass: no line lost to a design problem (L), and no feature misread.
