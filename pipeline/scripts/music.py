# Procedural, license-free background music + SFX for the ads.
import numpy as np, soundfile as sf, sys
from scipy.signal import butter, sosfilt, fftconvolve

SR = 48000
rng = np.random.default_rng(7)
OUT = sys.argv[1]

def lp(x, f, o=2):  return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2):  return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi):  return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), x)
def env(n, a, d, s=0.0, r=0.0, sl=None):
    a, d = int(a*SR), int(d*SR)
    e = np.zeros(n)
    a = min(a, n); e[:a] = np.linspace(0, 1, a, endpoint=False)
    dd = min(d, n-a); e[a:a+dd] = np.linspace(1, s, dd)
    e[a+dd:] = s
    return e
def note(m): return 440.0 * 2 ** ((m - 69) / 12)

def reverb(x, secs=2.2, mix=0.25, pre=0.02):
    n = int(secs*SR)
    t = np.arange(n)/SR
    ir = rng.standard_normal((2, n)) * np.exp(-t*6.5/secs)
    ir = np.stack([lp(hp(i, 300), 7000) for i in ir])
    ir[:, :int(pre*SR)] = 0
    ir /= np.abs(ir).sum(axis=1, keepdims=True) ** 0.5 * 40
    if x.ndim == 1: x = np.stack([x, x])
    wet = np.stack([fftconvolve(x[c], ir[c])[:x.shape[1]] for c in range(2)])
    return x*(1-mix) + wet*mix*3

def saw(f, n, detune=0.0):
    t = np.arange(n)/SR
    ph = (f*(1+detune))*t + rng.random()
    return 2*(ph - np.floor(ph)) - 1

BPM = 100
BEAT = 60 / BPM
BAR = 4 * BEAT
# Am - F - C - G (i - VI - III - VII), voiced mid register
PROG = [[57, 60, 64, 69], [53, 57, 60, 65], [48, 55, 60, 64], [55, 59, 62, 67]]
ROOTS = [33, 29, 36, 31]

def track(bars=40):
    n = int(bars*BAR*SR) + SR*3
    L = np.zeros((2, n))
    def add(sig, t0, gain=1.0, pan=0.0):
        i = int(t0*SR)
        if i >= n: return
        sig = sig[:n-i]
        if sig.ndim == 1:
            L[0, i:i+len(sig)] += sig*gain*(1-pan)
            L[1, i:i+len(sig)] += sig*gain*(1+pan)
        else:
            L[:, i:i+sig.shape[1]] += sig*gain

    # drums
    kl = int(0.45*SR); tk = np.arange(kl)/SR
    kick = np.sin(2*np.pi*np.cumsum(45 + 110*np.exp(-tk*28))/SR) * np.exp(-tk*7)
    kick += 0.3*np.sin(2*np.pi*np.cumsum(45+300*np.exp(-tk*80))/SR)*np.exp(-tk*40)
    cl = int(0.3*SR); tc = np.arange(cl)/SR
    clap = bp(rng.standard_normal(cl), 900, 4500) * (np.exp(-tc*22) + 0.4*np.exp(-((tc-0.012)*90)**2))
    hl = int(0.06*SR); th = np.arange(hl)/SR
    hat = hp(rng.standard_normal(hl), 8000) * np.exp(-th*70)
    ohat = hp(rng.standard_normal(int(0.25*SR)), 7000) * np.exp(-np.arange(int(0.25*SR))/SR*14)

    side = np.ones(n)  # sidechain envelope from kick
    duck = 1 - 0.55*np.exp(-np.arange(int(BEAT*SR))/SR*9)
    for b in range(bars):
        sec = b // 8   # 0 intro, 1.. full
        t0 = b*BAR
        ch = PROG[b % 4]
        # pad (detuned saws, filtered, slow attack)
        pl = int(BAR*SR) + SR
        pad = sum(saw(note(m), pl, d) for m in ch for d in (-0.004, 0.0, 0.005)) / 12
        cut = 900 if sec == 0 else 1800
        pad = lp(pad, cut, 2) * env(pl, 0.35, 0.5, 0.8)
        pad[-SR:] *= np.linspace(1, 0, SR)
        add(np.stack([pad, np.roll(pad, 240)]), t0, 0.55)
        # pluck arp 16ths
        if sec >= 1:
            seq = [ch[0]+12, ch[2]+12, ch[1]+12, ch[3]+12, ch[2]+12, ch[1]+24, ch[3]+12, ch[2]+12]
            for k in range(16):
                m = seq[k % 8]
                ln = int(0.25*SR)
                s = (saw(note(m), ln) + 0.5*np.sin(2*np.pi*note(m)*np.arange(ln)/SR))
                s = lp(s, 2500) * np.exp(-np.arange(ln)/SR*16)
                add(s, t0 + k*BEAT/4, 0.10, pan=0.35*np.sin(k))
        # sub bass, 8th notes
        if sec >= 1:
            for k in range(8):
                ln = int(BEAT/2*SR*0.9)
                f = note(ROOTS[b % 4] + (12 if k % 4 == 3 else 0))
                tt = np.arange(ln)/SR
                s = np.sin(2*np.pi*f*tt) + 0.25*np.tanh(3*np.sin(2*np.pi*f*tt))
                s *= env(ln, 0.005, 0.2, 0.7) * np.linspace(1, 0.6, ln)
                add(lp(s, 600), t0 + k*BEAT/2, 0.32)
        for q in range(4):
            tb = t0 + q*BEAT
            if sec >= 1 or q in (0, 2):
                add(kick, tb, 0.75 if sec >= 1 else 0.45)
                i = int(tb*SR); side[i:i+len(duck)] = np.minimum(side[i:i+len(duck)], duck[:n-i])
            if sec >= 1 and q in (1, 3): add(clap, tb, 0.28, pan=0.05)
            for e in range(2):
                sw = 0.02 if e else 0
                add(hat, tb + e*BEAT/2 + sw, (0.10 if e else 0.06) * (1 if sec >= 1 else 0.5), pan=-0.3)
            if sec >= 2 and q == 3: add(ohat, tb + BEAT/2, 0.06, pan=0.3)
    L *= side
    L = reverb(L, 1.8, 0.18)
    L = np.tanh(L*1.2)/1.2
    L /= np.abs(L).max() + 1e-9
    L *= 0.89
    return L

def whoosh(d=0.55, up=True):
    nn = int(d*SR); t = np.arange(nn)/SR
    x = rng.standard_normal(nn)
    out = np.zeros(nn)
    # moving band-pass via chunks
    ch = 256
    for i in range(0, nn, ch):
        p = i/nn
        fc = 300*(30**(p if up else 1-p))
        seg = x[max(0, i-1024):i+ch]
        y = bp(seg, fc*0.6, min(fc*1.6, 20000))
        out[i:i+ch] = y[-len(out[i:i+ch]):]
    e = np.sin(np.pi*np.clip(t/d, 0, 1))**2
    out = out*e
    s = np.stack([out*(1-0.5*t/d), out*(0.5+0.5*t/d)])
    s = reverb(s, 0.8, 0.25)
    return s/np.abs(s).max()*0.8

def pop():
    nn = int(0.12*SR); t = np.arange(nn)/SR
    s = np.sin(2*np.pi*np.cumsum(1400*np.exp(-t*30)+300)/SR) * np.exp(-t*45)
    return np.stack([s, s])*0.7

def click():
    nn = int(0.05*SR); t = np.arange(nn)/SR
    s = hp(rng.standard_normal(nn), 2500)*np.exp(-t*160) + 0.6*np.sin(2*np.pi*2200*t)*np.exp(-t*120)
    return np.stack([s, s])/np.abs(s).max()*0.6

def ding():
    nn = int(1.6*SR); t = np.arange(nn)/SR
    s = sum(a*np.sin(2*np.pi*f*t)*np.exp(-t*k) for f, a, k in [(1318.5, 1, 3), (2637, .4, 5), (1975.5, .3, 4), (3951, .15, 8)])
    s = reverb(s, 1.5, 0.3)
    return s/np.abs(s).max()*0.6

def riser(d=1.6):
    nn = int(d*SR); t = np.arange(nn)/SR
    f = 200*(16**(t/d))
    s = 0.4*saw(1, nn)*0  # placeholder
    s = np.sin(2*np.pi*np.cumsum(f)/SR) * 0.25 + 0.0
    nz = hp(rng.standard_normal(nn), 2000)*(t/d)**2*0.5
    s = (s*(t/d) + nz)
    s = reverb(s, 1.2, 0.3)
    return s/np.abs(s).max()*0.7

def impact():
    nn = int(1.4*SR); t = np.arange(nn)/SR
    boom = np.sin(2*np.pi*np.cumsum(40+90*np.exp(-t*12))/SR)*np.exp(-t*3.5)
    crack = lp(rng.standard_normal(nn), 3000)*np.exp(-t*25)*0.5
    s = reverb(boom+crack, 2.0, 0.3)
    return s/np.abs(s).max()*0.9

def swipe():
    return whoosh(0.28, True)

def typing():
    nn = int(0.03*SR); t = np.arange(nn)/SR
    s = bp(rng.standard_normal(nn), 1500, 6000)*np.exp(-t*250)
    return np.stack([s, s])/np.abs(s).max()*0.4

if __name__ == '__main__':
    sf.write(f'{OUT}/music.wav', track(44).T, SR)
    for name, fn in [('whoosh', whoosh), ('whoosh_dn', lambda: whoosh(0.5, False)), ('pop', pop), ('click', click),
                     ('ding', ding), ('riser', riser), ('impact', impact), ('swipe', swipe), ('tick', typing)]:
        sf.write(f'{OUT}/sfx_{name}.wav', fn().T, SR)
    print('done')
