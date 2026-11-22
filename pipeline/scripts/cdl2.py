# retry-download specific Commons files (rate-limit friendly): python3 -I scripts/cdl2.py "File:A.jpg" "File:B.jpg"
import json, subprocess, re, time, sys
P='stock/commons.json'; UA='FitFinfluencerEditPipeline/1.0 (video editing)'
todo=list(sys.argv[1:])
for rnd in range(20):
    d=json.load(open(P))
    for k in list(todo):
        v=d[k]; fn='stock/commons/'+re.sub(r'[^A-Za-z0-9]+','_',k[5:].rsplit('.',1)[0])[:60]+'.'+k.rsplit('.',1)[1].lower()
        r=subprocess.run(['curl','-s','-m','180','-A',UA,'-o',fn,'-w','%{http_code}',v['url']],capture_output=True,text=True)
        if r.stdout.strip()=='200':
            d=json.load(open(P)); d[k]['file']=fn; json.dump(d,open(P,'w'),indent=1,ensure_ascii=False); print('ok',k,fn,flush=True); todo.remove(k)
        time.sleep(5)
    if not todo: break
    time.sleep(60*(rnd+1))
print('left', todo)
