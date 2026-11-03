import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v8'); T, TE = S.T, S.TE
D = S.tl['dur']
h1 = TE('hain', T('exercises')) + 0.15
S.add({'type': 'chips', 't0': 0.0, 't1': h1, 'y': 130, 'items': [
    {'t': T('youtube'), 'icon': '▶️', 'text': 'Hazaaron *videos*'}, {'t': T('podcasts'), 'icon': '🎙️', 'text': 'Hazaaron *podcasts*'},
    {'t': T('diet'), 'icon': '🥗', 'text': 'Hazaaron *diet systems*'}, {'t': T('exercises'), 'icon': '🏋️', 'text': 'Hazaaron *exercises*'}]})
S.add({'type': 'title', 't0': T('phir') - 0.05, 't1': T('addict') - 0.08, 'y': 160, 'kicker': 'Phir bhi', 'lines': ['Lifestyle', '~theek nahi~?'], 'sizes': [96, 104]})
S.add({'type': 'slam', 't0': T('addict') - 0.05, 't1': T('aur', T('addict')) - 0.05, 'y': 200, 'text': '~Addicted~', 'size': 140, 'sub': 'Kharab lifestyle ke saath'})
S.punch(T('addict'), 0.14, 0.9)
S.add({'type': 'title', 't0': T('aur', T('addict')), 't1': T('aap', T('stuck')) - 0.08, 'y': 190, 'lines': ['*Stuck* ho chuke ho'], 'sizes': [104]})
p0 = T('aap', T('stuck')) - 0.1; p1 = TE('sako', T('reverse')) + 0.25
S.card(p0, p1)
S.add({'type': 'checklist', 't0': p0, 't1': p1, 'y': 170, 'title': 'Aapko chahiye ek system', 'items': [
    {'t': T('monotonous'), 'text': 'Monotonous zindagi <span>se bahar</span>', 'mark': 'check'},
    {'t': T('healthy'), 'text': 'Lifestyle <span>healthy</span>', 'mark': 'check'},
    {'t': T('bimaariyan'), 'text': 'Bimaariyan <span>reverse</span>', 'mark': 'check'}]})
S.add({'type': 'title', 't0': T('aur', p1 - 0.3) - 0.05, 't1': T('toh', T('possible')) - 0.08, 'y': 170, 'lines': ['Sab *possible* hai', 'agar lifestyle theek ho'], 'sizes': [96, 64]})
S.add({'type': 'slam', 't0': T('system', T('problems')) - 0.05, 't1': TE('maine', T('system', T('problems'))) + 0.25, 'y': 200, 'text': '*System* ✓', 'size': 140, 'sub': 'Maine bana diya hai'})
S.punch(T('system', T('problems')), 0.12, 0.8)
S.add({'type': 'badge', 't0': T('aap', T('maine')) - 0.05, 't1': T('agar', T('karke')) - 0.1, 'y': 200, 'text': 'Live webinar', 'sub': '👇 Link pe *click* karo'})
w0 = T('agar', T('karke')) - 0.1; w1 = TE('diya', T('protocol', T('karke'))) + 0.2
S.card(w0, w1)
S.add({'type': 'checklist', 't0': w0, 't1': w1, 'y': 170, 'title': 'Webinar mein milega', 'items': [
    {'t': T('diet', w0), 'text': 'Diet <span>kaise karni hai</span>', 'mark': 'check'},
    {'t': T('exercise', w0), 'text': 'Exercise <span>kaise karni hai</span>', 'mark': 'check'},
    {'t': T('protocol', w0), 'text': 'Poora ka poora <span>protocol</span>', 'mark': 'check'}]})
cta = T('milte') - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 1030, 'kicker': '🔴 Live webinar', 'title': 'Milte hain<br>*webinar* mein', 'sub': 'Poora protocol · ek jagah', 'button': 'LINK NEECHE HAI', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.08, 1.24]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.0, 'faceY': 0.45}
caps = S.captions(hl_pats=[r'youtube', r'videos', r'podcasts', r'diet', r'exercises?', r'lifestyle', r'addict', r'stuck', r'protocol', r'system', r'healthy',
                           r'bimaariyan', r'reverse', r'possible', r'webinar', r'link', r'click'])

B = S.broll
B(4911, T('youtube'), T('podcasts') - 0.05, off=1.0)
B(2948, T('podcasts'), T('diet') - 0.05, off=1.0)
B(40531, T('diet'), T('exercises') - 0.05)
B(52080, T('exercises'), h1 - 0.05, off=4.0)
B(372, T('addict') - 0.05, T('aur', T('addict')) - 0.05, off=1.0)
B(51405, T('aur', T('addict')), T('aap', T('stuck')) - 0.1, off=2.0)
B(1755, T('monotonous'), T('apni', T('sako')) - 0.05, off=2.0)
B(4629, T('healthy') - 0.3, T('apni', T('healthy')) - 0.05, off=1.0)
B(42729, T('bimaariyan') - 0.3, p1 - 0.1, off=1.0)
B(10446, T('aap', T('maine')) - 0.05, T('agar', T('karke')) - 0.12, off=1.0)
B(40529, T('diet', w0), T('aap', T('diet', w0)) - 0.05)
B(40248, T('exercise', w0), T('saari', T('exercise', w0)) - 0.05, off=1.5)
B(50109, T('saari', T('exercise', w0)), w1 - 0.1, off=1.0)
S.save(caps, cta_t=cta, hold=1.2)
