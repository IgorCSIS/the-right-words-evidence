# Case Study 01: Ridgeline Coffee vectorize, independent verification

Source: ridgeline_source.jpg (copy of the Grok-generated mark). Pipeline in run.py: palette quantize to prep.png, vtracer 0.6 with the reported settings, cleanup (strip comment, snap fills, drop translate(0,0)), then `npx svgo --multipass --precision 2` (svgo 4.1.0). Path commands counted as SVG command letters in all `d` attributes. Diff: clean SVG rendered with cairosvg at 512 px wide (512x344), flattened on white, compared with prep.png resized to 512x344 (Lanczos), mean absolute difference over RGB, 0-255 scale.

| Item | Grok reported | Measured | Result |
|---|---|---|---|
| Source size | 1168x784 | 1168x784 | MATCH |
| Raw path commands | 212 | 180 (4 paths) | DIFFERS |
| Raw size | 15.3 KB | 12.6 KB | DIFFERS |
| Clean paths | 4 | 4 | MATCH |
| Clean path commands | 166 | 152 | DIFFERS |
| Clean size | 4.0 KB | 3.5 KB | DIFFERS |
| Clean unique fills | 3 (palette) | 3: #1F2A44, #E07A2E, #FFF | MATCH |
| Mean abs diff at 512 px | 1.94 | 0.91 | DIFFERS |

Notes: vtracer output a near-palette fill (#1F2A43) that the snap step corrected. Differences are plausibly due to vtracer/svgo versions and the counting method; the shape count and palette agree, and the measured fidelity is better than reported.

Outputs: ridgeline_trace_raw.svg, ridgeline_clean.svg, ridgeline_16.png, ridgeline_32.png, ridgeline_512.png, ridgeline_1024.png, ridgeline_figure.png (source left, traced right, white background), prep.png.
