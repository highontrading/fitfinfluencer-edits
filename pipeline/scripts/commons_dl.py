# slow retrying downloader for Commons files marked file=None (rate-limit friendly)
import json, subprocess, re, time
P='stock/commons.json'; UA='FitFinfluencerEditPipeline/1.0 (video editing)'
for rnd in range(30):
    d=json.load(open(P)); todo=[(k,v) for k,v in d.items() if 'file' in v and v['file'] is None]
    if not todo: break
    for k,v in todo:
        t=k[5:]; ext='.png' if v['kind']=='image' else ('.'+t.rsplit('.',1)[1])
        fn='stock/commons/'+re.sub(r'[^A-Za-z0-9]+','_',t.rsplit('.',1)[0])[:60]+ext
        r=subprocess.run(['curl','-s','-m','180','-A',UA,'-o',fn,'-w','%{http_code}',v['url']],capture_output=True,text=True)
        if r.stdout.strip()=='200':
            d=json.load(open(P)); d[k]['file']=fn; json.dump(d,open(P,'w'),indent=1,ensure_ascii=False); print('ok',fn,flush=True)
        else: subprocess.run(['rm','-f',fn]); print(r.stdout,fn,flush=True); time.sleep(60)
    time.sleep(180)
print('DLDONE')
