import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v48', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
CM = '../stock/commons/'
RED = 'linear-gradient(180deg,#FF6B79,#C21D35)'; GRN = 'linear-gradient(180deg,#5CFFB5,#0FA968)'
# ---------------- hook: mom's red patches
K(0.05, T('allergy') - 0.05, ["MY MOM'S SKIN:", '~RED PATCHES~'], x=540, y=300, sizes=[84, 120], anim='slam', stagger=0.8)
S.add({'type': 'chips', 't0': T('allergy') - 0.05, 't1': T('aur', T('jaayega')) - 0.05, 'y': 240, 'items': [
    {'t': T('allergy'), 'text': 'Allergy?'}, {'t': T('fungal'), 'text': 'Fungal infection?'}, {'t': T('cream'), 'text': '"Just apply a cream"'}]})
K(T('aur', T('jaayega')) - 0.03, T('ye', T('galti')) - 0.05, ['OUR', '~BIGGEST MISTAKE~'], x=540, y=300, sizes=[100, 130], anim='slam')
Bh(T('ye', T('galti')) - 0.03, T('aur', T('autoimmune')) - 0.05, 'PSORIASIS', size=230, font='anton', anim='slam', color=R)
K(T('autoimmune') - 0.1, T('aur', T('autoimmune')) - 0.05, ['AN AUTOIMMUNE SKIN DISEASE'], x=540, y=1600, sizes=[60], font='oswald', anim='rise')
K(T('aur', T('autoimmune')) - 0.03, T('yaani') - 0.05, ['SEARCH IT ONLINE:', '*"AUTOIMMUNE"*'], x=540, y=300, sizes=[76, 110], anim='rise')
S.add({'type': 'photo', 't0': T('yaani') - 0.05, 't1': T('aur', T('toh', T('attack'))) - 0.05, 'x': 140, 'y': 180, 'w': 800, 'h': 640, 'src': CM + 'Psoriasis_on_elbow.jpg', 'fit': 'cover', 'label': 'Immune system vs your own skin', 'credit': 'Haley Otman, CC BY 3.0'})
K(T('aur', T('toh', T('attack'))) - 0.03, T('ab', T('hua')) - 0.05, ['WHAT WE DID:', 'USELESS CREAMS. ~FOR MONTHS.~'], x=540, y=300, sizes=[84, 76], anim='slam', stagger=0.9)
# ---------------- how it happens
K(T('ab', T('hua')) - 0.03, T('purani') - 0.05, ['HOW PSORIASIS', '*HAPPENS*'], x=540, y=300, sizes=[96, 130], anim='slam')
K(T('28') - 0.1, T('purani') - 0.05, ['NORMAL SKIN CELLS: RENEWED EVERY 28 DAYS'], x=540, y=1600, sizes=[48], font='oswald', anim='rise', fit=980)
CY = T('ye', T('aati', T('basal'))) - 0.4
p0 = T('purani') - 0.08; p1 = CY
S.card(p0, p1)
S.add({'type': 'photo', 't0': p0, 't1': p1, 'x': 140, 'y': 150, 'w': 800, 'h': 700, 'src': CM + '502_Layers_of_epidermis.jpg', 'fit': 'contain', 'bg': '#ffffff', 'label': 'Basal layer: new cells start here', 'credit': 'OpenStax College, CC BY 3.0'})
c0 = CY; c1 = T('ab', T('4')) - 0.08
S.card(c0, c1)
S.add({'type': 'compare', 't0': c0, 't1': c1, 'y': 170, 'title': 'Skin renewal cycle', 'max': 28, 'items': [
    {'t': T('28', c0), 'label': 'Normal', 'unit': ' days', 'value': 28, 'cls': 'green', 'color': GRN},
    {'t': T('psoriasis', c0), 'label': 'Psoriasis', 'text': '3-4', 'unit': ' days', 'value': 4, 'cls': 'red', 'color': RED}]})
K(T('ab', T('4')) - 0.03, T('aur', T('hona')) - 0.05, ['THOSE RED PATCHES?', 'THIS CYCLE ~GONE WRONG~'], x=540, y=300, sizes=[84, 84], anim='slam', stagger=1.0)
# ---------------- why: T cells + cytokines
w0 = T('aur', T('hona')) - 0.08; w1 = T('aur', T('bhoosi')) - 0.08
S.card(w0, w1)
S.add({'type': 'chain', 't0': w0, 't1': w1, 'y': 150, 'title': 'Why the cycle breaks', 'show': 4, 'items': [
    {'t': T('signal'), 'text': '*T cells* send wrong signals', 'st': 'no', 'stc': 'red'}, {'t': T('inflammatory'), 'text': 'Release *inflammatory cytokines*'},
    {'t': T('tnfalpha'), 'text': '*TNF-alpha, IL-17, IL-23*', 'st': 'up', 'stc': 'red'}, {'t': T('jaldi'), 'text': 'Skin told: *"Faster! Faster!"*', 'st': 'up', 'stc': 'red'},
    {'t': T('pakne'), 'text': 'No time to *mature*', 'st': 'no', 'stc': 'red'}, {'t': T('bhoosi'), 'text': 'Sheds like *husk*', 'st': 'down', 'stc': 'red'}]})
K(T('cytokines') - 0.1, T('jaldi') - 0.05, ['CYTOKINES = INFLAMMATION SIGNALS'], x=540, y=780, sizes=[40], font='oswald', anim='rise', fit=1000)
K(T('aur', T('bhoosi')) - 0.03, T('pata', T('bahar')) - 0.05, ['TRAPPED CELLS:', 'RED PATCHES + ~ITCHING~'], x=540, y=300, sizes=[90, 90], anim='slam', stagger=1.0)
# ---------------- our mistake
K(T('pata', T('bahar')) - 0.03, T('aur', T('andar')) - 0.05, ['OUR MISTAKE:', 'TREATING ONLY ~THE SURFACE~'], x=540, y=300, sizes=[90, 80], anim='slam', stagger=1.0)
S.add({'type': 'stat', 't0': T('aur', T('andar')) - 0.05, 't1': T('jab', T('ilaaj')) - 0.05, 'y': 260, 'kicker': 'Dermatologist after dermatologist', 'from': 0, 'to': 6, 'unit': ' YEARS',
       'label': 'And *no right treatment*', 'dir': 'up', 'count': 0.8})
K(T('jab', T('ilaaj')) - 0.03, T('agar', T('stress')) - 0.05, ['STRESS UP =', 'PSORIASIS ~UP~'], x=540, y=300, sizes=[110, 110], anim='slam', stagger=0.9)
# ---------------- what you should do
A0 = T('main', T('dermatologist')) - 0.35; G0 = T('agar', T('research')) - 0.3
K(T('agar', T('stress')) - 0.03, (T('dermatologist') - 0.6) - 0.05, ['RED PATCHES IN YOUR FAMILY?', "IT'S ~NOT AN ALLERGY~"], x=540, y=300, sizes=[70, 100], anim='slam', stagger=1.4)
K((T('dermatologist') - 0.6) - 0.03, (A0 - 0.02), ['SEE A *DERMATOLOGIST*', 'CONFIRM IF IT IS PSORIASIS'], x=540, y=300, sizes=[90, 64], anim='rise', stagger=0.9)
K(A0, T('jo', T('zaroor')) - 0.05, ["MY MOM'S FULL STORY:", 'COMING ON *INSTAGRAM*'], x=540, y=300, sizes=[76, 96], anim='rise', stagger=0.9)
K(T('jo', T('zaroor')) - 0.03, T('main', T('doonga')) - 0.05, ['THE MISTAKES I MADE,', "*YOU WON'T MAKE*"], x=540, y=300, sizes=[84, 110], anim='slam', stagger=1.0)
K(T('main', T('doonga')) - 0.03, (G0 - 0.02), ["I'LL TEACH YOU", 'WITH *THE SCIENCE*'], x=540, y=300, sizes=[96, 110], anim='rise', stagger=0.9)
K(T('research') - 0.1, (G0 - 0.02), ['BACKED BY RESEARCH PAPERS'], x=540, y=1600, sizes=[56], font='oswald', anim='rise')
K(G0, T('webinar') - 0.05, ['PSORIASIS', 'IN YOUR HOME?'], x=540, y=300, sizes=[120, 90], anim='slam', stagger=0.7)
S.add({'type': 'badge', 't0': T('webinar') - 0.05, 't1': T('toh', T('haath')) - 0.05, 'y': 260, 'text': 'Webinar', 'sub': "Meet the *Ayurvedic doctor* behind my mom's recovery"})
cta = T('toh', T('haath')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want this treatment?', 'title': 'Comment<br>*"PSORIASIS"*', 'sub': "I'll send you the webinar link. My job was to bring you the science.", 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'mummy', r'skin', r'red', r'patches', r'allergy', r'fungal', r'infection', r'cream', r'galti', r'psoriasis', r'autoimmune',
                           r'immunity', r'attack', r'cells', r'28', r'recycle', r'basal', r'layer', r'cycle', r'34', r'immune', r't', r'signal', r'inflammatory',
                           r'cytokines', r'tnfalpha', r'il17', r'il23', r'pagal', r'jaldi', r'bhoosi', r'itching', r'6', r'saal', r'dermatologists?', r'stress',
                           r'instagram', r'research', r'webinar', r'ayurvedic', r'doctor', r'ilaaj'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
