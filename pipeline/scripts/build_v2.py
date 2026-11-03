import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v2'); T, TE = S.T, S.TE
D = S.tl['dur']

# HOOK — title over the ceiling, then the cost chips
t_k = T('kilos')
S.add({'type': 'title', 't0': 0.05, 't1': T('25') - 0.05, 'y': 150, 'lines': ['I wish I knew this', '*10 years* ago'], 'sizes': [80, 112], 'hideCaps': True})
S.punch(T('10'), 0.08, 1.2)
S.add({'type': 'chips', 't0': T('25') - 0.1, 't1': T('heres') - 0.1, 'y': 120, 'items': [
    {'t': T('25'), 'icon': '⚖️', 'text': '*25 KG* extra'},
    {'t': T('thousands'), 'icon': '💸', 'text': '*₹ thousands* wasted'},
    {'t': T('frustration'), 'icon': '⏳', 'text': '*Years* of frustration'}]})
S.punch(T('nobody'), 0.10, 1.0)

# NOTHING WORKS ALONE — checklist in card layout
c0, c1 = T('diet') - 0.2, TE('work', T('meditation')) + 0.35
S.card(c0, c1)
S.add({'type': 'checklist', 't0': c0, 't1': c1, 'y': 170, 'title': 'Nobody told me this', 'items': [
    {'t': T('diet'), 'text': 'Diet <span>alone</span>', 'mark': 'x'},
    {'t': T('exercise'), 'text': 'Exercise <span>alone</span>', 'mark': 'x'},
    {'t': T('fasting'), 'text': 'Fasting <span>alone</span>', 'mark': 'x'},
    {'t': T('meditation'), 'text': 'Meditation <span>alone</span>', 'mark': 'x'}]})

# TURN
t_ch = T('changes')
S.events.append({'type': 'leak', 't0': T('but') - 0.1, 'd': 0.9}); S.fx('whoosh', T('but') - 0.25, -15)
S.add({'type': 'slam', 't0': t_ch, 't1': TE('everything') + 0.35, 'y': 230, 'text': 'Changes<br>*everything*', 'size': 120})
S.punch(t_ch, 0.12, 0.9)

# COMBINE ALL FOUR -> converge flowchart, then body markers, all in card layout
f0 = T('when') - 0.1; f1 = TE('deepens') + 0.4
S.card(f0, f1)
fx = [(230, 110), (770, 110), (230, 340), (770, 340)]
nd = [('🍽️', 'Diet'), ('🏋️', 'Exercise'), ('⏱️', 'Fasting'), ('🧘', 'Mind')]
t_all = T('all'); t_seq = T('sequence'); t_body = T('body', T('sequence'))
nodes = [{'t': t_all + 0.12 * i, 'x': x, 'y': y, 'icon': ic, 'text': tx} for i, ((x, y), (ic, tx)) in enumerate(zip(fx, nd))]
nodes.append({'t': t_seq, 'x': 500, 'y': 225, 'text': 'Right *sequence*', 'icon': '⚡'})
nodes.append({'t': t_body, 'x': 500, 'y': 600, 'text': 'Body responds<br>differently', 'target': True})
def wire(x, y):
    sx = 1 if x < 500 else -1; ey = 155 if y < 225 else 295
    return f'M {x} {ey} C {x} {225}, {x + sx*60} 225, {500 - sx*175} 225'
wires = [{'t': t_seq - 0.4, 'd': wire(x, y)} for x, y in fx] + [{'t': t_body - 0.35, 'd': 'M 500 270 L 500 520'}]
S.add({'type': 'flow', 't0': f0, 't1': T('insulin') - 0.05, 'y': 140, 'w': 1000, 'h': 720, 'nodes': nodes, 'wires': wires})
S.add({'type': 'checklist', 't0': T('insulin') - 0.05, 't1': f1, 'y': 170, 'title': 'What happens inside', 'items': [
    {'t': T('insulin'), 'text': 'Insulin <span>resets</span>', 'mark': 'check'},
    {'t': T('inflammation'), 'text': 'Inflammation <span>drops</span>', 'mark': 'check'},
    {'t': T('cortisol'), 'text': 'Cortisol <span>normalizes</span>', 'mark': 'check'},
    {'t': T('sleep'), 'text': 'Sleep <span>deepens</span>', 'mark': 'check'}]})

# FAT BURNS / BIOLOGY
S.add({'type': 'title', 't0': T('fat') - 0.05, 't1': TE('trying') + 0.2, 'y': 170, 'lines': ['*Fat burns* 🔥', 'without even trying'], 'sizes': [118, 64]})
S.punch(T('fat'), 0.08, 2.5)
S.add({'type': 'title', 't0': T('not', T('trying')) - 0.05, 't1': T('biology') - 0.08, 'y': 210, 'lines': ['Not ~motivation~'], 'sizes': [100]})
S.add({'type': 'slam', 't0': T('biology'), 't1': TE('biology') + 0.55, 'y': 200, 'text': '*Biology* 🧬', 'size': 150})
S.punch(T('biology'), 0.14, 0.7)

# RESULTS — card layout: weight counter, then BP before/after
r0 = T('i', T('biology')) - 0.1; r1 = TE('120/80') + 0.9
S.card(r0, r1)
S.add({'type': 'stat', 't0': T('110') - 0.25, 't1': T('my', T('110')) - 0.05, 'y': 250, 'kicker': 'My transformation', 'fromText': '110 KG',
       'from': 110, 'to': 85, 'unit': 'KG', 'label': 'Today', 'pill': '▼ 25 KG DOWN', 'dir': 'down', 'count': 1.4})
S.add({'type': 'compare', 't0': T('my', T('110')) - 0.05, 't1': r1, 'y': 170, 'title': "My wife's blood pressure", 'max': 170, 'items': [
    {'t': T('170/110'), 'label': 'Before', 'text': '170/110', 'value': 170, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('drops', T('170/110')), 'label': 'Now', 'text': '120/80', 'value': 120, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
S.events[-1]['items'][0]['unit'] = ''
S.events[-1]['items'][1]['unit'] = ''

# SAME PROTOCOL
S.add({'type': 'chips', 't0': T('same') - 0.1, 't1': TE('easily') + 0.3, 'y': 120, 'items': [
    {'t': T('same'), 'icon': '📋', 'text': 'Same *protocol*'},
    {'t': T('two'), 'icon': '👫', 'text': 'Two *bodies*'},
    {'t': T('both'), 'icon': '✅', 'text': 'Both *transformed*'}]})
S.punch(T('both'), 0.10, 1.6)

# WEBINAR
w0 = T('teaching') - 0.2
S.add({'type': 'badge', 't0': T('live') - 0.1, 't1': T('dont', T('live')) - 0.05, 'y': 190, 'text': 'Live webinar', 'sub': 'The full system · *step by step*'})
S.add({'type': 'title', 't0': w0, 't1': T('live') - 0.12, 'y': 180, 'lines': ['The *entire system*', 'step by step'], 'sizes': [92, 70]})
S.add({'type': 'title', 't0': T('dont', T('live')) - 0.05, 't1': TE('did') + 0.1, 'y': 180, 'lines': ["Don't waste", '*10 years* like I did'], 'sizes': [86, 76]})

# CTA
cta = T('dont', TE('did')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 1, 'y': 1040, 'kicker': '🔴 Live webinar', 'title': "Don't wait<br>another *decade*",
       'sub': 'See you in the webinar', 'button': 'CLICK THE LINK BELOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)

S.alt_zoom([1.0, 1.17])
caps = S.captions(hl_pats=[r'diet', r'exercise', r'fasting', r'meditation', r'everything', r'insulin', r'inflammation', r'cortisol',
                           r'sleep', r'fat', r'biology', r'webinar', r'system', r'decade', r'kgs?', r'kilos', r'protocol', r'transformed', r'live'])
S.save(caps, cta_t=cta)

# ===== stock b-roll =====
B = S.broll
B(18263, T('thousands'), T('and', T('rupees')) - 0.05, off=1.0)
B(39854, T('years', T('rupees')) - 0.05, T('heres') - 0.05, off=1.0)
B(40521, T('diet'), T('exercise') - 0.05)
B(52080, T('exercise'), T('fasting') - 0.05, off=4.0)
B(28894, T('fasting'), T('even') - 0.05, off=2.0)
B(32631, T('even'), c1 - 0.05, off=1.0)
B(4733, T('insulin'), T('inflammation') - 0.05, off=1.0)
B(4719, T('inflammation'), T('cortisol') - 0.05, off=1.0)
B(43798, T('cortisol'), T('sleep') - 0.05, off=1.0)
B(42896, T('sleep'), f1 - 0.05, off=1.0)
B(722, T('fat') - 0.05, T('and', T('trying')) - 0.05, off=4.0)
B(4773, T('biology') - 0.1, TE('biology') + 0.45, off=2.0)
B(44438, r1 + 0.3, TE('easily') + 0.2, off=0.5)
B(10446, T('teaching') - 0.1, T('live') - 0.12, off=1.0)
B(28890, T('waste'), T('dont', TE('did')) - 0.05, off=1.0)
S.save(caps, cta_t=cta)
