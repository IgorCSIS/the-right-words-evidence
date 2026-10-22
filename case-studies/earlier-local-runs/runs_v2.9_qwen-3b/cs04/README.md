# CS04 evidence: LinkedIn post pipeline (real public input run, Oct 21, 2026)
Input: REAL public-domain voice samples, two consecutive passages of Henry David Thoreau, Walden (1854), Project Gutenberg eBook #205, https://www.gutenberg.org/cache/epub/205/pg205.txt (lines 2649 to 2685). PROOF numbers measured on the box from the Project Gutenberg catalog CSV (79,634 items; 78,383 Type "Text"; 63,050 Language "en"). The author profile is a stand-in. There is no LinkedIn account, post or analytics behind this run. Nothing was posted.
Runner: Qwen2.5-3B-Instruct Q4_K_M (Ollama tag qwen3b:latest, 3.4B, family qwen2), local on the box, single turn, no tools, temperature 0.3, seed 42, num_ctx 16384, num_predict 3500. No cloud model API key was found in the environment, so this was the best model available. Prompt: the paste-ready prompt from case-studies/<file>.md, verbatim, followed by the inputs in input.md (full text sent: prompt_sent.txt). Output: output_qwen2.5-3b.md, unedited. Token counts: run_meta.json. Prompt tokens 2368, output tokens 3500, stopped at the token cap.
Observed:
- Produced Artifacts 1 to 7 in order. The proof number was rounded to "over 79,000 items", which is accurate to the input.
- Voice Card is weak: fields hold quotes instead of measurements (Average Sentence Length is a quoted sentence; "Words Avoided: hype, detail, superfluous, superfluous").
- Draft v1 is about 96 words by whitespace count, under the 120-word minimum, ends with two emoji, and does not sound like the Thoreau samples. The Review Table still marked Copy PASS.
- The Brief correctly left URL, date and metrics "[To be filled]".
- The Tracker Line broke down: after the real fields it filled the metric columns with "0" and then repeated "| 0" until the cap. Those zeros are invented metrics, against the tracker's no-invented-metrics rule.
What this shows: the draft-only flow and placeholders worked; the length gate, voice match and tracker rule did not hold on this model.
