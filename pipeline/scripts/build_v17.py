import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v17'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('raat') - 0.05, 'y': 150, 'kicker': 'India mein', 'lines': ['Har *4th–5th* aadmi', 'sharaab pee raha'], 'sizes': [92, 84], 'hideCaps': True})
S.add({'type': 'chips', 't0': T('raat') - 0.05, 't1': T('kyunki') - 0.08, 'y': 140, 'items': [
    {'t': T('neend'), 'icon': '🌙', 'text': 'Neend nahi aati'}, {'t': T('drink'), 'icon': '🥃', 'text': 'Ek drink'},
    {'t': T('8'), 'icon': '😴', 'text': '8 ghante soye'}, {'t': T('thake'), 'icon': '😩', 'text': 'Phir bhi *thake*'}]})
S.add({'type': 'slam', 't0': T('kyunki') - 0.05, 't1': T('samjho') - 0.05, 'y': 200, 'text': 'FAKE *SLEEP*', 'size': 124, 'sub': 'Aap sach mein soye hi nahi'})
S.punch(T('fake'), 0.14, 0.8)
S.add({'type': 'title', 't0': T('samjho') - 0.03, 't1': T('neend', T('rahi')) - 0.08, 'y': 170, 'lines': ['Neend ≠ *nasha*'], 'sizes': [112]})
S.add({'type': 'title', 't0': T('neend', T('rahi')) - 0.05, 't1': T('stage') - 0.08, 'y': 170, 'kicker': 'Neend ke', 'lines': ['*4 stages*'], 'sizes': [124]})
s0 = T('stage') - 0.1; s1 = T('aur', T('paati')) - 0.08
S.card(s0, s1)
S.add({'type': 'chain', 't0': s0, 't1': s1, 'y': 150, 'title': 'Neend ke stages', 'show': 4, 'items': [
    {'t': T('stage') + 0.1, 'icon': '🌙', 'text': 'Stage 1–2 · Light sleep', 'st': ''},
    {'t': T('relax'), 'icon': '🛌', 'text': 'Body relax', 'st': ''},
    {'t': T('stage', T('relax')), 'icon': '🔧', 'text': 'Stage 3 · *Deep sleep*', 'st': ''},
    {'t': T('repair'), 'icon': '🩹', 'text': 'Body repair', 'st': '✓', 'stc': 'green'},
    {'t': T('2.5'), 'icon': '⏱️', 'text': '8h mein sirf ~2.5h deep', 'st': ''}]})
S.add({'type': 'chips', 't0': s1 + 0.03, 't1': T('aur', T('fix')) - 0.08, 'y': 140, 'items': [
    {'t': T('muscles'), 'icon': '💪', 'text': 'Muscles'}, {'t': T('bone'), 'icon': '🦴', 'text': 'Bone'},
    {'t': T('immune'), 'icon': '🛡️', 'text': 'Immune system'}, {'t': T('fix'), 'icon': '🔧', 'text': 'Sab *fix*'}]})
r0 = T('aur', T('fix')) - 0.1; r1 = TE('hai', T('complete')) + 0.25
S.card(r0, r1)
S.add({'type': 'chain', 't0': r0, 't1': r1, 'y': 150, 'title': 'Stage 4 · REM sleep', 'show': 4, 'items': [
    {'t': T('rem'), 'icon': '🧠', 'text': 'REM sleep', 'st': ''},
    {'t': T('organize'), 'icon': '🗂️', 'text': 'Brain organize', 'st': '✓'},
    {'t': T('memory'), 'icon': '💾', 'text': 'Memory consolidate', 'st': '✓'},
    {'t': T('emotions'), 'icon': '💭', 'text': 'Emotions process', 'st': '✓'},
    {'t': T('complete'), 'icon': '✅', 'text': 'Neend complete', 'st': '✓'}]})
for it in S.events[-1]['items']: it['stc'] = 'green'
a0 = T('ab', r1 - 0.3) - 0.1; a1 = TE('uthte') + 0.25
S.card(a0, a1)
S.add({'type': 'chain', 't0': a0, 't1': a1, 'y': 150, 'title': 'Alcohol kya karta hai', 'show': 4, 'items': [
    {'t': T('fast'), 'icon': '⚡', 'text': 'Stage 1 → 2 fast', 'st': ''},
    {'t': T('jaldi'), 'icon': '😴', 'text': 'Jaldi so jaate ho', 'st': ''},
    {'t': T('destroy'), 'icon': '💥', 'text': 'Deep + REM *destroy*', 'st': '✗', 'stc': 'red'},
    {'t': T('repairing'), 'icon': '🔧', 'text': 'Body repair nahi', 'st': '✗', 'stc': 'red'},
    {'t': T('organizing'), 'icon': '🧠', 'text': 'Brain organize nahi', 'st': '✗', 'stc': 'red'},
    {'t': T('thake', T('subah', T('organizing'))), 'icon': '😩', 'text': 'Subah thake thake', 'st': '✗', 'stc': 'red'}]})
S.add({'type': 'title', 't0': a1 + 0.03, 't1': T('studies') - 0.08, 'y': 170, 'kicker': 'Yahi thakaan', 'lines': ['= *"Hangover"*'], 'sizes': [112]})
g0 = T('studies') - 0.1; g1 = TE('hui') + 0.25
S.card(g0, g1)
S.add({'type': 'chain', 't0': g0, 't1': g1, 'y': 150, 'title': 'Same breakfast · glucose spike', 'show': 4, 'items': [
    {'t': T('6', g0), 'icon': '😴', 'text': '6 ghante neend → *zyada*', 'st': '↑↑', 'stc': 'red'},
    {'t': T('7', g0), 'icon': '🛏️', 'text': '7 ghante → medium', 'st': '↑'},
    {'t': T('8', g0), 'icon': '✅', 'text': '8 ghante → *sabse kam*', 'st': '✓', 'stc': 'green'}]})
f0 = T('matlab', T('hui')) - 0.1; g1 = min(g1, f0); f1 = TE('jaayega', T('sab', T('exercise'))) + 0.25
S.card(f0, f1)
S.add({'type': 'chain', 't0': f0, 't1': f1, 'y': 150, 'title': 'Neend sahi nahi toh', 'show': 4, 'items': [
    {'t': T('neend', f0), 'icon': '😴', 'text': 'Kharab neend', 'st': ''},
    {'t': T('management'), 'icon': '📈', 'text': 'Glucose management fail', 'st': '✗'},
    {'t': T('diet', f0), 'icon': '🥗', 'text': 'Diet fail', 'st': '✗'},
    {'t': T('exercise', f0), 'icon': '🏋️', 'text': 'Exercise fail', 'st': '✗'},
    {'t': T('sab', T('exercise', f0)), 'icon': '❌', 'text': 'Sab kuch fail', 'st': '✗'}]})
for it in S.events[-1]['items']: it['stc'] = 'red'
S.add({'type': 'stat', 't0': f1 + 0.03, 't1': T('sleep', T('osteoporosis')) - 0.08, 'y': 230, 'kicker': '6 ghante sone waale', 'from': 0, 'to': 40, 'unit': '%', 'label': 'Zyada fractures', 'pill': '🦴 + Osteoporosis', 'dir': 'up', 'count': 1.0})
S.add({'type': 'slam', 't0': T('sleep', T('osteoporosis')) - 0.05, 't1': T('aur', T('pillar')) - 0.05, 'y': 200, 'text': 'SLEEP = *chhupa pillar*', 'size': 96, 'sub': 'Mere health protocol ka'})
S.punch(T('pillar'), 0.12, 0.8)
p0 = T('aur', T('pillar')) - 0.1; p1 = TE('thing') + 0.25
S.card(p0, p1)
S.add({'type': 'checklist', 't0': p0, 't1': p1, 'y': 170, 'title': 'Protocol ka matlab', 'items': [
    {'t': T('diet', p0), 'text': 'Diet', 'mark': 'check'},
    {'t': T('exercise', p0), 'text': 'Exercise', 'mark': 'check'},
    {'t': T('meditation'), 'text': 'Meditation', 'mark': 'check'},
    {'t': T('important'), 'text': 'Sleep <span>= most important</span>', 'mark': 'check'}]})
b0 = T('agar', T('thing')) - 0.1; p1 = min(p1, b0); b1 = TE('baad', T('khaane', T('diet', p1))) + 0.25
S.card(b0, b1)
S.add({'type': 'chain', 't0': b0, 't1': b1, 'y': 150, 'title': 'Sahi neend nahi toh', 'show': 4, 'items': [
    {'t': T('repair', b0), 'icon': '🔧', 'text': 'Body repair nahi', 'st': '✗'},
    {'t': T('toot.*', b0), 'icon': '💥', 'text': 'Body toot-ti jaayegi', 'st': '✗'},
    {'t': T('daily'), 'icon': '😩', 'text': 'Daily thake', 'st': '✗'},
    {'t': T('patle'), 'icon': '⚖️', 'text': 'Patle *nahi* ho paoge', 'st': '✗'},
    {'t': T('workout'), 'icon': '🏋️', 'text': 'Workout + diet ke baad bhi', 'st': ''}]})
for it in S.events[-1]['items']: it['stc'] = 'red'
cta = T('agar', T('hoon', T('chuka'))) - 0.1
S.add({'type': 'badge', 't0': b1 + 0.03, 't1': cta - 0.05, 'y': 200, 'text': 'Mere saath hua', 'sub': 'Isliye *bata raha hoon*'})
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Poora system chahiye?', 'title': 'Comment<br>*"SYSTEM"*', 'sub': 'Mera kaam tha science pahunchana · decision aapka hai', 'button': '💬 COMMENT "SYSTEM"', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'sharaab', r'neend', r'drink', r'thake', r'fake', r'sleep', r'nashe', r'stages?', r'light', r'deep', r'repair', r'muscles', r'bone', r'immune',
                           r'rem', r'brain', r'memory', r'emotions', r'alcohol', r'destroy', r'hangover', r'breakfast', r'glucose', r'spike', r'insulin', r'fail',
                           r'fracture', r'osteoporosis', r'pillar', r'important', r'patle', r'system'])
B = S.broll
B(8692, 0.6, T('raat') - 0.08, off=1.0)
B(31415, T('raat') - 0.05, T('drink') - 0.1, off=1.0)
B(5145, T('drink') - 0.1, T('so') - 0.05, off=1.0)
B(42896, T('deep') - 0.2, T('body', T('deep')) - 0.05, off=2.0)
B(50931, T('rem') - 0.2, T('brain', T('rem')) - 0.05, off=1.0)
B(22734, a0 + 0.1, T('stage', a0) - 0.05, off=2.0)
B(51399, T('destroy') - 0.3, T('matlab', T('destroy')) - 0.05, off=2.0)
B(51405, T('subah', T('organizing')) - 0.1, a1 - 0.1, off=2.0)
B(4607, T('jab', T('hangover')) - 0.1, T('studies') - 0.1, off=2.0)
B(4779, T('fracture') - 0.2, T('sleep', T('osteoporosis')) - 0.1, off=1.0)
B(40248, T('workout') - 0.1, b1 - 0.1, off=2.0)
S.save(caps, cta_t=cta, hold=1.2, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
