# SVG diagram builders for the 'anim' overlay component (timed reveals synced to narration). All sizes in px.
GOLD = '#FFC53D'; RED = '#FF4D5E'; GREEN = '#37F59B'; INK = '#0B0D12'; WHITE = '#FFFFFF'; MUTED = 'rgba(255,255,255,.55)'
FONT = "font-family:Poppins,sans-serif"; HEAD = "font-family:Oswald,sans-serif;font-weight:700;letter-spacing:2px"

def svg(w, h, body): return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">{body}</svg>'
def txt(x, y, s, t, size=40, fill=WHITE, anchor='middle', weight=700, style=HEAD, a='fade', d=0.45, extra=''):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{fill}" style="{style};font-weight:{weight}" data-t="{t:.2f}" data-a="{a}" data-d="{d}" {extra}>{s}</text>'
def title(w, s, t): return txt(w / 2, 46, s.upper(), t, 34, GOLD, style=HEAD)

def strike_list(words, times, t_final, final='BELIEF', w=900):
    """Each word appears and is struck through; then the final word pops in gold."""
    b = title(w, 'One thing every ultra-achiever had', times[0] - 0.3)
    for i, (wd, t) in enumerate(zip(words, times)):
        y = 140 + i * 105
        b += txt(w / 2, y, wd, t, 72, WHITE)
        b += f'<line x1="{w/2-230}" y1="{y-24}" x2="{w/2+230}" y2="{y-24}" stroke="{RED}" stroke-width="10" stroke-linecap="round" data-t="{t+0.55:.2f}" data-a="draw" data-d="0.35"/>'
    b += txt(w / 2, 140 + len(words) * 105 + 70, final, t_final, 130, GOLD, a='pop', d=0.6)
    return svg(w, 760, b)

def wall_door(t_wall, t_door, w=900):
    b = f'<g data-t="{t_wall:.2f}" data-a="fade">'
    b += f'<rect x="40" y="90" width="380" height="460" rx="24" fill="rgba(255,77,94,.12)" stroke="{RED}" stroke-width="4"/>'
    for r in range(8):
        for c in range(4):
            x = 60 + c * 88 + (44 if r % 2 else 0); y = 110 + r * 52
            if x + 80 < 410: b += f'<rect x="{x}" y="{y}" width="80" height="44" rx="4" fill="rgba(255,77,94,.35)"/>'
    b += '</g>' + txt(230, 610, 'NORMAL PEOPLE SEE A WALL', t_wall + 0.3, 30, RED)
    b += f'<g data-t="{t_door:.2f}" data-a="fade"><rect x="480" y="90" width="380" height="460" rx="24" fill="rgba(55,245,155,.10)" stroke="{GREEN}" stroke-width="4"/>'
    b += f'<rect x="560" y="140" width="220" height="410" fill="rgba(255,240,200,.85)"/></g>'
    b += f'<rect x="560" y="140" width="220" height="410" fill="#2b2016" stroke="{GREEN}" stroke-width="3" data-t="{t_door:.2f}" data-a="fade" data-off="{t_door+0.9:.2f}"/>'
    b += f'<polygon points="560,140 650,165 650,525 560,550" fill="#4a3522" stroke="{GREEN}" stroke-width="3" data-t="{t_door+0.9:.2f}" data-a="fade" data-d="0.5"/>'
    b += txt(670, 610, 'SUCCESSFUL PEOPLE SEE A DOOR', t_door + 0.3, 30, GREEN)
    return svg(w, 660, b)

# simplified medial (sagittal) view of the brain; DMN hubs at anatomically correct positions (front = left)
BRAIN = ('M 140 300 C 120 210 170 120 270 90 C 360 55 470 50 560 70 C 660 90 740 140 770 220 C 800 300 780 370 730 410 '
         'C 690 440 640 450 600 445 C 580 480 540 500 500 495 C 470 520 430 525 400 505 C 350 510 300 495 260 470 C 200 440 150 390 140 300 Z')
SULCI = ['M 230 160 C 280 200 300 260 290 320', 'M 330 110 C 360 170 370 240 350 300', 'M 450 80 C 450 150 440 220 420 290',
         'M 560 95 C 540 160 530 230 540 300', 'M 660 140 C 630 200 620 260 640 330', 'M 300 380 C 380 360 480 360 560 390']
HUBS = [('mPFC', 'Medial prefrontal cortex', 230, 300), ('PCC', 'Posterior cingulate cortex', 560, 250),
        ('AG', 'Angular gyrus', 680, 330), ('HC', 'Hippocampus (memory)', 470, 400)]
def dmn_brain(t, t_hubs=None, label='DEFAULT MODE NETWORK (DMN)', sub='Most active when you are NOT focused on a task', w=900):
    t_hubs = t_hubs or [t + 0.8 + i * 0.5 for i in range(4)]
    b = title(w, label, t)
    b += f'<g transform="translate(0,40)"><path d="{BRAIN}" fill="rgba(255,182,193,.10)" stroke="rgba(255,255,255,.75)" stroke-width="4" data-t="{t:.2f}" data-a="draw" data-d="1.2"/>'
    for i, s in enumerate(SULCI): b += f'<path d="{s}" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="3" data-t="{t+0.4+i*0.08:.2f}" data-a="draw" data-d="0.8"/>'
    for (a, _, x, y), (a2, _, x2, y2) in zip(HUBS, HUBS[1:] + HUBS[:1]):
        b += f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{GOLD}" stroke-width="4" stroke-dasharray="10 8" opacity=".8" data-t="{max(t_hubs)+0.3:.2f}" data-a="fade"/>'
    for (ab, name, x, y), th in zip(HUBS, t_hubs):
        b += f'<circle cx="{x}" cy="{y}" r="26" fill="{GOLD}" opacity=".9" data-t="{th:.2f}" data-a="pop"/>'
        b += f'<circle cx="{x}" cy="{y}" r="44" fill="none" stroke="{GOLD}" stroke-width="3" opacity=".45" data-t="{th+0.2:.2f}" data-a="pop"/>'
        b += txt(x, y + 76 if ab != 'PCC' else y - 54, name, th + 0.15, 26, WHITE, style=FONT, weight=600)
    b += txt(150, 470, 'FRONT', t + 1, 18, MUTED, style=HEAD) + txt(760, 470, 'BACK', t + 1, 18, MUTED, style=HEAD)
    b += '</g>' + txt(w / 2, 590, sub, max(t_hubs) + 0.4, 26, MUTED, style=FONT, weight=500)
    b += txt(w / 2, 620, 'Simplified medial view', max(t_hubs) + 0.4, 16, 'rgba(255,255,255,.35)', style=FONT, weight=500)
    return svg(w, 640, b)

def neurons(t, t_thick, label='NEW NEURAL PATHWAY', w=900, labels=('Neuron', 'Neuron')):
    def cell(x, y):
        dend = ''.join(f'<line x1="{x}" y1="{y}" x2="{x+dx}" y2="{y+dy}" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>' for dx, dy in ((-60, -50), (-70, 20), (-40, 70), (50, -70), (60, 60)))
        return dend + f'<circle cx="{x}" cy="{y}" r="38" fill="{GOLD}"/>'
    b = title(w, label, t)
    b += f'<g data-t="{t:.2f}" data-a="fade">{cell(170, 300)}</g><g data-t="{t+0.4:.2f}" data-a="fade">{cell(730, 300)}</g>'
    path = 'M 210 300 C 350 200 550 400 690 300'
    b += f'<path d="{path}" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round" data-t="{t+0.9:.2f}" data-a="draw" data-d="1.2"/>'
    for k, tt in enumerate(t_thick):
        b += f'<path d="{path}" fill="none" stroke="{GREEN}" stroke-width="{6+k*8}" stroke-linecap="round" opacity="{0.5+0.15*k}" data-t="{tt:.2f}" data-a="draw" data-d="0.9"/>'
    b += f'<circle r="12" fill="#fff" data-t="{t+1.4:.2f}" data-a="fade"><animateMotion dur="1.6s" repeatCount="indefinite" path="{path}"/></circle>'
    b += txt(170, 420, labels[0], t + 0.3, 24, MUTED, style=FONT, weight=600) + txt(730, 420, labels[1], t + 0.6, 24, MUTED, style=FONT, weight=600)
    return svg(w, 480, b)

def highway(times, labels=('1x', '10x', '100x', '1000x'), names=('JUNGLE PATH', 'WIDER PATH', 'ROAD', 'HIGHWAY'), w=900):
    b = title(w, 'Every repeat makes the road wider', times[0] - 0.2)
    widths = [4, 14, 34, 70]; cols = ['rgba(255,255,255,.6)', 'rgba(255,255,255,.7)', GOLD, GOLD]
    for tt, wd, col in zip(times, widths, cols):
        b += f'<path d="M 60 360 C 260 200 600 520 840 330" fill="none" stroke="{col}" stroke-width="{wd}" stroke-linecap="round" data-t="{tt:.2f}" data-a="draw" data-d="0.8"/>'
    for i, (tt, lb, nm) in enumerate(zip(times, labels, names)):
        x = 120 + i * 220
        b += txt(x, 560, lb, tt + 0.2, 52, GOLD, style=HEAD) + txt(x, 600, nm, tt + 0.3, 22, WHITE, style=FONT, weight=600)
    return svg(w, 640, b)

def loop(nodes, t_back, extra_feel=None, extra_beh=None, w=900):
    """Habit loop: nodes = [(label, color, t)] placed clockwise on a circle; arrows draw between them."""
    import math
    cx, cy, R = 450, 410, 300; b = title(w, 'The bad-habit loop', nodes[0][2] - 0.3); n = len(nodes)
    pos = [(cx + R * math.sin(2 * math.pi * i / n), cy - R * math.cos(2 * math.pi * i / n)) for i in range(n)]
    for i in range(n):
        (x1, y1), (x2, y2) = pos[i], pos[(i + 1) % n]; tt = nodes[(i + 1) % n][2] if i < n - 1 else t_back
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2; ox, oy = (mx - cx) * 0.35, (my - cy) * 0.35
        b += f'<path d="M {x1:.0f} {y1:.0f} Q {mx+ox:.0f} {my+oy:.0f} {x2:.0f} {y2:.0f}" fill="none" stroke="{GOLD}" stroke-width="5" stroke-dasharray="12 9" data-t="{tt-0.4:.2f}" data-a="draw" data-d="0.6"/>'
    for (lb, col, tt), (x, y) in zip(nodes, pos):
        wbox = max(170, len(lb) * 16 + 40)
        b += f'<g data-t="{tt:.2f}" data-a="pop"><rect x="{x-wbox/2:.0f}" y="{y-38:.0f}" width="{wbox}" height="76" rx="38" fill="{INK}" stroke="{col}" stroke-width="4"/>'
        b += f'<text x="{x:.0f}" y="{y+12:.0f}" text-anchor="middle" font-size="28" fill="{col}" style="{HEAD}">{lb}</text></g>'
    if extra_feel:
        for k, (s, tt) in enumerate(extra_feel): b += txt(cx, cy - 70 + k * 36, s, tt, 26, MUTED, style=FONT, weight=600, extra=f'data-off="{nodes[1][2]:.2f}"')
    if extra_beh:
        for k, (s, tt) in enumerate(extra_beh): b += txt(cx, cy - 50 + k * 36, s, tt, 26, MUTED, style=FONT, weight=600, extra=f'data-off="{nodes[2][2]:.2f}"')
    b += txt(cx, cy + 12, 'REPEAT', t_back, 40, RED, style=HEAD, a='pop')
    return svg(w, 780, b)

def ring(t, label='60 SEC', sub='Eyes closed. Do nothing.', t_breath=None, w=900, t_draw=None):
    t_draw = t_draw or t + 0.3
    b = f'<circle cx="450" cy="260" r="170" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="22" data-t="{t:.2f}" data-a="fade"/>'
    b += f'<circle cx="450" cy="260" r="170" fill="none" stroke="{GOLD}" stroke-width="22" stroke-linecap="round" transform="rotate(-90 450 260)" data-t="{t_draw:.2f}" data-a="draw" data-d="9"/>'
    b += txt(450, 280, label, t + 0.2, 80, WHITE, style=HEAD) + txt(450, 520, sub, t + 0.6, 34, WHITE, style=FONT, weight=600)
    if t_breath:
        b += f'<circle cx="450" cy="260" r="120" fill="rgba(55,245,155,.18)" stroke="{GREEN}" stroke-width="3" data-t="{t_breath:.2f}" data-a="breathe" data-per="4"/>'
        b += txt(450, 580, 'WATCH YOUR BREATH', t_breath + 0.2, 30, GREEN, style=HEAD)
    return svg(w, 620, b)

def seesaw(t, t_cen, t_dmn, w=900):
    b = title(w, 'Two networks. One at a time.', t)
    b += f'<polygon points="450,470 400,560 500,560" fill="rgba(255,255,255,.5)" data-t="{t:.2f}" data-a="fade"/>'
    beam = (f'<rect x="90" y="455" width="720" height="16" rx="8" fill="#fff"/>'
            f'<rect x="90" y="330" width="250" height="120" rx="20" fill="{INK}" stroke="{GOLD}" stroke-width="4"/>'
            f'<text x="215" y="385" text-anchor="middle" font-size="44" fill="{GOLD}" style="{HEAD}">CEN</text>'
            f'<text x="215" y="425" text-anchor="middle" font-size="22" fill="#fff" style="{FONT};font-weight:600">The CEO: focus, deadlines</text>'
            f'<rect x="560" y="330" width="250" height="120" rx="20" fill="{INK}" stroke="{GREEN}" stroke-width="4"/>'
            f'<text x="685" y="385" text-anchor="middle" font-size="44" fill="{GREEN}" style="{HEAD}">DMN</text>'
            f'<text x="685" y="425" text-anchor="middle" font-size="22" fill="#fff" style="{FONT};font-weight:600">The storyteller: ideas</text>')
    b += f'<g data-t="{t_cen:.2f}" data-a="tilt" data-from="0" data-to="-12" data-d="0.8">{beam}</g>'
    b = b.replace('</g>', '</g>', 1)
    b += txt(450, 130, 'BUSY + FOCUSED = CEN ON, DMN QUIET', t_cen + 0.2, 32, GOLD, extra=f'data-off="{t_dmn:.2f}"')
    b += txt(450, 130, 'BORED + IDLE = DMN ON: IDEAS SURFACE', t_dmn + 0.3, 32, GREEN)
    return svg(w, 600, b)

def tilt_seesaw(t, t_cen, t_dmn, w=900):
    """Seesaw with two phases: tips to CEN, then flips to DMN."""
    beam = (f'<rect x="90" y="455" width="720" height="16" rx="8" fill="#fff"/>'
            f'<rect x="90" y="330" width="250" height="120" rx="20" fill="{INK}" stroke="{GOLD}" stroke-width="4"/>'
            f'<text x="215" y="385" text-anchor="middle" font-size="44" fill="{GOLD}" style="{HEAD}">CEN</text>'
            f'<text x="215" y="425" text-anchor="middle" font-size="22" fill="#fff" style="{FONT};font-weight:600">The CEO: focus, deadlines</text>'
            f'<rect x="560" y="330" width="250" height="120" rx="20" fill="{INK}" stroke="{GREEN}" stroke-width="4"/>'
            f'<text x="685" y="385" text-anchor="middle" font-size="44" fill="{GREEN}" style="{HEAD}">DMN</text>'
            f'<text x="685" y="425" text-anchor="middle" font-size="22" fill="#fff" style="{FONT};font-weight:600">The storyteller: ideas</text>')
    b = title(w, 'Two networks. One at a time.', t)
    b += f'<polygon points="450,470 400,560 500,560" fill="rgba(255,255,255,.5)" data-t="{t:.2f}" data-a="fade"/>'
    b += f'<g data-t="{t_dmn:.2f}" data-a="tilt" data-from="0" data-to="24" data-d="0.9"><g data-t="{t_cen:.2f}" data-a="tilt" data-from="0" data-to="-12" data-d="0.8">{beam}</g></g>'
    b += txt(450, 130, 'BUSY + FOCUSED: CEN ON, DMN QUIET', t_cen + 0.2, 32, GOLD, extra=f'data-off="{t_dmn:.2f}"')
    b += txt(450, 130, 'BORED + IDLE: DMN ON, IDEAS SURFACE', t_dmn + 0.3, 32, GREEN)
    return svg(w, 600, b)

def chrono(t_am, t_bi, t_pm, w=900):
    """Energy curves across the day for the three chronotypes (shares are rough survey estimates)."""
    x0, x1, yb, yt = 90, 860, 520, 130
    def X(h): return x0 + (h - 6) / 18 * (x1 - x0)          # 6:00 -> 24:00
    def Y(e): return yb - e * (yb - yt)
    def path(pts): return 'M ' + ' L '.join(f'{X(h):.0f} {Y(e):.0f}' for h, e in pts)
    am = [(6, .55), (8, .95), (10, .9), (13, .7), (16, .5), (19, .35), (22, .2), (24, .1)]
    bi = [(6, .35), (9, .85), (11, .7), (14, .35), (17, .55), (19, .85), (21, .6), (24, .3)]
    pm = [(6, .1), (9, .25), (12, .4), (15, .55), (18, .7), (21, .9), (23, .95), (24, .9)]
    b = title(w, 'Energy through the day', t_am - 0.3)
    b += f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="rgba(255,255,255,.4)" stroke-width="3" data-t="{t_am-0.3:.2f}" data-a="fade"/>'
    for h in (6, 9, 12, 15, 18, 21, 24):
        lab = {6: '6 AM', 9: '9 AM', 12: 'NOON', 15: '3 PM', 18: '6 PM', 21: '9 PM', 24: '12 AM'}[h]
        b += txt(X(h), yb + 36, lab, t_am - 0.2, 20, MUTED, style=FONT, weight=600)
    for pts, col, tt, lab, share, lx, ly in ((am, GOLD, t_am, 'AM-SHIFTED', '~25%', 8.6, .99), (bi, GREEN, t_bi, 'BIPHASIC', '(MAJORITY)', 14.0, .12), (pm, RED, t_pm, 'PM-SHIFTED', '~10-15%', 21.2, 1.0)):
        b += f'<path d="{path(pts)}" fill="none" stroke="{col}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round" data-t="{tt:.2f}" data-a="draw" data-d="1.4"/>'
        b += txt(X(lx), Y(ly) - 22, f'{lab} {share}', tt + 0.9, 24, col, style=HEAD)
    b += txt(w / 2, 610, 'Shares are approximate (survey estimates)', t_pm + 1.2, 18, 'rgba(255,255,255,.4)', style=FONT, weight=500)
    return svg(w, 630, b)

def stress_curve(t_ok, t_burn, w=900, t0=None):
    x0, x1, yb = 70, 860, 470; t0 = t0 or t_ok - 0.3
    b = title(w, 'The stress cycle', t0)
    b += f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="rgba(255,255,255,.35)" stroke-width="3" data-t="{t0:.2f}" data-a="fade"/>'
    ok = f'M {x0} {yb} C 120 {yb} 140 200 190 200 C 240 200 260 {yb} 310 {yb} C 350 {yb} 370 220 420 220 C 470 220 490 {yb} 540 {yb}'
    b += f'<path d="{ok}" fill="none" stroke="{GREEN}" stroke-width="7" stroke-linecap="round" data-t="{t_ok:.2f}" data-a="draw" data-d="2.2"/>'
    b += txt(305, 150, 'UP, WORK, DOWN = HEALTHY', t_ok + 1.2, 28, GREEN)
    burn = f'M 540 {yb} C 570 {yb} 580 180 620 170 L 860 160'
    b += f'<path d="{burn}" fill="none" stroke="{RED}" stroke-width="7" stroke-linecap="round" data-t="{t_burn:.2f}" data-a="draw" data-d="1.6"/>'
    b += txt(730, 120, 'ALWAYS UP = BURNOUT', t_burn + 1.0, 30, RED)
    b += txt(705, 210, 'morning to night, week after week', t_burn + 1.3, 20, MUTED, style=FONT, weight=500)
    return svg(w, 560, b)

def filter_funnel(t, t_pass, w=900):
    b = title(w, 'Your beliefs = your brain\'s search filter', t)
    b += f'<path d="M 200 140 L 700 140 L 520 330 L 520 470 L 380 470 L 380 330 Z" fill="rgba(255,255,255,.06)" stroke="#fff" stroke-width="4" data-t="{t:.2f}" data-a="draw" data-d="0.9"/>'
    import random
    rnd = random.Random(3)
    for k in range(14):
        good = k % 3 == 0; x = 230 + rnd.random() * 440; tt = t_pass + k * 0.18
        col = GREEN if good else RED
        b += f'<circle cx="{x:.0f}" cy="105" r="13" fill="{col}" data-t="{tt:.2f}" data-a="fade" data-off="{tt+0.9:.2f}"/>'
        if good: b += f'<circle cx="450" cy="{500+ (k//3)*0:.0f}" r="13" fill="{GREEN}" data-t="{tt+0.8:.2f}" data-a="pop"/>'
    b += txt(450, 560, 'ONLY BELIEF-MATCHING DATA GETS THROUGH', t_pass + 1.2, 28, GREEN)
    return svg(w, 600, b)
