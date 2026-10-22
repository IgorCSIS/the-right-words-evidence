# Rubric (fixed before any run, 2026-10-21)

Each criterion scored 0, 1 or 2. Max 12 per output. Every output is judged
against the FULL scenario (the facts in the CRAFT/MASTER Situation), because
that is the real need of the reader. The bare prompt therefore starts without
those facts; that handicap is the thing being measured.

Scoring is blind: outputs are shuffled and given random IDs; the judge sees no
condition (bare/CRAFT/MASTER), no model name, no prompt. Two judges score every
output (grok-4.7 and claude-fable-5-1, the same two models under test), and the
score is the mean of both. Criteria marked AUTO are scored by script and
override the judges.

## Task A: cold email to a cafe owner (Dana Ruiz, Ember Coffee)
A1 Specific to recipient: 2 = names Dana/Ember and refers to her tax-season/shoebox post; 1 = some specific detail; 0 = could go to any owner.
A2 One small ask: 2 = single clear ask for a short call (about 15 minutes); 1 = ask present but vague, big, or multiple; 0 = no ask.
A3 (AUTO) Body length: 2 = email body (excluding subject, sign-off, follow-up) at most 120 words; 1 = 121-180; 0 = over 180.
A4 No invented facts: 2 = no fabricated clients, results, prices, credentials (placeholders fine); 1 = one minor invention; 0 = invented claims a sender could not stand behind.
A5 (AUTO) No cliches: 2 = no exclamation marks and no "hope this (email) finds you well"; 1 = one violation; 0 = two or more.
A6 Ready to paste: 2 = subject line plus body, usable as is, minimal chatter; 1 = usable after light cleanup; 0 = needs real rework.

## Task B: 4-week Security+ study plan (working adult)
B1 Fits time: 2 = every day respects weekday 60 min / Saturday 180 min / Sunday off; 1 = mostly fits; 0 = ignores or exceeds the budget.
B2 Weak areas first: 2 = cryptography and network attacks clearly get the largest share; 1 = mentioned but not prioritized; 0 = absent.
B3 Progress checks: 2 = timed practice test every week with a target score; 1 = some practice tests, no targets; 0 = none.
B4 Covers the whole exam in 4 weeks: 2 = 4 weeks, all major exam areas appear; 1 = gaps or wrong duration; 0 = badly off.
B5 Usable format: 2 = clear day-by-day schedule a person can follow tonight; 1 = followable with effort; 0 = vague.
B6 No invented or wrong facts/resources: 2 = no false exam facts, no resources presented as required that the user did not list (optional is fine); 1 = minor; 0 = clear errors or invented requirements.
