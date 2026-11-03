import json, subprocess, os
P='stock/meta.json'; m=json.load(open(P)); saved=0
for k,v in m.items():
    f=v.get('file')
    if not f or not os.path.exists(f) or max(v.get('w',0),v.get('h',0))<=1920: continue
    tmp=f+'.tmp.mp4'
    vf="scale='if(gt(iw,ih),1920,-2)':'if(gt(iw,ih),-2,1920)':flags=lanczos"
    r=subprocess.run(['ffmpeg','-v','error','-y','-i',f,'-vf',vf,'-an','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p',tmp])
    if r.returncode==0:
        a=os.path.getsize(f); os.replace(tmp,f); saved+=a-os.path.getsize(f)
        j=json.loads(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','json',f],capture_output=True,text=True).stdout)
        v['w'],v['h']=j['streams'][0]['width'],j['streams'][0]['height']
        json.dump(m,open(P,'w'),indent=1)
print('saved MB', saved//2**20)
