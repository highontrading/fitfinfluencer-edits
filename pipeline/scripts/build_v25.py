# Long-form (16:9) epigenome / biological-age video. Anchors by EDL chunk id (S=start, E=end in output time).
import sys, json, numpy as np
from spec_lib2 import Spec
W, H = 1920, 1080
S_ = Spec(sys.argv[1], 'v25', mood='serious', size=(W, H)); T, TE = S_.T, S_.TE
D = S_.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; GOLD = '#FFC53D'
edl = json.load(open('edl/v25.json')); shots = S_.tl['shots']
SS = {k['c']: sh['out0'] for k, sh in zip(edl['keep'], shots)}; EE = {k['c']: sh['out1'] for k, sh in zip(edl['keep'], shots)}
S = lambda c: SS[c]; E = lambda c: EE[c]
face = np.array(json.load(open(f'{sys.argv[1]}/v25_face.json'))['face'])
def side(t0, t1):   # put text on the side away from the speaker
    a, b = int(t0 * 29.97), max(int(t0 * 29.97) + 1, int(t1 * 29.97)); fx = np.median(face[a:b, 0])
    return (90, 'left') if fx > W / 2 else (W - 90, 'right')
def K(t0, t1, lines, y=170, sizes=None, x=None, align=None, **kw):
    if x is None: x, align = side(t0, t1)
    if isinstance(lines, str): lines = [lines]
    kw.setdefault('fit', 900)
    return S_.kin(t0, t1, lines, x=x, y=y, align=align or 'center', sizes=sizes or [96] * len(lines), **kw)
def Bh(t0, t1, word, **kw): kw['size'] = min(kw.get('size', 240), 240); kw.setdefault('z', 1.0); return S_.behind(t0, t1, word, **kw)
P = [40, 920]                        # left panel while the speaker sits in the right-hand card
CARD = {'rect': [1000, 90, 860, 900], 'r': 40, 'scale': 1.05, 'faceY': 0.42}
def card(t0, t1): S_.card(t0, t1, cap_y=990)
def add(ev): ev.setdefault('panel', P); return S_.add(ev)
def chapter(t, n, title):
    S_.add({'type': 'cine', 't0': t - 0.1, 't1': t + 2.4, 'h': 110}); S_.fx('whoosh_soft', t - 0.2, -14); S_.fx('hit_soft', t + 0.05, -14)
    S_.kin(t, t + 2.4, [f'CHAPTER {n}', title], x=W // 2, y=330, sizes=[44, 120], font='bebas', anim='track', fit=1700, color='#FFFFFF')
B = S_.broll
# ---------------- hook
card(S(1) - 0.05, S(4) - 0.08)
add({'type': 'compare', 't0': S(1), 't1': S(4) - 0.08, 'y': 170, 'title': 'My age', 'max': 35, 'items': [
    {'t': S(1) + 0.3, 'label': 'Passport age', 'text': '35', 'value': 35, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': S(3), 'label': 'Body age', 'text': '23-24', 'value': 24, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
Bh(S(4), S(5) - 0.05, 'AND YOURS?')
K(S(5), S(7) - 0.05, ['"MY PASSPORT AGE', '= MY BODY\'S AGE"'], sizes=[70, 70], font='serif', anim='type')
S_.add({'type': 'stamp', 't0': S(7) + 0.2, 't1': S(9) - 0.05, 'y': 240, 'text': 'WRONG', 'rot': -8, 'size': 130}); S_.punch(S(7) + 0.4, 0.12, 0.7)
B(4712, S(9), S(10) - 0.05, off=1.0); K(S(9), S(10) - 0.05, ['HARVARD', 'MEDICAL SCHOOL'], sizes=[110, 80], anim='wipe')
B(4767, S(10), S(11) - 0.05, off=2.0); K(S(10), S(11) - 0.05, ['25 YEARS OF', '*RESEARCH*'], sizes=[90, 120], anim='rise')
K(S(11), S(12) - 0.05, ['PASSPORT AGE', 'IS NOT ~BODY AGE~'], sizes=[100, 120], anim='slam')
card(S(12) - 0.05, S(14) - 0.08)
add({'type': 'chips', 't0': S(12), 't1': S(14) - 0.08, 'y': 200, 'items': [
    {'t': T('heart', S(12)), 'text': 'Heart: *its own age*'}, {'t': T('brain', S(12)), 'text': 'Brain: *its own age*'},
    {'t': T('liver', S(13) - 0.2), 'text': 'Liver: *its own age*'}, {'t': T('kidney', S(13)), 'text': 'Kidney: *its own age*'}]})
Bh(S(14), S(15) - 0.05, 'THE OLDEST ORGAN', size=230)
K(S(15), S(16) - 0.05, ['AGES ALL', 'THE ~OTHERS~'], sizes=[110, 130], anim='slam'); S_.fx('sub_drop', S(15) + 0.3, -12)
# Sinclair mice
K(S(16), S(18) - 0.05, ['PROF. DAVID SINCLAIR', 'HARVARD MEDICAL SCHOOL'], y=150, sizes=[64, 44], font='oswald', anim='wipe')
card(S(18) - 0.05, S(24) - 0.08)
add({'type': 'checklist', 't0': S(18), 't1': S(24) - 0.08, 'y': 130, 'title': 'The two-mice experiment', 'items': [
    {'t': S(19), 'text': 'Same mother', 'mark': 'check'}, {'t': S(20), 'text': 'Mouse 1: <span>healthy, active</span>', 'mark': 'check'},
    {'t': S(21), 'text': 'Mouse 2: <span>hunched, grey, wrinkled</span>', 'mark': 'x'}, {'t': S(22), 'text': 'Mouse 2: <span>memory gone</span>', 'mark': 'x'},
    {'t': S(23), 'text': 'Same DNA, <span>same parents, same age</span>', 'mark': 'check'}]})
K(S(24), S(25) - 0.05, ['ONLY ONE', 'DIFFERENCE'], sizes=[100, 120], anim='rise')
Bh(S(25), S(39) - 0.05, 'EPIGENOME', size=280, color=G)
card(S(39) - 0.05, S(44) - 0.08)
add({'type': 'checklist', 't0': S(39), 't1': S(44) - 0.08, 'y': 160, 'title': 'In this video', 'items': [
    {'t': S(40), 'text': 'What the *epigenome* is', 'mark': 'check'}, {'t': S(41), 'text': 'How it *ages* you', 'mark': 'check'},
    {'t': S(42), 'text': 'How I turned my biological age', 'mark': 'check'}, {'t': S(43), 'text': '*back 12 years*', 'mark': 'check'}]})
# ---------------- chapter 1
chapter(S(44), 1, 'YOUR DNA')
card(T('37', S(44)) - 0.15, S(45) - 0.08)
add({'type': 'stat', 't0': T('37', S(44)) - 0.1, 't1': S(45) - 0.08, 'y': 220, 'kicker': 'Cells in your body', 'from': 0, 'to': 37, 'unit': ' TRILLION', 'label': 'Every one has a copy of your DNA', 'count': 1.2})
card(S(45) - 0.05, S(47) - 0.08)
add({'type': 'dna', 't0': S(45), 't1': S(47) - 0.08, 'x': 30, 'y': 260, 'w': 860, 'h': 380, 'label': '6 FEET OF DNA IN EVERY CELL'})
K(S(47), S(48) - 0.05, ["YOUR BODY'S", '*INSTRUCTION MANUAL*'], sizes=[80, 110], anim='rise')
card(S(48) - 0.05, T('ab', S(49)) - 0.08)
add({'type': 'chips', 't0': S(48), 't1': T('heart', S(48) + 5) - 0.08, 'y': 220, 'items': [
    {'t': T('gear'), 'text': 'When to change gear'}, {'t': T('engine'), 'text': 'Where the engine is'}, {'t': T('ac'), 'text': 'How the AC works'}, {'t': T('brakes'), 'text': 'How to brake'}]})
add({'type': 'chips', 't0': T('heart', S(48) + 5) - 0.05, 't1': T('ab', S(49)) - 0.08, 'y': 260, 'items': [
    {'t': T('heart', S(48) + 5), 'text': 'What *heart* cells do'}, {'t': T('brain', S(49) - 0.1), 'text': 'What *brain* cells do'}, {'t': T('liver', S(49)), 'text': 'What *liver* cells do'}]})
K(T('ab', S(49)), S(56) - 0.05, ['LISTEN', 'CAREFULLY'], sizes=[110, 140], anim='slam')
K(S(56), S(57) + 1.5, ['THE SAME DNA', 'IN EVERY CELL'], sizes=[100, 100], anim='wipe')
K(S(57) + 1.5, S(61) - 0.05, ['SO HOW DOES A HEART CELL', 'KNOW IT\'S A *HEART CELL*?'], sizes=[64, 80], font='serif', anim='type')
# ---------------- chapter 2
chapter(S(61), 2, 'THE EPIGENOME')
Bh(S(62), S(64) - 0.05, 'EPIGENOME', size=280, color=G)
K(S(64), S(65) - 0.05, ['EPI = *ABOVE*', 'GENOME = *GENES*'], sizes=[110, 110], anim='rise', stagger=0.5)
K(S(65), S(66) - 0.05, ['A CONTROL SYSTEM', 'ABOVE YOUR GENES'], sizes=[90, 90], anim='wipe')
K(S(66), S(68) - 0.05, ["SINCLAIR'S", '*PIANO*'], sizes=[90, 150], anim='slam')
card(S(68) - 0.05, S(79) - 0.08)
add({'type': 'chain', 't0': S(68), 't1': S(79) - 0.08, 'y': 150, 'title': 'The piano', 'show': 4, 'items': [
    {'t': S(68) + 0.2, 'text': 'Every cell has a *piano*'}, {'t': S(71), 'text': 'The *same* piano'}, {'t': S(73), 'text': '20,000 genes = *20,000 keys*'},
    {'t': S(76), 'text': 'Each cell plays *some* keys'}]})
card(S(79) - 0.05, S(84) - 0.08)
add({'type': 'ecg', 't0': S(79), 't1': S(82) + 1.0, 'x': 40, 'y': 180, 'w': 840, 'h': 460, 'bpm': 72, 'label': 'HEART CELLS: HEART MUSIC'})
add({'type': 'chips', 't0': S(82) + 1.0, 't1': S(84) - 0.08, 'y': 240, 'items': [
    {'t': S(82) + 1.1, 'text': 'Brain cells: different keys'}, {'t': T('thoughts'), 'text': 'Thoughts'}, {'t': T('memories'), 'text': 'Memories'}, {'t': T('focus', S(83)), 'text': 'Focus'}]})
K(S(84), S(86) + 1.6, ['SAME PIANO.', '*DIFFERENT MUSIC.*'], sizes=[110, 120], anim='rise', stagger=0.4)
K(S(86) + 1.6, S(87) - 0.05, ['WHO PLAYS IT?'], sizes=[120], anim='slam')
Bh(S(87), S(98) - 0.05, 'EPIGENOME', size=280, color=G)
card(S(98) - 0.05, S(105) - 0.08)
add({'type': 'dna', 't0': S(98), 't1': S(101) - 0.05, 'x': 30, 'y': 240, 'w': 860, 'h': 380, 'label': 'DNA WRAPS AROUND PROTEINS'})
K(S(99), S(101) - 0.05, ['LIKE THREAD AROUND', 'A TENNIS BALL'], x=460, y=110, align='center', sizes=[56, 56], font='oswald', anim='wipe')
add({'type': 'chain', 't0': S(101), 't1': S(105) - 0.08, 'y': 160, 'title': 'Packaging = switch', 'show': 4, 'items': [
    {'t': S(101), 'text': 'DNA wrapped *tight*'}, {'t': S(102), 'text': 'Gene *OFF*', 'st': 'no', 'stc': 'red'},
    {'t': S(103), 'text': 'DNA *open*'}, {'t': S(104), 'text': 'Gene *ON*', 'st': 'yes', 'stc': 'green'}]})
K(S(105), S(107) - 0.05, ['OPEN vs CLOSED', '*CHROMATIN*'], sizes=[90, 130], anim='slam')
card(S(107) - 0.05, S(110) - 0.08)
add({'type': 'checklist', 't0': S(107), 't1': S(110) - 0.08, 'y': 160, 'title': 'When you are young', 'items': [
    {'t': S(107) + 0.3, 'text': 'Packaging: *perfect*', 'mark': 'check'}, {'t': T('heart', S(107)), 'text': 'Heart cells: <span>heart genes</span>', 'mark': 'check'},
    {'t': T('brain', S(107)), 'text': 'Brain cells: <span>brain genes</span>', 'mark': 'check'}, {'t': S(108), 'text': '*Beautiful music*', 'mark': 'check'}]})
# ---------------- chapter 3
chapter(S(110), 3, 'WHY WE AGE')
K(S(111), S(112) - 0.05, ['THE PACKAGING', '~BREAKS DOWN~'], sizes=[100, 120], anim='slam')
K(S(112), S(115) - 0.05, ['LIKE AN OLD', 'CASSETTE TAPE', '*TANGLED*'], sizes=[90, 90, 120], anim='rise', stagger=0.5)
card(S(115) - 0.05, S(122) - 0.08)
add({'type': 'chain', 't0': S(115), 't1': S(122) - 0.08, 'y': 150, 'title': 'An aging epigenome', 'show': 4, 'items': [
    {'t': S(115) + 0.2, 'text': 'Genes that should be off: *ON*', 'st': 'no', 'stc': 'red'},
    {'t': T('jo', S(115) + 2.5), 'text': 'Genes that should be on: *OFF*', 'st': 'no', 'stc': 'red'},
    {'t': S(117), 'text': 'Brain cells *forget* who they are'}, {'t': S(118), 'text': 'Acting like liver cells'},
    {'t': S(120), 'text': 'Like kidney cells'}, {'t': S(121), 'text': 'Like heart cells'}]})
K(S(122), S(124) - 0.05, ['MUSIC', '→ ~NOISE~'], sizes=[120, 150], anim='slam')
Bh(S(124), S(126) - 0.05, 'CACOPHONY', size=270, color=R)
S_.add({'type': 'cine', 't0': S(126), 't1': S(132) - 0.05, 'h': 110})
K(S(126), S(132) - 0.05, ['THE INFORMATION', 'THEORY OF AGING'], x=W // 2, y=150, align='center', sizes=[90, 120], anim='track', fit=1700)
K(S(132), S(133) - 0.05, ['AGING IS NOT', '~DAMAGED DNA~'], sizes=[110, 120], anim='slam'); S_.punch(S(132) + 0.3, 0.1, 0.7)
K(S(133), S(142) - 0.05, ['OLD SCIENCE:', '"AGING = DNA MUTATIONS"'], sizes=[70, 80], font='serif', anim='type')
card(S(142) - 0.05, S(146) - 0.08)
add({'type': 'chain', 't0': S(142), 't1': S(146) - 0.08, 'y': 160, 'title': "Sinclair's proof", 'show': 4, 'items': [
    {'t': S(142) + 0.3, 'text': 'DNA from a *100-year-old* cell'}, {'t': S(143), 'text': 'Can make a *young mouse*', 'st': 'yes', 'stc': 'green'},
    {'t': S(144), 'text': 'The DNA is *intact*', 'st': 'yes', 'stc': 'green'}, {'t': S(145), 'text': 'The problem: *the packaging*', 'st': 'no', 'stc': 'red'}]})
Bh(S(146), S(148) - 0.05, 'EPIGENOME', size=280, color=R)
K(S(148), S(152) - 0.05, ['CELLS FORGET', 'WHICH GENES ARE', '*ON* AND *OFF*'], sizes=[90, 70, 110], anim='rise', stagger=0.4)
# ---------------- chapter 4
chapter(S(152), 4, 'EVERY ORGAN HAS ITS OWN AGE')
card(S(154) - 0.05, S(159) - 0.08)
add({'type': 'chain', 't0': S(154), 't1': S(159) - 0.08, 'y': 150, 'title': 'Same person, different ages', 'show': 4, 'items': [
    {'t': T('passport', S(156)), 'text': 'Passport age', 'st': '30'}, {'t': T('heart', S(156)), 'text': '*Heart*', 'st': '40', 'stc': 'red'},
    {'t': T('brain', S(157)), 'text': '*Brain*', 'st': '25', 'stc': 'green'}, {'t': T('lungs'), 'text': '*Lungs*', 'st': '45', 'stc': 'red'}]})
S_.add({'type': 'photo', 't0': T('heart', S(156)), 't1': T('brain', S(157)) - 0.1, 'x': 1060, 'y': 140, 'w': 740, 'h': 760, 'src': '../stock/commons/Blausen_0451_Heart_Anterior.png', 'fit': 'contain', 'bg': '#ffffff', 'label': 'Heart', 'credit': 'Blausen Medical, CC BY 3.0'})
K(S(159), S(161) - 0.05, ['HOW IS THAT POSSIBLE?', 'AND HOW DO WE KNOW?'], sizes=[80, 80], anim='rise', stagger=0.6)
Bh(S(161), S(162) - 0.05, 'EPIGENETIC CLOCK', size=220)
card(S(162) - 0.05, S(171) - 0.08)
K(S(162), S(164) - 0.05, ['DR. STEVE HORVATH', 'BUILT THE CLOCK'], x=460, y=170, align='center', sizes=[70, 56], font='oswald', anim='wipe')
add({'type': 'dna', 't0': S(164), 't1': S(171) - 0.08, 'x': 30, 'y': 300, 'w': 860, 'h': 360, 'label': 'METHYL GROUPS ON YOUR DNA = A TIMER'})
K(S(164), S(165) - 0.05, ['A TIMER IN', '*EVERY CELL*'], x=460, y=120, align='center', sizes=[60, 80], anim='rise')
K(S(165), S(171) - 0.05, ['CHEMICAL MARKS SHOW', 'HOW OLD YOUR CELLS ARE'], x=460, y=120, align='center', sizes=[54, 54], font='oswald', anim='wipe')
K(S(171), T('is', S(172)) - 0.05, ['ONE', '*CHEEK SWAB*'], sizes=[100, 140], anim='slam')
card(S(172) - 0.05, S(174) - 0.08)
add({'type': 'chips', 't0': S(172), 't1': S(174) - 0.08, 'y': 260, 'items': [
    {'t': T('heart', S(172)), 'text': 'Your heart age'}, {'t': T('kidney', S(173)), 'text': 'Your kidney age'}, {'t': T('brain', S(173)), 'text': 'Your brain age'}]})
K(S(174), S(178) - 0.05, ['YOUR MOUTH CELLS STORE', "YOUR WHOLE BODY'S *MEMORY*"], sizes=[64, 80], anim='rise')
card(S(178) - 0.05, S(183) - 0.08)
add({'type': 'checklist', 't0': S(178), 't1': S(183) - 0.08, 'y': 150, 'title': 'One swab reveals', 'items': [
    {'t': S(179), 'text': 'Years of smoking', 'mark': 'x'}, {'t': T('heart', S(180)), 'text': 'Heart damage', 'mark': 'x'}, {'t': T('lungs', S(180)), 'text': 'Lung damage', 'mark': 'x'},
    {'t': T('fasting', S(181)), 'text': 'Fasting', 'mark': 'check'}, {'t': T('exercise', S(181)), 'text': 'Exercise', 'mark': 'check'}]})
# ---------------- chapter 5
chapter(S(183), 5, 'THE TWIN STUDY')
card(S(185) - 0.05, S(190) - 0.08)
add({'type': 'checklist', 't0': S(185), 't1': S(190) - 0.08, 'y': 130, 'title': 'Identical twins', 'items': [
    {'t': T('dna', S(185)), 'text': 'Same DNA', 'mark': 'check'}, {'t': T('parents', S(185)), 'text': 'Same parents', 'mark': 'check'},
    {'t': T('birth'), 'text': 'Same birth', 'mark': 'check'}, {'t': S(187), 'text': '*10 years apart* in biological age', 'mark': 'x'},
    {'t': S(189), 'text': 'Why? *Lifestyle*', 'mark': 'check'}]})
card(S(190) - 0.05, S(192) - 0.08)
add({'type': 'compare', 't0': S(190), 't1': S(192) - 0.08, 'y': 160, 'title': 'What decides your aging', 'max': 80, 'items': [
    {'t': S(190) + 0.2, 'label': 'Lifestyle', 'text': '80%', 'value': 80, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': S(191), 'label': 'Genes', 'text': '20%', 'value': 20, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
K(S(192), S(196) - 0.05, ['HARVARD STUDY', '78,865 WOMEN', '44,354 MEN', '34 YEARS'], sizes=[80, 70, 70, 90], anim='rise', stagger=0.7)
card(S(197) - 0.05, S(199) - 0.08)
add({'type': 'stat', 't0': S(197), 't1': S(199) - 0.08, 'y': 220, 'kicker': 'Follow just 5 habits', 'from': 0, 'to': 14, 'unit': ' YEARS', 'label': 'Of extra healthy life', 'pill': 'Harvard, 34-year study', 'dir': 'down', 'count': 1.0})
card(S(199) - 0.05, S(203) - 0.08)
add({'type': 'checklist', 't0': S(199), 't1': S(203) - 0.08, 'y': 130, 'title': 'The 5 habits', 'items': [
    {'t': T('overdrink'), 'text': "Don't overdrink", 'mark': 'check'}, {'t': T('smoke', S(200)), 'text': "Don't smoke", 'mark': 'check'},
    {'t': T('weight', S(200)), 'text': 'Control your weight', 'mark': 'check'}, {'t': T('stress', S(200)), 'text': 'Manage stress', 'mark': 'check'},
    {'t': S(201), 'text': 'Eat healthy', 'mark': 'check'}]})
K(S(203), S(204) - 0.05, ['SIMPLE.', 'BUT WHO DOES IT?'], sizes=[130, 80], font='serif', anim='rise')
# ---------------- chapter 6
chapter(S(204), 6, 'ZOMBIE CELLS'); S_.fx('tension', S(204) - 1.8, -14)
K(S(205), S(207) - 0.05, ['YOUR OLDEST ORGAN', '~AGES ALL THE OTHERS~'], sizes=[90, 90], anim='slam')
card(S(207) - 0.05, S(217) - 0.08)
fn = [{'t': S(207), 'x': 440, 'y': 70, 'text': 'Fat tissue from an *old* mouse'}, {'t': S(209) + 1.5, 'x': 440, 'y': 260, 'text': 'Transplanted into a *young* mouse'},
      {'t': S(211), 'x': 440, 'y': 450, 'text': 'Its whole body *started aging*', 'target': True}]
fw = [{'t': S(209) + 1.2, 'd': 'M 440 115 L 440 210'}, {'t': S(211) - 0.3, 'd': 'M 440 305 L 440 400'}]
add({'type': 'flow', 't0': S(207), 't1': S(217) - 0.08, 'y': 160, 'w': 880, 'h': 560, 'nodes': fn, 'wires': fw})
Bh(S(218), S(224) - 0.05, 'SASP', size=330, color=R)
K(S(223), S(224) - 0.05, ['SENESCENCE-ASSOCIATED', 'SECRETORY PHENOTYPE'], x=W // 2, y=740, align='center', sizes=[50, 50], font='mono', anim='type', fit=1600)
Bh(S(224), S(227) - 0.05, 'ZOMBIE CELLS', size=250, color=R)
card(S(227) - 0.05, S(232) - 0.08)
add({'type': 'checklist', 't0': S(227), 't1': S(232) - 0.08, 'y': 130, 'title': 'Zombie cells', 'items': [
    {'t': T('kaam', S(227)), 'text': "Don't work", 'mark': 'x'}, {'t': T('marti'), 'text': "But don't die", 'mark': 'x'},
    {'t': S(229), 'text': 'Release *inflammatory cytokines*', 'mark': 'x'}, {'t': T('il.*'), 'text': 'IL-6, TNF-alpha, TGF-beta', 'mark': 'x'},
    {'t': S(231), 'text': 'Age your *healthy cells*', 'mark': 'x'}]})
B(3954, S(229), S(230) - 0.05, off=2.0)
card(S(232) - 0.05, S(235) - 0.08)
add({'type': 'chain', 't0': S(232), 't1': S(235) - 0.08, 'y': 160, 'title': 'Your immune system', 'show': 4, 'items': [
    {'t': S(232) + 0.2, 'text': 'Young: clears zombie cells', 'st': 'yes', 'stc': 'green'}, {'t': T('kamzor'), 'text': 'Older: *weakens*', 'st': 'down', 'stc': 'red'},
    {'t': T('accumulate'), 'text': 'Zombie cells *pile up*', 'st': 'up', 'stc': 'red'}]})
Bh(T('hypothalamus'), S(236) - 0.05, 'HYPOTHALAMUS', size=230)
K(T('base'), S(236) - 0.05, ['AT THE BASE OF YOUR BRAIN'], x=W // 2, y=780, align='center', sizes=[56], font='oswald', anim='wipe', fit=1600)
K(S(236), S(237) - 0.05, ['OLD HYPOTHALAMUS = ~OLD BODY~', 'YOUNG HYPOTHALAMUS = ^YOUNG BODY^'], sizes=[60, 60], anim='rise', stagger=0.8)
K(S(238), S(239) - 0.05, ['LOOK YOUNGER.', 'LIVE *LONGER.*'], sizes=[110, 130], anim='rise', stagger=0.5)
# ---------------- chapter 7
chapter(S(239), 7, 'WHAT I DID')
card(S(239) + 2.5, S(242) - 0.08)
add({'type': 'compare', 't0': S(239) + 2.5, 't1': S(242) - 0.08, 'y': 160, 'title': 'Me today', 'max': 35, 'items': [
    {'t': T('passport', S(241)), 'label': 'Passport age', 'text': '35', 'value': 35, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('biological', S(241)), 'label': 'Biological age', 'text': '23-24', 'value': 24, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
K(S(242), S(244) - 0.05, ["IT'S ALL", '*VERY SIMPLE*'], sizes=[90, 120], anim='rise')
Bh(S(244), S(247) - 0.05, 'JUST 4 THINGS', size=250)
K(S(247), S(248), ['1', 'FASTING'], sizes=[160, 110], anim='slam', color=GOLD)
card(S(248) - 0.05, S(257) - 0.08)
add({'type': 'chain', 't0': S(248), 't1': S(257) - 0.08, 'y': 160, 'title': 'Fasting', 'show': 4, 'items': [
    {'t': S(248), 'text': 'Body in *adversity mode*'}, {'t': T('energy', S(248)), 'text': 'More *energy*', 'st': 'up', 'stc': 'green'},
    {'t': S(249), 'text': '*Autophagy* switches on'}, {'t': T('kharab', S(249)), 'text': 'Eats damaged proteins', 'st': 'yes', 'stc': 'green'}]})
card(S(257) - 0.05, S(264) - 0.08)
add({'type': 'checklist', 't0': S(257), 't1': S(264) - 0.08, 'y': 130, 'title': 'Two modes', 'items': [
    {'t': S(257), 'text': '3-4 meals: <span>abundance / growth mode</span>', 'mark': 'x'}, {'t': S(258), 'text': 'Aging *speeds up*', 'mark': 'x'},
    {'t': S(259), 'text': 'Fast + exercise + a little stress', 'mark': 'check'}, {'t': S(261), 'text': 'Adversity / *survival mode*', 'mark': 'check'},
    {'t': S(262), 'text': '*Anti-aging genes* switch on', 'mark': 'check'}]})
card(S(264) - 0.05, S(265) - 0.08)
sn = [{'t': S(264), 'x': 440, 'y': 70, 'text': '*Sirtuins* activate'}, {'t': T('repair', S(264)), 'x': 440, 'y': 260, 'text': 'DNA repair'},
      {'t': T('stable', S(264)), 'x': 440, 'y': 450, 'text': 'Epigenome *stable*', 'target': True}]
sw = [{'t': T('repair', S(264)) - 0.3, 'd': 'M 440 115 L 440 210'}, {'t': T('stable', S(264)) - 0.3, 'd': 'M 440 305 L 440 400'}]
add({'type': 'flow', 't0': S(264), 't1': S(265) - 0.08, 'y': 160, 'w': 880, 'h': 560, 'nodes': sn, 'wires': sw})
K(S(265), T('indian', S(265)) - 0.05, ['2', 'DIET'], sizes=[160, 110], anim='slam', color=GOLD)
card(T('indian', S(265)) - 0.05, T('number', S(270)) - 0.08)
add({'type': 'chips', 't0': T('indian', S(265)), 't1': T('number', S(270)) - 0.08, 'y': 160, 'items': [
    {'t': T('sabziyan'), 'text': 'Vegetables'}, {'t': T('daal', S(265)), 'text': 'Dal'}, {'t': T('haldi', S(265)), 'text': 'Turmeric'}, {'t': T('amla', S(265)), 'text': 'Amla'},
    {'t': S(266), 'text': 'Coloured plants: *polyphenols*'}, {'t': S(270), 'text': 'Switch on *SIRT1*'}]})
B(10420, T('sabziyan') - 0.1, S(266) - 0.05, off=1.0)
K(T('number', S(270)), S(271) - 0.05, ['3', 'EXERCISE'], sizes=[160, 110], anim='slam', color=GOLD)
B(52317, S(271), S(274) - 0.05, off=1.0)
card(S(274) - 0.05, S(282) - 0.08)
add({'type': 'checklist', 't0': S(274), 't1': S(282) - 0.08, 'y': 130, 'title': 'Exercise', 'items': [
    {'t': S(274), 'text': 'Weight training: *must*', 'mark': 'check'}, {'t': T('muscle', S(274)), 'text': 'Builds muscle', 'mark': 'check'},
    {'t': S(277), 'text': 'Muscle absorbs *glucose*', 'mark': 'check'}, {'t': S(280), 'text': 'Matters more *with age*', 'mark': 'check'}]})
B(52089, S(277), S(278) + 1.5, off=1.0)
K(S(282), S(283) - 0.05, ['4', 'MEDITATION'], sizes=[160, 110], anim='slam', color=GOLD)
B(43786, S(283), S(290) - 0.05, off=1.0)
K(S(283), S(290) - 0.05, ['+ STRESS', 'MANAGEMENT'], sizes=[90, 90], anim='wipe')
card(S(290) - 0.05, S(296) - 0.08)
add({'type': 'stat', 't0': S(290), 't1': S(296) - 0.08, 'y': 220, 'kicker': 'People asked me how', 'fromText': '110 KG', 'from': 110, 'to': 85, 'unit': 'KG', 'label': 'In 45-50 days', 'pill': 'Down 25 kg', 'dir': 'down', 'count': 1.4})
card(S(296) - 0.05, S(301) - 0.08)
add({'type': 'chain', 't0': S(296), 't1': S(301) - 0.08, 'y': 150, 'title': 'The foundation of my health protocol', 'show': 4, 'items': [
    {'t': S(297), 'text': 'Fasting'}, {'t': S(298), 'text': 'Diet'}, {'t': S(299), 'text': 'Exercise'}, {'t': T('meditation', S(299)), 'text': 'Meditation'}]})
for it in S_.events[-1]['items']: it['st'] = 'yes'; it['stc'] = 'green'
# ---------------- chapter 8
chapter(S(301), 8, 'THE FUTURE')
K(S(301) + 2.4, S(302) - 0.05, ['NOT SAYING:', 'TAKE SUPPLEMENTS. OR DON\'T.'], sizes=[70, 70], anim='wipe')
K(S(302), S(304) - 0.05, ['YOUR BODY KEEPS A', '*BACKUP COPY*', 'OF YOUR YOUNGER SELF'], sizes=[64, 110, 64], font='serif', anim='rise', stagger=0.4)
K(S(304), S(306) - 0.05, ['FIND THE', '*SWITCH*'], sizes=[110, 150], anim='slam')
S_.add({'type': 'badge', 't0': S(306), 't1': S(309) - 0.05, 'y': 150, 'text': 'ER-100', 'sub': 'Life Biosciences · Phase 1 trial'})
B(4767, S(307), S(309) - 0.05, off=1.0)
K(S(309), S(312) - 0.05, ['BEING TESTED', 'IN HUMANS'], sizes=[100, 100], anim='rise')
K(S(312), S(314) - 0.05, ['A PATH TO', '*EPIGENETIC REVERSAL*'], sizes=[80, 110], anim='wipe')
K(S(314), S(316) - 0.05, ['WHEN?', 'NOBODY KNOWS'], sizes=[130, 90], anim='slam')
Bh(T('tab', S(316)), S(319) - 0.05, 'LIFESTYLE', size=300, color=G)
K(T('haath', S(316)), S(319) - 0.05, ['IS IN YOUR HANDS'], x=W // 2, y=780, align='center', sizes=[60], font='oswald', anim='rise', fit=1600)
# ---------------- outro
K(S(319), S(324) - 0.05, ['SHOW THIS TO', 'YOUR *PARENTS*'], sizes=[90, 130], anim='rise')
K(S(324), S(327) - 0.05, ['TAKE CARE', 'OF THEM'], sizes=[110, 110], font='serif', anim='rise')
card(S(329) - 0.05, S(338) - 0.08)
add({'type': 'checklist', 't0': S(329), 't1': S(338) - 0.08, 'y': 150, 'title': 'Next video: the science of fasting', 'items': [
    {'t': S(331), 'text': 'Your brain switches on after *3 days*', 'mark': 'check'}, {'t': S(332), 'text': '*CMA* switches on', 'mark': 'check'},
    {'t': S(336), 'text': 'Chaperone-mediated autophagy', 'mark': 'check'}, {'t': T('deep', S(337)), 'text': '*Deep cleaning* of your body', 'mark': 'check'}]})
S_.add({'type': 'badge', 't0': S(338), 't1': S(340) - 0.05, 'y': 150, 'text': 'Subscribe', 'sub': 'And turn on the *bell*'})
cta = S(340)
S_.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 560, 'kicker': 'Want my health protocol?', 'title': 'Comment *"HEALTH PROTOCOL"*', 'sub': 'And tell me: what is your biological age?', 'button': 'COMMENT NOW', 'hideCaps': True})
S_.punch(cta, 0.05, 99)
# ---------------- camera, captions
S_.alt_zoom([1.0, 1.18, 1.08, 1.28]); S_.cam['faceY'] = 0.42; S_.cam['grain'] = 4; S_.cam['card'] = CARD
caps = S_.captions(max_words=4, max_chars=26, hl_pats=[r'passport', r'age', r'35', r'harvard', r'heart', r'brain', r'liver', r'kidney', r'organs?', r'sinclair', r'epigenome',
    r'dna', r'cells?', r'trillion', r'manual', r'piano', r'keys', r'genes', r'music', r'chromatin', r'packaging', r'cassette', r'noise', r'cacophony', r'aging',
    r'mutation', r'clock', r'horvath', r'methyl', r'swab', r'smoking', r'twins', r'lifestyle', r'80%', r'20%', r'sasp', r'zombie', r'cytokines', r'immune',
    r'hypothalamus', r'fasting', r'autophagy', r'sirtuins', r'polyphenols', r'sirt1', r'exercise', r'muscle', r'meditation', r'protocol', r'er.?100'])
S_.save(caps, cta_t=cta, cap_y=900, hold=1.0, extra={'capScale': 0.72, 'vigInCompose': True}, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
