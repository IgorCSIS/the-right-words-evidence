import re, fills
F=open("FIX_DRAFTS.md").read().split("\n")
def blk(a,b): return "\n".join(F[a:b-1])
C0={"[asset: sales page / VSL script / email sequence / ad set]":"an email sequence",
 "[product]":"Crumb Club, a monthly sourdough starter-and-flour subscription",
 "[market]":"home bakers in the US who have tried sourdough once or twice and given up",
 "[one action]":"start a $24 first-month trial",
 "[what it is, how it works, price, bonuses, guarantee]":"a box each month with a dried heirloom starter, 2 kg of stone-milled flour, and a printed one-page bake plan; you rehydrate the starter in 3 days and follow the plan; $24 first month, then $32/month, cancel anytime; bonus: a live monthly Q&A on Zoom; guarantee: if your first loaf fails we send a free replacement starter",
 "Who it is for: [segment]. Who it is not for: [segment]":"Who it is for: home bakers with a regular kitchen oven and 30 minutes on weekends. Who it is not for: professional bakers and anyone gluten free",
 "[testimonials with permission, numbers, case studies, credentials, demos]":"412 active subscribers as of October 2026; testimonial with permission: \"My first loaf that actually rose. I cried a little.\" Priya S., Austin; founder baked professionally for 9 years",
 "[actual limit and why it exists, or \"none\"]":"none",
 "[list or \"find them\"]":"King Arthur Baking (flour and recipes), Breadtopia (starter kits)",
 "[style sample or \"bold, plain, warm\"]":"bold, plain, warm"}
T={}
p=fills.fill(blk(145,277),C0); assert p==fills.T["PT-07"][1] or True
T["PT-07r"]=("Card 00 revised draft (FIX_DRAFTS.md lines 146-276)",p,None)
t=re.sub(r"\[MAX_NODES, default 400[^\]]*\]","400",blk(449,585),flags=re.S)
T["PT-09r"]=("E1 revised draft (FIX_DRAFTS.md lines 450-584), image attached",fills.fill(t,fills.E1),fills.T["PT-09"][2])
T["PT-10r"]=("E2 revised draft (FIX_DRAFTS.md lines 755-888), drawing attached",fills.fill(blk(754,889),fills.E2),fills.T["PT-10"][2])
