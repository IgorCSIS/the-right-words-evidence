import json,random,re,sys
sys.path.insert(0,'.'); from run import call
from concurrent.futures import ThreadPoolExecutor
rows=[json.loads(l) for l in open('calls_log.jsonl')]
key=json.load(open('<workspace>/blind_key.json'))
rub=open('RUBRIC.md').read()
sit={t:re.search(r'<situation>(.*?)</situation>',open(f'prompts/{t}_master.txt').read(),re.S).group(1).strip() for t in 'AB'}
def body_words(t):
    L=t.split('\n');s=e=None
    for i,l in enumerate(L):
        if s is None and re.match(r'\s*\**\s*(Hi|Hello|Dear|Dana)\b',l): s=i+1
        elif s is not None and re.match(r'\s*(Best|Thanks|Thank you|Cheers|Warmly|Regards|Sincerely|All the best|—|-- ?$|\[Your)',l): e=i;break
    if s is None: return None
    return len(re.findall(r"\S+"," ".join(L[s:e])))
def auto(t):
    w=body_words(t); a3=None if w is None else (2 if w<=120 else 1 if w<=180 else 0)
    v=(1 if '!' in t else 0)+(1 if re.search(r'hope this (email |note |message )?finds you',t,re.I) else 0)
    return w,a3,max(0,2-v)
def judge(bid):
    r=rows[key[bid]];t=r['task']
    p=f"""You are a blind judge. Score ONE output against this rubric (Task {t} only). Judge against the full scenario facts below.
RUBRIC:\n{rub}\nFULL SCENARIO FACTS (task {t}):\n{sit[t]}\nOUTPUT {bid}:\n<<<\n{r['text']}\n>>>
Return only JSON: {{"{t}1":n,"{t}2":n,"{t}3":n,"{t}4":n,"{t}5":n,"{t}6":n,"note":"<=20 words"}} with each n in 0,1,2."""
    for k in range(3):
        try:
            o=call('grok-4.7',p,4000);j=json.loads(re.search(r'\{.*\}',o['text'],re.S).group(0));return bid,j,o['cost_usd']
        except Exception as ex: err=ex
    return bid,{'error':str(err)},0
with ThreadPoolExecutor(6) as ex: res=list(ex.map(judge,sorted(key)))
jc=sum(c for _,_,c in res); out=[]
for bid,j,c in res:
    r=rows[key[bid]];t=r['task'];d=dict(blind_id=bid,task=t,condition=r['condition'],model=r['model'],rep=r['rep'])
    for n in range(1,7): d[f'c{n}']=j.get(f'{t}{n}')
    if t=='A':
        w,a3,a5=auto(r['text']);d['body_words']=w
        if a3 is not None: d['c3']=a3
        d['c5']=a5
    d['total']=sum(d[f'c{n}'] for n in range(1,7)); d['judge_note']=j.get('note','');d['judge_cost']=c;out.append(d)
json.dump(dict(rows=out,judge_cost=jc),open('<workspace>/judged.json','w'),indent=1);print('judge cost',jc)
