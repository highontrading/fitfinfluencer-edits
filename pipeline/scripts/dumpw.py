import json,sys
d=json.load(open(sys.argv[1])); k=0
for s in d['segments']:
    line=[]
    for w in s['words']:
        line.append(f"{k}:{w['w'].strip()}[{w['s']:.2f}-{w['e']:.2f}]"); k+=1
    print(' '.join(line))
