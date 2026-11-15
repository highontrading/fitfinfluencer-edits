import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v28', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
CM = '../stock/commons/'
# ---------------- hook: the reading
Bh(0.05, T('itna') - 0.05, '170/110', size=330, font='anton', anim='slam', color=R)
K(T('number') - 0.05, T('itna') - 0.05, ["MY WIFE'S", 'BLOOD PRESSURE'], x=540, y=1560, sizes=[70, 70], font='oswald', anim='rise')
S.add({'type': 'stamp', 't0': T('itna') - 0.05, 't1': T('normal') - 0.05, 'y': 1150, 'text': 'DANGEROUSLY<br>HIGH', 'rot': -7, 'size': 80}); S.punch(T('high'), 0.14, 0.7)
K(T('normal') - 0.03, T('aur', T('kehte')) - 0.05, ["WHAT'S NORMAL?", '*120/80*'], x=540, y=300, sizes=[84, 150], anim='slam')
K(T('but', T('kehte')) - 0.03, T('kuch', T('aata')) - 0.05, ['A NORMAL *RANGE*', 'AROUND 120/80'], x=70, y=300, align='left', sizes=[90, 70], anim='rise', stagger=0.5)
K(T('kuch', T('aata')) - 0.03, T('toh', T('batate')) - 0.05, ['SOME EVEN CALL', '130/100 "NORMAL"'], x=1010, y=300, align='right', sizes=[70, 90], anim='wipe')
# ---------------- 170/110
v0 = T('toh', T('batate')) - 0.08; v1 = T('aur', T('diastolic')) - 0.08
S.card(v0, v1)
S.add({'type': 'compare', 't0': v0, 't1': v1, 'y': 170, 'title': 'Her reading vs normal', 'max': 170, 'items': [
    {'t': T('170', v0), 'label': 'Systolic', 'value': 170, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('110', v0), 'label': 'Diastolic', 'value': 110, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('dangerous') - 0.1, 'label': 'Normal', 'text': '120/80', 'value': 120, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
# ---------------- no symptoms
K(T('aur', T('diastolic')) - 0.03, T('usko') - 0.05, ['THE SCARIEST PART?'], x=540, y=330, sizes=[110], anim='track')
K(T('usko') - 0.03, T('usko', T('feel')) - 0.05, ['SHE FELT', '~NOTHING~'], x=70, y=300, align='left', sizes=[100, 140], anim='slam')
S.add({'type': 'checklist', 't0': T('usko', T('feel')) - 0.05, 't1': T('aur', T('nahi', T('dizziness'))) - 0.05, 'y': 220, 'title': 'Symptoms', 'items': [
    {'t': T('headache'), 'text': 'Headache', 'mark': 'x'}, {'t': T('dizziness'), 'text': 'Dizziness', 'mark': 'x'}, {'t': T('nothing'), 'text': 'Anything at all', 'mark': 'x'}]})
Bh(T('aur', T('nahi', T('dizziness'))) - 0.03, T('ye', T('naam')) - 0.05, 'SILENT KILLER', size=210, font='anton', anim='slam', color=R)
K(T('ye', T('naam')) - 0.03, T('high', T('bolta')) - 0.05, ['NOT JUST A NAME.', 'IT\'S *THE DATA*.'], x=540, y=300, sizes=[84, 100], anim='rise', stagger=0.8)
# ---------------- what high BP does
a0 = T('high', T('bolta')) - 0.08; a1 = T('heart', T('tight', T('plaque'))) - 0.08
S.card(a0, a1)
S.add({'type': 'chain', 't0': a0, 't1': a1, 'y': 150, 'title': 'What high BP does to arteries', 'show': 4, 'items': [
    {'t': T('inner'), 'text': 'Damages the *inner wall*'}, {'t': T('endothelium'), 'text': 'The *endothelium*: one silky layer'},
    {'t': T('patli'), 'text': 'So thin, it *breaks* easily', 'st': 'no', 'stc': 'red'}, {'t': T('ldl'), 'text': '*LDL* starts to build up', 'st': 'up', 'stc': 'red'},
    {'t': T('plaque'), 'text': '~Plaque~ forms', 'st': 'up', 'stc': 'red'}, {'t': T('tight', T('plaque')), 'text': 'Arteries *narrow*', 'st': 'down', 'stc': 'red'}]})
S.fx('sub_drop', T('plaque'), -12)
h0 = a1 + 0.02; h1 = T('aur', T('tight', T('wahan'))) - 0.08
S.card(h0, h1)
S.add({'type': 'photo', 't0': h0, 't1': h1, 'x': 140, 'y': 210, 'w': 800, 'h': 640, 'src': CM + 'Blausen_0457_Heart_SectionalAnatomy.png', 'fit': 'contain', 'bg': '#ffffff', 'label': 'Heart wall thickens', 'credit': 'Blausen Medical, CC BY 3.0'})
K(T('left') - 0.05, h1, ['LEFT VENTRICULAR *HYPERTROPHY*'], x=540, y=120, sizes=[48], font='oswald', anim='rise')
k0 = h1 + 0.02; k1 = T('brain') - 0.08
S.card(k0, k1)
S.add({'type': 'photo', 't0': k0, 't1': k1, 'x': 140, 'y': 160, 'w': 800, 'h': 680, 'src': CM + 'Blausen_0592_KidneyAnatomy_01.png', 'fit': 'contain', 'bg': '#ffffff', 'label': 'Tiny kidney arteries: damaged', 'credit': 'Blausen Medical, CC BY 3.0'})
K(T('brain') - 0.03, T('aur', T('arteries', T('brain'))) - 0.05, ['BRAIN ARTERIES:', '~DAMAGED TOO~'], x=540, y=300, sizes=[90, 110], anim='slam')
K(T('aur', T('arteries', T('brain'))) - 0.03, T('achha') - 0.05, ['NO SYMPTOMS.', '*FOR YEARS.*'], x=540, y=300, sizes=[100, 120], anim='rise', stagger=1.2)
# ---------------- the story
K(T('achha') - 0.03, T('34') - 0.05, ['THANK GOD FOR A', '*ROUTINE CHECKUP*'], x=540, y=300, sizes=[80, 100], anim='rise')
Bh(T('34') - 0.03, T('aur', T('shock')) - 0.05, 'AGE 34', size=360, font='anton', anim='slam', color=Y)
K(T('shock') - 0.1, T('aur', T('shock')) - 0.05, ['I WAS IN SHOCK'], x=540, y=1560, sizes=[80], font='oswald', anim='rise')
m0 = T('aur', T('shock')) - 0.08; m1 = T('but', T('padengi')) - 0.08
S.card(m0, m1)
S.add({'type': 'chain', 't0': m0, 't1': m1, 'y': 150, 'title': "Doctor's verdict", 'show': 4, 'items': [
    {'t': T('reading'), 'text': 'Start medicine *right away*'}, {'t': T('telmisartan'), 'text': '*Telmisartan 40 mg*'},
    {'t': T('subah'), 'text': 'Twice a day', 'st': 'up', 'stc': 'red'}, {'t': T('zindagi'), 'text': '~"For the rest of your life"~', 'st': 'no', 'stc': 'red'}]})
K(T('but', T('padengi')) - 0.03, T('aur', T('khaayi')) - 0.05, ['TODAY:', '*1.5 MONTHS*', 'WITHOUT MEDICINE'], x=540, y=280, sizes=[80, 130, 70], anim='slam', stagger=0.5)
S.punch(T('khaayi'), 0.12, 0.7); S.fx('ding', T('khaayi'), -14)
S.add({'type': 'badge', 't0': T('aur', T('khaayi')) - 0.05, 't1': T('maine') - 0.05, 'y': 260, 'text': "All under a *doctor's supervision*", 'sub': 'No medicine needed now'})
K(T('maine') - 0.03, T('kyunki', T('sakta')) - 0.05, ['I STUDIED THE SCIENCE.', 'BUILT *A PROTOCOL*.'], x=540, y=300, sizes=[76, 96], anim='rise', stagger=1.0)
K(T('kyunki', T('sakta')) - 0.03, T('log', T('sudhaar')) - 0.05, ['ANY DISEASE CAN', 'BE IMPROVED *FROM WITHIN*'], x=540, y=300, sizes=[70, 80], font='serif', anim='type')
K(T('log', T('sudhaar')) - 0.03, T('toh', T('pahunchti')) - 0.05, ['FIRST IN THE MIND.', 'THEN IN *THE BODY*.'], x=540, y=300, sizes=[84, 96], anim='rise', stagger=1.1)
Bh(T('170', T('pahunchti')) - 0.03, T('aur', T('time', T('controlled'))) - 0.05, '170/110', size=330, font='anton', anim='slam', color=R)
S.add({'type': 'stamp', 't0': T('controlled') - 0.1, 't1': T('aur', T('time', T('controlled'))) + 1.5, 'y': 1180, 'text': 'CONTROLLED', 'rot': -6, 'color': '#37F59B', 'size': 120}); S.punch(T('controlled'), 0.12, 0.7)
Bh(T('lifestyle') - 0.4, T('main', T('lifestyle')) - 0.05, 'LIFESTYLE', size=300, font='anton', anim='slam', color=G)
K(T('ismein') - 0.35, T('lifestyle') - 0.45, ['THE BIGGEST ROLE?'], x=540, y=330, sizes=[100], anim='track')
K(T('main', T('lifestyle')) - 0.03, T('aur', T('process')) - 0.05, ['FULL STORY +', '*STEP-BY-STEP PROCESS*', 'COMING ON THIS CHANNEL'], x=540, y=280, sizes=[70, 84, 56], anim='rise', stagger=0.6)
# ---------------- check your BP
K(T('aur', T('process')) - 0.03, T('jitne') - 0.05, ['NEVER CHECKED', 'YOUR BP?'], x=540, y=300, sizes=[96, 140], anim='slam')
K(T('regular') - 0.05, T('jitne') - 0.05, ['CHECK IT *REGULARLY*'], x=540, y=1560, sizes=[80], font='oswald', anim='rise')
K(T('jitne') - 0.03, T('kyunki', T('shuru', T('sardard'))) - 0.05, ['FREQUENT HEADACHES?', '*GET CHECKED*'], x=70, y=300, align='left', sizes=[76, 110], anim='rise', stagger=0.6)
K(T('chhupa') - 0.1, T('mera') - 0.05, ['A HIDDEN,', '~DANGEROUS DISEASE~'], x=540, y=300, sizes=[96, 100], anim='slam')
cta = T('mera') - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want the full story?', 'title': 'Follow for<br>*part 2*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'FOLLOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'170', r'110', r'120', r'80', r'wife', r'bp', r'high', r'normal', r'dangerous', r'systolic', r'diastolic', r'scary', r'feel',
                           r'headache', r'dizziness', r'silent', r'killer', r'data', r'arteries', r'endothelium', r'layer', r'damage', r'ldl', r'cholesterol',
                           r'plaque', r'heart', r'hypertrophy', r'kidney', r'brain', r'symptom', r'checkup', r'34', r'shock', r'telmisartan', r'zindagi',
                           r'dawai', r'protocol', r'controlled', r'lifestyle', r'check', r'science'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

