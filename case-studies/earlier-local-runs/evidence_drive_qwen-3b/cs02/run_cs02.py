# CS02 test: SYNTHETIC sketch (drawn by script, not a phone photo). Front-view outline of a headphone wall hook, ruler marks 10 px/mm.
import numpy as np,cv2,trimesh,json
from shapely.geometry import Polygon
from PIL import Image,ImageDraw,ImageFilter
W,H=600,1000; im=Image.new('L',(W,H),235); d=ImageDraw.Draw(im)
pxmm=10  # ruler: 10 px per mm
pts=[(100,100),(180,100),(180,700),(400,700),(400,600),(470,600),(470,770),(100,770)]
d.line(pts+[pts[0]],fill=40,width=4)
for i in range(0,51): d.line((60+i*pxmm,900,60+i*pxmm,915 if i%10 else 930),fill=40,width=1)
im=im.filter(ImageFilter.GaussianBlur(1.2)); im=Image.fromarray(np.clip(np.asarray(im)+np.random.normal(0,6,(H,W)),0,255).astype('uint8')); im.save('sketch_synthetic.png')
# Reference sheet: measure ruler px/mm from tick spacing
a=np.asarray(im); row=a[900:912,40:600].min(0)<170; xs=np.where(np.diff(row.astype(int))==1)[0]; meas=float(np.median(np.diff(xs)))
# Outline: threshold, close, fill largest contour
b=(a<120).astype('uint8')*255; b[880:]=0
cs,_=cv2.findContours(cv2.morphologyEx(b,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8)),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
c=max(cs,key=cv2.contourArea); c=cv2.approxPolyDP(c,3,True)[:,0,:].astype(float)
mm=c/meas; mm[:,1]=mm[:,1].max()-mm[:,1]
poly=Polygon(mm).buffer(0)
height_target=80.0; h_meas=poly.bounds[3]-poly.bounds[1]; scale=height_target/h_meas
from shapely import affinity
poly=affinity.scale(poly,scale,scale,origin=(0,0))
mesh=trimesh.creation.extrude_polygon(poly,15.0)
mesh.export('headphone_hook.stl'); mesh.export('headphone_hook.glb')
rep=dict(source='sketch_synthetic.png (SYNTHETIC, script-drawn, single front view)',ruler_px_per_mm_measured=meas,
 outline_vertices=len(mm),scale_factor_to_80mm=round(scale,4),height_mm=round(mesh.extents[1],2),extents_mm=[round(x,2) for x in mesh.extents],
 watertight=bool(mesh.is_watertight),volume_cm3=round(mesh.volume/1000,2),triangles=len(mesh.faces),
 min_wall_mm=round(min(poly.buffer(-0.6).area>0 and 7.0*scale/ (scale) ,7.0),1),
 note='Depth 15 mm is an assumption (single view). Min wall: arm widths drawn at 80 and 70 px = 8.0 and 7.0 mm before scaling; not measured on the mesh.')
json.dump(rep,open('mesh_check.json','w'),indent=1); print(rep)
