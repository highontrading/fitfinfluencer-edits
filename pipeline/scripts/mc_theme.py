# Moon Crew (Mooncrew Club) brand theme for Reels: quiet luxury. Black #0A0A0B, ivory #EDE7DA, champagne #CDB98B,
# yellow #F2C94C only for the logo's "Club" + lines. Cormorant Garamond headlines, Michroma labels, Manrope body.
CSS = r"""
:root { --gold:#CDB98B; --gold2:#B39C69; --red:#D4917C; --green:#BFD0A8; --ink:#0A0A0B; --glass:rgba(10,10,11,.86); --line:rgba(237,231,218,.16); }
body { font-family:'Cormorant Garamond',serif; color:#EDE7DA; }
.title .ln, .stat .big, .col .v, .cta h1 { font-family:'Cormorant Garamond',serif; font-weight:600; letter-spacing:0; }
.title .w { margin:0 12px; }
.cw { font-family:'Manrope',sans-serif; font-weight:800; letter-spacing:0; color:#EDE7DA; }
.cw.hl, .cw.on { color:#CDB98B; }
.cw.hl.on { background:linear-gradient(180deg,#E6D8B0,#C2AC78); color:#0A0A0B; }
.kicker { font-family:'Michroma',sans-serif; font-weight:400; font-size:24px; letter-spacing:7px; color:#CDB98B; }
.chip, .check .row, .node, .stat .lbl, .stat .from, .pill, .col .k, .badge, .link, .cta p, .btn, #brand { font-family:'Manrope',sans-serif; }
.card { background:linear-gradient(160deg, rgba(22,21,20,.94), rgba(10,10,11,.93)); border:1.5px solid rgba(205,185,139,.28); }
.chip .ic { background:rgba(205,185,139,.14); border-color:rgba(205,185,139,.45); }
.node.target, .link.cur { background:linear-gradient(180deg,#E6D8B0,#C2AC78); color:#0A0A0B; }
.link.cur .acc, .node.target .acc { color:#5A4520; }
svg.wires path { stroke:#CDB98B; filter:none; }
.btn { background:linear-gradient(180deg,#EDE7DA,#CDB98B); color:#0A0A0B; box-shadow:0 18px 50px rgba(0,0,0,.5); letter-spacing:3px; }
.cta .shade { background:linear-gradient(180deg, rgba(10,10,11,0) 0%, rgba(10,10,11,.62) 36%, rgba(10,10,11,.96) 66%); }
#prog { background:linear-gradient(90deg,#B39C69,#EDE7DA); box-shadow:none; height:6px; }
#brand { background:rgba(10,10,11,.6); border-color:rgba(237,231,218,.18); font-family:'Michroma',sans-serif; font-weight:400; font-size:20px; letter-spacing:5px; color:#EDE7DA; }
#brand i { display:none; }
#leak { background:radial-gradient(closest-side, rgba(237,231,218,.55), rgba(205,185,139,.25) 45%, transparent 75%); }
"""
# final logo, exactly per brand spec (scaled 1.0 for a 1080-wide frame)
LOGO = ('<div style="display:flex;flex-direction:column;align-items:center">'
        '<svg width="140" height="120" viewBox="0 0 140 120"><defs><mask id="mcm"><rect width="140" height="120" fill="#fff"/><circle cx="74" cy="60" r="50" fill="#000"/></mask></defs>'
        '<circle cx="58" cy="60" r="50" fill="#EDE7DA" mask="url(#mcm)"/><circle cx="74" cy="60" r="50" fill="none" stroke="#EDE7DA" stroke-width="1.25"/></svg>'
        '<div style="height:56px"></div>'
        '<span style="font-family:\'Cormorant Garamond\',serif;font-weight:500;font-size:88px;line-height:1;letter-spacing:0.16em;padding-left:0.16em;color:#EDE7DA">MOONCREW</span>'
        '<div style="height:28px"></div>'
        '<div style="display:flex;align-items:center;gap:24px"><div style="width:122px;height:1px;background:#F2C94C"></div>'
        '<span style="font-family:\'Cormorant Garamond\',serif;font-style:italic;font-weight:500;font-size:44px;line-height:1;color:#F2C94C">Club</span>'
        '<div style="width:122px;height:1px;background:#F2C94C"></div></div></div>')
BRAND = {'text': 'MOONCREW CLUB'}
def end_card(S, t0, t1, ask, sub, y=1180):
    """Moon Crew end: black card, comment ask, then the final logo."""
    S.add({'type': 'cta', 't0': t0, 't1': t1, 'y': 300, 'kicker': 'Mooncrew Club', 'title': ask, 'sub': sub, 'button': 'COMMENT', 'hideCaps': True})
    S.add({'type': 'html', 't0': t0 + 0.8, 't1': t1, 'y': y, 'html': LOGO})
CSS += """
.chev { display:none; }
.cta .shade { background:rgba(10,10,11,.94); }
.cta h1 { font-size:96px; text-transform:none; }
.cta h1 .acc { font-style:italic; }
"""
CSS += """
.f-mc { font-family:'Cormorant Garamond',serif; font-weight:700; text-transform:uppercase; letter-spacing:.06em; }
.f-mci { font-family:'Cormorant Garamond',serif; font-style:italic; font-weight:600; letter-spacing:0; }
.f-label { font-family:'Michroma',sans-serif; font-weight:400; text-transform:uppercase; letter-spacing:.22em; }
"""
CSS += """
.f-bebas, .f-anton, .f-oswald, .f-inter { font-family:'Cormorant Garamond',serif !important; font-weight:700; letter-spacing:.03em; text-transform:uppercase; line-height:1.0; }
.kin .acc, .kin .red, .kin .green { font-style:italic; font-weight:600; text-transform:none; letter-spacing:0; }
"""
CSS += """
.kin.sh1 { text-shadow:0 2px 2px rgba(0,0,0,.65), 0 6px 26px rgba(0,0,0,.85), 0 0 70px rgba(0,0,0,.55); }
"""
