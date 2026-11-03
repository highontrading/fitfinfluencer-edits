import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v4'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('willpower') - 0.05, 'y': 140, 'kicker': 'Weight loss', 'lines': ['The biggest', '*misconception*'], 'sizes': [84, 112], 'hideCaps': True})
S.add({'type': 'title', 't0': T('willpower'), 't1': T('its', T('not')) - 0.1, 'y': 170, 'lines': ['It\'s ~willpower~?'], 'sizes': [104]})
S.punch(T('not'), 0.10, 0.6)
S.add({'type': 'slam', 't0': T('biology') - 0.05, 't1': T('when') - 0.1, 'y': 200, 'text': '*Biology* 🧬', 'size': 150, 'sub': "It's not willpower"})
S.punch(T('biology'), 0.14, 0.9)
# insulin lock — card + flow
i0 = T('when') - 0.1; i1 = TE('it', T('unlocks')) + 0.25
S.card(i0, i1)
nodes = [{'t': T('insulin'), 'x': 500, 'y': 70, 'icon': '📈', 'text': 'Insulin chronically *high*'},
         {'t': T('locked'), 'x': 500, 'y': 290, 'icon': '🔒', 'text': 'Fat locked away'},
         {'t': T('no', T('locked')), 'x': 500, 'y': 510, 'icon': '💪', 'text': 'Willpower ~can\'t unlock~', 'target': True}]
wires = [{'t': T('cant') - 0.3, 'd': 'M 500 120 L 500 240'}, {'t': T('no', T('locked')) - 0.3, 'd': 'M 500 340 L 500 460'}]
S.add({'type': 'flow', 't0': i0, 't1': i1, 'y': 160, 'w': 1000, 'h': 640, 'nodes': nodes, 'wires': wires})
# cortisol -> belly fat
c0 = T('when', i1 - 0.5) - 0.1; c1 = TE('response') + 0.25
S.card(c0, c1)
n2 = [{'t': T('stress'), 'x': 260, 'y': 70, 'icon': '😫', 'text': 'Stress'},
      {'t': T('sleep'), 'x': 740, 'y': 70, 'icon': '😴', 'text': 'Bad sleep'},
      {'t': T('cortisol') + 0.4, 'x': 500, 'y': 290, 'icon': '⚠️', 'text': 'Cortisol *high*'},
      {'t': T('belly'), 'x': 500, 'y': 510, 'icon': '🛡️', 'text': 'Belly fat stored', 'sub': 'Survival response', 'target': True}]
w2 = [{'t': T('sleep') + 0.1, 'd': 'M 260 120 C 260 200, 400 240, 420 245'}, {'t': T('sleep') + 0.1, 'd': 'M 740 120 C 740 200, 600 240, 580 245'},
      {'t': T('belly') - 0.35, 'd': 'M 500 340 L 500 440'}]
S.add({'type': 'flow', 't0': c0, 't1': c1, 'y': 160, 'w': 1000, 'h': 640, 'nodes': n2, 'wires': w2})
# not weak
S.add({'type': 'title', 't0': T('you') - 0.05, 't1': T('your', T('weak')) - 0.08, 'y': 170, 'lines': ['You are', '*not weak*'], 'sizes': [84, 120]})
S.add({'type': 'slam', 't0': T('your', T('weak')), 't1': TE('broken') + 0.3, 'y': 200, 'text': 'System = ~broken~', 'size': 100})
# 4 systems grid
g0 = T('and', TE('broken')) - 0.1; g1 = TE('four', T('meditation')) + 0.3
S.card(g0, g1)
S.add({'type': 'title', 't0': g0, 't1': T('fasting') - 0.05, 'y': 260, 'kicker': 'My protocol attacks', 'lines': ['All *4 systems*', 'simultaneously'], 'sizes': [104, 70]})
grid = [(260, 120), (740, 120), (260, 400), (740, 400)]
gn = [{'t': T(k), 'x': x, 'y': y, 'num': i + 1, 'text': tx} for i, ((x, y), (k, tx)) in enumerate(zip(grid, [('fasting', 'Fasting'), ('diet', 'Diet'), ('exercise', 'Exercise'), ('meditation', 'Meditation')]))]
S.add({'type': 'flow', 't0': T('fasting') - 0.1, 't1': g1, 'y': 170, 'w': 1000, 'h': 520, 'nodes': gn, 'wires': []})
S.fx('ding', T('all', T('meditation')), -16)
# results
r0 = T('i', T('four', T('meditation'))) - 0.1; r1 = TE('only') + 0.3
S.card(r0, r1)
S.add({'type': 'stat', 't0': T('110') - 0.25, 't1': T('i', T('days')) - 0.05, 'y': 230, 'kicker': 'In just 45 days', 'fromText': '110 KG', 'from': 110, 'to': 85, 'unit': 'KG', 'label': 'Today', 'pill': '▼ 25 KG', 'dir': 'down', 'count': 1.3})
S.add({'type': 'stat', 't0': T('i', T('days')) - 0.05, 't1': r1, 'y': 230, 'kicker': 'Last 30 days', 'from': 0, 'to': 10, 'unit': '%', 'label': 'Body fat reduced', 'pill': '🔥 Pure fat loss', 'dir': 'down', 'count': 1.1})
# webinar + CTA
S.add({'type': 'badge', 't0': T('teach') - 0.2, 't1': T('stop') - 0.1, 'y': 200, 'text': 'Live webinar', 'sub': 'The *entire system*'})
cta = T('stop') - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 1000, 'kicker': '🔴 Live webinar', 'title': 'Stop fighting biology.<br>Start *working with it*', 'sub': 'See you in the webinar', 'button': 'JOIN THE LIVE WEBINAR', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'weight', r'loss', r'willpower', r'biology', r'insulin', r'fat', r'cortisol', r'stress', r'sleep', r'belly', r'weak', r'broken',
                           r'protocol', r'fasting', r'diet', r'exercise', r'meditation', r'kgs', r'webinar', r'system', r'survival'])

B = S.broll
B(4701, T('willpower'), T('but') - 0.05, off=1.5)
B(4733, T('biology') - 0.05, T('when') - 0.1, off=1.0)
B(3533, T('insulin'), T('your', T('high')) - 0.05, off=1.0)
B(25592, T('stress'), T('sleep') - 0.05, off=1.5)
B(51405, T('sleep'), T('your', T('sleep')) - 0.05, off=2.0)
B(372, T('belly') - 0.3, c1 - 0.1, off=1.0)
B(28886, T('fasting'), T('diet') - 0.05)
B(40531, T('diet'), T('exercise') - 0.05)
B(42898, T('exercise'), T('meditation') - 0.05, off=1.0)
B(43786, T('meditation'), g1 - 0.1, off=1.0)
B(44432, T('i', T('days')) - 0.05, r1 - 0.1, off=1.0)
B(4834, T('teach') - 0.2, T('stop') - 0.1, off=1.0)
S.save(caps, cta_t=cta, hold=1.2)
