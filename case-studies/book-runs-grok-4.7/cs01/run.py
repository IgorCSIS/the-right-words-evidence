import re,os,io,subprocess,numpy as np,vtracer,cairosvg
from PIL import Image
P=np.array([[255,255,255],[0x1F,0x2A,0x44],[0xE0,0x7A,0x2E]])
a=np.array(Image.open('ridgeline_source.jpg').convert('RGB')).astype(int)
idx=((a[:,:,None,:]-P[None,None])**2).sum(-1).argmin(-1)
Image.fromarray(P[idx].astype(np.uint8)).save('prep.png')
vtracer.convert_image_to_svg_py('prep.png','ridgeline_trace_raw.svg',colormode='color',hierarchical='stacked',mode='spline',filter_speckle=4,color_precision=6,layer_difference=16,corner_threshold=60,length_threshold=4.0,max_iterations=10,splice_threshold=45,path_precision=8)
s=open('ridgeline_trace_raw.svg').read()
s=re.sub(r'<!--.*?-->','',s,flags=re.S)
def snap(m):
    h=m.group(1);c=np.array([int(h[i:i+2],16) for i in (0,2,4)])
    return 'fill="#%02X%02X%02X"'%tuple(P[((P-c)**2).sum(1).argmin()])
s=re.sub(r'fill="#([0-9A-Fa-f]{6})"',snap,s)
s=re.sub(r'\s*transform="translate\(0,0\)"','',s)
open('snapped.svg','w').write(s)
subprocess.run('npx -y svgo --multipass --precision 2 -i snapped.svg -o ridgeline_clean.svg',shell=True,check=True)
def st(f):
    t=open(f).read();ds=re.findall(r' d="([^"]*)"',t)
    return dict(paths=len(ds),cmds=sum(len(re.findall(r'[MmLlHhVvCcSsQqTtAaZz]',d)) for d in ds),fills=sorted(set(x.upper() for x in re.findall(r'fill="?(#[0-9A-Fa-f]{3,6})',t))),kb=round(os.path.getsize(f)/1024,1))
def rend(f,w):
    im=Image.open(io.BytesIO(cairosvg.svg2png(url=f,output_width=w))).convert('RGBA')
    bg=Image.new('RGBA',im.size,'white');return Image.alpha_composite(bg,im).convert('RGB')
for w in (16,32,512,1024): rend('ridgeline_clean.svg',w).save(f'ridgeline_{w}.png')
r=np.array(rend('ridgeline_clean.svg',512)).astype(int)
p=np.array(Image.open('prep.png').resize((r.shape[1],r.shape[0]),Image.LANCZOS)).astype(int)
print('raw',st('ridgeline_trace_raw.svg'));print('clean',st('ridgeline_clean.svg'));print('diff',round(np.abs(r-p).mean(),2),r.shape)
src=Image.open('ridgeline_source.jpg').convert('RGB');tr=rend('ridgeline_clean.svg',1168)
W,H=src.size;g=48;fig=Image.new('RGB',(2*W+3*g,H+2*g),'white');fig.paste(src,(g,g));fig.paste(tr,(2*g+W,g));fig.save('ridgeline_figure.png')
