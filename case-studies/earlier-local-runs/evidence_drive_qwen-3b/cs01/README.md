# CS01 evidence: vectorize a raster mark (real run, Oct 21, 2026)
Tool: vtracer 0.6.15 (Python package), render check with CairoSVG at 512 px wide, mean absolute grayscale difference (0 to 255).
Caps from the prompt's variables example: colors <= 3, nodes <= 400, size <= 15 KB, diff <= 6.
Source A: brand/marks/src/monogram_source_crop.png (crop of the book's cover art; origin per brand/marks/TRACE_LOG.md). Source B: stacked_source_crop.png (the THE RIGHT WORDS wordmark).
Whether the cover art itself is AI-generated is not recorded in the trace log: UNVERIFIED.

| Source | Run | Settings | Colors | Nodes | KB | Diff | All caps pass |
|---|---|---|---|---|---|---|---|
| Monogram | 1 | spline, color_precision 6, filter_speckle 4 | 3 | 60 | 2.3 | 0.86 | Yes |
| Monogram | 2 | spline, filter_speckle 8, fills snapped to palette | 3 | 60 | 2.3 | 0.86 | Yes |
| Monogram | 3 | polygon, filter_speckle 8, snapped | 3 | 50 | 0.9 | 0.81 | Yes |
| Wordmark | 1 | spline, filter_speckle 4 | 7 | 1395 | 142.7 | 2.39 | No (colors, nodes, KB) |
| Wordmark | 2 | spline, filter_speckle 8, snapped | 3 | 1395 | 142.7 | 1.51 | No (nodes, KB) |
| Wordmark | 3 | polygon, filter_speckle 8, snapped | 3 | 924 | 8.2 | 1.63 | No (nodes) |

Node count = path commands (M, L, C, Q, Z) in d attributes. Files: run1-3.svg, stacked/run1-3.svg, settings_log.json, run_cs01.py.
What worked: a simple mark passes every gate on the first run. What did not: a multi-letter wordmark cannot meet a 400-node cap with vtracer alone; the cap in the example needs to scale with letter count, or text should be set in a font and outlined instead of traced. filter_speckle 4 vs 8 changed nothing on these clean crops.
