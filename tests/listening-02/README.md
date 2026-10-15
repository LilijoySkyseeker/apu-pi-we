# Listening 02: a voice that can say Apupiwe (2026-10-15)

**Question:** can free text-to-speech produce the reference pronunciation well enough for the author to listen, where listening-01's voices (Piper, Kokoro, MBROLA) failed? Decided by the author 2026-10-15 (design log: the free voice step; the author is the listener; the paid crowd study stays deferred).

**Voice:** VOICEVOX 0.25.2 (Japanese neural TTS; `nixpkgs#voicevox-engine`, unfree, runs without root on 127.0.0.1:50021). Its input can be given mora by mora (consonant, vowel, pitch), so `speak.py` passes each Apupiwe syllable as one mora, final n as the moraic n, and sets pitch by our rules (2.4, 2.6, 2.7): stressed first syllable high (+0.40 log-F0), a small step down per stressed syllable, grammar words low, reset at pauses. Durations are VOICEVOX's own (Japanese timing). Nearest sounds: l → Japanese r [ɾ], f → [ɸ]~[f]; yi and wu are requested even though Japanese lacks them (the engine accepts them and gives them normal durations).

**Run:** start the engine (`voicevox-engine --host 127.0.0.1 --port 50021`), then `direnv exec . python3 tests/listening-02/speak.py OUTDIR [SPEAKER]` (30 = No.7 announcer, 13 = a male voice). The clips went to the author's vault (`Language/apupiwe-voice/voice-check.md`), not the repo.

**Results:** waiting for the author's listening notes (what to listen for is in the vault note: g/d/b before u, yi and wu, stress, l and f, final n, the voicing pairs). If the voice holds up, next is listening-01's 32 pairs with this voice, the author as listener.

## Round 2: Piper with IPA input (2026-10-15)

The author on round 1: guyi sounded like "guh yee" (female voice, step down) and "buh yee" (male voice, step up). The male voice was a bug here (absolute pitches far above its range; fixed in `speak.py`), but "guh" is Japanese itself: its u is short and unrounded. The author: "can we move to something that can do true ipa?" Options were Piper with IPA input (local, free), a cloud voice with SSML IPA (needs the author's account), or eSpeak NG (exact but robotic); the author chose Piper for now.

`speak_piper.py` turns each word into broad IPA (stress mark ˈ before stressed first syllables; p t k unaspirated, a harmless variant, since these voices never learned aspiration) and passes it inside `[[ ]]`, which Piper 1.8 (`nixpkgs#piper-tts`) says as given (its debug log shows the phonemes unchanged: `ˈ ɡ u j i`). Voices from `rhasspy/piper-voices` (kept in `~/work/tools/piper-voices`, outside the repo): es_ES davefx, es_MX claude, it_IT paola, id_ID news_tts. The clips are in the author's vault (`Language/apupiwe-voice/`); step 1 there is picking a voice.

Run: `direnv exec . python3 tests/listening-02/speak_piper.py OUTDIR PIPER VOICEDIR`.

**Result (author, 2026-10-15):** all four Piper voices "sneak extra syllables and wrong sounds into them, and are not even close". Voice work parked (design log); lesson 1 points to real words instead. Next try, when the author sets up an account: a cloud voice with SSML `<phoneme alphabet="ipa">`.
