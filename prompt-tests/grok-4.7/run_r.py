import os,json,time,base64,datetime,urllib.request,sys
import fills_r as fills
KEY=os.environ["XAI_API_KEY"]; URL="https://api.x.ai/v1/chat/completions"; MODEL="grok-4.7"
def call(msgs):
    body=json.dumps({"model":MODEL,"messages":msgs}).encode()
    req=urllib.request.Request(URL,body,{"Authorization":"Bearer "+KEY,"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=900) as r: return json.load(r)
def once(msgs):
    try: return call(msgs),None
    except Exception as e:
        err=str(e)
        if hasattr(e,"read"):
            try: err+=" "+e.read().decode()[:500]
            except: pass
        return None,err
ids=sys.argv[1:] or list(fills.T)
for tid in ids:
    name,prompt,extra=fills.T[tid]
    turns=extra if isinstance(extra,list) else [prompt]
    msgs=[];rec={"test":tid,"prompt_source":name,"model":MODEL,"endpoint":URL,"turns":[]}
    for i,p in enumerate(turns):
        content=p
        if i==0 and isinstance(extra,str):
            b=base64.b64encode(open(extra,"rb").read()).decode()
            content=[{"type":"image_url","image_url":{"url":"data:image/jpeg;base64,"+b}},{"type":"text","text":p}]
            rec["attachment"]=extra
        msgs.append({"role":"user","content":content})
        ts=datetime.datetime.now().astimezone().isoformat()
        r,err=once(msgs)
        if r is None:
            r,err2=once(msgs); err=None if r else f"attempt1: {err} | attempt2: {err2}"
        t={"timestamp":ts,"prompt":p}
        if r is None:
            t["error"]=err; rec["turns"].append(t); break
        out=r["choices"][0]["message"].get("content","")
        t.update(output=out,usage=r.get("usage"),model_returned=r.get("model"),raw_response=r)
        rec["turns"].append(t); msgs.append({"role":"assistant","content":out})
    json.dump(rec,open(f"{tid}.json","w"),indent=1)
    with open(f"{tid}.md","w") as f:
        f.write(f"# {tid}: {name}\nModel: {MODEL}\n")
        for i,t in enumerate(rec["turns"]):
            f.write(f"\n## Turn {i+1} ({t['timestamp']})\n### Prompt sent\n```\n{t['prompt']}\n```\n")
            if "error" in t: f.write(f"### ERROR\n{t['error']}\n")
            else: f.write(f"### Usage\n{json.dumps(t['usage'])}\n### Raw output\n\n{t['output']}\n")
    print(tid,"done",[("ERR" if "error" in t else t["usage"].get("total_tokens")) for t in rec["turns"]],flush=True)
