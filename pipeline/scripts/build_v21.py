import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v21', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; K = S.kin; Bh = S.behind
# hook
Bh(0.05, T('aur') - 0.08, 'SUGAR', size=380, font='anton', anim='slam')
K(0.2, T('aur') - 0.08, ["YOU'RE USING IT *WRONG*"], x=540, y=1600, sizes=[66], font='oswald', anim='rise')
K(T('aur') - 0.05, T('mere') - 0.08, ['AND YOU', "DON'T EVEN KNOW IT"], x=70, y=300, align='left', sizes=[90, 90], anim='wipe')
# family history
f0 = T('mere') - 0.1; f1 = T('aur', T('pre.*')) - 0.08
S.card(f0, f1); S.fx('heartbeat', f0 + 0.2, -12); S.fx('heartbeat', f0 + 1.1, -14)
S.add({'type': 'chain', 't0': f0, 't1': f1, 'y': 150, 'title': 'My family history', 'show': 4, 'items': [
    {'t': T('par.*'), 'text': 'Great-grandfather', 'st': 'Diabetes', 'stc': 'red'},
    {'t': T('dada', T('par.*') + 0.3), 'text': 'Grandfather', 'st': 'Diabetes', 'stc': 'red'},
    {'t': T('dadi'), 'text': 'Grandmother', 'st': 'Diabetes', 'stc': 'red'},
    {'t': T('papa'), 'text': 'Father', 'st': 'Pre-diabetic', 'stc': 'red'}]})
K(f1 + 0.03, T('mujhe') - 0.05, ['ME TODAY:', '*35 YEARS OLD*'], x=70, y=300, align='left', sizes=[80, 120], anim='wipe')
Bh(T('mujhe') - 0.05, T('aap', T('naam.*')) - 0.05, 'ZERO', size=420, font='anton', anim='slam', color=G)
K(T('diabetes', T('mujhe')) - 0.05, T('aap', T('naam.*')) - 0.05, ['SIGNS OF DIABETES'], x=540, y=1600, sizes=[60], font='oswald', anim='rise')
# just sugar?
K(T('aap', T('naam.*')) - 0.03, T('aap', T('sugar', T('sirf'))) - 0.05, ['"IT\'S JUST', 'SUGAR"'], x=1010, y=300, align='right', sizes=[110, 140], font='serif', anim='rise')
K(T('aap', T('sugar', T('sirf'))) - 0.03, T('magar') - 0.05, ['EAT IT.', 'GET ENERGY.', 'DONE?'], x=70, y=280, align='left', sizes=[100, 100, 130], anim='rise', stagger=0.25)
S.add({'type': 'stamp', 't0': T('galat', T('magar')) - 0.1, 't1': T('ye', T('magar') + 0.8) - 0.05, 'y': 1120, 'text': 'WRONG', 'rot': -8}); S.punch(T('galat', T('magar')), 0.14, 0.6)
# glycation
K(T('ye', T('magar') + 0.8) - 0.03, T('chipak') - 0.05, ['SUGAR ENTERS', 'YOUR BODY'], x=1010, y=300, align='right', sizes=[96, 96], anim='wipe')
K(T('chipak') - 0.05, T('permanently') - 0.08, ['AND *STICKS*', 'TO YOUR PROTEINS'], x=540, y=300, sizes=[130, 90], anim='slam')
Bh(T('permanently') - 0.05, T('is', T('utarti')) - 0.05, 'FOREVER', size=330, font='anton', anim='slam', color=R)
Bh(T('glycation') - 0.05, T('maillard') - 0.05, 'GLYCATION', size=280, font='anton', anim='slam')
K(T('maillard') - 0.03, T('1912') - 0.05, ['IN CHEMISTRY:', 'THE *MAILLARD REACTION*'], x=540, y=300, sizes=[70, 100], anim='rise')
K(T('1912') - 0.05, T('aur', T('tha', T('1912'))) - 0.05, ['DISCOVERED IN 1912'], x=540, y=330, sizes=[80], font='serif', anim='type')
K(T('aur', T('tha', T('1912'))) - 0.03, T('sugar', T('brown')) - 0.05, ['THE SAME REACTION THAT', 'BROWNS YOUR *ROTI*'], x=540, y=300, sizes=[70, 110], anim='rise')
K(T('sugar', T('brown')) - 0.03, T('wahi', T('roti', T('heat'))) - 0.05, ['SUGAR + PROTEIN + HEAT', '= *BROWN ROTI*'], x=540, y=300, sizes=[80, 120], font='bebas', anim='rise', stagger=0.18)
K(T('wahi', T('roti', T('heat'))) - 0.03, T('slowly') - 0.05, ['IT HAPPENS', '*INSIDE YOU* TOO'], x=70, y=300, align='left', sizes=[100, 120], anim='slam')
K(T('slowly') - 0.03, T('glucose') - 0.05, ['SLOWLY.', 'OVER DECADES.', '~BUT IT HAPPENS.~'], x=1010, y=270, align='right', sizes=[90, 90, 90], anim='rise', stagger=0.3)
# biochemistry chain
g0 = T('glucose') - 0.1; g1 = T('aur', T('banta')) - 0.08
S.card(g0, g1)
gn = [{'t': g0 + 0.1, 'x': 500, 'y': 40, 'text': 'Glucose in your blood'},
      {'t': T('lysine'), 'x': 500, 'y': 165, 'text': 'Binds to lysine + arginine', 'sub': 'amino acids in proteins'},
      {'t': T('schiff'), 'x': 500, 'y': 300, 'text': 'Schiff base'},
      {'t': T('amadori'), 'x': 500, 'y': 425, 'text': 'Amadori product'},
      {'t': T('ages'), 'x': 500, 'y': 560, 'text': '*AGEs* build up', 'sub': 'Advanced Glycation End-products', 'target': True}]
gw = [{'t': T('lysine') - 0.3, 'd': 'M 500 80 L 500 115'}, {'t': T('schiff') - 0.3, 'd': 'M 500 220 L 500 260'},
      {'t': T('amadori') - 0.3, 'd': 'M 500 340 L 500 385'}, {'t': T('ages') - 0.3, 'd': 'M 500 465 L 500 505'}]
S.add({'type': 'flow', 't0': g0, 't1': g1, 'y': 120, 'w': 1000, 'h': 660, 'nodes': gn, 'wires': gw})
S.fx('tension', g1 - 1.8, -15)
K(g1 + 0.03, T('aur', T('irreversible')) - 0.05, ['PERMANENT.', '~IRREVERSIBLE.~'], x=540, y=300, sizes=[120, 140], anim='slam')
S.fx('sub_drop', T('irreversible'), -12)
# RAGE
K(T('aur', T('irreversible')) - 0.03, T('rage') - 0.08, ['AGEs SWITCH ON', 'A RECEPTOR'], x=1010, y=300, align='right', sizes=[100, 100], anim='wipe')
Bh(T('rage') - 0.05, T('rage', T('sahi')) - 0.5, 'RAGE', size=430, font='anton', anim='slam', color=R)
K(T('receptor', T('rage')) - 0.05, T('rage', T('sahi')) - 0.5, ['RECEPTOR FOR ADVANCED', 'GLYCATION END-PRODUCTS'], x=540, y=1570, sizes=[44, 44], font='mono', anim='type')
n0 = T('rage', T('sahi')) - 0.1; n1 = T('collagen') - 0.08
S.card(n0, n1)
S.add({'type': 'chain', 't0': n0, 't1': n1, 'y': 150, 'title': 'What RAGE does', 'show': 4, 'items': [
    {'t': n0 + 0.15, 'text': 'RAGE switched on'}, {'t': T('nf.*'), 'text': '*NF-kB* pathway on', 'st': 'up', 'stc': 'red'},
    {'t': T('chronic'), 'text': 'Chronic inflammation', 'st': 'up', 'stc': 'red'}, {'t': T('cancer'), 'text': 'Linked to cancer', 'st': 'up', 'stc': 'red'}]})
# where the damage shows
d1 = T('sirf', T('karaate', T('isi'))) - 0.05
K(T('collagen') - 0.05, d1, ['COLLAGEN', '= *WRINKLES*'], x=70, y=250, align='left', sizes=[70, 100], anim='slam')
K(T('blood', T('collagen')) - 0.05, d1, ['BLOOD VESSELS', '= *HIGH BP*'], x=1010, y=520, align='right', sizes=[70, 100], anim='slam')
K(T('aankhon') - 0.05, d1, ['EYES', '= *CATARACT*'], x=70, y=790, align='left', sizes=[70, 100], anim='slam')
K(T('haemoglobin') - 0.05, d1, ['HAEMOGLOBIN', '= *HbA1c*'], x=1010, y=1060, align='right', sizes=[60, 90], font='oswald', anim='slam', case='none')
K(T('hba1c') + 0.3, d1, ['THE TEST YOU ALREADY TAKE'], x=540, y=1600, sizes=[56], font='oswald', anim='rise')
# hidden sugar
K(d1 + 0.03, T('wo', T('barbaad')) - 0.05, ['ONE HABIT IS', '~DESTROYING~ YOUR BODY'], x=540, y=300, sizes=[84, 100], anim='rise')
Bh(T('wo', T('barbaad')) - 0.03, T('ketchup') - 0.08, 'HIDDEN SUGAR', size=250, font='anton', anim='slam', color=R)
S.add({'type': 'chips', 't0': T('ketchup') - 0.08, 't1': T('aur', T('36')) - 0.05, 'y': 260, 'items': [
    {'t': T('ketchup'), 'text': 'Ketchup: *4 g*', 'num': 1}, {'t': T('juice'), 'text': '"Healthy" juice: *25-30 g*', 'num': 2}, {'t': T('bread', T('juice')), 'text': 'Bread: *3-6 g*', 'num': 3}]})
K(T('aur', T('36')) - 0.03, T('doctor') - 0.05, ['AND NOBODY', 'TELLS YOU'], x=540, y=300, sizes=[110, 110], anim='track')
# doctor prediction
K(T('doctor') - 0.05, T('aaj', T('jaayegi')) - 0.05, ['MY DOCTOR, WHEN I WAS 16:'], x=540, y=250, sizes=[60], font='oswald', anim='wipe')
K(T('sabko', T('family')) - 0.05, T('aaj', T('jaayegi')) - 0.05, ['"YOU WILL GET DIABETES', 'BY 25-30"'], x=540, y=340, sizes=[66, 90], font='serif', anim='type')
K(T('aaj', T('jaayegi')) - 0.03, T('kaise', T('perfect')) - 0.05, ['TODAY: 35', 'HbA1c: ^PERFECT^'], x=70, y=300, align='left', sizes=[100, 120], font='oswald', anim='slam', case='none')
Bh(T('kaise', T('perfect')) - 0.05, T('glycation', T('batata')) - 0.05, 'HOW?', size=420, font='anton', anim='slam')
# the answer
K(T('glycation', T('batata')) - 0.03, T('lekin', T('reverse')) - 0.05, ["GLYCATION CAN'T", 'BE ~REVERSED~'], x=70, y=300, align='left', sizes=[96, 120], anim='wipe')
K(T('lekin', T('reverse')) - 0.03, T('health', T('sakti')) - 0.05, ['BUT IT CAN BE', '^STOPPED^'], x=1010, y=300, align='right', sizes=[96, 150], anim='slam')
S.add({'type': 'badge', 't0': T('health', T('sakti')) - 0.05, 't1': T('aur', T('step', T('sakti'))) - 0.05, 'y': 260, 'text': 'Health Protocol', 'sub': 'Every step explained'})
K(T('aur', T('step', T('sakti'))) - 0.03, T('agar', T('hoon', T('mazaak'))) - 0.05, ["I'M NOT", 'JOKING'], x=540, y=300, sizes=[110, 160], anim='slam')
K(T('agar', T('hoon', T('mazaak'))) - 0.03, T('kabhi', T('sudhaar')) - 0.05, ['FIX YOUR LIFESTYLE', '*TODAY*'], x=70, y=300, align='left', sizes=[90, 140], anim='wipe')
Bh(T('kabhi', T('sudhaar')) - 0.05, T('bhale') - 0.05, 'NEVER', size=420, font='anton', anim='slam', color=G)
K(T('diabetes', T('kabhi', T('sudhaar'))) - 0.05, T('bhale') - 0.05, ['GET DIABETES. EVER.'], x=540, y=1600, sizes=[64], font='oswald', anim='rise')
K(T('bhale') - 0.03, T('aap', T('hoga', T('rakha'))) - 0.05, ['EVEN IF YOUR', 'WHOLE *FAMILY TREE*', 'HAS IT'], x=540, y=260, sizes=[80, 110, 80], anim='rise', stagger=0.2)
K(T('aap', T('hoga', T('rakha'))) - 0.03, T('mera', T('rakhein')) - 0.05, ["IT'S IN", '*YOUR HANDS*'], x=1010, y=300, align='right', sizes=[100, 150], anim='slam')
cta = T('mera', T('rakhein')) - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'You are watching', 'title': 'Fit<span class="acc">Finfluencer</span>', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'FOLLOW FOR MORE', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'sugar', r'starch', r'diabetes', r'pre.?diabetic', r'35', r'proteins', r'permanently', r'glycation', r'maillard', r'1912', r'roti', r'brown',
                           r'decades', r'glucose', r'blood', r'lysine', r'arginine', r'schiff', r'amadori', r'ages', r'irreversible', r'rage', r'nf.?kb', r'inflammation',
                           r'cancer', r'collagen', r'wrinkles', r'bp', r'cataract', r'hba1c', r'hidden', r'ketchup', r'juice', r'bread', r'doctor', r'perfect', r'lifestyle'])
B = S.broll
B(5078, T('aur') - 0.05, T('mere') - 0.1, off=1.0)
B(3768, T('chipak') - 0.1, T('permanently') - 0.1, off=1.0)
B(42464, T('roti') - 0.2, T('sugar', T('brown')) - 0.08, off=1.0)
B(3968, T('wahi', T('roti', T('heat'))) - 0.05, T('slowly') - 0.08, off=2.0)
B(3954, T('cancer') - 0.3, n1 - 0.1, off=2.0)
B(4764, T('wrinkles') - 0.2, T('blood', T('collagen')) - 0.1, off=1.0)
B(42467, T('bread', T('juice')) - 0.1, T('aur', T('36')) - 0.08, off=1.0)
B(4779, T('doctor') - 0.1, T('sabko', T('family')) - 0.08, off=2.0)
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
