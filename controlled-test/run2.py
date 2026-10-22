import json,os,threading
from run import call
from concurrent.futures import ThreadPoolExecutor
CAP={"grok-4.7":2.0,"claude-fable-5-1":8.0}
LOG="calls_log.jsonl";lock=threading.Lock()
def spent():
    s={m:0 for m in CAP}
    if os.path.exists(LOG):
        for l in open(LOG): r=json.loads(l); s[r["model"]]+=r.get("cost_usd",0)
    return s
def run_call(model,prompt,meta,max_tokens=6000):
    with lock:
        if spent()[model]>CAP[model]-0.35: return None
    r=call(model,prompt,max_tokens); r.update(meta,model=model)
    with lock: open(LOG,"a").write(json.dumps(r)+"\n")
    return r
if __name__=="__main__":
    done=set()
    if os.path.exists(LOG):
        for l in open(LOG):
            r=json.loads(l)
            if r.get("phase")=="gen": done.add((r["task"],r["condition"],r["model"],r["rep"]))
    jobs=[(t,c,m,i) for t in "AB" for c in ["bare","craft","master"] for m in CAP for i in (1,2,3) if (t,c,m,i) not in done]
    def go(j):
        t,c,m,i=j
        try: return run_call(m,open(f"prompts/{t}_{c}.txt").read(),dict(phase="gen",task=t,condition=c,rep=i,prompt_file=f"prompts/{t}_{c}.txt"))
        except Exception as e: print("ERR",j,e)
    with ThreadPoolExecutor(8) as ex: list(ex.map(go,jobs))
    print(spent())
