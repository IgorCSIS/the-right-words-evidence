import json,re,sys,subprocess,os,tempfile
r=json.load(open(sys.argv[1])); allt="\n".join(t.get('assistant','') for t in r['turns'])
blocks=re.findall(r'```mermaid\n(.*?)```',allt,re.S); ok=0; bad=[]
d=tempfile.mkdtemp()
cfg=os.path.join(d,"p.json"); json.dump({"executablePath":"/usr/bin/google-chrome","args":["--no-sandbox"]},open(cfg,"w"))
for i,b in enumerate(blocks):
    f=os.path.join(d,f"{i}.mmd"); open(f,"w").write(b)
    p=subprocess.run(["mmdc","-p",cfg,"-i",f,"-o",f+".svg"],capture_output=True,text=True,timeout=120)
    if p.returncode==0: ok+=1
    else: bad.append((i,b.split('\n')[0],(p.stderr or p.stdout).strip().split('\n')[0][:160]))
print(sys.argv[1],"mermaid blocks",len(blocks),"render ok",ok,"failed",len(bad))
for x in bad: print(" ",x)
