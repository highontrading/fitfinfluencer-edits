# Devanagari -> readable Hinglish (Roman) for caption drafts: schwa deletion + a lexicon of common words.
import re
V = {'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au', 'ऋ': 'ri', 'ऑ': 'o'}
M = {'ा': 'aa', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', 'ृ': 'ri', 'ॉ': 'o', 'ॅ': 'e'}
C = {'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'n', 'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'n', 'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
     'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n', 'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm', 'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh',
     'ष': 'sh', 'स': 's', 'ह': 'h', 'क़': 'q', 'ख़': 'kh', 'ग़': 'gh', 'ज़': 'z', 'ड़': 'd', 'ढ़': 'rh', 'फ़': 'f', 'य़': 'y'}
NUK = {'क': 'q', 'ख': 'kh', 'ग': 'gh', 'ज': 'z', 'ड': 'd', 'ढ': 'rh', 'फ': 'f'}
LEX = {'है': 'hai', 'हैं': 'hain', 'नहीं': 'nahi', 'ने': 'ne', 'को': 'ko', 'की': 'ki', 'का': 'ka', 'के': 'ke', 'में': 'mein', 'से': 'se', 'पर': 'par', 'पे': 'pe',
       'और': 'aur', 'तो': 'toh', 'भी': 'bhi', 'ही': 'hi', 'कि': 'ki', 'क्या': 'kya', 'क्यों': 'kyun', 'क्यूँ': 'kyun', 'क्योंकि': 'kyunki', 'क्यूंकि': 'kyunki',
       'मैं': 'main', 'मैंने': 'maine', 'मेरा': 'mera', 'मेरी': 'meri', 'मेरे': 'mere', 'मुझे': 'mujhe', 'हम': 'hum', 'हमारा': 'hamara', 'हमारी': 'hamari', 'हमारे': 'hamare',
       'आप': 'aap', 'आपका': 'aapka', 'आपकी': 'aapki', 'आपके': 'aapke', 'आपको': 'aapko', 'लोग': 'log', 'लोगों': 'logon', 'यह': 'ye', 'ये': 'ye', 'वो': 'wo', 'वह': 'wo',
       'इसको': 'isko', 'उसको': 'usko', 'इस': 'is', 'उस': 'us', 'इसी': 'isi', 'उसी': 'usi', 'जो': 'jo', 'जब': 'jab', 'तब': 'tab', 'अब': 'ab', 'सब': 'sab', 'कुछ': 'kuch',
       'बहुत': 'bahut', 'ज्यादा': 'zyada', 'जादा': 'zyada', 'ज़्यादा': 'zyada', 'कम': 'kam', 'एक': 'ek', 'दो': 'do', 'तीन': 'teen', 'चार': 'chaar', 'पांच': 'paanch',
       'होता': 'hota', 'होती': 'hoti', 'होते': 'hote', 'हो': 'ho', 'गया': 'gaya', 'गई': 'gayi', 'गए': 'gaye', 'था': 'tha', 'थी': 'thi', 'थे': 'the', 'रहा': 'raha',
       'रही': 'rahi', 'रहे': 'rahe', 'करना': 'karna', 'करते': 'karte', 'करता': 'karta', 'करती': 'karti', 'कर': 'kar', 'करो': 'karo', 'किया': 'kiya', 'जाता': 'jaata',
       'जाती': 'jaati', 'जाते': 'jaate', 'जाएगा': 'jaayega', 'जाएगी': 'jaayegi', 'जाएंगे': 'jaayenge', 'देता': 'deta', 'देती': 'deti', 'लेते': 'lete', 'खाना': 'khaana',
       'खाते': 'khaate', 'खाओ': 'khao', 'पानी': 'paani', 'शरीर': 'shareer', 'चीज': 'cheez', 'चीज़': 'cheez', 'चीजें': 'cheezein', 'चीज़ें': 'cheezein', 'सारी': 'saari',
       'सारे': 'saare', 'पूरा': 'poora', 'पूरी': 'poori', 'मतलब': 'matlab', 'यानी': 'yaani', 'यानि': 'yaani', 'लेकिन': 'lekin', 'मगर': 'magar', 'बट': 'but',
       'अगर': 'agar', 'सिर्फ': 'sirf', 'सिर्फ़': 'sirf', 'एकदम': 'ekdam', 'हमेशा': 'hamesha', 'आज': 'aaj', 'कल': 'kal', 'साल': 'saal', 'दिन': 'din', 'रात': 'raat',
       'बताता': 'batata', 'बताया': 'bataya', 'समझो': 'samjho', 'देखो': 'dekho', 'चाहिए': 'chahiye', 'सकते': 'sakte', 'सकता': 'sakta', 'वाले': 'waale', 'वाली': 'waali',
       'मिलते': 'milte', 'वीडियो': 'video', 'हेल्थ': 'health', 'प्रोटोकॉल': 'protocol', 'बॉडी': 'body', 'बोडी': 'body', 'बोड़ी': 'body', 'कमेंट': 'comment',
       'साइंस': 'science', 'साइन्स': 'science', 'पहुंचाना': 'pahunchana', 'पहुचाना': 'pahunchana', 'डिसीजन': 'decision', 'डिसिजन': 'decision', 'फास्टिंग': 'fasting'}
def word(w):
    core = re.sub(r'[।,.?!]', '', w); tail = w[len(core):] if w.startswith(core) else ''
    if not re.search('[ऀ-ॿ]', core): return w
    if core in LEX: return LEX[core] + tail
    out = []; i = 0; chars = list(core)
    while i < len(chars):
        ch = chars[i]; nx = chars[i + 1] if i + 1 < len(chars) else ''
        if ch in C or ch in NUK:
            base = NUK[ch] if nx == '़' and ch in NUK else C.get(ch, '')
            if nx == '़': i += 1; nx = chars[i + 1] if i + 1 < len(chars) else ''
            if nx == '्': out.append(base); i += 2; continue
            if nx in M: out.append(base + M[nx]); i += 2; continue
            out.append(base + 'A'); i += 1; continue   # 'A' = inherent schwa (decided below)
        if ch in V: out.append(V[ch])
        elif ch in ('ं', 'ँ'): out.append('n')
        elif ch == 'ः': out.append('h')
        elif ch.isdigit(): out.append(ch)
        i += 1
    s = ''.join(out)
    s = re.sub(r'A$', '', s)                                   # word-final schwa
    s = re.sub(r'(?<=[aeiouA][^aeiouA])A(?=[^aeiouA][aeiou])', '', s)   # VC(a)CV -> VCCV
    s = s.replace('A', 'a')
    s = re.sub(r'ee$', 'i', s); s = re.sub(r'aa$', 'a', s); s = re.sub(r'oo$', 'u', s)
    s = s.replace('w', 'v')
    return s + tail
def line(text): return ' '.join(word(w) for w in text.split())
if __name__ == '__main__':
    import sys, json
    for c in json.load(open(sys.argv[1])): print(c['id'], line(c['text']))
