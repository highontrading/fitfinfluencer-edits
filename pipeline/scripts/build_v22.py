import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v22', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; K = S.kin; Bh = S.behind; B = S.broll
K(0.1, T('but') - 0.05, ['I MADE THIS MISTAKE', '*FOR YEARS*'], x=70, y=300, align='left', sizes=[86, 120], anim='wipe')
K(T('but') - 0.03, T('ye', 3.0) - 0.05, ["DON'T", 'REPEAT IT'], x=1010, y=300, align='right', sizes=[110, 110], anim='slam')
# colour drains from the vegetables
v1 = T('iska'); v2 = T('aur', T('gayi')) - 0.05
B(10420, T('ye', 3.0) - 0.05, v1, off=0.5, sat=1.15)
B(10420, v1, T('aur', T('gayi', T('gal'))) - 0.05, off=1.8, sat=0.1, bright=-0.04, kb=0.12)
K(T('colour') - 0.05, T('aur', T('gayi', T('gal'))) - 0.05, ['COLOUR: GONE', 'NOW GREY', '~AND MUSHY~'], x=70, y=260, align='left', sizes=[96, 96, 96], anim='rise', stagger=0.45)
K(T('aur', T('gayi', T('gal'))) - 0.03, T('harvard') - 0.05, ['NOT WORTH', '~EATING~ ANYMORE'], x=540, y=300, sizes=[100, 120], anim='slam')
# Sinclair quote
K(T('harvard') - 0.05, T('kyun') - 0.05, ['DR. DAVID SINCLAIR, HARVARD'], x=70, y=1600, align='left', sizes=[56], font='oswald', anim='wipe')
B(1692, T('if') - 0.1, T('kyun') - 0.05, off=1.0)
K(T('if') - 0.05, T('kyun') - 0.05, ['"IF YOUR VEGETABLES START', 'TO LOSE COLOUR, YOU HAVE', 'GONE TO THE UNHEALTHY SIDE"'], x=540, y=300, sizes=[58, 58, 58], font='serif', anim='type', stagger=0.03)
K(T('kyun') - 0.03, T('usko') - 0.05, ['THE COLOUR', 'IS THE *CHEMICAL*', 'KEEPING YOU HEALTHY'], x=70, y=260, align='left', sizes=[90, 110, 70], anim='rise', stagger=0.4)
Bh(T('usko') - 0.03, T('plant') - 0.48, 'POLYPHENOLS', size=250, font='anton', anim='slam', color=G)
# what polyphenols are
p0 = T('plant') - 0.1; p1 = T('aur', T('liye')) - 0.08
S.card(p0, p1)
S.add({'type': 'chain', 't0': p0, 't1': p1, 'y': 150, 'title': 'What polyphenols are', 'show': 4, 'items': [
    {'t': p0 + 0.15, 'text': "A plant's *stress-survival* chemical"}, {'t': T('dhoop'), 'text': 'Too little sunlight'},
    {'t': T('paani', T('dhoop')), 'text': 'Too little water'}, {'t': T('polyphenols', T('paani', T('dhoop'))), 'text': 'Plant makes polyphenols', 'st': 'yes', 'stc': 'green'}]})
B(51106, T('dhoop') - 0.2, T('aur', T('dhoop')) - 0.05, off=1.0)
B(43697, T('aur', T('dhoop')) - 0.05, T('polyphenols', T('paani', T('dhoop'))) - 0.05, off=2.0)
# what they do in us
f0 = p1 + 0.02; f1 = T('aur', T('kam', T('inflammation'))) - 0.08
S.card(f0, f1)
fn = [{'t': f0 + 0.1, 'x': 500, 'y': 50, 'text': 'We eat the plant'},
      {'t': T('polyphenols', f0), 'x': 500, 'y': 195, 'text': 'Polyphenols enter the body'},
      {'t': T('sirt1'), 'x': 500, 'y': 345, 'text': '*SIRT1* switched on', 'sub': 'anti-aging enzyme'},
      {'t': T('repair', f0), 'x': 500, 'y': 520, 'text': 'DNA repair + *less inflammation*', 'target': True}]
fw = [{'t': T('polyphenols', f0) - 0.3, 'd': 'M 500 95 L 500 150'}, {'t': T('sirt1') - 0.3, 'd': 'M 500 240 L 500 295'}, {'t': T('repair', f0) - 0.3, 'd': 'M 500 400 L 500 465'}]
S.add({'type': 'flow', 't0': f0, 't1': f1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': fn, 'wires': fw})
# overcooking
Bh(T('overcook') - 0.05, T('toh', T('sabziyon')) - 0.05, 'OVERCOOKED', size=280, font='anton', anim='slam', color=R)
K(T('toh', T('sabziyon')) - 0.03, T('colour', T('destroy')) - 0.05, ['POLYPHENOLS', '~DESTROYED~'], x=540, y=300, sizes=[100, 140], anim='slam')
B(10420, T('destroy') - 0.1, T('colour', T('destroy')) - 0.05, off=3.0, sat=0.08, bright=-0.05)
K(T('colour', T('destroy')) - 0.03, T('aur', T('gayi', T('health'))) - 0.05, ['COLOUR GONE', '= ~HEALTH GONE~'], x=540, y=300, sizes=[110, 130], anim='slam'); S.fx('sub_drop', T('health') - 0.1, -12)
# Indian thali
K(T('aur', T('gayi', T('health'))) - 0.03, T('haldi') - 0.05, ['THE INDIAN THALI:', "THE WORLD'S BEST", '*ANTI-AGING DIET*'], x=540, y=260, sizes=[70, 90, 110], anim='rise', stagger=0.25)
S.add({'type': 'chips', 't0': T('haldi') - 0.05, 't1': T('mediterranean') - 0.08, 'y': 220, 'items': [
    {'t': T('haldi'), 'text': 'Turmeric'}, {'t': T('palak'), 'text': 'Spinach'}, {'t': T('amla'), 'text': 'Amla: *vitamin C bomb*'},
    {'t': T('achaar'), 'text': 'Pickle: *probiotics*'}, {'t': T('daal'), 'text': 'Dal + vegetables: *polyphenols*'}]})
# Mediterranean
K(T('mediterranean') - 0.05, T('same', T('maani')) - 0.05, ['THE MEDITERRANEAN DIET', '"HEALTHIEST IN THE WORLD"'], x=540, y=260, sizes=[80, 70], anim='wipe')
B(52467, T('mediterranean') - 0.1, T('duniya', T('mediterranean')) - 0.05, off=1.0)
K(T('same', T('maani')) - 0.03, T('bas') - 0.05, ['SAME', 'COMPOSITION'], x=540, y=300, sizes=[160, 100], anim='slam')
K(T('bas') - 0.03, T('ek', T('thi')) - 0.05, ['THEY HAD THE STUDIES.', '~WE DIDN\'T.~'], x=540, y=300, sizes=[84, 110], anim='rise')
# hack
K(T('ek', T('thi')) - 0.03, T('haldi', T('hack')) - 0.05, ['ONE MORE', '*HACK*'], x=70, y=300, align='left', sizes=[100, 150], anim='slam')
K(T('haldi', T('hack')) - 0.05, T('curcumin') - 0.05, ['TURMERIC', '+ GHEE', '+ BLACK PEPPER'], x=1010, y=260, align='right', sizes=[100, 100, 100], anim='rise', stagger=0.35)
B(52462, T('kaali') - 0.2, T('curcumin') - 0.05, off=1.0)
S.add({'type': 'stat', 't0': T('curcumin') - 0.05, 't1': T('aur', T('deta')) - 0.08, 'y': 260, 'kicker': 'Curcumin absorption', 'from': 0, 'to': 2000, 'unit': '%', 'label': 'Increase', 'pill': 'Turmeric + ghee + black pepper', 'dir': 'up', 'count': 1.3})
K(T('aur', T('deta')) - 0.03, T('science', T('rahe')) - 0.05, ['OUR GRANDPARENTS', '*ALREADY KNEW*'], x=540, y=300, sizes=[90, 110], anim='rise')
K(T('science', T('rahe')) - 0.03, T('mummy') - 0.05, ['SCIENCE PROVED IT', '~ONLY NOW~'], x=540, y=300, sizes=[90, 110], anim='wipe')
# mother's story
m0 = T('mummy') - 0.1; m1 = T('same', T('dekha')) - 0.08
S.card(m0, m1); S.fx('heartbeat', m0 + 0.2, -14)
S.add({'type': 'checklist', 't0': m0, 't1': m1, 'y': 150, 'title': 'My mother: psoriasis on her feet', 'items': [
    {'t': T('coloured'), 'text': 'Lots of *coloured plants*', 'mark': 'check'}, {'t': T('processed'), 'text': 'Processed food: *zero*', 'mark': 'check'},
    {'t': T('improvement'), 'text': 'We saw *improvement*', 'mark': 'check'}]})
K(m1 + 0.03, T('polyphenols', T('ghar')) - 0.05, ['THE SAME SCIENCE.', 'AT *HOME*.'], x=540, y=300, sizes=[96, 140], anim='slam')
K(T('polyphenols', T('ghar')) - 0.03, T('aur', T('down')) - 0.05, ['POLYPHENOLS: ^ON^', 'SIRT1: ^ON^', 'INFLAMMATION: ^DOWN^'], x=70, y=260, align='left', sizes=[86, 86, 86], anim='rise', stagger=0.6, case='none')
q0 = T('aur', T('down')) - 0.1; q1 = T('toh', T('hain', T('rakhi'))) - 0.08
S.card(q0, q1)
S.add({'type': 'checklist', 't0': q0, 't1': q1, 'y': 150, 'title': 'In my health protocol', 'items': [
    {'t': T('kaun'), 'text': 'Which plant', 'mark': 'check'}, {'t': T('kitna', T('kaun')), 'text': 'How much', 'mark': 'check'},
    {'t': T('kab', T('kaun')), 'text': 'When to eat it', 'mark': 'check'}, {'t': T('kis'), 'text': 'What to pair it with', 'mark': 'check'}]})
cta = q1 + 0.02
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want my health protocol?', 'title': 'Comment<br>*"HP"*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'COMMENT "HP"', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'galti', r'sabzi', r'colour', r'grey', r'harvard', r'sinclair', r'vegetables', r'unhealthy', r'chemical', r'polyphenols?', r'stress', r'survival',
                           r'dhoop', r'paani', r'sirt1', r'enzyme', r'dna', r'repair', r'inflammation', r'overcook', r'destroy', r'health', r'thaali', r'haldi', r'palak',
                           r'amla', r'achaar', r'probiotics', r'daal', r'mediterranean', r'studies', r'ghee', r'mirch', r'curcumin', r'2000%', r'psoriasis', r'processed', r'hp'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
