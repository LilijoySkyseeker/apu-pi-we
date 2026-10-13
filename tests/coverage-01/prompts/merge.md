Task: clean a ranked list of concept labels for a vocabulary study, chunk by chunk.

Folder: /home/agent/work/repos/universal-language/tests/coverage-01/

Input: `concepts.tsv` (columns rank, concept, languages, score). Each concept is an English label for a word sense, gathered from word-frequency lists of 20 languages via dictionary glosses; rank 1 is the most common across languages. Work on ranks 1–{TOP}. Also read `existing.tsv` (form, gloss, kind) once: the words the constructed language already has (kind root, loan, phrase, grammar, number).

Output: `merged.tsv`, one line per input label in rank order, with tab-separated columns:
`rank  label  canonical  type  covered  note`
- **canonical**: the plain, most common English word or short phrase for the concept, so synonyms and variants share one name: "large" → `big`, "automobile" → `car`, "mom" → `mother`, "speak" and "talk" → `speak` only if they're the same concept in everyday use (they mostly are), "say" stays `say`. Keep distinct concepts distinct: `hand` ≠ `arm`, `buy` ≠ `sell`, `moon` ≠ `month`, `word` ≠ `language`. Keep a running list in `canon.txt` (one canonical name per line, add new ones as you go) and reuse names from it so the same concept always gets the same name across chunks.
- **type**: `content` (a thing, action, quality, place, time, person…), `grammar` (what a grammar word or particle does: pronouns, "here", "why", "very", "and", "not", "this", "all", aspect, question; numbers too), `name` (a proper name or nationality-as-name, e.g. "Hausa language" is content but "Kano" is a name), or `bad` (not a real concept: a dictionary artifact such as "dummy verb that takes tense marking", a gloss fragment, a sense that is clearly wrong for a frequent word).
- **covered**: the existing form(s) from `existing.tsv` that already say this concept, comma-separated (e.g. `guyi`, or `pu yema simi` for a phrase); `none` if nothing does. Match by meaning, not spelling; an existing word whose gloss covers the concept as one of its senses counts.
- **note**: optional, a few words (e.g. "merged with big", "sense error from sw la").

Work in chunks of 200 ranks. Before starting, if `merged.tsv` exists, continue after its last rank (the job may be resumed after an interruption). Append each chunk's lines when the chunk is done. Don't read other files in the repository. When finished, reply with counts per type, the number of distinct canonical content concepts, and how many of those are covered.
