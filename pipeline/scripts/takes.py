# Retake detector (EDITING_RULES: always keep the LAST take). Prints the chunk list with earlier takes marked.
# python3 -I scripts/takes.py work/chN.json
import json, sys, re, difflib
ch = json.load(open(sys.argv[1]))
def toks(c): return [re.sub(r'[^\w%]', '', w['w'].lower()) for w in c['words'] if re.sub(r'[^\w%]', '', w['w'])]
T = {c['id']: toks(c) for c in ch}
def sim(a, b):
    if not a or not b: return 0
    m = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return sum(bl.size for bl in m.get_matching_blocks() if bl.size >= 2) / len(a)   # runs of 2+ words, relative to the earlier chunk
sup = {}
for i, c in enumerate(ch):
    a = T[c['id']]
    if len(a) < 2: continue
    for d in ch[i + 1:]:
        if d['s'] - c['e'] > 45: break
        # c is superseded if a later chunk repeats most of it (the speaker restarted the line)
        if sim(a, T[d['id']]) >= 0.65:
            sup[c['id']] = d['id']; break
        # or a later chunk *starts* the same way (a restart that runs longer)
        if len(a) >= 3 and T[d['id']][:3] == a[:3]:
            sup[c['id']] = d['id']; break
for c in ch:
    tag = f"  <- EARLIER TAKE, use c{sup[c['id']]}" if c['id'] in sup else ''
    print(f"{c['id']:3d} {c['s']:7.2f}-{c['e']:7.2f} {c['text'][:90]}{tag}")
