# Long-form 51 (16:9): "Billionaire ka dimaag alag kyun hota hai". Anchors by EDL chunk id: S(c) = output start of chunk c.
import sys, json, numpy as np
from spec_lib2 import Spec
import lf_svg as V
W, H = 1920, 1080
S_ = Spec(sys.argv[1], 'v51', mood='serious', size=(W, H)); T, TE = S_.T, S_.TE
D = S_.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; GOLD = '#FFC53D'
shots = S_.tl['shots']; SS, EE = {}, {}
for sh in shots: SS.setdefault(sh['c'], sh['out0']); EE[sh['c']] = sh['out1']
def S(c): return SS[c]
def E(c): return EE[c]
face = np.array(json.load(open(f'{sys.argv[1]}/v51_face.json'))['face'])
def side(t0, t1):
    a, b = int(t0 * 29.97), max(int(t0 * 29.97) + 1, int(t1 * 29.97)); fx = np.median(face[a:b, 0])
    return (110, 'left') if fx > W / 2 else (W - 110, 'right')
def K(t0, t1, lines, y=170, sizes=None, x=None, align=None, **kw):
    if x is None: x, align = side(t0, t1)
    if isinstance(lines, str): lines = [lines]
    kw.setdefault('fit', 860)
    return S_.kin(t0, t1, lines, x=x, y=y, align=align or 'center', sizes=sizes or [92] * len(lines), **kw)
def KC(t0, t1, lines, y=150, sizes=None, **kw):   # centred, for full-frame moments
    if isinstance(lines, str): lines = [lines]
    kw.setdefault('fit', 1700)
    return S_.kin(t0, t1, lines, x=W // 2, y=y, align='center', sizes=sizes or [92] * len(lines), **kw)
def Bh(t0, t1, word, **kw): kw['size'] = min(kw.get('size', 240), 260); kw.setdefault('z', 1.0); return S_.behind(t0, t1, word, **kw)
P = [40, 920]
CARD = {'rect': [1000, 90, 860, 900], 'r': 40, 'scale': 1.05, 'faceY': 0.42}
def card(t0, t1): S_.card(t0, t1, cap_y=990)
def add(ev): ev.setdefault('panel', P); return S_.add(ev)
def anim(t0, t1, html, y=110, x=50, w=900, fx=True):
    if fx: S_.fx('whoosh_soft', t0, -16)
    return S_.add({'type': 'anim', 't0': t0, 't1': t1, 'x': x, 'y': y, 'w': w, 'html': html})
def chapter(t, n, title):
    S_.add({'type': 'cine', 't0': t - 0.1, 't1': t + 2.4, 'h': 110}); S_.fx('whoosh_soft', t - 0.2, -14); S_.fx('hit_soft', t + 0.05, -14)
    S_.kin(t, t + 2.4, [f'PART {n}', title], x=W // 2, y=300, sizes=[44, 116], font='bebas', anim='track', fit=1700, color='#FFFFFF')
B = S_.broll
RED = 'linear-gradient(180deg,#FF6B79,#C21D35)'; GRN = 'linear-gradient(180deg,#5CFFB5,#0FA968)'

# ================= COLD OPEN
K(S(0), S(7) - 0.05, ['SUPER-SUCCESSFUL', '*PEOPLE*'], sizes=[90, 110], anim='rise')
B(34566, S(7), S(8) - 0.05, off=1.0)
K(S(7), S(8) - 0.05, ['FROM ZERO', 'TO *100*'], sizes=[110, 140], anim='slam')
K(S(8), S(9) - 0.05, ['1 COMMON', '*TRAIT*'], sizes=[110, 130], anim='slam')
card(S(9) - 0.05, S(12) - 0.08)
anim(S(9), S(12) - 0.08, V.strike_list(['IDEAS', 'LUCK', 'TALENT', 'CONNECTIONS'], [T('idea', S(9)), T('luck', S(9)), T('talent', S(9)), T('connection', S(9))], S(11)))
K(S(12), S(15) - 0.05, ['THEY TRULY BELIEVED', 'IT COULD *COME TRUE*'], sizes=[76, 96], anim='rise', stagger=0.9)
Bh(S(15), S(18) - 0.05, 'MS DHONI', size=230, color=GOLD)
card(S(18) - 0.05, S(28) - 0.08)
add({'type': 'flow', 't0': S(18), 't1': S(28) - 0.08, 'y': 140, 'w': 900, 'h': 640, 'nodes': [
    {'t': S(18) + 0.3, 'x': 450, 'y': 60, 'text': 'A railway *TT job*'}, {'t': S(19) + 0.3, 'x': 450, 'y': 215, 'text': 'Where most careers ~end~'},
    {'t': S(25), 'x': 450, 'y': 370, 'text': '"Beta, *don\'t quit* the job"'}, {'t': S(26), 'x': 450, 'y': 530, 'text': 'A cricket legend', 'target': True}],
    'wires': [{'t': S(19), 'd': 'M 450 105 L 450 165'}, {'t': S(25) - 0.3, 'd': 'M 450 260 L 450 320'}, {'t': S(26) - 0.3, 'd': 'M 450 415 L 450 480'}]})
K(S(28), S(31) - 0.05, ['THAT IS', '*BELIEF*'], sizes=[100, 150], anim='slam')
card(S(31) - 0.05, S(36) - 0.08)
anim(S(31), S(36) - 0.08, V.wall_door(S(31) + 0.6, T('darwaaza', S(33))), y=160)
Bh(S(36), S(37) - 0.05, 'NEUROSCIENCE', size=210, color=G)
K(S(37), S(40) - 0.05, ['A NETWORK THAT', 'CONTROLS YOUR *BELIEFS*'], sizes=[80, 92], anim='rise')
K(S(40), S(51) - 0.05, ['TODAY: HOW IT WORKS', '+ HOW TO *REPROGRAM* IT'], sizes=[76, 92], anim='rise', stagger=1.4)

# ================= PART 1: DMN
chapter(S(51), 1, "YOUR BRAIN'S STORYTELLER")
card(S(51) + 2.4, S(61) - 0.08)
anim(S(51) + 2.4, S(61) - 0.08, V.dmn_brain(S(51) + 2.5, [S(52) + 0.2, S(52) + 0.6, S(52) + 1.0, S(52) + 1.4]), y=80)
S_.add({'type': 'chips', 't0': S(56) - 0.05, 't1': S(61) - 0.08, 'y': 760, 'panel': P, 'items': [
    {'t': S(56), 'text': 'Doing nothing'}, {'t': S(57), 'text': 'Daydreaming'}, {'t': S(58), 'text': 'Bored, *in the shower*'}]})
K(S(61), S(63) - 0.05, ['IT TELLS YOU', '*STORIES*'], sizes=[100, 140], anim='slam')
K(S(63), S(66) - 0.05, ['ABOUT', '*YOU*'], sizes=[100, 160], anim='slam')
card(S(66) - 0.05, S(71) - 0.08)
add({'type': 'chips', 't0': S(66), 't1': S(71) - 0.08, 'y': 220, 'items': [
    {'t': S(66) + 0.2, 'text': 'Who am I?'}, {'t': T('possible', S(67)), 'text': "What's *possible*?"}, {'t': T('future', S(67)), 'text': 'What will my *future* be?'}]})
Bh(S(71), S(74) - 0.05, '24x7 NARRATOR', size=200, color=GOLD)
K(S(74), S(76) - 0.05, ["WHAT'S DIFFERENT IN", '*BILLIONAIRES*'], sizes=[70, 110], anim='rise')
card(S(76) - 0.05, S(92) - 0.08)
add({'type': 'checklist', 't0': S(76), 't1': S(92) - 0.08, 'y': 150, 'title': 'What their DMN tells them', 'items': [
    {'t': S(76) + 0.4, 'text': '"You can do it"', 'mark': 'check'}, {'t': S(78), 'text': '"No limits"', 'mark': 'check'},
    {'t': S(79), 'text': '"This door will open"', 'mark': 'check'}, {'t': T('solution', S(84)), 'text': '*Solution*-based thinking', 'mark': 'check'},
    {'t': T('problem', S(84)), 'text': '~Problem-based thinking~', 'mark': 'x'}]})
Bh(S(92), S(96) - 0.05, 'BIOLOGICAL LAW', size=200, color=R); S_.fx('sub_drop', T('law', S(92)), -12)
card(S(96) - 0.05, S(98) - 0.08)
anim(S(96), S(98) - 0.08, V.filter_funnel(S(96), S(96) + 0.8), y=140)
K(S(98), S(106) - 0.05, ['"MY LIFE IS BAD"', '= BRAIN FINDS *MORE BAD*'], sizes=[80, 80], anim='rise', stagger=1.4)
K(S(106), S(108) - 0.05, ['"SEE? IT WENT WRONG AGAIN.', 'I *TOLD YOU*."'], sizes=[70, 90], font='serif', anim='rise')
K(S(108), S(118) - 0.05, ['THE BELIEF', 'GETS ~STRONGER~'], sizes=[90, 120], anim='slam')
card(S(118) - 0.05, S(136) - 0.08)
add({'type': 'chain', 't0': S(118), 't1': S(136) - 0.08, 'y': 150, 'title': 'Believe in opportunities', 'show': 4, 'items': [
    {'t': S(119), 'text': 'Brain searches for *opportunities*'}, {'t': S(120), 'text': '...and *good ideas*'},
    {'t': S(124), 'text': 'Sees what others ~miss~'}, {'t': T('opportunity', S(128)), 'text': '"Opportunity here, *opportunity there*"', 'st': 'yes', 'stc': 'green'},
    {'t': T('problems', S(131)), 'text': 'Not problems: *solutions*', 'st': 'yes', 'stc': 'green'}]})
K(S(136), T('random', S(138)) - 0.05, ['"SUDDENLY I MET SOMEONE."', '"SUDDENLY AN IDEA CAME."'], sizes=[64, 64], font='serif', anim='rise', stagger=1.6)
K(T('random', S(138)) - 0.03, S(139) - 0.05, ["IT'S NOT", '*RANDOM*'], sizes=[100, 150], anim='slam')
K(S(139), S(145) - 0.05, ['THEIR BELIEFS', '*TRAINED* THEIR BRAIN'], sizes=[90, 100], anim='rise')

# ================= PART 2: BELIEF DESIGN
chapter(S(145), 2, 'DESIGN YOUR BELIEFS')
K(S(145) + 2.4, S(146) - 0.05, ['CAN WE', '*CHANGE IT?*'], sizes=[100, 130], anim='rise')
Bh(S(146), S(153) - 0.05, '100%', size=260, color=G); S_.fx('hit_soft', S(146), -12)
card(S(153) - 0.05, S(162) - 0.08)
anim(S(153), S(162) - 0.08, V.neurons(S(153) + 0.2, [S(157), S(158) + 0.4], label='Repeat a belief, rewire the DMN'), y=150)
K(S(158), S(162) - 0.08, ['NEW NEURAL PATHWAYS'], x=490, y=820, align='center', sizes=[50], font='oswald', anim='rise', fit=880)
K(S(162), S(167) - 0.05, ['THE 4-STEP', '*FRAMEWORK*'], sizes=[100, 130], anim='slam')
K(S(164), S(167) - 0.05, ['MISS ONE STEP AND IT WON\'T WORK'], y=820, sizes=[48], font='oswald', anim='rise')
card(S(167) - 0.05, S(178) - 0.08)
add({'type': 'checklist', 't0': S(167), 't1': S(178) - 0.08, 'y': 150, 'title': 'Step 1: Identity', 'items': [
    {'t': S(167) + 1.5, 'text': '"I am the type of person who ___"', 'mark': 'check'}, {'t': S(171), 'text': '...puts my *health* first', 'mark': 'check'},
    {'t': S(172), 'text': '...puts my *family* first', 'mark': 'check'}, {'t': S(174), 'text': 'Because: *performance + happiness*', 'mark': 'check'}]})
card(S(178) - 0.05, S(187) - 0.08)
add({'type': 'checklist', 't0': S(178), 't1': S(187) - 0.08, 'y': 150, 'title': 'Step 2: Data', 'items': [
    {'t': S(179), 'text': 'Facts that *support* the belief', 'mark': 'check'}, {'t': S(182), 'text': 'Sleep: *better focus*', 'mark': 'check'},
    {'t': S(183), 'text': 'Exercise: *more energy*', 'mark': 'check'}, {'t': S(184), 'text': 'Write it *all down*', 'mark': 'check'}]})
card(S(187) - 0.05, S(198) - 0.08)
add({'type': 'checklist', 't0': S(187), 't1': S(198) - 0.08, 'y': 150, 'title': 'Step 3: Better future', 'items': [
    {'t': S(188), 'text': 'If it comes true, *what happens?*', 'mark': 'check'}, {'t': S(193), 'text': '*Smarter*', 'mark': 'check'},
    {'t': S(194), 'text': '*Healthier*, more focused', 'mark': 'check'}, {'t': S(195), 'text': 'My *best version*', 'mark': 'check'}]})
card(S(198) - 0.05, S(205) - 0.08)
add({'type': 'checklist', 't0': S(198), 't1': S(205) - 0.08, 'y': 150, 'title': 'Step 4: New habits', 'items': [
    {'t': S(199), 'text': 'Behaviour that *matches* the belief', 'mark': 'check'}, {'t': S(202), 'text': 'Phone away before *11 PM*', 'mark': 'check'},
    {'t': S(203), 'text': '*7-8 hours* of sleep', 'mark': 'check'}, {'t': S(204), 'text': 'Eat well, *exercise*', 'mark': 'check'}]})
card(S(205) - 0.05, S(210) - 0.08)
sent = ('<div style="font-family:\'Playfair Display\',serif;font-style:italic;font-weight:700;color:#fff;font-size:58px;line-height:1.25;padding:60px 40px">'
        f'<span data-t="{S(206):.2f}">"I am the type of person who</span> <span data-t="{S(206)+1.0:.2f}" style="color:#FFC53D">sleeps 7 hours every night,</span> '
        f'<span data-t="{S(207):.2f}">because I know it gives me</span> <span data-t="{S(209):.2f}" style="color:#FFC53D">my edge."</span></div>')
anim(S(205), S(210) - 0.08, sent, y=180)
K(S(210), S(212) - 0.05, ["YOU DON'T HAVE TO", 'BELIEVE IT *YET*'], sizes=[80, 100], anim='rise')
Bh(S(212), S(215) - 0.05, 'FAKE IT TILL YOU MAKE IT', size=150, color=GOLD)
B(44411, S(216), S(218) - 0.05, off=1.0)
K(S(215), S(218) - 0.05, ['SCIENCE-BACKED.', 'TRAIN YOUR BRAIN *LIKE A MUSCLE*'], sizes=[70, 76], anim='rise', stagger=1.2)
K(S(218), S(233) - 0.05, ['YOUR DMN', '*REWRITES* THE STORY'], sizes=[90, 100], anim='slam')
card(S(233) - 0.05, S(240) - 0.08)
add({'type': 'flow', 't0': S(233), 't1': S(240) - 0.08, 'y': 140, 'w': 900, 'h': 640, 'nodes': [
    {'t': S(233) + 0.4, 'x': 450, 'y': 60, 'text': 'Opportunities, ideas, *people*'}, {'t': S(235), 'x': 450, 'y': 215, 'text': 'Not *random*'},
    {'t': S(236), 'x': 450, 'y': 370, 'text': 'You changed your *search filter*'}, {'t': S(238), 'x': 450, 'y': 530, 'text': 'CHANGE BELIEFS, CHANGE LIFE', 'target': True}],
    'wires': [{'t': S(235) - 0.3, 'd': 'M 450 105 L 450 165'}, {'t': S(236) - 0.3, 'd': 'M 450 260 L 450 320'}, {'t': S(238) - 0.3, 'd': 'M 450 415 L 450 480'}]})

# ================= PART 3: IMPLEMENTATION INTENTIONS
chapter(S(240), 3, 'GOALS NEED A PLAN')
K(S(240) + 2.4, S(242) - 0.05, ['BELIEF: DONE.', 'NOW *IMPLEMENTATION*'], sizes=[80, 90], anim='rise')
K(S(242), S(244) - 0.05, ['GOAL = PRAYER.', 'PLAN = *POWER*.'], sizes=[110, 110], anim='slam', stagger=1.0)
K(S(244), S(252) - 0.05, ['EVEN I TRY TO', '*SLEEP EARLY*'], sizes=[80, 100], anim='rise')
S_.add({'type': 'badge', 't0': S(252), 't1': S(258) - 0.05, 'y': 140, 'text': 'Implementation intention', 'sub': 'Tested in *100+ studies*'})
K(S(252) + 1.2, S(258) - 0.05, ["A PRE-DECIDED 'WHEN X, THEN I DO Y' PLAN"], x=W // 2, y=860, align='center', sizes=[46], font='oswald', anim='rise', fit=1700)
card(S(258) - 0.05, S(270) - 0.08)
wt = ('<div style="font-family:Oswald,sans-serif;font-weight:700;color:#fff;font-size:72px;line-height:1.35;padding:40px 30px;text-transform:uppercase">'
      f'<div data-t="{S(258)+0.3:.2f}">WHEN <span style="color:#FFC53D;border-bottom:6px solid #FFC53D">&nbsp;&nbsp;&nbsp;&nbsp;___&nbsp;&nbsp;&nbsp;&nbsp;</span></div>'
      f'<div data-t="{S(259):.2f}">THEN I <span style="color:#37F59B;border-bottom:6px solid #37F59B">&nbsp;&nbsp;&nbsp;&nbsp;___&nbsp;&nbsp;&nbsp;&nbsp;</span></div>'
      f'<div data-t="{S(261):.2f}" style="font-size:48px;color:#FFC53D;margin-top:40px;font-family:Poppins;text-transform:none">When the alarm rings at 11 PM,</div>'
      f'<div data-t="{S(262):.2f}" style="font-size:48px;color:#37F59B;font-family:Poppins;text-transform:none">then: phone on the charger, into bed.</div></div>')
anim(S(258), S(270) - 0.08, wt, y=150)
card(S(270) - 0.05, S(284) - 0.08)
add({'type': 'chain', 't0': S(270), 't1': S(284) - 0.08, 'y': 150, 'title': 'See it like a movie', 'show': 4, 'items': [
    {'t': S(275), 'text': '*11 PM*, at home'}, {'t': S(276), 'text': 'Phone on the *charger*'}, {'t': S(278), 'text': 'Lie down in *bed*'},
    {'t': S(279), 'text': 'Review today, *plan tomorrow*'}, {'t': S(281), 'text': '*Specific.* Clear.', 'st': 'yes', 'stc': 'green'},
    {'t': S(283), 'text': 'That is why *it works*', 'st': 'yes', 'stc': 'green'}]})
card(S(284) - 0.05, S(306) - 0.08)
add({'type': 'chain', 't0': S(284), 't1': S(306) - 0.08, 'y': 150, 'title': 'Start small', 'show': 4, 'items': [
    {'t': S(287), 'text': 'Alarm at *11 PM*'}, {'t': S(290), 'text': 'Phone *aside*'}, {'t': S(294), 'text': "Write tomorrow's *plan*"},
    {'t': S(297), 'text': 'Brush your teeth'}, {'t': S(299), 'text': '*Eyes closed*, wind down'}, {'t': S(301), 'text': 'Small steps get *easy*', 'st': 'yes', 'stc': 'green'}]})

# ================= PART 4: THE BAD-HABIT LOOP
chapter(S(306), 4, 'THE BAD-HABIT LOOP')
K(S(306) + 2.4, S(309) - 0.05, ['BREAKING A HABIT', 'IS *HARDER*'], sizes=[90, 120], anim='slam')
K(S(309), S(313) - 0.05, ['SMOKING BECOMES', 'A *NEED*'], sizes=[90, 110], anim='rise')
K(S(313), S(316) - 0.05, ["LET'S UNDERSTAND", '*NEURAL NETWORKS*'], sizes=[76, 100], anim='rise')
card(S(316) - 0.05, S(325) - 0.08)
anim(S(316), S(325) - 0.08, V.highway([S(316) + 0.4, T('das', S(319)), T('sau', S(320)), T('hazaar', S(322))]), y=120)
K(S(323), S(325) - 0.08, ['HABITS AND ADDICTIONS SHARE THE SAME REWARD CIRCUITRY'], x=490, y=860, align='center', sizes=[34], font='oswald', anim='rise', fit=880)
card(S(325) - 0.05, S(346) - 0.08)
anim(S(325), S(346) - 0.08, V.neurons(S(325) + 0.3, [S(333), S(334) + 0.8], label='Learning to drive: neurons connect', labels=('Neuron', 'Neuron')), y=150)
K(S(334), S(346) - 0.08, ['NEURONS THAT FIRE TOGETHER, WIRE TOGETHER'], x=490, y=820, align='center', sizes=[40], font='oswald', anim='rise', fit=880)
K(S(346), S(349) - 0.05, ['NOW IT LIVES IN YOUR', '*SUBCONSCIOUS*'], sizes=[76, 110], anim='rise')
card(S(349) - 0.05, S(356) - 0.08)
add({'type': 'chips', 't0': S(349), 't1': S(356) - 0.08, 'y': 220, 'items': [
    {'t': S(350), 'text': 'Addiction = a behaviour you *repeat*'}, {'t': S(351), 'text': 'Exercise'}, {'t': S(354), 'text': 'Kindness'},
    {'t': T('scrolling', S(355)), 'text': 'Scrolling'}, {'t': T('smoking', S(355)), 'text': 'Smoking'}, {'t': T('mechanism', S(355)), 'text': '*Same mechanism*'}]})
K(S(356), S(367) - 0.05, ['THE', '*HABIT LOOP*'], sizes=[90, 150], anim='slam')
card(S(367) - 0.05, S(417) - 0.08)
anim(S(367), S(417) - 0.08, V.loop([('FEELING', '#FFFFFF', S(367) + 0.2), ('ESCAPE BEHAVIOUR', GOLD, S(375)), ('TEMPORARY RELIEF', G, S(400) + 0.8),
                                   ('BEHAVIOUR ENDS', '#9AA4B2', S(406)), ('STRESS + SHAME', R, S(407))], S(413),
                                  extra_feel=[('stress', T('stress', S(370))), ('boredom', T('bore', S(370))), ('overwhelm', S(371)), ('tiredness', S(372)), ('loneliness', S(374))],
                                  extra_beh=[('scrolling', T('scroll', S(381))), ('sweets', T('mithaai', S(381))), ('cigarettes', T('cigarette', S(381))), ('binge-watching', T('binge', S(381)))]), y=60)
K(S(417), S(427) - 0.05, ['EVERY LOOP MAKES THE', 'HIGHWAY *STRONGER*'], sizes=[76, 100], anim='rise')
B(44416, S(427), S(431) - 0.05, off=1.0)
K(S(427), S(435) - 0.05, ['GOOD HABITS', '*LOOP TOO*'], sizes=[100, 120], anim='rise')
K(S(431), S(435) - 0.05, ['GOOD LOOP OR BAD LOOP: YOUR CHOICE'], x=W // 2, y=860, align='center', sizes=[48], font='oswald', anim='rise', fit=1700)
K(S(435), S(436) - 0.05, ['HOW TO', '*BREAK IT*'], sizes=[100, 140], anim='slam')
card(S(436) - 0.05, S(454) - 0.08)
add({'type': 'checklist', 't0': S(436), 't1': S(454) - 0.08, 'y': 150, 'title': 'Step 1: Awareness', 'items': [
    {'t': S(436) + 0.5, 'text': 'Notice the *loop* running', 'mark': 'check'}, {'t': T('ruko', S(440)), 'text': 'About to scroll? *STOP*', 'mark': 'check'},
    {'t': T('cognitive', S(441)), 'text': 'Take a *cognitive pause*', 'mark': 'check'}, {'t': S(443), 'text': 'Ask: *why* do I want this?', 'mark': 'check'},
    {'t': S(447), 'text': 'Name the *feeling*', 'mark': 'check'}, {'t': S(450), 'text': 'Good for my *future*?', 'mark': 'check'}]})
card(S(454) - 0.05, S(472) - 0.08)
anim(S(454), S(472) - 0.08, V.ring(S(454) + 0.3, label='60 SEC', sub='Replace it: eyes closed, do nothing', t_breath=S(462), t_draw=T('60', S(458))), y=170)
K(S(454), S(472) - 0.08, ['STEP 2: REPLACEMENT BEHAVIOUR'], x=490, y=120, align='center', sizes=[44], font='oswald', anim='rise', fit=880)
K(T('dhyaan', S(464)) - 0.1, S(472) - 0.08, ['THIS IS MEDITATION'], x=490, y=860, align='center', sizes=[44], font='oswald', anim='rise', fit=880)
K(S(472), S(473) - 0.05, ['YOU START TO', '*RECOGNISE* YOUR LOOP'], sizes=[76, 96], anim='rise')
card(S(473) - 0.05, S(482) - 0.08)
add({'type': 'chain', 't0': S(473), 't1': S(482) - 0.08, 'y': 150, 'title': 'Step 3: Permission', 'show': 4, 'items': [
    {'t': S(473) + 0.5, 'text': '60-sec pause, *then decide*'}, {'t': S(476), 'text': '*No shame* either way', 'st': 'yes', 'stc': 'green'},
    {'t': S(478), 'text': '1st time: you still scroll'}, {'t': S(480), 'text': '2nd time: *maybe not*'}, {'t': S(481), 'text': '3rd time: *easy*', 'st': 'yes', 'stc': 'green'}]})
card(S(482) - 0.05, S(501) - 0.08)
anim(S(482), S(501) - 0.08, V.highway([S(482) + 0.3, T('dheere', S(483)), T('road', S(483)), T('highway', S(483))], names=('NEW PATH', 'WIDER', 'ROAD', 'HIGHWAY'), labels=('', '', '', '')), y=120)
K(S(482) + 0.5, S(501) - 0.08, ['THE OLD HIGHWAY WEAKENS. THE NEW ROAD GROWS.'], x=490, y=860, align='center', sizes=[38], font='oswald', anim='rise', fit=880)
K(S(501), S(504) - 0.05, ['YOUR BRAIN', '*CAN CHANGE*'], sizes=[100, 130], anim='slam')

# ================= PART 5: CREATIVITY
chapter(S(504), 5, 'BOREDOM = IDEAS')
K(S(504) + 2.4, S(508) - 0.05, ['"I\'M NOT', 'CREATIVE"'], sizes=[100, 120], font='serif', anim='rise')
K(S(508), S(509) - 0.05, ['NO BOREDOM', '= ~NO IDEAS~'], sizes=[110, 120], anim='slam')
card(S(509) - 0.05, S(523) - 0.08)
anim(S(509), S(523) - 0.08, V.dmn_brain(S(509) + 0.1, [S(511), S(511) + 0.4, S(513), S(513) + 0.4], label='The DMN switches on when you are idle', sub='Daydreaming. Mind-wandering. Boredom.'), y=80)
card(S(523) - 0.05, S(533) - 0.08)
anim(S(523), S(533) - 0.08, V.tilt_seesaw(S(523) + 0.2, S(528), S(529) + 1.0), y=150)
K(S(523) + 0.3, S(533) - 0.08, ['CEN = CENTRAL EXECUTIVE NETWORK'], x=490, y=860, align='center', sizes=[40], font='oswald', anim='rise', fit=880)
K(S(533), S(535) - 0.05, ['SHOWER THOUGHTS', '= *SCIENCE*'], sizes=[100, 120], anim='slam')
card(S(535) - 0.05, S(559) - 0.08)
add({'type': 'chain', 't0': S(535), 't1': S(559) - 0.08, 'y': 150, 'title': 'How a new idea appears', 'show': 4, 'items': [
    {'t': S(535) + 0.4, 'text': '*Load* the problem'}, {'t': S(538), 'text': 'No solution yet', 'st': 'no', 'stc': 'red'},
    {'t': S(539), 'text': '*Walk away*: walk, run, shower, cook'}, {'t': S(545), 'text': 'Something on *autopilot*'},
    {'t': S(550), 'text': '*New variables*: water, sounds, place'}, {'t': S(556), 'text': 'Networks *rearrange*'},
    {'t': S(557), 'text': 'IDEA', 'st': 'yes', 'stc': 'green'}]})
K(S(559), S(562) - 0.05, ['NOT RANDOM.', '*PREDICTABLE SCIENCE.*'], sizes=[100, 90], anim='slam', stagger=0.9)
S_.add({'type': 'badge', 't0': S(562), 't1': S(574) - 0.05, 'y': 140, 'text': 'Think time', 'sub': '15-20 min a day. *No phone. No scroll.*'})

# ================= PART 6: 5 AM MYTH
chapter(S(574), 6, 'THE 5 AM CLUB MYTH')
card(S(575) - 0.05, S(580) - 0.08)
add({'type': 'checklist', 't0': S(575), 't1': S(580) - 0.08, 'y': 150, 'title': 'The "success routine"', 'items': [
    {'t': S(575) + 0.1, 'text': 'Wake up at *5 AM*', 'mark': 'check'}, {'t': S(576), 'text': 'Cold plunge', 'mark': 'check'},
    {'t': T('lemon', S(578)), 'text': 'Lemon water', 'mark': 'check'}, {'t': T('pushups', S(578)), 'text': 'Push-ups', 'mark': 'check'},
    {'t': T('journaling', S(578)), 'text': 'Journaling', 'mark': 'check'}, {'t': S(579), 'text': '~= Success?~', 'mark': 'x'}]})
K(S(580), S(582) - 0.05, ['I WAKE UP AT *8-9 AM*.', 'I WORK TILL *1-2 AM*.'], sizes=[84, 84], anim='rise', stagger=1.4)
KC(S(582), S(593) - 0.05, ['RIGHT NOW:', '*11:43 PM*'], y=140, sizes=[60, 150], anim='slam', stagger=1.0)
K(S(593), S(602) - 0.05, ['SOUNDS GOOD.', 'NOT FOR *EVERYONE*.'], sizes=[100, 100], anim='rise', stagger=1.4)
K(S(602), T('circadian', S(603)) - 0.05, ['2017 NOBEL PRIZE:', 'HOW THE *BODY CLOCK* WORKS'], sizes=[80, 84], anim='rise', stagger=1.0)
K(T('circadian', S(603)) - 0.03, S(607) - 0.05, ["BUT NOT EVERYONE'S CLOCK", 'IS SET THE *SAME*'], sizes=[70, 90], anim='rise', stagger=1.0)
card(S(607) - 0.05, S(629) - 0.08)
anim(S(607), S(629) - 0.08, V.chrono(S(607) + 0.3, S(613), S(618)), y=110)
K(S(621), S(629) - 0.08, ['FORCING 5 AM = WASTING YOUR PEAK HOURS'], x=490, y=860, align='center', sizes=[40], font='oswald', anim='rise', fit=880)
card(S(629) - 0.05, S(651) - 0.08)
cols = [('AM-SHIFTED', GOLD, S(633), ['Morning: *focus work*', 'Evening: admin']), ('BIPHASIC', G, S(635) + 2.0, ['Morning: *focus*', 'Afternoon: break, exercise', 'Evening: *2nd session*']),
        ('PM-SHIFTED', R, S(643), ['Morning: creative, reading', 'Night: *deep work*'])]
def col_html(name, c, t, items):
    import re
    bold = lambda x: re.sub(r'[*](.*?)[*]', lambda m: f'<b style="color:{c}">{m.group(1)}</b>', x)
    li = ''.join(f'<div data-t="{t+0.4+0.5*i:.2f}" style="margin:14px 0">{bold(x)}</div>' for i, x in enumerate(items))
    return (f'<div data-t="{t:.2f}" style="flex:1;background:rgba(12,14,20,.86);border:2px solid {c};border-radius:24px;padding:26px 20px;margin:0 8px;min-height:520px">'
            f'<div style="font-family:Oswald;font-weight:700;font-size:38px;color:{c};letter-spacing:1px">{name}</div>'
            f'<div style="font-family:Poppins;font-weight:600;font-size:28px;color:#fff;line-height:1.3">{li}</div></div>')
anim(S(629), S(651) - 0.08, '<div style="display:flex;padding:0 10px">' + ''.join(col_html(*c) for c in cols) + '</div>', y=160)
K(S(629), S(651) - 0.08, ['KNOW YOUR TYPE. DESIGN YOUR DAY.'], x=490, y=110, align='center', sizes=[44], font='oswald', anim='rise', fit=880)
K(S(651), S(655) - 0.05, ["I'M", '*CHRONOTYPE 3*'], sizes=[100, 130], anim='slam')
K(S(655), S(658) - 0.05, ['2 AM TO 8 AM.', '*7 HOURS.* NO PROBLEM.'], sizes=[90, 84], anim='rise', stagger=1.0)
K(S(658), S(660) - 0.05, ['THE 5 AM CLUB:', 'SOUNDS SEXY, ~MAY NOT WORK~'], sizes=[80, 76], anim='slam', stagger=1.2)
K(S(660), S(663) - 0.05, ['7 HOURS OF GOOD SLEEP FIRST.', 'EVERYTHING ELSE IS *SECONDARY*'], sizes=[66, 70], anim='rise', stagger=1.4)

# ================= PART 7: BURNOUT
chapter(S(663), 7, 'BURNOUT + THE 3M FRAMEWORK')
K(S(663) + 2.4, S(665) - 0.05, ['EVERY 25-YEAR-OLD:', '*"I\'M BURNED OUT"*'], sizes=[76, 92], anim='rise')
card(S(665) - 0.05, S(681) - 0.08)
anim(S(665), S(681) - 0.08, V.stress_curve(S(671), S(679), t0=S(665) + 0.3), y=140)
K(S(665), S(671) - 0.08, ['STRESS IS NORMAL. CORTISOL HELPS YOU FOCUS.'], x=490, y=860, align='center', sizes=[38], font='oswald', anim='rise', fit=880)
K(S(681), S(682) - 0.05, ['DAILY STRESS', '~IS NOT~ BURNOUT'], sizes=[100, 110], anim='slam')
Bh(S(682), S(684) - 0.05, '3M FRAMEWORK', size=220, color=GOLD)
card(S(684) - 0.05, S(706) - 0.08)
add({'type': 'checklist', 't0': S(684), 't1': S(706) - 0.08, 'y': 150, 'title': 'M1: Micro breaks (daily)', 'items': [
    {'t': S(685), 'text': '*10-15 min*, every day', 'mark': 'check'}, {'t': S(686), 'text': 'Something *challenging*', 'mark': 'check'},
    {'t': S(687), 'text': 'New recipe, an instrument', 'mark': 'check'}, {'t': S(689), 'text': 'A *new route* for your walk', 'mark': 'check'},
    {'t': S(691), 'text': '~No phone~', 'mark': 'x'}, {'t': S(693), 'text': '*Complete psychological detachment*', 'mark': 'check'}]})
K(S(693), S(706) - 0.08, ['PSYCHOLOGICAL DETACHMENT = MENTALLY SWITCHING OFF FROM WORK'], x=490, y=880, align='center', sizes=[30], font='oswald', anim='rise', fit=880)
card(S(706) - 0.05, S(725) - 0.08)
add({'type': 'checklist', 't0': S(706), 't1': S(725) - 0.08, 'y': 150, 'title': 'M2: Meso breaks (weekly)', 'items': [
    {'t': S(709), 'text': '*2-4 hours*, every week', 'mark': 'check'}, {'t': S(710), 'text': 'A hobby: painting, *cricket*', 'mark': 'check'},
    {'t': S(713), 'text': 'Learn something *new*', 'mark': 'check'}, {'t': S(717), 'text': '*Forget your worries*', 'mark': 'check'},
    {'t': S(722), 'text': 'Your brain *resets*', 'mark': 'check'}]})
card(S(725) - 0.05, S(736) - 0.08)
add({'type': 'checklist', 't0': S(725), 't1': S(736) - 0.08, 'y': 150, 'title': 'M3: Macro breaks (monthly)', 'items': [
    {'t': S(728), 'text': '*Half a day* to a full day', 'mark': 'check'}, {'t': S(729), 'text': '*Completely disconnected*', 'mark': 'check'},
    {'t': S(733), 'text': '~No work, no email~', 'mark': 'x'}, {'t': S(734), 'text': 'Do *what you love*', 'mark': 'check'}]})
K(S(736), S(740) - 0.05, ['THE ONE CONDITION:', '*COMPLETE DETACHMENT*'], sizes=[76, 96], anim='rise', stagger=1.0)
B(4911, S(740), S(744) - 0.05, off=1.0)
K(S(740), S(744) - 0.05, ['SCROLLING', '~IS NOT A BREAK~'], sizes=[110, 100], anim='slam')
K(S(744), S(749) - 0.05, ['IT TIRES YOUR', 'BRAIN *MORE*'], sizes=[100, 120], anim='rise')
K(S(749), S(757) - 0.05, ['WATCH A *GOOD MOVIE*', 'TRAVEL. LAUGH.'], sizes=[90, 90], anim='rise', stagger=1.4)

# ================= RECAP + CLOSE
chapter(S(757), 8, 'WHAT WE LEARNED')
card(S(758) - 0.05, S(785) - 0.08)
add({'type': 'checklist', 't0': S(758), 't1': S(785) - 0.08, 'y': 120, 'title': 'Your brain\'s blueprint', 'items': [
    {'t': S(758), 'text': '1. Belief, not luck or talent', 'mark': 'check'}, {'t': S(765), 'text': '2. *Design* your beliefs: 4 steps', 'mark': 'check'},
    {'t': S(767), 'text': '3. Goals are cute, *plans work*', 'mark': 'check'}, {'t': T('buri', S(770)), 'text': '4. Break the loop: *60-sec pause*', 'mark': 'check'},
    {'t': S(773), 'text': '5. Need ideas? *Get bored*', 'mark': 'check'}, {'t': S(778), 'text': '6. Know your *chronotype*', 'mark': 'check'},
    {'t': S(781), 'text': '7. Burnout? *Micro, meso, macro*', 'mark': 'check'}]})
Bh(S(785), S(787) - 0.05, 'BIOLOGICAL LAWS', size=210, color=G)
K(S(787), S(790) - 0.05, ['IGNORE THEM: ~SUFFER~', 'FOLLOW THEM: *SUPERHUMAN*'], sizes=[80, 80], anim='rise', stagger=1.6)
K(S(790), S(796) - 0.05, ['FOCUS MACHINE. STORY MACHINE.', '*IDEA MACHINE.*'], sizes=[70, 100], anim='rise', stagger=1.4)
S_.add({'type': 'badge', 't0': S(796), 't1': S(813) - 0.05, 'y': 140, 'text': 'Subscribe', 'sub': 'Share it with your *friends, family and kids*'})
cta = S(813)
S_.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 520, 'kicker': 'My job was to bring you the science', 'title': 'Same science.<br>*Different language.*', 'sub': 'The decision is yours.', 'button': 'SUBSCRIBE', 'hideCaps': True})
S_.punch(cta, 0.05, 99)

# ---------------- camera, captions, music map
S_.alt_zoom([1.0, 1.15, 1.06, 1.22]); S_.cam['faceY'] = 0.42; S_.cam['grain'] = 4; S_.cam['card'] = CARD
caps = S_.captions(max_words=4, max_chars=26, hl_pats=[r'belief', r'beliefs', r'billionaires', r'dhoni', r'legend', r'neuroscience', r'network', r'dmn', r'story',
    r'narrator', r'limit', r'solution', r'biological', r'law', r'opportunities', r'opportunity', r'random', r'100%', r'pathways', r'framework', r'identity', r'data',
    r'future', r'habits?', r'edge', r'fake', r'filter', r'implementation', r'intention', r'studies', r'specific', r'small', r'highway', r'addiction', r'neurons?',
    r'subconscious', r'loop', r'feeling', r'shame', r'awareness', r'pause', r'cognitive', r'60', r'dhyaan', r'permission', r'ideas?', r'bore', r'bored', r'cen',
    r'shower', r'variables', r'autopilot', r'myth', r'nobel', r'chronotype', r'circadian', r'peak', r'neend', r'burnout', r'stress', r'cortisol', r'micro', r'meso',
    r'macro', r'detachment', r'scrolling', r'movies', r'superhuman', r'machine', r'science', r'subscribe'])
S_.save(caps, cta_t=cta, cap_y=900, hold=1.0, extra={'capScale': 0.72, 'vigInCompose': True}, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
mus = {'dur': D + 1.0, 'sections': [], 'drops': [S(11), S(92), S(146), T('porn', S(658)), S(740)], 'hits': []}
bounds = [(0, 'curiosity'), (S(51), 'teaching'), (S(145), 'uplift'), (S(240), 'focus'), (S(306), 'dark'), (S(435), 'hope'), (S(504), 'light'),
          (S(574), 'energy'), (S(663), 'calm'), (S(757), 'inspire')]
for (t0, m), (t1, _) in zip(bounds, bounds[1:] + [(D + 1.0, None)]): mus['sections'].append({'t0': t0, 't1': t1, 'mood': m})
json.dump(mus, open(f'{sys.argv[1]}/v51_music.json', 'w'), indent=1)
