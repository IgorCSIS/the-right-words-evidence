# CS03 evidence (run Oct 21, 2026)
Input: the "Filled example" input from case-studies/cs03_*.md (input.md). For CS04 those numbers are the author's measured audit as stated in that file; for CS03 and CS05 the file labels the input illustrative or anonymized.
Runner: Qwen2.5-3B-Instruct Q4_K_M, local, single turn, no tools. Output: output_qwen2.5-3b.md. This is text-only; no code was built (CS03), nothing was posted (CS04), nothing was sent (CS05).
The scored test run with a generated scenario is in ../CS03.json.
Observed: produced Discovery and PRD artifacts in order with Given/When/Then requirements; did not reach the rules files (AGENTS.md etc.) inside the token cap. No token-saving claim can be made from this run.
