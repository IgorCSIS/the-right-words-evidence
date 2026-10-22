import re
M="<book-workspace>/out-v2.14/The_Right_Words_manuscript_v2.14.md"
L=open(M).read().split("\n")
def blk(a,b): return "\n".join(L[a:b-1])  # lines a+1..b-1 (inside fences at a,b)
def fill(t,d):
    for k,v in d.items():
        if k not in t: raise SystemExit("missing "+k)
        t=t.replace(k,v)
    return t
MAYA_KIT=blk(1305,1338)
T={}
T["PT-01"]=("Ch3 CRAFT in practice, Example 1 (lines 327-341)",blk(326,342),None)
T["PT-02"]=("Ch4 The full prompt (lines 590-648)",blk(589,649),None)
T["PT-03"]=("Ch6 A meta prompt you can use today (lines 1081-1103)",fill(blk(1080,1104),{
 "[task]":"turning my rough meeting notes into a client follow-up email","[audience]":"freelance bookkeepers who work with small restaurants"}),None)
T["PT-04"]=("Ch7 one-question interview, Block 1 bio (lines 1164-1169)",blk(1163,1170),None)
T["PT-05"]=("Ch9 three-email sequence brief (lines 1644-1652), with Ch7 sample kit plus <offer>/<proof>",
 MAYA_KIT+"\n\n<offer>\nCharge to Chair: a six-week online leadership program for RNs with 8+ years of experience. Six live Tuesday-evening Zoom sessions (7 to 8:30 p.m. Pacific), weekly worksheets, and one 30-minute 1:1 call with Maya. Price $690, or 3 payments of $240. Cohort limited to 20 seats so every 1:1 call fits in Maya's calendar. Starts November 17, 2026.\n</offer>\n\n<proof>\n\"I went from informal charge nurse to unit educator in four months, and I still work two bedside shifts a month.\" Dana R., RN, ICU, pilot cohort 2025 (shared with permission).\n</proof>\n\n"+fill(blk(1643,1653),{"[date]":"November 10, 2026"}),None)
T["PT-06"]=("Ch10 Diverge, converge, dig (3-step chain, lines 1688-1702)",None,[
 "Give me 10 topic ideas for a blog about organizing retreats.",
 "Give me 5 specific blog post ideas for each of the 10 topics above.",
 "Give me 25 ideas for posts, exercises, or handouts about running a silent morning on a corporate retreat."])
T["PT-07"]=("Card 00 World's Best Copywriter (lines 1940-2066)",fill(blk(1939,2067),{
 "[asset: sales page / VSL script / email sequence / ad set]":"an email sequence",
 "[product]":"Crumb Club, a monthly sourdough starter-and-flour subscription",
 "[market]":"home bakers in the US who have tried sourdough once or twice and given up",
 "[one action]":"start a $24 first-month trial",
 "[what it is, how it works, price, bonuses, guarantee]":"a box each month with a dried heirloom starter, 2 kg of stone-milled flour, and a printed one-page bake plan; you rehydrate the starter in 3 days and follow the plan; $24 first month, then $32/month, cancel anytime; bonus: a live monthly Q&A on Zoom; guarantee: if your first loaf fails we send a free replacement starter",
 "[segment]":"home bakers with a regular kitchen oven and 30 minutes on weekends",
 "[testimonials with permission, numbers, case studies, credentials, demos]":"412 active subscribers as of October 2026; testimonial with permission: \"My first loaf that actually rose. I cried a little.\" Priya S., Austin; founder baked professionally for 9 years",
 "[actual limit and why it exists, or \"none\"]":"none",
 "[list or \"find them\"]":"King Arthur Baking (flour and recipes), Breadtopia (starter kits)",
 "[style sample or \"bold, plain, warm\"]":"bold, plain, warm"},),None)
T["PT-07"]=(T["PT-07"][0],T["PT-07"][1].replace("Who it is for: home bakers with a regular kitchen oven and 30 minutes on weekends. Who it is not for: home bakers with a regular kitchen oven and 30 minutes on weekends","Who it is for: home bakers with a regular kitchen oven and 30 minutes on weekends. Who it is not for: professional bakers and anyone gluten free"),None)
T["PT-08"]=("Card 06 World's Best Chef (lines 2413-2457)",fill(blk(2412,2458),{
 "[meal]":"a weeknight dinner","[number]":"4","[time]":"45 minutes",
 "Pantry and fridge: [list]":"Pantry and fridge: 1 lb boneless chicken thighs, 2 cups jasmine rice, 1 head broccoli, 1 onion, 4 garlic cloves, 1 can coconut milk, soy sauce, eggs, half a bag of frozen peas, limes, chili flakes",
 "[allergies, diets, kids]":"two adults, two kids aged 6 and 9; one kid will not eat anything spicy; no allergies",
 "Equipment: [list]":"Equipment: one large skillet, one saucepan, a sheet pan, oven","[level]":"comfortable home cook","[amount]":"$10"}),None)
E1={"[SOURCE_IMAGE]":"ridgeline_source.jpg (attached)","[WIDTH x HEIGHT]":"1168 x 784","[ORIGIN, e.g. \"image model\"]":"an image model",
 "[USES, e.g. favicon, site header, print at 2 in]":"favicon, site header, print at 2 in on a coffee bag label",
 "[PALETTE_HEX or \"derive from source, max N colors\"]":"#1F2A44, #E07A2E, #FFFFFF","[TOOLS, e.g. Photopea in a browser, vtracer CLI, Inkscape 1.x, svgo]":"vtracer CLI 0.6, Inkscape 1.3, svgo 4",
 "[MAX_COLORS, default 4]":"3","[MAX_COLORS]":"3","[MAX_KB, default 15]":"15","[MAX_KB]":"15","[MAX_DIFF, default 6]":"6","[MAX_DIFF]":"6",
 "[MIN_AREA, default 0.05 percent]":"0.05 percent","[PALETTE_HEX]":"#1F2A44,#E07A2E,#FFFFFF","[NAME]":"ridgeline","[MAX_NODES]":"400"}
t=blk(4745,4874); t=re.sub(r"\[MAX_NODES, default 400[^\]]*\]","400",t,flags=re.S)
T["PT-09"]=("Set E1 Vectorize (lines 4746-4873), image attached",fill(t,E1),"<book-workspace>/grok_runs/cs01/ridgeline_source.jpg")
E2={"[SKETCH_PHOTO]":"huck_lockbolt_fig3.jpg (attached)","[TARGET_FORMATS]":"STL and GLB","[OBJECT_DESCRIPTION]":"a Huck-style lockbolt (pin with domed head, grooved shank, and swaged collar) from a patent drawing",
 "[KEY_DIMENSION, e.g. \"overall height 80 mm\"]":"shank diameter 6.4 mm","[KEY_DIMENSION]":"shank diameter 6.4 mm","[USE: 3D print on [PRINTER_AND_NOZZLE] / web viewer / both]":"both: 3D print on a Prusa MK4 with a 0.4 mm nozzle, and a web viewer",
 "[VIEWS, e.g. front only / front + side / front + side + top]":"front only","[TOOLS, e.g. Blender 4.x, a hosted image-to-3D tool, a slicer]":"Blender 4.2, PrusaSlicer 2.8",
 "[GENERATOR or \"none\"]":"none","[GENERATOR]":"none","[SCALE_TOL, default 2]":"2","[SCALE_TOL]":"2","[MIN_WALL, default 1.2]":"1.2","[MIN_WALL]":"1.2","[MAX_MB, default 10]":"10","[MAX_MB]":"10","[MAX_TRIS, default 100000]":"100000","[MAX_TRIS]":"100000","[NAME]":"huck_lockbolt"}
T["PT-10"]=("Set E2 Sketch to 3D (lines 4883-5011), drawing attached",fill(blk(4882,5012),E2),"<book-workspace>/case-studies/runs_v2.9/cs02/huck_lockbolt_fig3.jpg")
E3={"[PROJECT_BRIEF: 5 to 15 lines in plain words: who it is for, the problem, the core flow]":"A small local tool for readers who want free classic books.\nProblem: the Project Gutenberg catalog CSV (pg_catalog.csv, about 80,000 rows, 9 columns) is hard to browse.\nCore flow: load the CSV, search by title or author, filter by language and subject, open the book's Gutenberg page,\nsave books to a reading list, and export the list as Markdown.\nOne user, on their own laptop. No accounts.",
 "[STACK or \"propose one, then wait for approval\"]":"Python 3.12, FastAPI, SQLite","[AGENTS, e.g. Claude Code, Cursor, GitHub Copilot, Codex]":"Cursor, Claude Code","[AGENTS]":"Cursor, Claude Code",
 "[STORAGE or \"none\"]":"SQLite","[UI_TYPE, e.g. web, CLI, desktop]":"web (localhost)","[SOURCES or \"none\"]":"docs/brief.md, https://www.gutenberg.org/policy/linking.html",
 "[RULES_MAX_LINES, default 150]":"150","[RULES_MAX_LINES]":"150","[COVERAGE, default 80]":"80"}
T["PT-11"]=("Set E3 Docs-First Vibecoding (lines 5021-5152)",fill(blk(5020,5153),E3),None)
E4={"[AUTHOR_PROFILE: who you are, what you build, who you want to reach]":"Igor Lima, student; I write prompts and just finished a book on prompt engineering for non-programmers; I want to reach small business owners and students who use chat assistants daily.",
 "[VOICE_SAMPLES: 2 or 3 of your past posts, pasted verbatim]":"Post 1: \"I ran my own book through an audit today. 36 flagged phrases. I fixed every one by hand. Down to 0. The fix was not a better tool. It was reading slower.\"\nPost 2: \"Most bad prompts are missing one thing: what done looks like. Tell the model when to stop and what to hand you. That one line changes more than any clever wording.\"",
 "[TRACKER: the current tracker file, or \"empty\"]":"empty","[IDEA, one or two rough lines]":"Case studies in my book print what broke, not just what worked. Failure is the useful part.",
 "[PROOF, e.g. a demo link or a real number from your own log, or \"none\"]":"5 real runs; in 2 of them the skeptic pass found 5 objections and fixed 0","[PROOF]":"5 real runs; in 2 of them the skeptic pass found 5 objections and fixed 0",
 "[EXPERIMENT or \"none\"]":"none","[MIN_WORDS]":"120","[MAX_WORDS]":"200","[LINK_POLICY]":"no link policy (links never allowed)","[HASHTAG_POLICY, default none]":"none","[VOICE_OR_RULE, default: the tone rule]":"the tone rule"}
T["PT-12"]=("Set E4 LinkedIn Pipeline (lines 5162-5272)",fill(blk(5161,5273),E4),None)
t=blk(5281,5390)
t=re.sub(r"\[LEADS: rows of business[^\]]*\]","business,contact,trade,town,website,email\nHillcrest Roofing,Dave,roofing,[TOWN REMOVED],hillcrestroofing.example,info@hillcrestroofing.example\nCanyon View Plumbing,,plumbing,Santee CA,canyonviewplumbing-example.com,(no public email)",t,flags=re.S)
E5={"[SENDER: your name, business name, town, a valid physical postal address, phone]":"Igor Lima, Lima Content Co., [TOWN REMOVED], [POSTAL ADDRESS REMOVED], [PHONE REMOVED]",
 "[OFFER: one sentence on what you help with]":"I write and schedule a month of before-and-after social posts for local trades businesses.",
 "[TOUCH_LOG: the CSV of every past touch, or \"empty\"]":"empty","[MAX_WORDS, default 90]":"90","[MAX_WORDS]":"90","[LINK_RULE, default no links]":"no links","[DAILY_CAP, default 10]":"10","[FU1_DAYS, default 3]":"3","[FU2_DAYS, default 7]":"7"}
T["PT-13"]=("Set E5 Contractor Outreach (lines 5282-5389)",fill(t,E5),None)
T["PT-02"]=(T["PT-02"][0],fill(T["PT-02"][1],{"[podcast]":"Lead Track","[name]":"Sarah Chen","[episode]":"her conversation with Marcus Webb on skip-level meetings","[reason]":"he admitted his first skip-levels made his managers feel spied on","[guest]":"Marcus Webb"}),None)
