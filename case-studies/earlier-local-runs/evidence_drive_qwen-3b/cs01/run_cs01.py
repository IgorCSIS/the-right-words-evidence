import vtracer,re,io,json,cairosvg,numpy as np
from PIL import Image
src=Image.open('source.png').convert('RGB'); W,H=src.size
PAL=[(0xF4,0xF1,0xEA),(0x14,0x14,0x14),(0xC2,0x41,0x2D)]
def snap(svg):
    def f(m):
        h=m.group(1); c=tuple(int(h[i:i+2],16) for i in (0,2,4))
        p=min(PAL,key=lambda q:sum((a-b)**2 for a,b in zip(c,q))); return 'fill="#%02X%02X%02X"'%p
    return re.sub(r'fill="#([0-9A-Fa-f]{6})"',f,svg)
def metrics(svg):
    fills=set(re.findall(r'fill="(#[0-9A-Fa-f]{6})"',svg))
    nodes=sum(len(re.findall(r'[MLCQZmlcqz]',d)) for d in re.findall(r' d="([^"]+)"',svg))
    kb=len(svg.encode())/1024
    png=cairosvg.svg2png(bytestring=svg.encode(),output_width=512,output_height=round(512*H/W),background_color='#F4F1EA')
    a=np.asarray(Image.open(io.BytesIO(png)).convert('L'),float); b=np.asarray(src.resize((a.shape[1],a.shape[0])).convert('L'),float)
    return len(fills),nodes,round(kb,1),round(float(np.abs(a-b).mean()),2)
runs=[('spline, color_precision 6, filter_speckle 4',dict(colormode='color',mode='spline',filter_speckle=4,color_precision=6,layer_difference=16),False),
      ('spline, color_precision 6, filter_speckle 8, fills snapped to palette',dict(colormode='color',mode='spline',filter_speckle=8,color_precision=6,layer_difference=16),True),
      ('polygon, filter_speckle 8, fills snapped to palette',dict(colormode='color',mode='polygon',filter_speckle=8,color_precision=6,layer_difference=16),True)]
log=[]
for i,(desc,kw,s) in enumerate(runs,1):
    svg=vtracer.convert_raw_image_to_svg(open('source.png','rb').read(),img_format='png',**kw)
    svg=re.sub(r'<\?xml[^>]*>|<!--.*?-->','',svg,flags=re.S)
    if s: svg=snap(svg)
    open(f'run{i}.svg','w').write(svg); c,n,k,d=metrics(svg)
    log.append(dict(run=i,tool='vtracer 0.6.x (Python)',settings=desc,colors=c,nodes=n,kb=k,diff=d))
caps=dict(colors=3,nodes=400,kb=15,diff=6)
for r in log: r['pass']={k:r[k]<=v for k,v in caps.items()}
json.dump(dict(source='brand/marks/src/monogram_source_crop.png',size=[W,H],caps=caps,runs=log),open('settings_log.json','w'),indent=1)
for r in log: print(r)
