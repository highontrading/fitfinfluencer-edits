import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v6'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('i') - 0.05, 'y': 140, 'lines': ['No *time*', 'to get healthy?'], 'sizes': [118, 74], 'hideCaps': True})
b0 = T('i') - 0.1; b1 = TE('this', T('like')) + 0.2
S.card(b0, b1)
S.add({'type': 'chips', 't0': b0, 't1': b1, 'y': 150, 'items': [
    {'t': T('construction'), 'icon': '🏗️', 'text': 'Built a *construction company*'},
    {'t': T('trucks'), 'icon': '🚛', 'text': '*7 years* in trucking'},
    {'t': T('upsc'), 'icon': '📚', 'text': 'Failed *UPSC* multiple times'},
    {'t': T('family'), 'icon': '👨‍👩‍👧', 'text': 'A *family* to run'},
    {'t': T('110'), 'icon': '⚖️', 'text': '*110 KG*'}]})
S.add({'type': 'title', 't0': T('and', b1 - 0.4) - 0.05, 't1': T('and', T('looking')) - 0.05, 'y': 170, 'lines': ['Still found', 'the *time*'], 'sizes': [84, 120]})
S.add({'type': 'title', 't0': T('and', T('looking')), 't1': TE('time', T('fits')) + 0.2, 'y': 170, 'kicker': 'Stopped looking for time', 'lines': ['Built a *system*', 'that fits my time'], 'sizes': [100, 64]})
S.punch(T('system'), 0.10, 1.2)
S.add({'type': 'title', 't0': T('this', T('fits')) - 0.05, 't1': T('it', T('day')) - 0.08, 'y': 190, 'lines': ['~3 hours a day~'], 'sizes': [110]})
p0 = T('it', T('day')) - 0.1; p1 = TE('counting') + 0.25
S.card(p0, p1)
S.add({'type': 'checklist', 't0': p0, 't1': p1, 'y': 170, 'title': 'It only asks for', 'items': [
    {'t': T('30'), 'text': '30–40 min <span>training</span>', 'mark': 'check'},
    {'t': T('structured'), 'text': 'Structured <span>eating window</span>', 'mark': 'check'},
    {'t': T('5minute'), 'text': '5-min <span>breathwork</span>', 'mark': 'check'},
    {'t': T('10000'), 'text': '10,000 <span>steps</span>', 'mark': 'check'}]})
w0 = T('i', T('counting')) - 0.1; w1 = TE('twice') + 0.3
S.card(w0, w1)
S.add({'type': 'stat', 't0': w0, 't1': w1, 'y': 230, 'kicker': 'My water fast', 'from': 0, 'to': 72, 'unit': 'HRS', 'label': '20,000 steps / day', 'pill': '🏋️ Gym twice a day', 'dir': 'down', 'count': 1.3})
S.add({'type': 'title', 't0': T('time', w1 - 0.3) - 0.05, 't1': T('system', T('problem')) - 0.08, 'y': 190, 'lines': ['Time wasn\'t', 'the ~problem~'], 'sizes': [90, 110]})
S.add({'type': 'slam', 't0': T('system', T('problem')), 't1': TE('was', T('problem')) + 0.4, 'y': 200, 'text': '*System* was', 'size': 140})
S.punch(T('system', T('problem')), 0.14, 0.8)
S.add({'type': 'badge', 't0': T('show') - 0.2, 't1': T('you', T('webinar')) - 0.1, 'y': 200, 'text': 'Live webinar', 'sub': 'Built around *your schedule*'})
cta = T('you', T('webinar')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 1000, 'kicker': '🔴 Live webinar', 'title': 'You have time.<br>You need a *system*', 'sub': 'See you in the webinar', 'button': 'JOIN THE LIVE WEBINAR', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'time', r'healthy', r'construction', r'company', r'trucks', r'upsc', r'family', r'kgs', r'fat', r'system', r'protocol', r'training',
                           r'eating', r'breathwork', r'steps', r'water', r'fast', r'gym', r'webinar', r'schedule'])

B = S.broll
B(1755, T('you') - 0.05, T('i') - 0.08, off=2.0)
B(4010, T('construction') - 0.1, T('failed') - 0.05, off=1.0)
B(28321, T('failed'), T('had') - 0.05, off=2.0)
B(39767, T('family') - 0.2, T('and', T('family')) - 0.05, off=1.0)
B(28890, T('looking'), T('and', T('looking')) - 0.05, off=1.0)
B(1439, T('started'), TE('time', T('fits')) + 0.15, off=1.0)
B(52080, T('30'), T('a', T('training')) - 0.05, off=4.0)
B(3795, T('structured'), T('5minute') - 0.05, off=1.0)
B(32625, T('5minute'), T('10000') - 0.05, off=1.0)
B(40656, T('10000'), p1 - 0.1, off=1.0)
B(4546, T('water') - 0.1, T('and', T('steps')) - 0.05, off=1.0)
B(40248, T('and', T('steps')), w1 - 0.1, off=1.5)
B(28894, T('time', w1 - 0.3) - 0.05, T('system', T('problem')) - 0.05, off=2.0)
B(10446, T('show') - 0.2, T('you', T('webinar')) - 0.1, off=1.0)
S.save(caps, cta_t=cta, hold=1.2)
