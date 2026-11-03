import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v14'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('pata') - 0.05, 'y': 150, 'kicker': 'Roz 3–4 litre paani', 'lines': ['Phir bhi', '*pyaas*?'], 'sizes': [84, 120], 'hideCaps': True})
S.add({'type': 'title', 't0': T('pata') - 0.05, 't1': T('chemical') - 0.08, 'y': 170, 'lines': ['Sahi tareeke se', '~nahi~ pee raha tha'], 'sizes': [84, 92]})
S.add({'type': 'slam', 't0': T('chemical') - 0.05, 't1': T('har') - 0.05, 'y': 200, 'text': 'H₂O = *CHEMICAL*', 'size': 110, 'sub': '2 Hydrogen + 1 Oxygen · bas'})
S.punch(T('chemical'), 0.14, 0.8)
S.add({'type': 'title', 't0': T('par', T('har')) - 0.05, 't1': T('tabhi') - 0.1, 'y': 170, 'lines': ['Kaun sa *paani*', 'peena hai?'], 'sizes': [104, 84]})
m0 = T('tabhi') - 0.1; m1 = TE('se', T('banta')) + 0.25
S.card(m0, m1)
S.add({'type': 'checklist', 't0': m0, 't1': m1, 'y': 170, 'title': 'Patthar se guzra paani = minerals', 'items': [
    {'t': T('calcium'), 'text': 'Calcium', 'mark': 'check'},
    {'t': T('magnesium'), 'text': 'Magnesium', 'mark': 'check'},
    {'t': T('sodium'), 'text': 'Sodium', 'mark': 'check'},
    {'t': T('potassium'), 'text': 'Potassium', 'mark': 'check'}]})
r0 = T('phir', m1 - 0.3) - 0.1; r1 = TE('diye') + 0.25
S.card(r0, r1)
S.add({'type': 'chain', 't0': r0, 't1': r1, 'y': 150, 'title': 'Paani ka safar', 'show': 4, 'items': [
    {'t': T('pollution', r0), 'icon': '🏭', 'text': 'Pollution aaya', 'st': ''},
    {'t': T('filter', r0), 'icon': '🧪', 'text': 'Filter aaya', 'st': ''},
    {'t': T('ro', r0), 'icon': '💧', 'text': 'RO aaya', 'st': ''},
    {'t': T('gandagi'), 'icon': '🧹', 'text': 'Gandagi nikli', 'st': '✓', 'stc': 'green'},
    {'t': T('minerals', T('saath', r0)), 'icon': '⚠️', 'text': 'Saare *minerals* bhi gaye', 'st': '✗', 'stc': 'red'}]})
S.add({'type': 'title', 't0': T('india') - 0.05, 't1': T('main', T('lena')) - 0.1, 'y': 170, 'kicker': 'India mein paani ki sthiti', 'lines': ['~Ekdam kharab~'], 'sizes': [104]})
S.add({'type': 'badge', 't0': T('main', T('lena')) - 0.05, 't1': T('ab', T('follow')) - 0.1, 'y': 200, 'text': 'Research papers', 'sub': 'Isi channel pe · *follow* karo'})
c0 = T('ab', T('follow')) - 0.1; c1 = TE('rehti') + 0.25
S.card(c0, c1)
S.add({'type': 'title', 't0': c0, 't1': T('intracellular', c0 + 1.0) - 0.08, 'y': 220, 'lines': ['Intra vs *Extra*', 'cellular paani'], 'sizes': [92, 84]})
i1 = T('extracellular', T('karata')) - 0.08
S.add({'type': 'checklist', 't0': T('intracellular', c0 + 1.0) - 0.05, 't1': i1, 'y': 170, 'title': 'Intracellular · cells ke andar', 'items': [
    {'t': T('organs'), 'text': 'Organs <span>chalate hain</span>', 'mark': 'check'},
    {'t': T('brain', c0), 'text': 'Brain <span>chalta hai</span>', 'mark': 'check'},
    {'t': T('reactions'), 'text': 'Reactions <span>chalte hain</span>', 'mark': 'check'}]})
S.add({'type': 'checklist', 't0': i1 + 0.03, 't1': c1, 'y': 170, 'title': 'Extracellular · cells ke bahar', 'items': [
    {'t': T('guzar'), 'text': 'Sirf <span>guzar raha hai</span>', 'mark': 'x'},
    {'t': T('bladder'), 'text': 'Munh → <span>bladder → bahar</span>', 'mark': 'x'},
    {'t': T('cell', i1), 'text': 'Cell ke <span>andar jaata hi nahi</span>', 'mark': 'x'},
    {'t': T('dehydrated'), 'text': 'Body <span>dehydrated</span>', 'mark': 'x'}]})
S.add({'type': 'title', 't0': T('aur', c1 - 0.3) - 0.05, 't1': T('sirf', c1) - 0.08, 'y': 170, 'lines': ['*Brain* bhi', 'dehydrate hota hai'], 'sizes': [104, 80]})
s0 = T('sirf', c1) - 0.05; s1 = T('memory') - 0.08
S.add({'type': 'stat', 't0': s0, 't1': s1, 'y': 230, 'kicker': 'Sirf', 'from': 0, 'to': 2, 'unit': '%', 'label': 'Dehydration', 'pill': '🧠 Cognitive skills ↓', 'dir': 'down', 'count': 0.8})
d0 = T('memory') - 0.1; d1 = TE('hai', T('weak')) + 0.25
S.card(d0, d1)
S.add({'type': 'chain', 't0': d0, 't1': d1, 'y': 150, 'title': '2% dehydration =', 'show': 4, 'items': [
    {'t': T('memory'), 'icon': '🧠', 'text': 'Memory slow', 'st': '↓'},
    {'t': T('mood'), 'icon': '😤', 'text': 'Mood disturb', 'st': '↓'},
    {'t': T('focus', d0), 'icon': '🎯', 'text': 'Focus toot gaya', 'st': '✗'},
    {'t': T('decision'), 'icon': '⚖️', 'text': 'Decision making weak', 'st': '↓'}]})
for it in S.events[-1]['items']: it['stc'] = 'red'
S.add({'type': 'title', 't0': T('sochiye') - 0.05, 't1': T('ye', T('hai', T('saath', T('sochiye')))) - 0.08, 'y': 170, 'kicker': 'Office mein · 3 litre paani', 'lines': ['Phir bhi *focus* nahi?'], 'sizes': [96]})
S.add({'type': 'slam', 't0': T('pandemic') - 0.3, 't1': T('meeting') - 0.05, 'y': 200, 'text': 'Ekdam *PANDEMIC*', 'size': 112})
S.punch(T('pandemic'), 0.12, 0.8)
S.add({'type': 'chips', 't0': T('meeting') - 0.05, 't1': T('mere', T('khinch')) - 0.05, 'y': 140, 'items': [
    {'t': T('meeting'), 'icon': '🗣️', 'text': 'Meeting mein *bhool*'},
    {'t': T('irritated'), 'icon': '😠', 'text': 'Shaam tak irritated'},
    {'t': T('gym'), 'icon': '🏋️', 'text': 'Gym mein sprain'},
    {'t': T('muscles'), 'icon': '💪', 'text': 'Muscles *khinch* rahi'}]})
S.add({'type': 'title', 't0': T('mere', T('khinch')) - 0.05, 't1': T('ek', T('fix')) - 0.08, 'y': 170, 'kicker': 'Mere saath bhi hua', 'lines': ['Iska *fix*?'], 'sizes': [112]})
S.add({'type': 'slam', 't0': T('ek', T('fix')) - 0.05, 't1': T('paani', T('salt')) - 0.08, 'y': 200, 'text': 'Khaari namak 🧂', 'size': 104, 'sub': '*Sea salt*'})
S.punch(T('khaari'), 0.12, 0.8)
f0 = T('paani', T('salt')) - 0.1; f1 = TE('jaayenge') + 0.3
S.card(f0, f1)
S.add({'type': 'title', 't0': f0, 't1': T('aap', f0) - 0.05, 'y': 220, 'lines': ['Paani + *thoda sea salt*'], 'sizes': [88]})
S.add({'type': 'chips', 't0': T('aap', f0) - 0.05, 't1': f1, 'y': 160, 'items': [
    {'t': T('saare', f0), 'icon': '🦴', 'text': 'Calcium'}, {'t': T('minerals', f0), 'icon': '⚡', 'text': 'Magnesium'},
    {'t': T('milna'), 'icon': '🧂', 'text': 'Sodium'}, {'t': T('shuru', f0), 'icon': '🍌', 'text': 'Potassium'},
    {'t': T('jaayenge'), 'icon': '✅', 'text': '*Minerals wapas*'}]})
S.add({'type': 'badge', 't0': T('hacks') - 0.1, 't1': T('agar', T('hacks')) - 0.1, 'y': 200, 'text': 'Health Protocol', 'sub': 'Aise chhote chhote *hacks*'})
cta = T('agar', T('hacks')) - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Health protocol chahiye?', 'title': 'Comment<br>*"HP"*', 'sub': 'You are watching FitFinfluencer · link aapke paas pahunch jaayega', 'button': '💬 COMMENT "HP"', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'paani', r'pyaas', r'washroom', r'chemical', r'h2o', r'hydrogen', r'oxygen', r'stream', r'nadiyon', r'minerals', r'calcium', r'magnesium',
                           r'sodium', r'potassium', r'pollution', r'filter', r'ro', r'intracellular', r'extracellular', r'cells?', r'brain', r'dehydrated', r'dehydration',
                           r'memory', r'mood', r'focus', r'pandemic', r'sprain', r'muscles', r'fix', r'namak', r'salt', r'hp', r'protocol'])
B = S.broll
B(4546, T('paani') - 0.1, T('uske') - 0.05, off=1.0)
B(108, T('washroom') - 0.6, T('phir', T('washroom')) + 0.4, off=2.0)
B(50576, T('stream') - 0.1, T('pattharon') - 0.05, off=1.0)
B(51600, T('pattharon') - 0.05, m0 - 0.05, off=2.0)
B(2186, T('pollution') - 0.1, T('pollution', T('aaya')) - 0.05, off=1.0)
B(4733, T('research') - 0.15, T('toh', T('channel')) - 0.05, off=1.0)
B(4547, T('office') - 0.3, T('phir', T('office')) - 0.05, off=2.0)
B(4607, T('phir', T('office')) - 0.05, T('ye', T('hai', T('saath', T('sochiye')))) - 0.08, off=3.0)
B(4701, T('meeting') - 0.05, T('gym') - 0.08, off=2.0)
B(40248, T('gym') - 0.05, T('mere', T('khinch')) - 0.08, off=2.0)
B(42898, T('hacks') - 0.1, cta - 0.05, off=2.0)
S.save(caps, cta_t=cta, hold=1.2, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
