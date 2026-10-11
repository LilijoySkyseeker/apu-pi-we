# Comma test 01: results (2026-10-10)

| Text | Comma uses (Claude's count) | Lines that lost meaning without commas |
|---|---|---|
| Economy chat (English) | 10: fronted clause 3, stance 1, other 6 | 0 of 22 |
| Stage 2 English (persuasive) | 21: fronted clause 7, address at end 1, other 13 | 0 of 23 |
| Retest Hindi–Urdu (hierarchical) | 54: fronted clause 11, address at start 3, stance 4, other 36 | 0 of 22 |
| **Total** | **85** | **0 of 67** |

- **Near misses (resolved by context):**
  - an if-clause ending in a noun right before a name (English 22);
  - a name used to call someone at the start of a quote (Hindi 7);
  - a reply word read into the next clause (economy 7, no meaning lost).
- **Once the comma hurt:** "**no wungu, en danisu**" (the manager, Denise) was
  read *with* the comma as calling Denise at the end, and correctly *without*
  it as title + name. The current rule already writes title + name with no
  comma; the docs now say so explicitly.
- **Reading:** context recovered every dropped comma. The predicted breaks
  didn't happen in practice, so the comma stays the precise option, and chat
  can drop it, as the user's principle allows.
- **Limits:** the texts weren't built to stress the risky cases: a topic
  opener never occurred, and a name at the end only once. The readers are AI
  agents, who are strong at using context. Add back a targeted test if real
  misreadings of names at the end or topic openers turn up.
