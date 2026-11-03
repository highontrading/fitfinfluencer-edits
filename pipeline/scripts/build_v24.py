import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v24', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; K = S.kin; Bh = S.behind; B = S.broll
K(0.05, T('wo', T('karke')) - 0.05, ["LAST NIGHT'S MUSIC", 'AT *FULL VOLUME*'], x=70, y=270, align='left', sizes=[80, 110], anim='wipe')
B(44742, T('earphone') - 0.5, T('wo', T('karke')) - 0.05, off=1.0)
Bh(T('wo', T('karke')) - 0.03, T('aur', T('diya')) - 0.05, '+2 YEARS', size=360, font='anton', anim='slam', color=R)
K(T('kaan') - 0.05, T('aur', T('diya')) - 0.05, ['ADDED TO YOUR EARS'], x=540, y=1600, sizes=[64], font='oswald', anim='rise'); S.punch(T('boodha'), 0.12, 0.7)
K(T('aur', T('diya')) - 0.03, T('harvard') - 0.05, ['NOT MY', 'CLAIM'], x=1010, y=300, align='right', sizes=[110, 140], anim='slam')
K(T('harvard') - 0.03, T('ki', T('hain', T('scientists'))) - 0.05, ['HARVARD PROFESSORS', 'AND *SCIENTISTS*'], x=70, y=300, align='left', sizes=[90, 110], anim='rise')
B(831, T('every') - 0.1, T('yaani') - 0.1, off=1.0)
K(T('every') - 0.05, T('yaani') - 0.1, ['"EVERY TIME WE BLAST OUR EARS', 'WITH HIGH VOLUME, WE GO', 'HOME WITH OLDER EARS"'], x=540, y=320, sizes=[58, 58, 58], font='serif', anim='type', stagger=0.03)
B(46893, T('parties.*') - 0.3, T('aap', T('ho', T('sun'))) - 0.05, off=1.0)
K(T('yaani') - 0.03, T('aap', T('ho', T('sun'))) - 0.05, ['PARTIES.', '*HIGH VOLUME.*'], x=1010, y=300, align='right', sizes=[120, 120], anim='rise', stagger=0.6)
Bh(T('aap', T('ho', T('sun'))) - 0.03, T('kyun') - 0.05, 'OLDER EARS', size=300, font='anton', anim='slam', color=R)
K(T('kyun') - 0.03, T('jab', T('hain', T('samajhte'))) - 0.05, ['WHY?'], x=540, y=300, sizes=[240], font='anton', anim='slam')
# mechanism
m0 = T('jab', T('hain', T('samajhte'))) - 0.1; m1 = T('aur', T('jaate', T('breaks'))) - 0.08
S.card(m0, m1)
mn = [{'t': T('extreme') - 0.05, 'x': 500, 'y': 60, 'text': 'Extreme *sound waves*'}, {'t': T('cells'), 'x': 500, 'y': 215, 'text': 'Hit the cells of your ear'},
      {'t': T('physical'), 'x': 500, 'y': 370, 'text': 'Physical damage'}, {'t': T('dna'), 'x': 500, 'y': 530, 'text': '*DNA breaks*', 'target': True}]
mw = [{'t': T('cells') - 0.3, 'd': 'M 500 105 L 500 165'}, {'t': T('physical') - 0.3, 'd': 'M 500 260 L 500 320'}, {'t': T('dna') - 0.3, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': m0, 't1': m1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': mn, 'wires': mw})
e0 = m1 + 0.02; e1 = T('aur', T('mechanism')) - 0.08
S.card(e0, e1)
S.add({'type': 'dna', 't0': e0, 't1': T('jab', T('wrap')) - 0.05, 'x': 40, 'y': 300, 'w': 1000, 'h': 400, 'label': 'DNA, WRAPPED BY THE EPIGENOME'})
K(T('packaging') - 0.05, T('jab', T('wrap')) - 0.05, ['THE *EPIGENOME*:', 'PROTEIN PACKAGING', 'AROUND YOUR DNA'], x=540, y=140, sizes=[64, 50, 50], anim='rise', stagger=0.2)
S.add({'type': 'chain', 't0': T('jab', T('wrap')) - 0.05, 't1': e1, 'y': 150, 'title': 'What happens on every break', 'show': 4, 'items': [
    {'t': T('break', T('wrap')), 'text': 'DNA breaks'}, {'t': T('chhod'), 'text': 'Packaging leaves to *fix it*'},
    {'t': T('saare', T('wapas')), 'text': 'Not all of it comes back', 'st': 'no', 'stc': 'red'}, {'t': T('loose'), 'text': 'Packaging stays *loose*', 'st': 'no', 'stc': 'red'},
    {'t': T('fundamental'), 'text': '= the root mechanism of *aging*', 'st': 'up', 'stc': 'red'}]})
S.fx('sub_drop', T('fundamental'), -12)
# other causes
o0 = T('aur', T('mechanism')) - 0.05; o1 = T('aap', T('toot.*')) - 0.05
S.add({'type': 'chips', 't0': o0, 't1': o1, 'y': 240, 'items': [
    {'t': T('loud'), 'text': 'Loud music'}, {'t': T('excessive'), 'text': 'Too much sun: *thymine dimers*'},
    {'t': T('capillaries'), 'text': 'Capillaries *shrink*'}, {'t': T('x.*rays'), 'text': 'X-rays: *DNA breaks*'}]})
B(34371, T('excessive') - 0.1, T('wo', T('hain', T('bante'))) - 0.05, off=1.0)
K(T('aap', T('toot.*')) - 0.03, T('bees') - 0.05, ['SOUNDS FAKE?', "IT'S *100% TRUE*"], x=540, y=300, sizes=[100, 120], anim='rise')
S.add({'type': 'stat', 't0': T('bees') - 0.05, 't1': T('aur', T('hain', T('alive'))) - 0.08, 'y': 260, 'kicker': 'DNA breaks in your body', 'from': 0, 'to': 20, 'unit': ' TRILLION', 'label': 'Every single day', 'pill': 'Just from staying alive', 'dir': 'up', 'count': 1.2})
K(T('aur', T('hain', T('alive'))) - 0.03, T('isko') - 0.05, ['THE WORST PART?'], x=540, y=330, sizes=[120], anim='track')
K(T('isko') - 0.03, T('sirf', T('sakte', T('rok'))) - 0.05, ["YOU CAN'T", '~STOP IT~'], x=70, y=300, align='left', sizes=[110, 140], anim='slam')
K(T('sirf', T('sakte', T('rok'))) - 0.03, T('jab', T('ho.', T('slow')) if False else T('slow')) + 0.7, ['ONLY', '^SLOW IT DOWN^'], x=1010, y=300, align='right', sizes=[110, 130], anim='slam')
# what I changed
c0 = T('jab', T('slow')) - 0.1; c1 = T('aur', T('lage', T('improve'))) - 0.08
S.card(c0, c1)
S.add({'type': 'checklist', 't0': c0, 't1': c1, 'y': 150, 'title': 'What I changed', 'items': [
    {'t': T('standing'), 'text': 'Standing desk', 'mark': 'check'}, {'t': T('kabhi', T('easily')), 'text': 'No very loud music', 'mark': 'check'},
    {'t': T('volume', T('shor')), 'text': 'Volume limit on my phone', 'mark': 'check'}, {'t': T('fasting'), 'text': 'Fasting for *DNA repair*', 'mark': 'check'}]})
S.add({'type': 'badge', 't0': c1 + 0.03, 't1': T('toh', T('hain', T('rakh'))) - 0.05, 'y': 260, 'text': 'Health Protocol', 'sub': 'Everything in one *system*'})
cta = T('toh', T('hain', T('rakh'))) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want the whole system?', 'title': 'Comment<br>*"HEALTH PROTOCOL"*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'volume', r'earphone', r'kaan', r'boodha', r'boodhe', r'harvard', r'professors', r'scientists', r'ears', r'sound', r'waves', r'cells',
                           r'damage', r'dna', r'breaks?', r'epigenome', r'packaging', r'protein', r'loose', r'aging', r'mechanism', r'sun', r'thymine', r'dimers',
                           r'capillaries', r'x.?rays', r'trillion', r'standing', r'desk', r'limit', r'fasting', r'repair', r'protocol'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
