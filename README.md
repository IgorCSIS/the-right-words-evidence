# The Right Words: evidence

This repo holds the test logs behind the book "The Right Words" by Igor Lima. Every model output here is unedited, apart from the scrubbing listed in SCRUB_REPORT.md. Model names and dates are given as tested on October 21, 2026.

## Contents

- `prompt-tests/`: 13 prompt tests (PT-01 to PT-13) of the book's prompts.
  - `grok-4.7/`: the first run (v2.14 prompt text, rescored for v2.15), with runner and fill values.
  - `grok-4.6/` and `claude-fable-5-1/`: the same 13 tests on v2.15 text. `RESULTS_model2.md` has the scores for all three models.
  - The aborted claude-opus-5-5 partial run is not included.
- `controlled-test/`: the bare vs CRAFT vs MASTER controlled test (v2.17): RUBRIC.md, prompts/, calls_log.jsonl (every call), scores.csv, RESULTS.md, judge.py, run.py, run2.py.
- `case-studies/`:
  - `book-runs-grok-4.7/`: my notes from the five Case Study runs printed in the book (CS01 to CS05), the CS01 trace files and my check script, and the CS02 STL, GLB and screenshots. CS03 to CS05 notes are summaries, not transcripts.
  - `reruns-v2.18/`: full raw transcripts (JSON and Markdown) of the CS03 and CS05 reruns on grok-4.7 and claude-fable-5-1, the exact prompts, the runner, costs (spent.json) and logs. `aborted/` holds an errored grok-4.7 attempt and the log of a stopped claude-fable-5-1 attempt.
  - `earlier-local-runs/`: earlier text runs of CS01 to CS05 on a small local model (Qwen2.5 3B), kept for comparison.

## Notes

- API keys were read from environment variables and never written to files. See SCRUB_REPORT.md for the scan.
- CS05 uses fictional example businesses on reserved `.example` domains. No real person or business was contacted, and nothing was sent.
- Large public source files (the Gutenberg catalog CSV and Walden text) are not included; links are in `case-studies/earlier-local-runs/runs_v2.9_qwen-3b/REMOVED_LARGE_FILES.md`.
