# Prompt tests on a second model, v2.15 text, 2026-10-21 PDT

Model 2 (primary): claude-fable-5-1 (Anthropic API, /v1/models list read 2026-10-21; Fable 5.1 is listed as the top tier for demanding reasoning). Different vendor from grok-4.7.
Extra comparison: grok-4.6 (xAI, same vendor as grok-4.7). Started before the Anthropic key arrived; kept as a separate comparison.
Aborted: claude-opus-5-5 run stopped after PT-01 to PT-05 when I switched to Fable 5.1; partial logs kept in claude-opus-5-5_ABORTED_partial/, not scored.
Prompts: same fills as the grok-4.7 run, text taken from the v2.15 manuscript. Only difference from the grok-4.7 prompts: PT-09 includes the new E1 line "Attach the logo or art image itself...". Same image attachments for PT-09 and PT-10. First turn judged for interview-style prompts.
Scores: pass/fail against what the prompt promises, plus the fresh editor's 0 to 2 scale (2 full deliverable meeting the prompt, 1 correct but partial, 0 failed). grok-4.7 scores are the fresh editor's v2.15 re-scores.

| Test | Prompt | grok-4.7 | grok-4.6 | claude-fable-5-1 | Fable reason |
|---|---|---|---|---|---|
| PT-01 | Ch3 CRAFT Ex.1 | PASS 2 | PASS 2 | PASS 2 | Hook, 2 detail lines, time and price line, 3 hashtags, no exclamation marks |
| PT-02 | Ch4 full prompt | PASS 2 | PASS 2 | PASS 1 | Full format and NEED line, but adds an invented detail ("most useful two minutes") |
| PT-03 | Ch6 meta prompt | PASS 1 | PASS 1 | PASS 1 | Turn 1 asks one question (with examples) |
| PT-04 | Ch7 interview | PASS 1 | PASS 1 | PASS 1 | Turn 1 asks one question |
| PT-05 | Ch9 3 emails | PASS 2 | PASS 2 | PASS 2 | Bodies 212, 248, 235 words (under 250), subject and preview each, [NEED] used |
| PT-06 | Ch10 chain | PASS 2 | PASS 2 | PASS 2 | Exactly 10, 50, 25 |
| PT-07 | Card 00 | FAIL 0 | FAIL 0 | PASS 1 | Said it has no search, asked for pasted VOC with a list, offered "proceed assumed", asked 1 question; no artifacts yet |
| PT-08 | Card 06 | PASS 2 | PASS 2 | PASS 2 | Artifacts 1 to 4 with gates, 165F flag, balance notes, Eval line |
| PT-09 | E1 | FAIL 0 | FAIL 0 | PASS 1 | Prep Note from the image, exact commands, logs marked pending; no faked counts |
| PT-10 | E2 | FAIL 0 | PASS 1 | PASS 1 | Reference Sheet, assumptions, full Blender script, cells PENDING; no faked mesh numbers |
| PT-11 | E3 | PASS 2 | FAIL 0 | PASS 2 | Full Artifact 1, [VARIABLES], 3 questions, "Gate: FAIL, because..."; no code |
| PT-12 | E4 | PASS 2 | PASS 2 | FAIL 1 | 7 artifacts, 142-word body, 11-word line 1; but invents "Three runs did it" (not in PROOF), breaking "never invent outcomes" |
| PT-13 | E5 | PASS 1 | PASS 1 | PASS 1 | No invented observation; asks for page text; scaffold only, marked NOT READY |
| Total | | 10 pass, 3 fail; 18 of 26 | 10 pass, 3 fail; 16 of 26 | 12 pass, 1 fail; 17 of 26 | |

grok-4.6 notes: PT-07 and PT-09 announced tool use and stopped (same as 4.7); PT-10 stopped honestly per the E2 "if a tool is missing, stop and say so" rule (score 1); PT-11 announced it would fetch the linking policy and stopped (27 words).
Dashes: Fable used em dashes in PT-07 (6) and PT-08 (13); neither Card 00 nor Card 06 bans them. None in E1 to E5 outputs.

Tokens and cost
- claude-fable-5-1: 27,274 input, 46,929 output (thinking included). At list price $10/M in, $50/M out: $2.62.
- grok-4.6: 26,577 input, 44,323 output (7,660 text + 36,663 reasoning). At $2/M in, $6/M out: $0.32 (xAI billed $0.31 per cost_in_usd_ticks).
- claude-opus-5-5 aborted partial: 2,403 input, 6,606 output, $0.14 at $4/$20.
