import os,json,time,requests,sys
P={"grok-4.7":(2/1e6,6/1e6),"claude-fable-5-1":(10/1e6,50/1e6)}
def call(model,prompt,max_tokens=6000):
    t=time.time()
    if model.startswith("grok"):
        r=requests.post("https://api.x.ai/v1/chat/completions",headers={"Authorization":"Bearer "+os.environ["XAI_API_KEY"]},json={"model":model,"messages":[{"role":"user","content":prompt}],"max_tokens":max_tokens},timeout=600).json()
        u=r["usage"];txt=r["choices"][0]["message"]["content"]
        inp=u["prompt_tokens"];cached=u.get("prompt_tokens_details",{}).get("cached_tokens",0)
        out=u["completion_tokens"]+u.get("completion_tokens_details",{}).get("reasoning_tokens",0)
        cost=(inp-cached)*2/1e6+cached*0.5/1e6+out*6/1e6
    else:
        r=requests.post("https://api.anthropic.com/v1/messages",headers={"x-api-key":os.environ["ANTHROPIC_API_KEY"],"anthropic-version":"2023-06-01"},json={"model":model,"messages":[{"role":"user","content":prompt}],"max_tokens":max_tokens},timeout=600).json()
        u=r["usage"];txt="".join(c.get("text","") for c in r["content"] if c["type"]=="text")
        inp=u["input_tokens"];out=u["output_tokens"];cost=inp*10/1e6+out*50/1e6
    return dict(text=txt,input_tokens=inp,output_tokens=out,cost_usd=round(cost,6),seconds=round(time.time()-t,1),usage=u)
if __name__=="__main__":
    from concurrent.futures import ThreadPoolExecutor
    jobs=[(t,c,m,i) for t in "AB" for c in ["bare","craft","master"] for m in P for i in (1,2,3)]
    def go(j):
        t,c,m,i=j;p=open(f"prompts/{t}_{c}.txt").read()
        for k in range(3):
            try: return dict(task=t,condition=c,model=m,rep=i,prompt_file=f"prompts/{t}_{c}.txt",**call(m,p))
            except Exception as e: err=str(e);time.sleep(5)
        return dict(task=t,condition=c,model=m,rep=i,error=err)
    with ThreadPoolExecutor(8) as ex: res=list(ex.map(go,jobs))
    json.dump(res,open("raw_outputs.json","w"),indent=1)
    print(sum(r.get("cost_usd",0) for r in res),[r for r in res if "error" in r])
