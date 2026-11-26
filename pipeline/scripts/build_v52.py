# Trailer for long-form 51: strongest lines, a question card before each, cine bars, music build, title card.
import sys, json
from spec_lib2 import Spec
W, H = 1920, 1080
S_ = Spec(sys.argv[1], 'v52', mood='serious', size=(W, H)); T = S_.T
D = S_.tl['dur']; edl = json.load(open('../edl/v52.json')); shots = S_.tl['shots']
Q = {31: 'WHY DO SOME PEOPLE SEE <b>DOORS</b> WHERE YOU SEE WALLS?', 96: 'WHY DOES YOUR BRAIN ONLY FIND PROOF OF WHAT YOU <b>ALREADY BELIEVE</b>?',
     322: 'WHY ARE BAD HABITS SO <b>HARD TO BREAK</b>?', 410: 'WHAT KEEPS YOU <b>STUCK IN THE LOOP</b>?', 508: 'WHY DO YOUR BEST IDEAS COME <b>IN THE SHOWER</b>?',
     580: 'IS THE <b>5 AM CLUB</b> A LIE?', 740: 'IS SCROLLING REALLY <b>A BREAK</b>?', 790: 'WHAT IS YOUR BRAIN <b>REALLY</b> CAPABLE OF?'}
card = lambda q: ('<div style="width:1920px;height:1080px;background:rgba(4,5,8,.92);display:flex;align-items:center;justify-content:center">'
                  '<div style="font-family:Anton,sans-serif;font-size:104px;line-height:1.08;color:#fff;text-align:center;max-width:1500px;letter-spacing:1px">'
                  + q.replace('<b>', '<span style="color:#FFC53D">').replace('</b>', '</span>') + '</div></div>')
pre = []
for it, sh in zip(edl['keep'], shots):
    if 'pre' in it:
        t0 = sh['out0']; t1 = t0 + it['pre'] / 1.1 - 0.05; pre.append((t0, t1))
        S_.add({'type': 'html', 't0': t0, 't1': t1, 'y': 0, 'html': card(Q[it['c']]), 'hideCaps': True})
        S_.fx('whoosh_soft', t0, -12); S_.fx('hit_soft', t1 - 0.05, -16)
S_.add({'type': 'cine', 't0': 0, 't1': D, 'h': 120})
title_t = D - 0.02
S_.add({'type': 'html', 't0': title_t, 't1': D + 3.2, 'y': 0, 'html':
        '<div style="width:1920px;height:1080px;background:#000;display:flex;flex-direction:column;align-items:center;justify-content:center">'
        '<div style="font-family:Oswald,sans-serif;font-weight:700;font-size:40px;letter-spacing:12px;color:#FFC53D">FITFINFLUENCER PRESENTS</div>'
        '<div style="font-family:Anton,sans-serif;font-size:128px;line-height:1.05;color:#fff;text-align:center;max-width:1600px;margin-top:30px">WHY IS A BILLIONAIRE\'S<br>BRAIN <span style="color:#FFC53D">DIFFERENT?</span></div>'
        '<div style="font-family:Poppins,sans-serif;font-weight:600;font-size:40px;color:rgba(255,255,255,.7);margin-top:34px">The brain science school never taught you</div></div>'})
S_.fx('impact', title_t, -10)
S_.cam['faceY'] = 0.42; S_.cam['grain'] = 5; S_.alt_zoom([1.05, 1.2, 1.1, 1.25])
caps = S_.captions(max_words=4, max_chars=26, hl_pats=[r'deewar', r'darwaaza', r'beliefs', r'highway', r'sharam', r'stress', r'ideas', r'bore', r'porn', r'scrolling', r'break', r'machine'])
S_.save(caps, cap_y=900, hold=3.2, extra={'capScale': 0.72, 'vigInCompose': True})
json.dump({'pre': pre, 'title': title_t}, open(f'{sys.argv[1]}/v52_pre.json', 'w'))
json.dump({'dur': D + 3.2, 'sections': [{'t0': 0, 't1': D + 3.2, 'mood': 'trailer'}], 'drops': [], 'hits': [title_t]}, open(f'{sys.argv[1]}/v52_music.json', 'w'))
