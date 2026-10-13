Task: give English sense labels for frequent {LANGUAGE} words, for a word-frequency study.

Input: /home/agent/work/repos/universal-language/tests/coverage-01/data/unmatched-{code}.txt (one word per line, most frequent first, 1500 words, from {LANGUAGE} web text 2017). {NOTES}
Output: /home/agent/work/repos/universal-language/tests/coverage-01/data/aigloss-{code}.tsv, one line per input word, in input order: `word<TAB>labels`.

Labels: the word's everyday senses in modern use, most common first, at most 4, separated by " | ". Each label is a short plain English word or phrase naming the concept, lowercase, no "to" before verbs, no articles: e.g. `year`, `go`, `government`, `police`, `say`. For an inflected form give the lemma's concept. Use `#fn` for a purely grammatical word, and `#fn | concept` if it also has a content sense. Use `#name` for a proper name, `#foreign` for a foreign word quoted as-is, and `?` if you don't know. Don't guess: `?` is better than a wrong sense.

Work in chunks of 100 words: read the next 100 input words, append their lines to the output file, repeat. Before starting, if the output file exists, count its lines and continue after them. Don't read any other files in the repository. When done, reply with the number of lines written and how many are `?`.

(Used 2026-10-13 for ha, qu, th with sonnet; NOTES per language: Hausa tone/length marks absent, hooked letters plain; Quechua agglutinative, gloss the root; Thai tokens may be several words run together, give each content word's concept in order.)
