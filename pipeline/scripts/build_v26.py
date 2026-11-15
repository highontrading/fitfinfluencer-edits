import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v26', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
Bh(0.05, T('sab') - 0.05, 'PEPTIDES', size=330, font='anton', anim='slam')
K(T('lehar') - 0.1, T('sab') - 0.05, ['EVERYWHERE.'], x=540, y=1560, sizes=[96], font='oswald', anim='rise')
K(T('sab') - 0.03, T('laga') - 0.05, ['"JUST EAT THEM"'], x=70, y=300, align='left', sizes=[96], anim='wipe')
K(T('laga') - 0.15, T('koi', T('laga')) - 0.05, ['"JUST INJECT THEM"'], x=1010, y=430, align='right', sizes=[96], anim='wipe')
K(T('koi', T('laga')) - 0.03, T('log') - 0.05, ['NOBODY TELLS YOU:', 'THERE ARE *3 CATEGORIES*'], x=540, y=300, sizes=[70, 96], anim='rise', stagger=0.4)
S.punch(T('teen'), 0.10, 0.7)
S.add({'type': 'chips', 't0': T('log') - 0.05, 't1': T('peptides', T('dete')) - 0.05, 'y': 240, 'items': [
    {'t': T('bpc157'), 'text': 'BPC-157'}, {'t': T('ozempic'), 'text': 'Ozempic'}, {'t': T('sermorelin'), 'text': 'Sermorelin'},
    {'t': T('basket') - 0.1, 'text': 'All in *one basket?*'}]})
K(T('peptides', T('dete')) - 0.03, T('but', T('risk')) - 0.05, ['DIFFERENT DRUGS.', 'DIFFERENT *EVIDENCE.*', 'DIFFERENT ~RISK.~'], x=70, y=260, align='left', sizes=[84, 84, 84], anim='rise', stagger=0.9)
K(T('but', T('risk')) - 0.03, T('ekdam') - 0.05, ['~OVERCOMPLICATED~'], x=540, y=330, sizes=[120], font='anton', anim='slam')
K(T('ekdam') - 0.03, T('peptides', T('dekhna')) - 0.05, ['TODAY: THE', '*SIMPLE VERSION*'], x=1010, y=300, align='right', sizes=[80, 110], anim='slam')
# ---------------- category 1
c0 = T('peptides', T('dekhna')) - 0.08; c1 = T('category', T('kar', T('proven'))) - 0.08
S.card(c0, c1)
S.add({'type': 'checklist', 't0': c0, 't1': c1, 'y': 150, 'title': 'Category 1: GLP-1 agonists', 'items': [
    {'t': T('ozempic', c0 + 1), 'text': 'Ozempic', 'mark': 'check'}, {'t': T('mounjaro'), 'text': 'Mounjaro', 'mark': 'check'},
    {'t': T('retatrutide'), 'text': 'Retatrutide', 'mark': 'check'}, {'t': T('weight'), 'text': 'All for *weight loss*', 'mark': 'check'},
    {'t': T('phases'), 'text': '*Phase 3* trials done', 'mark': 'check'}, {'t': T('fda'), 'text': 'Some *FDA approved*', 'mark': 'check'},
    {'t': T('millions'), 'text': 'Used by *millions*', 'mark': 'check'}, {'t': T('proven'), 'text': '*Proven* to work', 'mark': 'check'}]})
S.fx('ding', T('proven'), -14)
# ---------------- category 2
d0 = c1 + 0.02; d1 = T('category', T('mixed')) - 0.08
K(d0 + 0.02, T('ya', d0) - 0.05, ['CATEGORY 2', '*GH SECRETAGOGUES*'], x=540, y=300, sizes=[80, 100], anim='slam')
S.add({'type': 'chips', 't0': T('ya', d0) - 0.05, 't1': T('tesamorelin', d0) - 0.05, 'y': 240, 'items': [
    {'t': T('sermorelin', d0), 'text': 'Sermorelin'}, {'t': T('ipamorelin'), 'text': 'Ipamorelin'}, {'t': T('mk677'), 'text': 'MK-677'},
    {'t': T('growth'), 'text': 'Raise *growth hormone*'}]})
K(T('tesamorelin', d0) - 0.03, T('baaki') - 0.05, ['TESAMORELIN:', '*FDA APPROVED*', 'FOR ONE CONDITION'], x=70, y=260, align='left', sizes=[80, 96, 64], anim='rise', stagger=0.5)
K(T('baaki') - 0.03, T('evidence', T('baaki')) - 0.05, ['THE REST:', 'STILL *RESEARCH*'], x=1010, y=300, align='right', sizes=[80, 100], anim='wipe')
Bh(T('evidence', T('baaki')) - 0.03, d1, 'MIXED', size=340, font='anton', anim='slam', color=Y)
# ---------------- category 3
e0 = d1 + 0.02
K(e0 + 0.02, T('bpc157', e0) - 0.05, ['CATEGORY 3', '*RECOVERY PEPTIDES*'], x=540, y=300, sizes=[80, 100], anim='slam')
S.add({'type': 'chips', 't0': T('bpc157', e0) - 0.05, 't1': T('saare', T('kehte')) - 0.05, 'y': 240, 'items': [
    {'t': T('bpc157', e0), 'text': 'BPC-157'}, {'t': T('tb500'), 'text': 'TB-500'}, {'t': T('wolverine'), 'text': '"Wolverine stack"'}]})
B(2956, T('saare', T('kehte')) - 0.05, T('abhi', T('ki', T('baat'))) - 0.05, off=1.0)
K(T('saare', T('kehte')) - 0.03, T('abhi', T('ki', T('baat'))) - 0.05, ['CELEBRITIES. TV.', '*PODCASTS.*'], x=540, y=330, sizes=[90, 110], anim='rise', stagger=0.6)
S.add({'type': 'badge', 't0': T('abhi', T('ki', T('baat'))) - 0.05, 't1': T('toh', T('kam')) - 0.05, 'y': 260, 'text': 'Research: ~close to zero~', 'sub': 'A few pilot studies, some animal studies'})
S.fx('sub_drop', T('zero'), -12)
# ---------------- ratings
r0 = T('toh', T('kam')) - 0.08; r1 = T('toh', T('jin') - 1) - 0.08
S.card(r0, r1)
S.add({'type': 'compare', 't0': r0, 't1': r1, 'y': 170, 'title': 'Evidence rating', 'max': 5, 'items': [
    {'t': T('one', T('category', T('jinko'))), 'label': 'Cat 1: GLP-1', 'unit': '/5', 'value': 5, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('three', T('two', T('jinko'))), 'label': 'Cat 2: GH', 'unit': '/5', 'value': 3, 'cls': 'acc', 'color': 'linear-gradient(180deg,#FFD873,#E59A00)'},
    {'t': T('one', T('jinko')) - 0.2, 'label': 'Cat 3: Recovery', 'unit': '/5', 'value': 1, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
# ---------------- FDA
Bh(r1 + 0.02, T('jin', T('approve', r1)) - 0.05, 'FDA', size=380, font='anton', anim='slam', color=G)
K(T('evidence', r1) - 0.05, T('jin', T('approve', r1)) - 0.05, ['EVIDENCE IN =', '*SLOWLY APPROVED*'], x=540, y=1560, sizes=[64, 80], font='oswald', anim='rise')
K(T('jin', T('approve', r1)) - 0.03, T('ab', T('paayi')) - 0.05, ['NO EVIDENCE.', 'NO TRIALS.', '~NOT APPROVED.~'], x=70, y=260, align='left', sizes=[90, 90, 100], anim='rise', stagger=0.9)
# ---------------- hype
K(T('ab', T('paayi')) - 0.03, T('abhi', T('weight', T('tesamorelin'))) - 0.05, ['"TESAMORELIN IS THE BEST', 'FOR *WEIGHT LOSS*"'], x=540, y=300, sizes=[64, 80], font='serif', anim='type')
K(T('abhi', T('weight', T('tesamorelin'))) - 0.03, T('retatrutide', T('lilly')) - 0.05, ['NEW RESEARCH'], x=1010, y=300, align='right', sizes=[110], anim='slam')
Bh(T('retatrutide', T('lilly')) - 0.03, T('ye', T('retatrutide', T('lilly'))) - 0.05, 'RETATRUTIDE', size=210, font='anton', anim='slam', color=G)
S.add({'type': 'stat', 't0': T('ye', T('retatrutide', T('lilly'))) - 0.05, 't1': T('ab', T('jaayega')) - 0.05, 'y': 260, 'kicker': 'Retatrutide vs GLP-1', 'from': 1, 'to': 2, 'unit': 'X', 'label': 'Faster weight loss', 'pill': 'What the new research claims', 'dir': 'up', 'count': 0.8})
# ---------------- marketing
K(T('ab', T('jaayega')) - 0.03, T('kuch', T('harm')) - 0.05, ['MARKETED WITHOUT', 'THINKING ABOUT ~THE HARM~'], x=70, y=260, align='left', sizes=[80, 80], anim='wipe')
K(T('kuch', T('harm')) - 0.03, T('toh', T('lagaaye')) - 0.05, ['RESEARCH-ONLY PEPTIDES', '*PEOPLE INJECT ANYWAY*'], x=540, y=300, sizes=[70, 84], anim='rise', stagger=0.6)
Bh(T('toh', T('lagaaye')) - 0.03, T('jo', T('irony')) - 0.05, 'IRONY', size=360, font='anton', anim='slam')
B(43385, T('jo', T('irony')) - 0.05, T('aur', T('evidence', T('weak'))) - 0.05, off=0.8)
K(T('jo', T('irony')) - 0.03, T('aur', T('evidence', T('weak'))) - 0.05, ['MOST POPULAR ON INSTAGRAM', '= ~WEAKEST EVIDENCE~'], x=540, y=330, sizes=[64, 90], anim='rise', stagger=0.8)
K(T('aur', T('evidence', T('weak'))) - 0.03, T('ab', T('chahte')) - 0.05, ['ACTUALLY PROVEN', '= *NOBODY TALKS ABOUT IT*'], x=540, y=330, sizes=[64, 84], anim='rise', stagger=0.6)
# ---------------- India / the pitch
K(T('ab', T('chahte')) - 0.03, T('toh', T('bik')) - 0.05, ['INDIA:'], x=70, y=300, align='left', sizes=[110], anim='slam')
S.add({'type': 'stamp', 't0': T('fake') - 0.1, 't1': T('toh', T('bik')) + 1.2, 'y': 1180, 'text': 'FAKES SOLD', 'rot': -8, 'size': 120}); S.punch(T('fake'), 0.14, 0.7)
K(T('toh', T('bik')) + 1.25, T('but', T('lijiyega')) - 0.05, ["DON'T BUY", '~PEPTIDES HERE~'], x=1010, y=300, align='right', sizes=[96, 110], anim='slam')
p0 = T('ye', T('bech')) - 0.05
K(p0, T('toh', T('kara')) - 0.05, ['THE PITCH:', '"INJECT. GET A BLOOD TEST."'], x=540, y=300, sizes=[80, 64], font='oswald', anim='rise', stagger=0.5)
B(3952, T('blood', p0) - 0.1, T('toh', T('kara')) - 0.05, off=1.0)
K(T('toh', T('kara')) - 0.03, T('but', T('ho', T('patle'))) - 0.05, ['"IT\'S FDA APPROVED.', 'INJECT AND *GET LEAN*."'], x=540, y=300, sizes=[70, 80], font='serif', anim='type')
# ---------------- doctor
q0 = T('but', T('ho', T('patle'))) - 0.08; q1 = T('peptides', T('padega')) - 0.08
import os
DOC = '../stock/commons/Female_doctor_showing_blood_pressure_monitor_closeup.png'
if os.path.exists(DOC):   # run from scripts/, same relative root as render/
    S.card(q0, T('achhe', T('kariyega')) - 0.05)
    S.add({'type': 'photo', 't0': q0, 't1': T('achhe', T('kariyega')) - 0.05, 'x': 140, 'y': 180, 'w': 800, 'h': 640, 'src': DOC, 'fit': 'cover', 'label': 'Under a doctor', 'credit': 'Shixart1985, CC BY 2.0'})
else:
    B(4767, q0 + 0.05, T('achhe', T('kariyega')) - 0.05, off=1.0)
S.add({'type': 'badge', 't0': T('achhe', T('kariyega')) - 0.05, 't1': T('peptides', T('karein', T('jisko'))) - 0.05, 'y': 260, 'text': "Doctor's supervision", 'sub': 'A *good* doctor who knows peptides'})
K(T('peptides', T('karein', T('jisko'))) - 0.03, q1, ['A FULL *PROTOCOL*.', 'WITH *CYCLES*.'], x=540, y=300, sizes=[90, 90], anim='rise', stagger=0.9)
S.add({'type': 'stamp', 't0': q1, 't1': T('peptides', T('steroids')) - 0.05, 'y': 1150, 'text': 'NOT<br>STEROIDS', 'rot': -6, 'size': 84}); S.punch(q1, 0.12, 0.7)
K(T('peptides', T('steroids')) - 0.03, T('but', T('video', T('naye'))) - 0.05, ['FULL PEPTIDE VIDEO', '*COMING SOON*'], x=540, y=300, sizes=[80, 100], anim='rise')
cta = T('but', T('video', T('naye'))) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Part 2 is coming', 'title': 'Follow for the<br>*full peptide video*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'FOLLOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'peptides?', r'bpc157', r'ozempic', r'sermorelin', r'ipamorelin', r'tesamorelin', r'retatrutide', r'mounjaro', r'glp1', r'agonists',
                           r'mk677', r'tb500', r'wolverine', r'categories', r'category', r'evidence', r'risk', r'fda', r'approved?', r'proven', r'trials',
                           r'zero', r'weight', r'irony', r'instagram', r'fake', r'india', r'injection', r'doctor', r'protocol', r'cycle', r'steroids', r'science'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
