# CS02 evidence: sketch to 3D (partial run, Oct 21, 2026)
Input: NO real sketch exists. sketch_synthetic.png is a SCRIPT-DRAWN stand-in (front view of a headphone wall hook, blurred and noised, with a 10 px/mm ruler). It is not a phone photo and must not be printed as a worked result.
Pipeline that ran: ruler measured from tick spacing (10.0 px/mm), outline found with OpenCV, scaled so overall height = 80 mm (KEY_DIMENSION), extruded 15 mm with trimesh, exported STL and GLB.
Mesh check: height 80.0 mm, extents 44.5 x 80.0 x 15.0 mm, watertight yes, 28 triangles, volume 17.87 cm3. Depth 15 mm is an ASSUMPTION (single view, no side view). Minimum wall was not measured on the mesh; drawn arm widths are 7 to 8 mm before the 1.194 scale: UNVERIFIED as a mesh measurement.
Not done: no free image-to-3D generator was run (no GPU on the box, and none is installed); no slicer check (PrusaSlicer not installed); no real photo checks (flat light, perpendicular).
What this shows: the prompt's measured path (scale reference, single key dimension, extrude, watertight check) works with free Python tools for a flat, prismatic part. It does not test the prompt's generator branch or curved objects.
Files: sketch_synthetic.png, headphone_hook.stl, headphone_hook.glb, mesh_check.json, run_cs02.py.
