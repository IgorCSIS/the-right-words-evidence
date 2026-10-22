import json,re,sys,time,urllib.request,pathlib
MAP={'cs02':'cs02_sketch_to_3d.md','cs03':'cs03_docs_first_vibecoding.md','cs04':'cs04_linkedin_post_pipeline.md','cs05':'cs05_contractor_outreach_emails.md'}
OPTS={"temperature":0.3,"seed":42,"num_ctx":16384,"num_predict":3500}
for cs in sys.argv[1:]:
    src=pathlib.Path('..')/MAP[cs]; t=src.read_text()
    prompt=re.search(r'## Paste-ready prompt\n```text\n(.*?)\n```',t,re.S).group(1)
    inp=pathlib.Path(cs,'input.md').read_text()
    full=prompt+"\n\nMy inputs for the bracketed variables:\n"+inp
    pathlib.Path(cs,'prompt_sent.txt').write_text(full)
    t0=time.time()
    r=json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:11434/api/chat',json.dumps({"model":"qwen3b:latest","stream":False,"options":OPTS,"messages":[{"role":"user","content":full}]}).encode(),{'Content-Type':'application/json'}),timeout=1800))
    out=r['message']['content']; pathlib.Path(cs,'output_qwen2.5-3b.md').write_text(out)
    meta={k:r.get(k) for k in('model','created_at','prompt_eval_count','eval_count','done_reason')}; meta['options']=OPTS; meta['wall_secs']=round(time.time()-t0,1)
    pathlib.Path(cs,'run_meta.json').write_text(json.dumps(meta,indent=1)); print(cs,meta,flush=True)
