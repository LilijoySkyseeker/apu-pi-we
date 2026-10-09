# Back-translation test 04: deep nesting (A7)

**Question:** relative clauses have no end marker. Does "heavy goes last" hold up in contract-style prose, or does the language need a clause-closing word?

**Round 1:** two original contract sentences with relative clauses inside relative clauses, a deposit clause, a while-clause, a before-clause, a because-clause inside an if-clause, and a limit ("at most 14 days").
- The blind reader's readings were **fully correct**.
- The reader listed where it relied on plausibility: which clause the final "before…" and "while…" clauses belonged to, and where the subject's nested clauses ended.

**Rules added** (`docs/language.md`, rule 15):
- A relative clause attaches to the nearest noun before it.
- A time, reason or condition clause at the start of a sentence belongs to the main clause; at the end, to the innermost clause.
- A pause ends a fronted or embedded clause.

**Round 2:** five sentences, three deliberately neutral so that only the rules could decide.
- **All five correct.** The final "while it rained" went to the innermost clause; the fronted one went to the main clause; "the friend of the teacher who sings" gave the teacher singing.
- **Two remaining gaps the reader flagged:**
  1. In the long sentence there was no pause between the subject's last clause and the main verb ("…the landlord sent | must pay"), so the reader decided by sense.
  2. "give [the tenant] [the keys…]" could be read as one noun, "one who rents keys", because a word-building marker can take a phrase.

  Both are fixed by the pause rule, which now covers a subject containing a clause and a recipient before a long object.

**Decision:** no clause-closing word. Positional rules plus pauses (intonation in speech, commas in writing) carry the structure, as they do in natural languages. Add-back trigger: a blind test where attachment fails despite these rules.

**Caveat:** the reader had the rules. Real legal drafting would also need the habit of fronting main-clause adverbials, which is a matter of style.
