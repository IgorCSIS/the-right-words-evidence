import json,re,sys
r=json.load(open(sys.argv[1]))
allt="\n".join(t.get('assistant','') for t in r['turns'])
print("turns",len(r['turns']),"cost",r['total_cost_usd'],"end",r.get('end'))
for i,t in enumerate(r['turns']):
    a=t.get('assistant','')
    g=[l.strip() for l in a.split('\n') if re.search(r'Gate:',l)]
    print(f"T{i+1} chars {len(a)} stop {t.get('stop_reason')} gates {[x[:150] for x in g]}")
print("FR ids",sorted(set(re.findall(r'FR-\d\d',allt))))
print("mermaid blocks",allt.count('```mermaid'))
print("python code blocks",len(re.findall(r'```python',allt)),"em",allt.count('\u2014'),"en",allt.count('\u2013'))
# file sections and line counts
secs=re.split(r'\n#{2,3} (?=[`\w./-]*\.(?:md|mdc|example|gitignore)\b|\.)',allt)
for s in secs[1:]:
    name=s.split('\n',1)[0].strip('` ')
    if any(k in name for k in ['AGENTS.md','CLAUDE.md','.mdc','copilot','.gitignore','.env.example']):
        m=re.search(r'```[a-z]*\n(.*?)\n```',s,re.S)
        print("FILE",name,"lines",len(m.group(1).split('\n')) if m else None)
for k in ['Report counts','objection','Counts','gaps']:
    for l in allt.split('\n'):
        if re.search(r'(\d+ (gaps|objections)|fixed|closed).*\d',l,re.I) and len(l)<300 and ('fix' in l.lower() or 'open' in l.lower()):
            pass
print([l for l in allt.split('\n') if re.search(r'\b\d+\b.*\b(fixed|open|not apply|closed)\b',l,re.I)][:12])
