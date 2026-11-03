import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v11'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('toh') - 0.05, 'y': 150, 'lines': ['Namak', '*zeher* hai?'], 'sizes': [92, 118], 'hideCaps': True})
S.add({'type': 'title', 't0': T('toh'), 't1': T('kisi') - 0.08, 'y': 170, 'kicker': 'Toh hospital mein', 'lines': ['*Zeher* kyun', 'chadhate hain?'], 'sizes': [104, 76]})
S.add({'type': 'chips', 't0': T('kisi') - 0.1, 't1': T('sabse', T('jaanche')) - 0.1, 'y': 140, 'items': [
    {'t': T('stroke'), 'icon': '🧠', 'text': 'Stroke'}, {'t': T('heart'), 'icon': '❤️', 'text': 'Heart attack'},
    {'t': T('collapse'), 'icon': '😵', 'text': 'Collapse'}, {'t': T('behosh'), 'icon': '💤', 'text': 'Behosh'}]})
S.add({'type': 'slam', 't0': T('saline') - 0.05, 't1': T('saline', T('saline') + 0.2) - 0.05, 'y': 200, 'text': '*SALINE* 💧', 'size': 150, 'sub': 'Sabse pehle'})
S.punch(T('saline'), 0.14, 0.8)
S.add({'type': 'title', 't0': T('saline', T('saline') + 0.2) - 0.05, 't1': T('ab') - 0.08, 'y': 170, 'kicker': 'Saline yaani', 'lines': ['*NaCl*', 'sodium chloride'], 'sizes': [130, 70]})
s0 = T('ab') - 0.1; s1 = TE('hai', T('nason')) + 0.25
S.card(s0, s1)
S.add({'type': 'stat', 't0': s0, 't1': s1, 'y': 230, 'kicker': 'Ek saline bag mein', 'from': 0, 'to': 9000, 'unit': 'mg', 'label': 'Sodium', 'pill': '⚠️ Double bag = 18,000 mg', 'dir': 'up', 'count': 1.4})
n0 = T('ab', s1 - 0.3) - 0.1; n1 = TE('ko', T('dengi')) + 0.25
S.card(n0, n1)
S.add({'type': 'checklist', 't0': n0, 't1': n1, 'y': 170, 'title': 'Sodium = electrolyte', 'items': [
    {'t': T('paani'), 'text': 'Cell ke andar-bahar <span>paani balance</span>', 'mark': 'check'},
    {'t': T('kidneys'), 'text': 'Kidneys <span>filter</span>', 'mark': 'check'},
    {'t': T('heart', n0), 'text': 'Heart <span>pump</span>', 'mark': 'check'},
    {'t': T('nerves'), 'text': 'Nerve <span>signals</span>', 'mark': 'check'}]})
k0 = T('ab', n1 - 0.3) - 0.1; k1 = TE('se', T('meethe')) + 0.25
S.card(k0, k1)
S.add({'type': 'title', 't0': k0, 't1': T('jab', k0) - 0.1, 'y': 270, 'kicker': 'Kidneys ka', 'lines': ['*Secret*', 'function'], 'sizes': [120, 90]})
S.add({'type': 'chain', 't0': T('jab', k0) - 0.1, 't1': k1, 'y': 150, 'title': 'Kya hota hai', 'show': 4, 'items': [
    {'t': T('kam', k0), 'icon': '🧂', 'text': 'Sodium kam', 'st': '↓'},
    {'t': T('reabsorb'), 'icon': '🫘', 'text': 'Kidneys reabsorb', 'st': ''},
    {'t': T('insulin', k0), 'icon': '💉', 'text': 'Insulin', 'st': '↑'},
    {'t': T('blood'), 'icon': '🩸', 'text': 'Sugar cells mein', 'st': ''},
    {'t': T('drop'), 'icon': '📉', 'text': 'Sugar drop', 'st': '↓'},
    {'t': T('danger'), 'icon': '🧠', 'text': 'Brain: danger!', 'st': '⚠️'},
    {'t': T('meetha', k0), 'icon': '🍬', 'text': 'Meetha craving', 'st': '↑↑'}]})
S.add({'type': 'title', 't0': T('aapko', k1 - 0.3) - 0.05, 't1': T('namak', T('aapko', k1 - 0.3)) - 0.05, 'y': 170, 'lines': ['Aapko laga', '*meetha* chahiye'], 'sizes': [84, 104]})
S.add({'type': 'slam', 't0': T('namak', T('aapko', k1 - 0.3)) - 0.05, 't1': T('aur', T('namak', T('aapko', k1 - 0.3))) - 0.05, 'y': 200, 'text': 'Body ko<br>*NAMAK* 🧂', 'size': 130})
S.punch(T('namak', T('aapko', k1 - 0.3)), 0.14, 0.9)
S.add({'type': 'title', 't0': T('aur', T('namak', T('aapko', k1 - 0.3))), 't1': T('ek', T('karein')) - 0.08, 'y': 160, 'kicker': 'Duniya ne kya kiya?', 'lines': ['~Namak~ = villain', '*Sugar* industries chamki'], 'sizes': [96, 70]})
v0 = T('ek', T('karein')) - 0.1; v1 = TE('hai', T('permanently')) + 0.25
S.card(v0, v1)
S.add({'type': 'checklist', 't0': v0, 't1': v1, 'y': 170, 'title': 'Ek aur baat', 'items': [
    {'t': T('salt'), 'text': 'Excess salt <span>· urine se bahar</span>', 'mark': 'check'},
    {'t': T('sugar', T('salt')), 'text': 'Excess sugar <span>· fat store</span>', 'mark': 'x'},
    {'t': T('permanently'), 'text': 'Fat <span>· permanently store</span>', 'mark': 'x'}]})
q0 = T('ab', v1 - 0.3) - 0.1; q1 = TE('cheezein', T('personalized')) + 0.25
S.card(q0, q1)
S.add({'type': 'title', 't0': q0, 't1': T('salt', T('chahiye', q0)) - 0.1, 'y': 270, 'kicker': 'Sawaal ye hai', 'lines': ['Kitna *sodium*?', 'Kaun sa *salt*?'], 'sizes': [96, 96]})
S.add({'type': 'chips', 't0': T('salt', T('chahiye', q0)) - 0.1, 't1': T('aur', T('sea')) - 0.05, 'y': 160, 'items': [
    {'t': T('iodized'), 'icon': '🧂', 'text': 'Iodized'}, {'t': T('rock'), 'icon': '🪨', 'text': 'Rock salt'}, {'t': T('sea'), 'icon': '🌊', 'text': 'Sea salt'}]})
S.add({'type': 'checklist', 't0': T('aur', T('sea')) - 0.05, 't1': q1, 'y': 170, 'title': 'Depend karta hai', 'items': [
    {'t': T('weight', q0), 'text': 'Body <span>weight</span>', 'mark': 'check'},
    {'t': T('activity'), 'text': 'Activity <span>level</span>', 'mark': 'check'},
    {'t': T('sweat'), 'text': 'Sweat <span>rate</span>', 'mark': 'check'},
    {'t': T('personalized'), 'text': '= <span>Personalized</span>', 'mark': 'check'}]})
m0 = T('kyunki') - 0.1; m1 = TE('tha', T('koi', m0)) + 0.2
S.card(m0, m1)
S.add({'type': 'checklist', 't0': m0, 't1': m1, 'y': 170, 'title': 'Khud apni body pe apply kiya', 'items': [
    {'t': T('weight', m0), 'text': 'Weight <span>kaise ghatega</span>', 'mark': 'check'},
    {'t': T('pachega'), 'text': 'Kya khana <span>pachega</span>', 'mark': 'check'},
    {'t': T('gut'), 'text': 'Gut ko <span>kya achha lagega</span>', 'mark': 'check'},
    {'t': T('sugar', T('gut')), 'text': 'Sugar <span>kyun kharab</span>', 'mark': 'check'}]})
cta = T('mera') - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'You are watching', 'title': 'Fit<span class="acc">Finfluencer</span>', 'sub': 'Mera kaam tha science pahunchana · decision aapka hai', 'button': 'FOLLOW FOR MORE', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'namak', r'zeher', r'hospital', r'stroke', r'heart', r'saline', r'nacl', r'sodium', r'chloride', r'electrolyte', r'kidneys',
                           r'insulin', r'sugar', r'brain', r'meetha', r'villain', r'salt', r'fat', r'personalized', r'science', r'gut', r'weight'])
B = S.broll
B(4779, T('hospital') - 0.1, T('kisi') - 0.08, off=0.5)
B(597, T('paani') - 0.2, T('aur', T('paani')) - 0.05, off=2.0)
B(4733, T('blood') - 0.1, T('aur', T('blood')) - 0.05, off=1.0)
B(41227, T('meetha', k0) - 0.2, k1 - 0.1, off=1.0)
B(5078, T('taaki'), T('ek', T('karein')) - 0.08, off=2.0)
B(44001, T('sugar', T('salt')) - 0.1, T('aur', T('sugar', T('salt'))) - 0.05, off=1.0)
B(4546, T('sweat') - 0.2, T('personalized') - 0.05, off=1.0)
B(44432, T('weight', m0) - 0.2, T('kya', T('weight', m0)) - 0.05, off=1.0)
B(40529, T('gut') - 0.3, T('kyun', T('gut')) - 0.05, off=1.0)
S.save(caps, cta_t=cta, hold=1.2, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
