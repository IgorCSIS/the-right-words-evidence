# Prompt test results, v2.14, grok-4.7 (api.x.ai), run 2026-10-21 PDT

| Test | Prompt | Result | Reason |
|---|---|---|---|
| PT-01 | Ch3 CRAFT Example 1 | PASS | Hook, 2 detail lines, time and price line, 3 hashtags, under 80 words, no exclamation marks. |
| PT-02 | Ch4 The full prompt | PASS | Angle, 3 numbered subjects under 50 chars, email under 120 words, follow-up, NEED line; no invented facts. |
| PT-03 | Ch6 meta prompt | PASS | Turn 1 asks exactly one question as step 1 requires (later steps need a live interview). |
| PT-04 | Ch7 Block 1 bio interview | PASS | Turn 1 asks one interview question and nothing else. |
| PT-05 | Ch9 three-email sequence | PASS | 3 emails, each under 250 words with subject and preview; email 1 no pitch; real testimonial; deadline used; [NEED] where proof missing. |
| PT-06 | Ch10 Diverge, converge, dig | PASS | Returned exactly 10, then 50 (5 x 10), then 25 ideas on the chosen subtopic. |
| PT-07 | Card 00 Copywriter | FAIL | Returned only a plan line and stopped; no artifacts, and it did not say it could not search or ask for pasted VOC as the card requires. |
| PT-08 | Card 06 Chef | PASS | Artifacts 1 to 4 with gate results, final deliverable, balance notes, 165F/74C safety flag, mild plate for the kid. |
| PT-09 | E1 Vectorize | FAIL | One line saying it would inspect tools, then stopped; no Prep Note, logs or Acceptance Report; no tool access over the API. |
| PT-10 | E2 Sketch to 3D | FAIL | One line saying it would measure the figure, then stopped; no artifacts or mesh report. |
| PT-11 | E3 Docs-first | PASS | Artifact 1 with mission, facts, [VARIABLE] unknowns, 3 questions, "Gate: FAIL, because..."; no code; unread sources marked UNVERIFIED. |
| PT-12 | E4 LinkedIn pipeline | PASS | 7 artifacts; final body 154 words (120 to 200), line 1 is 10 words, no link, no hashtags, no em dashes, tracker metrics [to fill]. |
| PT-13 | E5 Contractor outreach | PASS (partial test) | Could not verify the (fictional) sites, so 0 drafts and no invented observation; all 7 artifacts; drafting itself not exercised. |

Totals: 10 PASS, 3 FAIL. Pattern: the 3 failures are the tool-heavy prompts (web research, image tracing, 3D modeling); over a plain API the model announces it will use tools and stops instead of saying it cannot.
Tokens: 36,315 input, 9,436 output plus 58,044 reasoning (billed as output) = 103,795 total. Cost at $2/M in and $6/M out: $0.48.
Note: PT-06 and PT-08 outputs contain em dashes; neither prompt bans them.

## Revised drafts (FIX_DRAFTS.md), run 2026-10-21 15:54 PDT, grok-4.7

| Test | Prompt | Result | Reason |
|---|---|---|---|
| PT-07r | Card 00 Copywriter, revised draft | FAIL | Same failure as PT-07: announced it was "searching now" and stopped. Breaks the new "Never announce a tool call and stop" rule; no one-line no-tool note, no request for pasted material, no artifacts. |
| PT-09r | E1 Vectorize, revised draft | Not run | Not needed (tool-based, works with tools), per Igor. |
| PT-10r | E2 Sketch to 3D, revised draft | Not run | Not needed (tool-based, works with tools), per Igor. |

PT-07r tokens: 3,433 input, 528 output (39 text + 489 reasoning). Cost: $0.0100.
