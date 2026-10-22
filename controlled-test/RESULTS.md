# Controlled prompt test v2.17: bare vs CRAFT vs MASTER

Date: 2026-10-21. 2 tasks x 3 conditions x 2 models x 3 reps = 36 generations (already logged in calls_log.jsonl; no new generations made).

## Method
- Rubric fixed before any run (RUBRIC.md): 6 criteria per task, 0 to 2 each, max 12. All outputs judged against the full scenario facts, so the bare prompt is handicapped by design (that handicap is what is measured).
- Blind scoring: outputs shuffled (seed 217) and given random IDs X00 to X35; the judge saw only the task rubric, scenario facts and the output text, never condition, model or prompt.
- Judge: one pass by grok-4.7. Deviation from RUBRIC.md: the rubric specifies two judges (grok-4.7 and claude-fable-5-1, averaged); only the grok-4.7 judge was run to stay inside the budget. A single judge that is also one of the models under test is a known bias risk.
- AUTO criteria scored by script and overriding the judge: A3 (email body word count, greeting to sign-off) and A5 (exclamation marks, "hope this finds you well").
- Per-output scores in scores.csv.

## Results (total score out of 12; mean and range over 3 reps)

| Task | Model | Bare | CRAFT | MASTER |
|---|---|---|---|---|
| A cold email | grok-4.7 | 8.33 (8 to 9) | 12.00 (12 to 12) | 11.00 (11 to 11) |
| A cold email | claude-fable-5-1 | 3.33 (3 to 4) | 12.00 (12 to 12) | 11.00 (11 to 11) |
| B study plan | grok-4.7 | 6.00 (6 to 6) | 11.00 (11 to 11) | 11.00 (11 to 11) |
| B study plan | claude-fable-5-1 | 5.33 (5 to 6) | 10.67 (10 to 11) | 11.33 (11 to 12) |
| All | both | 5.75 | 11.42 | 11.08 |

## Finding
- The big effect is giving the model the situation. Structured prompts (CRAFT or MASTER) roughly doubled scores versus bare (5.75 to about 11.2 of 12), on both models and both tasks.
- MASTER did not beat CRAFT overall (11.08 vs 11.42). On the cold email CRAFT won on both models (12 vs 11): MASTER outputs lost a point on "ready to paste" because the required angle line, subject list and NEED line wrap the email in extra material. On the study plan MASTER tied on grok-4.7 and was slightly ahead on claude-fable-5-1 (11.33 vs 10.67), mainly from weekly practice tests with target scores (B3), which only MASTER asked for explicitly.
- Bare claude-fable-5-1 emails were long (175 to 213 word bodies) and generic; bare outputs never referenced Dana's post or the user's time budget, since they did not have those facts.
- Caveats: n=3 per cell, one judge, ceiling effects (several cells at 11 to 12), differences between CRAFT and MASTER are within one point and should not be overstated.

## Cost
- Generation (36 calls): $2.37
- Judge pass (36 grok-4.7 calls): $1.02 (slightly over the $1 target)
- Total: $3.39
