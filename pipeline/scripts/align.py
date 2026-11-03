# Align caption words (Roman/Hinglish or English) to ASR words (Devanagari/English) by phonetic similarity.
import re, difflib
V = {'अ':'a','आ':'aa','इ':'i','ई':'ee','उ':'u','ऊ':'oo','ए':'e','ऐ':'ai','ओ':'o','औ':'au','ऋ':'ri','ऑ':'o'}
M = {'ा':'aa','ि':'i','ी':'ee','ु':'u','ू':'oo','े':'e','ै':'ai','ो':'o','ौ':'au','ृ':'ri','ॉ':'o','ॅ':'e'}
C = {'क':'k','ख':'kh','ग':'g','घ':'gh','ङ':'n','च':'ch','छ':'chh','ज':'j','झ':'jh','ञ':'n','ट':'t','ठ':'th','ड':'d','ढ':'dh','ण':'n',
     'त':'t','थ':'th','द':'d','ध':'dh','न':'n','प':'p','फ':'ph','ब':'b','भ':'bh','म':'m','य':'y','र':'r','ल':'l','व':'v','श':'sh',
     'ष':'sh','स':'s','ह':'h','ड़':'r','ढ़':'rh','क़':'k','ख़':'kh','ग़':'g','ज़':'z','फ़':'f'}
def translit(w):
    out = []; i = 0; s = w
    while i < len(s):
        ch = s[i]
        if i + 1 < len(s) and s[i+1] == '़':
            ch = s[i:i+2]; i += 1
        if ch in C:
            nxt = s[i+1] if i + 1 < len(s) else ''
            if nxt == '्': out.append(C[ch]); i += 2; continue
            if nxt in M: out.append(C[ch] + M[nxt]); i += 2; continue
            out.append(C[ch] + ('a' if i + 1 < len(s) and s[i+1] not in 'ंँः' else ''))
            i += 1; continue
        if ch in V: out.append(V[ch])
        elif ch in 'ंँ': out.append('n')
        elif ch in M: out.append(M[ch])
        elif ch.isascii(): out.append(ch.lower())
        i += 1
    return ''.join(out)
def key(w):
    w = translit(w) if re.search(r'[ऀ-ॿ]', w) else w.lower()
    w = re.sub(r'[^a-z0-9%]', '', w)
    w = w.replace('aa', 'a').replace('ee', 'i').replace('oo', 'u').replace('w', 'v').replace('z', 'j').replace('ph', 'f')
    return w
def skel(k): return re.sub(r'[aeiou]', '', k) or k
def sim(a, b):
    if not a or not b: return 0.0
    r1 = difflib.SequenceMatcher(None, a, b).ratio(); r2 = difflib.SequenceMatcher(None, skel(a), skel(b)).ratio()
    return max(r1, r2)
def align(cap, asr):
    """cap: list of str; asr: list of dict(w,s,e). Returns list of (s,e) per caption word."""
    ck = [key(c) for c in cap]; ak = [key(a['w']) for a in asr]
    n, m = len(ck), len(ak); G = -0.35
    S = [[0.0] * (m + 1) for _ in range(n + 1)]; B = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = i * G; B[i][0] = 1
    for j in range(1, m + 1): S[0][j] = j * G; B[0][j] = 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sc = sim(ck[i-1], ak[j-1]); d = S[i-1][j-1] + (sc - 0.45) * 2
            u = S[i-1][j] + G; l = S[i][j-1] + G
            if d >= u and d >= l: S[i][j], B[i][j] = d, 0
            elif u >= l: S[i][j], B[i][j] = u, 1
            else: S[i][j], B[i][j] = l, 2
    i, j = n, m; match = [None] * n
    while i > 0 or j > 0:
        b = B[i][j]
        if i > 0 and j > 0 and b == 0: match[i-1] = j - 1; i -= 1; j -= 1
        elif i > 0 and (j == 0 or b == 1): i -= 1
        else: j -= 1
    # times: matched words take asr times; unmatched interpolate between neighbours
    t = [None] * n
    for i, j in enumerate(match):
        if j is not None: t[i] = (asr[j]['s'], asr[j]['e'])
    known = [i for i in range(n) if t[i]]
    nm = len(known)
    if not known:
        s0, e0 = asr[0]['s'], asr[-1]['e']
        return [(s0 + (e0 - s0) * i / n, s0 + (e0 - s0) * (i + 1) / n) for i in range(n)], 0.0
    i = 0
    while i < n:
        if t[i]: i += 1; continue
        j = i
        while j < n and not t[j]: j += 1
        a = t[i-1][1] if i > 0 else asr[0]['s']
        b = t[j][0] if j < n else asr[-1]['e']
        if b - a < 0.08 * (j - i):   # no room: squeeze into neighbour's end
            a = (t[i-1][0] + t[i-1][1]) / 2 if i > 0 else a
            if i > 0: t[i-1] = (t[i-1][0], a)
        span = max(b - a, 0.06 * (j - i)) / (j - i)
        for k in range(i, j): t[k] = (a + span * (k - i), a + span * (k - i + 1))
        i = j
    # monotonic
    for i in range(1, n):
        if t[i][0] < t[i-1][0]: t[i] = (t[i-1][0] + 0.05, max(t[i][1], t[i-1][0] + 0.1))
    return t, nm / max(n, 1)
