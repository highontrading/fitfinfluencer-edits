import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v12'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('aur') - 0.05, 'y': 150, 'lines': ['Aap ek', '*drug addict* ho'], 'sizes': [84, 112], 'hideCaps': True})
S.add({'type': 'title', 't0': T('aur'), 't1': T('sugar') - 0.08, 'y': 170, 'lines': ['Drug ka naam?'], 'sizes': [104]})
S.add({'type': 'slam', 't0': T('sugar'), 't1': T('cocaine') - 0.15, 'y': 200, 'text': '*SUGAR* 🍬', 'size': 160})
S.punch(T('sugar'), 0.14, 0.6)
S.add({'type': 'chips', 't0': T('cocaine') - 0.05, 't1': T('par', T('doge')) - 0.1, 'y': 140, 'items': [
    {'t': T('cocaine'), 'icon': '🚫', 'text': 'Cocaine ki aadat → *rehab*'},
    {'t': T('sweet'), 'icon': '🍬', 'text': 'Sweet tooth → 😂 *hans doge*'}]})
c0 = T('par', T('doge')) - 0.1; c1 = TE('se', T('addictive')) + 0.25
S.card(c0, c1)
fn = [{'t': T('sugar', c0), 'x': 260, 'y': 90, 'icon': '🍬', 'text': 'Sugar'},
      {'t': T('cocaine', c0), 'x': 740, 'y': 90, 'icon': '❄️', 'text': 'Cocaine'},
      {'t': T('center', c0) - 0.1, 'x': 500, 'y': 330, 'icon': '🧠', 'text': 'Same *brain center*', 'target': True}]
fw = [{'t': T('hit', c0) - 0.2, 'd': 'M 260 140 C 260 250, 400 300, 410 300'}, {'t': T('hit', c0, 2) - 0.2, 'd': 'M 740 140 C 740 250, 600 300, 590 300'}]
S.add({'type': 'flow', 't0': c0, 't1': T('aur', T('hit', c0, 2)) - 0.05, 'y': 170, 'w': 1000, 'h': 520, 'nodes': fn, 'wires': fw})
S.add({'type': 'stat', 't0': T('aur', T('hit', c0, 2)) - 0.05, 't1': c1, 'y': 230, 'kicker': 'Science kehti hai', 'from': 0, 'to': 8, 'unit': 'X', 'label': 'Zyada addictive', 'pill': '🍬 Sugar vs ❄️ Cocaine', 'dir': 'up', 'count': 1.0})
r0 = T('samjho') - 0.1; r1 = TE('nahi', T('problem')) + 0.25
S.card(r0, r1)
S.add({'type': 'title', 't0': r0, 't1': T('jab', r0) - 0.1, 'y': 270, 'kicker': 'Reward center', 'lines': ['*Nucleus*', '*accumbens*'], 'sizes': [104, 104]})
S.add({'type': 'chain', 't0': T('jab', r0) - 0.1, 't1': r1, 'y': 160, 'title': 'Brain mein kya hota hai', 'show': 4, 'items': [
    {'t': T('meetha', r0), 'icon': '🍬', 'text': 'Meetha khaya', 'st': ''},
    {'t': T('dopamine', r0), 'icon': '⚡', 'text': 'Dopamine', 'st': 'release'},
    {'t': T('pleasure'), 'icon': '😊', 'text': 'Pleasure', 'st': 'achha laga'},
    {'t': T('jab', T('pleasure')), 'icon': '🔁', 'text': 'Har baar', 'st': 'repeat'}]})
t0 = T('problem', r1 - 0.3) - 0.05
S.add({'type': 'title', 't0': t0, 't1': T('matlab') - 0.08, 'y': 160, 'kicker': 'Asli problem', 'lines': ['Brain *depend*', 'ho jaata hai'], 'sizes': [104, 76]})
l0 = T('matlab') - 0.1; l1 = TE('jaayega', T('paanch')) + 0.2
S.add({'type': 'chain', 't0': l0, 't1': l1, 'y': 130, 'title': 'Tolerance', 'show': 4, 'items': [
    {'t': T('ek', l0), 'icon': '🍩', 'text': '1 laddoo', 'st': 'khushi'},
    {'t': T('do', l0), 'icon': '🍩', 'text': '2 laddoo', 'st': 'khushi'},
    {'t': T('teen', l0), 'icon': '🍩', 'text': '3 laddoo', 'st': 'khushi'},
    {'t': T('chaar'), 'icon': '🍩', 'text': '4 · 5 · 6 ...', 'st': '↑↑'}]})
for it in S.events[-1]['items']: it['stc'] = 'red'
S.add({'type': 'slam', 't0': T('pattern') - 0.1, 't1': T('aur', T('addiction')) - 0.05, 'y': 200, 'text': 'Same *pattern*', 'size': 130, 'sub': 'Jo cocaine addiction mein'})
S.add({'type': 'title', 't0': T('aur', T('addiction')), 't1': T('ab', T('tolerance')) - 0.08, 'y': 170, 'lines': ['*Tolerance*', 'build hoti hai ↑'], 'sizes': [112, 72]})
p0 = T('ab', T('tolerance')) - 0.1; p1 = TE('india', T('capital')) + 0.25
S.card(p0, p1)
S.add({'type': 'stat', 't0': p0, 't1': T('protein', p0, 2) - 0.05, 'y': 230, 'kicker': 'Ab sochiye', 'from': 0, 'to': 73, 'unit': '%', 'label': 'Indians protein deficient', 'pill': '🥚 Protein ki kami', 'dir': 'up', 'count': 1.2})
pn = [{'t': T('protein', p0, 2), 'x': 260, 'y': 80, 'icon': '🥚', 'text': 'Protein ~kam~'},
      {'t': T('namak', p0), 'x': 740, 'y': 80, 'icon': '🧂', 'text': 'Namak ~kam~'},
      {'t': T('craving', p0) - 0.1, 'x': 500, 'y': 280, 'icon': '🍬', 'text': 'Sugar craving ↑↑'},
      {'t': T('diabetes'), 'x': 500, 'y': 480, 'icon': '🇮🇳', 'text': 'Diabetes capital', 'target': True}]
pw = [{'t': T('craving', p0) - 0.4, 'd': 'M 260 130 C 260 230, 380 270, 390 270'}, {'t': T('craving', T('namak', p0)) - 0.4, 'd': 'M 740 130 C 740 230, 620 270, 610 270'},
      {'t': T('diabetes') - 0.35, 'd': 'M 500 330 L 500 420'}]
S.add({'type': 'flow', 't0': T('protein', p0, 2) - 0.1, 't1': p1, 'y': 170, 'w': 1000, 'h': 600, 'nodes': pn, 'wires': pw})
S.add({'type': 'title', 't0': T('is', p1 - 0.3) - 0.05, 't1': T('aur', T('rehab', p1, 2)) - 0.05, 'y': 160, 'kicker': 'Cocaine ke liye rehab', 'lines': ['Meethe ke liye', 'bhi *system*'], 'sizes': [84, 112]})
S.add({'type': 'title', 't0': T('aur', T('rehab', p1, 2)), 't1': T('brain', T('hoga')) - 0.05, 'y': 170, 'lines': ['"Meetha mat khao"', '~kaam nahi karta~'], 'sizes': [84, 84]})
s0 = T('brain', T('hoga')) - 0.1; s1 = TE('jaayega', T('system', T('integrated'))) + 0.2
S.card(s0, s1)
S.add({'type': 'checklist', 't0': s0, 't1': s1, 'y': 170, 'title': 'Integrated system', 'items': [
    {'t': T('rewire'), 'text': 'Brain <span>rewire</span>', 'mark': 'check'},
    {'t': T('timing'), 'text': 'Protein <span>timing</span>', 'mark': 'check'},
    {'t': T('sodium'), 'text': 'Sodium <span>balance</span>', 'mark': 'check'}]})
S.add({'type': 'title', 't0': T('aur', s1 - 0.3) - 0.05, 't1': T('aur', T('jaanne')) - 0.1, 'y': 160, 'kicker': 'Maine ye system build kiya', 'lines': ['*Fastest* weight loss', 'jo maine dekha'], 'sizes': [92, 64]})
cta = T('agar', s1) - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'FitFinfluencer', 'title': 'Comment<br>*"SYSTEM"*', 'sub': 'Mera kaam tha science pahunchana · decision aapka hai', 'button': '💬 COMMENT "SYSTEM"', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'drug', r'addict', r'sugar', r'cocaine', r'rehab', r'science', r'brain', r'addictive', r'dopamine', r'pleasure', r'reward',
                           r'laddoo', r'tolerance', r'protein', r'namak', r'craving', r'diabetes', r'india', r'system', r'rewire', r'sodium', r'comment'])
B = S.broll
B(5078, T('sugar') - 0.05, T('cocaine') - 0.12, off=2.0)
B(41227, T('sweet') - 0.1, T('par', T('doge')) - 0.12, off=1.0)
B(4733, T('science'), T('cocaine', c0) - 0.1, off=1.0)
B(41117, T('meetha', r0) - 0.1, T('dopamine', r0) - 0.05, off=1.0)
B(40830, T('jab', T('pleasure')), r1 - 0.1, off=0.5)
B(100354, T('ek', l0) - 0.1, T('chaar') - 0.05, off=1.0)
B(100357, T('chaar'), l1 - 0.1, off=2.0)
B(42910, T('protein', p0, 2) - 0.1, T('aur', T('protein', p0, 2)) - 0.05, off=1.0)
B(44096, T('craving', T('namak', p0)) - 0.2, T('matlab', T('namak', p0)) - 0.05, off=1.0)
B(4779, T('rehab', p1) - 0.2, T('meethe', p1) - 0.05, off=0.5)
B(44432, T('jab', s1) - 0.1, T('agar', s1) - 0.12, off=1.0)
S.save(caps, cta_t=cta, hold=1.2, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
