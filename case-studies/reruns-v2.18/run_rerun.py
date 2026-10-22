import os,json,time,sys,re,datetime,requests
CASE,MODEL=sys.argv[1],sys.argv[2]
BUDGET={"grok-4.7":1.9,"claude-fable-5-1":4.85}[MODEL]
spent_file="spent.json"; spent=json.load(open(spent_file)) if os.path.exists(spent_file) else {}
def cost_of(u,grok):
    if grok:
        inp=u["prompt_tokens"];c=u.get("prompt_tokens_details",{}).get("cached_tokens",0)
        out=u["completion_tokens"]+u.get("completion_tokens_details",{}).get("reasoning_tokens",0)
        return (inp-c)*2e-6+c*0.5e-6+out*6e-6
    w=u.get("cache_creation_input_tokens",0) or 0; r=u.get("cache_read_input_tokens",0) or 0
    return u["input_tokens"]*10e-6+w*12.5e-6+r*1e-6+u["output_tokens"]*50e-6
def sse(r):
    for line in r.iter_lines(decode_unicode=True):
        if line and line.startswith("data:"):
            d=line[5:].strip()
            if d=="[DONE]": break
            yield json.loads(d)
def call_once(msgs):
    grok=MODEL.startswith("grok")
    if grok:
        r=requests.post("https://api.x.ai/v1/chat/completions",headers={"Authorization":"Bearer "+os.environ["XAI_API_KEY"]},json={"model":MODEL,"messages":msgs,"max_tokens":20000,"stream":True,"stream_options":{"include_usage":True}},timeout=(30,300),stream=True)
        if r.status_code!=200: raise RuntimeError(f"HTTP {r.status_code} {r.text[:300]}")
        txt="";u=None;stop=None;mid=None;rid=None
        for ev in sse(r):
            rid=ev.get("id",rid); mid=ev.get("model",mid)
            for ch in ev.get("choices",[]):
                txt+=(ch.get("delta",{}) or {}).get("content") or ""
                stop=ch.get("finish_reason") or stop
            if ev.get("usage"): u=ev["usage"]
        return txt,u,stop,{"id":rid,"model":mid,"streamed":True},cost_of(u,True)
    m2=[dict(x) for x in msgs]; m2[-1]={"role":"user","content":[{"type":"text","text":msgs[-1]["content"],"cache_control":{"type":"ephemeral"}}]}
    body=dict({"model":MODEL,"messages":m2,"max_tokens":12000,"stream":True},**({"output_config":{"effort":os.environ["EFFORT"]}} if os.environ.get("EFFORT") else {}))
    r=requests.post("https://api.anthropic.com/v1/messages",headers={"x-api-key":os.environ["ANTHROPIC_API_KEY"],"anthropic-version":"2023-06-01"},json=body,timeout=(30,300),stream=True)
    if r.status_code!=200: raise RuntimeError(f"HTTP {r.status_code} {r.text[:300]}")
    txt="";u={};stop=None;mid=None;rid=None
    for ev in sse(r):
        t=ev.get("type")
        if t=="message_start": m=ev["message"]; rid=m["id"]; mid=m["model"]; u.update(m.get("usage",{}))
        elif t=="content_block_delta" and ev["delta"].get("type")=="text_delta": txt+=ev["delta"]["text"]
        elif t=="message_delta": stop=ev["delta"].get("stop_reason",stop); u.update({k:v for k,v in ev.get("usage",{}).items() if v is not None})
        elif t=="error": raise RuntimeError(str(ev))
    return txt,u,stop,{"id":rid,"model":mid,"streamed":True},cost_of(u,False)
def call(msgs):
    err=""
    for k in range(3):
        try: return call_once(msgs)
        except Exception as e:
            err=f"{type(e).__name__}: {str(e)[:400]}"; print("retry",k,err,flush=True); time.sleep(10)
    raise RuntimeError(err)
def reply(case,txt,hist,stop):
    T=txt.upper()
    if stop in ("max_tokens","length"): return "You hit the output limit. Continue exactly where you stopped. Do not repeat what you already sent."
    if case=="CS03":
        seen7=any("ARTIFACT 7" in h.upper() for h in hist+[txt])
        if seen7 and ("TREE" in T) and re.search(r"FR.?ID",txt) and "TEST" in T: return None
        if seen7: return "Accepted. Send the final message now: the doc tree and the FR ID, Diagram(s), Task(s), Test(s) table."
        if "TASKS.MD" in T and "ARTIFACT 5" in T and "ARTIFACT 6" not in T:
            return "approved. For this test, do not write code in this chat. Continue with Phase 6, then Phase 7, then the final message, one artifact per message."
        return "Accepted, continue to the next phase."
    else:
        if "ARTIFACT 7" in T or "DATE_PT" in T: return None
        return "No further answers needed; use the inputs as given and accept your assumptions. Continue with the remaining phases through Artifact 7."
def save():
    rec["total_cost_usd"]=round(sum(t.get("cost_usd",0) for t in rec["turns"]),4); rec["settings"]={"effort":os.environ.get("EFFORT","default")}
    base=f"{CASE}_{MODEL}"+os.environ.get("TAG","")
    json.dump(rec,open(base+".json","w"),indent=1)
    with open(base+".md","w") as f:
        f.write(f"# {CASE} rerun on {MODEL}\nPrompt: {rec['prompt_file']} (Set E text from manuscript v2.18 plus inputs). End: {rec.get('end')}. Cost: ${rec['total_cost_usd']}\n")
        for i,t in enumerate(rec["turns"]):
            f.write(f"\n---\n## Turn {i+1} ({t['timestamp']})\n### User\n```\n{t['user'][:200]+'... [full prompt in prompt file]' if i==0 else t['user']}\n```\n")
            f.write(f"### Error\n{t['error']}\n" if "error" in t else f"### Usage\n{json.dumps(t['usage'])}\nStop: {t['stop_reason']}. Cost: ${t['cost_usd']}\n### Assistant\n\n{t['assistant']}\n")
    
prompt=open(f"prompt_sent_{CASE}.txt").read()
msgs=[{"role":"user","content":prompt}]; rec={"case":CASE,"model":MODEL,"prompt_file":f"prompt_sent_{CASE}.txt","turns":[]}; total=0; hist=[]
for turn in range(16):
    ts=datetime.datetime.now().astimezone().isoformat(timespec="seconds"); t0=time.time()
    try: txt,u,stop,raw,c=call(msgs)
    except Exception as e: rec["turns"].append({"timestamp":ts,"user":msgs[-1]["content"],"error":str(e)}); break
    spent=json.load(open(spent_file)); spent[MODEL]=spent.get(MODEL,0)+c; json.dump(spent,open(spent_file,"w"))
    rec["turns"].append({"timestamp":ts,"seconds":round(time.time()-t0,1),"user":msgs[-1]["content"],"assistant":txt,"usage":u,"stop_reason":stop,"cost_usd":round(c,5),"model_returned":raw.get("model"),"response_id":raw.get("id")})
    print(CASE,MODEL,"turn",turn+1,round(c,4),stop,len(txt),flush=True)
    msgs.append({"role":"assistant","content":txt}); hist.append(txt)
    nxt=reply(CASE,txt,hist[:-1],stop); save()
    if nxt is None: rec["end"]="final artifact reached"; break
    if spent[MODEL]+1.3*c>BUDGET: rec["end"]=f"stopped: budget guard {BUDGET}"; break
    msgs.append({"role":"user","content":nxt})
else: rec["end"]="max turns"
save()
print("DONE",CASE,MODEL,rec.get("end"),rec["total_cost_usd"])
