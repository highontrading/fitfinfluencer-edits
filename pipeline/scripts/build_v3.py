import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v3'); T, TE = S.T, S.TE
D = S.tl['dur']

# HOOK
S.add({'type': 'title', 't0': 0.05, 't1': T('dekh') - 0.05, 'y': 130, 'lines': ['Bas *1 chhota sa*', '*change*'], 'sizes': [92, 140], 'hideCaps': True})
S.punch(T('badal'), 0.10, 1.2)
S.punch(T('kitna'), 0.08, 1.5)

# BODY FAT — card
b0 = T('main') - 0.15; b1 = TE('hai', T('ghata')) + 0.3
S.card(b0, b1)
S.add({'type': 'compare', 't0': b0, 't1': T('30', T('15%')) - 0.1, 'y': 170, 'title': 'Mera body fat', 'max': 27, 'items': [
    {'t': T('26.9%') - 0.1, 'label': '30 din pehle', 'value': 26.9, 'dec': 1, 'unit': '%', 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('15%') - 0.1, 'label': 'Aaj', 'value': 15, 'unit': '%', 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
S.add({'type': 'stat', 't0': T('30', T('15%')) - 0.1, 't1': b1, 'y': 230, 'kicker': 'Sirf 30 din mein', 'from': 0, 'to': 11, 'unit': '%',
       'label': 'Body fat kam', 'pill': '▼ 26.9% → 15%', 'dir': 'down', 'count': 1.2})

# NOT DIET / EXERCISE / SUPPLEMENT
S.add({'type': 'title', 't0': T('sirf') - 0.1, 't1': T('aur', T('wajah')) - 0.1, 'y': 170, 'lines': ['Sirf *isi change*', 'ki wajah se'], 'sizes': [92, 76]})
k0 = T('aur', T('wajah')) - 0.1; k1 = TE('hai', T('bilkul')) + 0.3
S.card(k0, k1)
S.add({'type': 'checklist', 't0': k0, 't1': k1, 'y': 200, 'title': 'Ye change kya hai?', 'items': [
    {'t': T('diet'), 'text': 'Diet', 'mark': 'x'},
    {'t': T('exercise'), 'text': 'Exercise', 'mark': 'x'},
    {'t': T('supplement'), 'text': 'Supplement', 'mark': 'x'}]})
S.add({'type': 'slam', 't0': T('fasting'), 't1': T('kis') - 0.1, 'y': 210, 'text': '*Fasting* ⏱️', 'size': 150, 'sub': 'Ye hai wo change'})
S.punch(T('fasting'), 0.14, 1.2)
S.add({'type': 'title', 't0': T('kis') - 0.05, 't1': T('aur', T('kis')) - 0.1, 'y': 170, 'lines': ['*Sahi tareeke* se', 'fasting'], 'sizes': [96, 96]})
S.add({'type': 'title', 't0': T('aur', T('kis')) - 0.05, 't1': T('eating') - 0.1, 'y': 170, 'kicker': 'The domino effect', 'lines': ['Kaise *shuru* hota hai'], 'sizes': [88]})

# DOMINO CHAIN part 1 — card
d0 = T('eating') - 0.15; t_fk = T('ki', T('energy')) - 0.35; d1 = t_fk - 0.05
S.card(d0, d1)
ch1 = [
    {'t': T('eating', d0), 'icon': '🍽️', 'text': 'Eating window', 'st': 'chhota', 'stc': 'green'},
    {'t': T('insulin', d0), 'icon': '📉', 'text': 'Insulin', 'st': '↓ girta', 'stc': 'green'},
    {'t': T('fat', d0), 'icon': '🔥', 'text': 'Fat burning', 'st': 'START', 'stc': 'green'},
    {'t': T('energy', d0), 'icon': '⚡', 'text': 'Energy', 'st': '↑ aati', 'stc': 'green'}]
S.add({'type': 'chain', 't0': d0, 't1': d1, 'y': 150, 'title': 'Domino effect', 'show': 4, 'items': ch1})
S.add({'type': 'slam', 't0': t_fk, 't1': TE('hai', T('khatarnak')) + 0.25, 'y': 220, 'text': 'Fat ki energy ⚡', 'size': 88, 'sub': 'Bahut zyada khatarnak'})
S.punch(T('khatarnak'), 0.12, 0.8)

# DOMINO CHAIN part 2 — card
e0 = T('jab', T('khatarnak')) - 0.15; e1 = TE('aati', T('consistency', e0)) + 0.3
S.card(e0, e1)
ch2 = [
    {'t': T('jab', T('khatarnak')), 'icon': '⚡', 'text': 'Energy', 'st': '↑ high'},
    {'t': T('exercise', e0), 'icon': '🏋️', 'text': 'Exercise', 'st': 'zyada'},
    {'t': T('push', e0), 'icon': '💪', 'text': 'Khud ko push', 'st': '↑'},
    {'t': T('thakti', e0), 'icon': '🥵', 'text': 'Body thakti', 'st': '✓'},
    {'t': T('neend', e0), 'icon': '😴', 'text': 'Neend', 'st': 'achhi'},
    {'t': T('stress', e0), 'icon': '🧘', 'text': 'Stress', 'st': '↓ girta'},
    {'t': T('cortisol', e0), 'icon': '⚖️', 'text': 'Cortisol', 'st': 'normal'},
    {'t': T('fat', T('cortisol', e0)), 'icon': '🔥', 'text': 'Fat burn', 'st': 'aur tez'},
    {'t': T('result', e0), 'icon': '📈', 'text': 'Result', 'st': 'dikhta'},
    {'t': T('motivation', e0), 'icon': '🚀', 'text': 'Motivation', 'st': '↑'},
    {'t': T('consistency', e0), 'icon': '🔁', 'text': 'Consistency', 'st': '∞'}]
for it in ch2: it['stc'] = 'green'
S.add({'type': 'chain', 't0': e0, 't1': e1, 'y': 150, 'title': 'Domino effect', 'show': 4, 'items': ch2})

# SYSTEM / HABITS
h0 = T('aur', T('consistency', e0)) - 0.05
S.add({'type': 'title', 't0': h0, 't1': T('ek', T('trigger')) - 0.1, 'y': 170, 'kicker': 'Ye ek system hai', 'lines': ['Ek cheez → *doosri*'], 'sizes': [88]})
S.add({'type': 'title', 't0': T('ek', T('trigger')) - 0.05, 't1': TE('hai', T('trigger', T('aadat'))) + 0.25, 'y': 170, 'lines': ['1 achhi aadat', '→ *next achhi aadat*'], 'sizes': [86, 80]})
S.punch(T('aadat'), 0.10, 1.6)

# WEBINAR
S.add({'type': 'badge', 't0': T('saari', h0) - 0.1, 't1': T('link') - 0.1, 'y': 200, 'text': 'Live webinar', 'sub': 'Poora system · *2 ghante*'})
S.punch(T('2'), 0.10, 1.2)

# CTA
cta = T('link') - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 1, 'y': 1030, 'kicker': '🔴 Live webinar · 2 ghante', 'title': 'Abhi<br>*join* kijiye',
       'sub': 'Milte hain webinar mein!', 'button': 'LINK NEECHE HAI', 'hideCaps': True})
S.punch(cta, 0.06, 99)

S.alt_zoom([1.22, 1.40])
S.cam['faceY'] = 0.34
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.55, 'faceY': 0.40}
caps = S.captions(hl_pats=[r'change', r'result', r'fat', r'diet', r'exercise', r'supplement', r'fasting', r'insulin', r'energy', r'neend', r'stress',
                           r'cortisol', r'motivation', r'consistency', r'system', r'webinar', r'trigger', r'join', r'link', r'push'])
S.save(caps, cta_t=cta, music_offset=19.2)

# ===== stock b-roll =====
B = S.broll
B(44429, T('30', T('15%')) - 0.05, b1 - 0.1, off=1.0)
B(40529, T('diet'), T('exercise') - 0.05)
B(40248, T('exercise'), T('supplement') - 0.05, off=1.5)
B(2856, T('supplement'), k1 - 0.05)
B(28897, T('fasting') - 0.05, T('kis') - 0.08)
B(3795, T('eating', d0), T('insulin', d0) - 0.05)
B(32792, T('fat', d0), T('energy', d0) - 0.05)
B(42896, T('neend', e0), T('stress', e0) - 0.05, off=1.0)
B(887, T('stress', e0), T('cortisol', e0) - 0.05, off=1.0)
B(722, T('fat', T('cortisol', e0)), T('result', e0) - 0.05, off=8.0)
B(4840, T('result', e0), T('motivation', e0) - 0.05, off=1.0)
B(34566, T('motivation', e0), T('consistency', e0) - 0.05, off=1.0)
B(609, T('consistency', e0), e1 - 0.05, off=3.0)
B(597, T('ek', T('trigger')) - 0.05, TE('hai', T('trigger', T('aadat'))) + 0.2, off=2.0)
B(10443, T('saari', h0) - 0.1, T('link') - 0.12, off=1.0)
S.save(caps, cta_t=cta, music_offset=19.2)
