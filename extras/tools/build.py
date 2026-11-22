#!/usr/bin/env python3
"""Builds the five self-contained profile SVGs. Edit CONFIG, drop real id.png /
right_pointing.png next to this file, then run:  python3 build.py
"""
import base64, json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "assets")
FONTS = os.path.join(HERE, "..", "node_modules", "@fontsource")
os.makedirs(OUT, exist_ok=True)

CONFIG = dict(
    name1="ROHAN", name2="MISHRA", user="rohan-mishra07",
    greeting="> hello, world. i'm",
    roles=["Developer Engineer", "Full-Stack Builder", "Python + JavaScript", "Always Shipping"],
    pitch="I build web platforms and tools, one repo at a time.",
    chips=["@rohan-mishra07", "Developer Engineer"],
    capabilities=[("Full-stack web apps", "React, Vite, Spring Boot"),
                  ("Backend services", "APIs and task tooling"),
                  ("Python projects", "Platform tooling"),
                  ("Shipping live", "Deployed on Vercel")],
    slides=[("NOW BUILDING", "SkillSphere Nexus", "Learning, skill analytics, workforce tools and an AI copilot in one platform."),
            ("PYTHON PROJECT", "Industrial Knowledge Platform", "A Python project in the industrial knowledge space."),
            ("LIVE ON VERCEL", "3D AI Portfolio", "A 3D-themed portfolio site, deployed and live.")],
    stack_orbit=["python", "javascript", "react", "vite", "springboot", "ejs", "git", "github", "vercel"],
    stack_groups=[("LANGUAGES", ["Python", "JavaScript", "Java"]),
                  ("FRONTEND", ["React", "Vite", "EJS"]),
                  ("BACKEND", ["Spring Boot"]),
                  ("TOOLS", ["Git", "GitHub", "Vercel"])],
    metrics=[("17", "Public repos"), ("2", "Stars earned"), ("2", "Live demos")],
    metrics_date="20 NOV 2026",
    socials=[("LinkedIn", "in/rohan-mishra-6193162a5", "in"),
             ("Instagram", "@na_nu5967", "instagram"),
             ("GitHub", "@rohan-mishra07", "github")],
)
C = CONFIG
NAVY, BLUE, RED, WHITE = "#070b16", "#247bff", "#ff354f", "#f2f4fa"
ICONS = json.load(open(os.path.join(HERE, "icons.json")))


def b64(path):
    return base64.b64encode(open(path, "rb").read()).decode()


def font_css():
    sg = b64(f"{FONTS}/space-grotesk/files/space-grotesk-latin-700-normal.woff2")
    sg5 = b64(f"{FONTS}/space-grotesk/files/space-grotesk-latin-500-normal.woff2")
    jb = b64(f"{FONTS}/jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2")
    ff = lambda n, w, d: ("@font-face{font-family:'%s';font-weight:%d;src:url(data:font/woff2;base64,%s) format('woff2')}" % (n, w, d))
    return ff("SG", 700, sg) + ff("SG", 500, sg5) + ff("JB", 500, jb)


FONT_CSS = font_css()
PORTRAIT = b64(os.path.join(HERE, "id.png"))
POINTING = b64(os.path.join(HERE, "right_pointing.png"))


def wrap(p, w, h, css, body, defs=""):
    """Common shell: navy card, dot texture, gradient hairline border."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<defs>
<style>{FONT_CSS}
.{p}d{{font-family:'SG','Helvetica Neue',Arial,sans-serif}}
.{p}m{{font-family:'JB','SFMono-Regular',Consolas,monospace}}
{css}
@media (prefers-reduced-motion: reduce){{*{{animation:none!important}}}}
</style>
<linearGradient id="{p}hair" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{RED}"/></linearGradient>
<pattern id="{p}dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{WHITE}" fill-opacity=".07"/></pattern>
{defs}
</defs>
<rect width="{w}" height="{h}" rx="28" fill="{NAVY}"/>
<rect width="{w}" height="{h}" rx="28" fill="url(#{p}dots)"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="27" fill="none" stroke="url(#{p}hair)" stroke-width="1.5" stroke-opacity=".75"/>
{body}
</svg>'''


def icon(name, size, color=None):
    i = ICONS[name]
    col = color or ("#" + i["hex"])
    # lift near-black brand colours so they stay visible on navy
    if not color and int(i["hex"][0:2], 16) < 0x40 and int(i["hex"][2:4], 16) < 0x40:
        col = WHITE
    s = size / 24
    return f'<g transform="scale({s:.3f})"><path d="{i["path"]}" fill="{col}"/></g>'


def write(name, svg):
    path = os.path.join(OUT, name)
    open(path, "w").write(svg)
    print(name, round(len(svg) / 1024), "KB")


# ---------------------------------------------------------------- hero
def hero():
    p = "h"
    W, H = 900, 460
    greet = C["greeting"]
    gw = len(greet) * 12.0
    css = f'''
.{p}fade{{animation:{p}in .9s ease both}}
.{p}f2{{animation-delay:.6s}}.{p}f3{{animation-delay:1.2s}}
@keyframes {p}in{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
@keyframes {p}fl{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-8px)}}}}
.{p}float{{animation:{p}fl 6s ease-in-out infinite}}
'''
    defs = f'''
<clipPath id="{p}cg"><rect x="56" y="70" width="{gw:.0f}" height="36"><animate attributeName="width" from="0" to="{gw:.0f}" dur="1.4s" begin="0s" calcMode="discrete" fill="freeze" values="0;{gw*.25:.0f};{gw*.5:.0f};{gw*.75:.0f};{gw:.0f}" keyTimes="0;.25;.5;.75;1"/></rect></clipPath>
<clipPath id="{p}c1"><rect x="40" y="108" width="540" height="96"/></clipPath>
<clipPath id="{p}c2"><rect x="40" y="188" width="540" height="96"/></clipPath>
<linearGradient id="{p}ng" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{WHITE}"/><stop offset="1" stop-color="#9fc3ff"/></linearGradient>
<radialGradient id="{p}glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{BLUE}" stop-opacity=".45"/><stop offset=".6" stop-color="{RED}" stop-opacity=".12"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>'''

    def rise(y, text, delay):
        kt = f"0;{delay:.3f};1"
        return (f'<g clip-path="url(#{p}c{1 if y < 200 else 2})"><g>'
                f'<animateTransform attributeName="transform" type="translate" begin="0s" dur="2.2s" fill="freeze" calcMode="spline" '
                f'keyTimes="{kt}" keySplines="0 0 1 1;.2 .8 .2 1" values="0 110;0 110;0 0"/>'
                f'<text x="56" y="{y}" class="{p}d" font-size="88" font-weight="700" fill="url(#{p}ng)" letter-spacing="-2">{text}</text></g></g>')

    roles = ""
    n = len(C["roles"])
    cyc = 3 * n
    for i, r in enumerate(C["roles"]):
        a, b = i / n, (i + 1) / n
        eps = .02
        if i == 0:
            kt, vals = f"0;{b-eps:.3f};{b:.3f};1", "1;1;0;0"
        else:
            kt = f"0;{a:.3f};{a+eps:.3f};{b-eps:.3f};{b:.3f};1"
            vals = "0;0;1;1;0;0"
        roles += (f'<text x="56" y="338" class="{p}m" font-size="28" fill="{RED}" opacity="{1 if i == 0 else 0}">'
                  f'<animate attributeName="opacity" begin="0s" dur="{cyc}s" repeatCount="indefinite" keyTimes="{kt}" values="{vals}"/>'
                  f'<tspan fill="{BLUE}">&#9656; </tspan>{r}</text>')

    chips = ""
    x = 56
    for c in C["chips"]:
        w = len(c) * 9.6 + 36
        chips += (f'<rect x="{x}" y="402" width="{w:.0f}" height="36" rx="18" fill="{WHITE}" fill-opacity=".05" stroke="{BLUE}" stroke-opacity=".5"/>'
                  f'<text x="{x+w/2:.0f}" y="425" text-anchor="middle" class="{p}m" font-size="15" fill="{WHITE}">{c}</text>')
        x += w + 12

    body = f'''
<circle cx="720" cy="250" r="230" fill="url(#{p}glow)"/>
<g class="{p}float"><image href="data:image/png;base64,{PORTRAIT}" x="560" y="70" width="300" height="360" preserveAspectRatio="xMidYMid meet"/></g>
<text x="56" y="96" class="{p}m" font-size="20" fill="{BLUE}" clip-path="url(#{p}cg)">{greet}</text>
{rise(190, C["name1"], .3)}
{rise(270, C["name2"], .45)}
<g class="{p}fade {p}f2">{roles}</g>
<text x="56" y="380" class="{p}m {p}fade {p}f3" font-size="16" fill="{WHITE}" fill-opacity=".72">{C["pitch"]}</text>
<g class="{p}fade {p}f3">{chips}</g>'''
    write("hero.svg", wrap(p, W, H, css, body, defs))


# ---------------------------------------------------------------- about
def about():
    p = "a"
    W, H = 900, 460
    css = f'''
.{p}fade{{animation:{p}in .8s ease both}}
@keyframes {p}in{{from{{opacity:0;transform:translateX(-14px)}}to{{opacity:1;transform:none}}}}
'''
    cards = ""
    for i, (t, s) in enumerate(C["capabilities"]):
        y = 118 + i * 78
        cards += (f'<g class="{p}fade" style="animation-delay:{i*.15:.2f}s">'
                  f'<rect x="48" y="{y}" width="360" height="64" rx="16" fill="{WHITE}" fill-opacity=".04" stroke="{BLUE}" stroke-opacity=".35"/>'
                  f'<rect x="48" y="{y+14}" width="4" height="36" rx="2" fill="{RED}"/>'
                  f'<text x="72" y="{y+28}" class="{p}d" font-size="20" font-weight="700" fill="{WHITE}">{t}</text>'
                  f'<text x="72" y="{y+49}" class="{p}m" font-size="13" fill="{WHITE}" fill-opacity=".62">{s}</text></g>')
    n = len(C["slides"])
    cyc = 4 * n
    sl = ""
    for i, (tag, title, line) in enumerate(C["slides"]):
        a, b = i / n, (i + 1) / n
        e = .02
        if i == 0:
            kt, vals = f"0;{b-e:.3f};{b:.3f};1", "1;1;0;0"
        else:
            kt = f"0;{a:.3f};{a+e:.3f};{b-e:.3f};{b:.3f};1"
            vals = "0;0;1;1;0;0"
        # wrap the one-line description at ~34 chars
        words, lines, cur = line.split(), [], ""
        for w_ in words:
            if len(cur) + len(w_) + 1 > 34:
                lines.append(cur); cur = w_
            else:
                cur = (cur + " " + w_).strip()
        lines.append(cur)
        txt = "".join(f'<text x="470" y="{268+k*24}" class="{p}m" font-size="15" fill="{WHITE}" fill-opacity=".75">{l}</text>' for k, l in enumerate(lines))
        sl += (f'<g opacity="{1 if i == 0 else 0}"><animate attributeName="opacity" begin="0s" dur="{cyc}s" repeatCount="indefinite" keyTimes="{kt}" values="{vals}"/>'
               f'<text x="470" y="170" class="{p}m" font-size="14" fill="{RED}" letter-spacing="3">{tag}</text>'
               f'<text x="470" y="222" class="{p}d" font-size="{min(34, int(376/(len(title)*.6)))}" font-weight="700" fill="{WHITE}">{title}</text>{txt}</g>')
    bars = ""
    bw = 120
    for i in range(n):
        x = 470 + i * (bw + 10)
        a, b = i / n, (i + 1) / n
        kt = f"0;{a:.3f};{b:.3f};1" if i else f"0;{b:.3f};1"
        vals = f"0;0;{bw};{bw}" if i else f"0;{bw};{bw}"
        # first bar starts full-width when animation unsupported (base value)
        bars += (f'<rect x="{x}" y="380" width="{bw}" height="5" rx="2.5" fill="{WHITE}" fill-opacity=".14"/>'
                 f'<rect x="{x}" y="380" width="{bw if i == 0 else 0}" height="5" rx="2.5" fill="{BLUE}">'
                 f'<animate attributeName="width" begin="0s" dur="{cyc}s" repeatCount="indefinite" keyTimes="{kt}" values="{vals}"/></rect>')
        if i:  # reset bars to empty after their slide ends
            pass
    body = f'''
<text x="48" y="78" class="{p}m" font-size="14" fill="{BLUE}" letter-spacing="3">WHAT I DO</text>
<text x="470" y="78" class="{p}m" font-size="14" fill="{BLUE}" letter-spacing="3">THINGS I'M BUILDING</text>
{cards}
<rect x="446" y="100" width="408" height="310" rx="22" fill="{WHITE}" fill-opacity=".04" stroke="url(#{p}hair)" stroke-opacity=".7"/>
{sl}{bars}'''
    write("about-life.svg", wrap(p, W, H, css, body))


# ---------------------------------------------------------------- stack
def ellipse_path(rx, ry, start):
    # closed ellipse path starting at angle `start` (degrees) so icons are spread out
    a = math.radians(start)
    x0, y0 = rx * math.cos(a), ry * math.sin(a)
    x1, y1 = -x0, -y0
    return (f"M{x0:.1f},{y0:.1f} A{rx},{ry} 0 1,1 {x1:.1f},{y1:.1f} A{rx},{ry} 0 1,1 {x0:.1f},{y0:.1f} Z")


def stack():
    p = "s"
    W, H = 900, 600
    css = f'''
.{p}fade{{animation:{p}in .8s ease both}}
@keyframes {p}in{{from{{opacity:0;transform:scale(.92)}}to{{opacity:1;transform:none}}}}
'''
    cx, cy = 450, 230
    orbits = [(340, 88, -18, 34), (255, 66, 22, 28), (170, 44, -52, 22)]
    names = C["stack_orbit"]
    per = math.ceil(len(names) / 3)
    g = ""
    k = 0
    for oi, (rx, ry, rot, dur) in enumerate(orbits):
        g += f'<g transform="translate({cx},{cy}) rotate({rot})">'
        g += f'<ellipse rx="{rx}" ry="{ry}" fill="none" stroke="url(#{p}hair)" stroke-opacity=".5" stroke-width="1.5" stroke-dasharray="3 7"/>'
        for j in range(per):
            if k >= len(names):
                break
            nm = names[k]; k += 1
            start = 360 / per * j + oi * 40
            path = ellipse_path(rx, ry, start)
            # counter-rotate icon so it stays upright is unnecessary (tilt is small); keep simple
            g += (f'<g><animateMotion begin="0s" dur="{dur}s" repeatCount="indefinite" path="{path}"/>'
                  f'<g transform="rotate({-rot})"><circle r="25" fill="{NAVY}" stroke="{WHITE}" stroke-opacity=".25"/>'
                  f'<g transform="translate(-13,-13)">{icon(nm, 26)}</g></g></g>')
        g += '</g>'
    # static start positions are the path start points => readable if SMIL unsupported
    chips = ""
    x0 = 48
    colw = (W - 96) / len(C["stack_groups"])
    for gi, (title, items) in enumerate(C["stack_groups"]):
        x = x0 + gi * colw
        chips += f'<text x="{x:.0f}" y="438" class="{p}m" font-size="13" fill="{RED}" letter-spacing="3">{title}</text>'
        for ii, it in enumerate(items):
            w = len(it) * 9.5 + 28
            chips += (f'<g class="{p}fade" style="animation-delay:{gi*.15+ii*.1:.2f}s">'
                      f'<rect x="{x:.0f}" y="{454+ii*44}" width="{w:.0f}" height="34" rx="17" fill="{WHITE}" fill-opacity=".05" stroke="{BLUE}" stroke-opacity=".5"/>'
                      f'<text x="{x+w/2:.0f}" y="{476+ii*44}" text-anchor="middle" class="{p}d" font-size="16" font-weight="500" fill="{WHITE}">{it}</text></g>')
    body = f'''
<text x="48" y="64" class="{p}m" font-size="14" fill="{BLUE}" letter-spacing="3">TECH STACK</text>
<circle cx="{cx}" cy="{cy}" r="60" fill="{BLUE}" fill-opacity=".14" stroke="{BLUE}" stroke-opacity=".6"/>
<text x="{cx}" y="{cy+8}" text-anchor="middle" class="{p}d" font-size="22" font-weight="700" fill="{WHITE}">STACK</text>
{g}{chips}'''
    write("stack.svg", wrap(p, W, H, css, body))


# ---------------------------------------------------------------- id card
def barcode(seed, x, y, w, h):
    bars, cur = "", x
    i = 0
    while cur < x + w - 3:
        v = ord(seed[i % len(seed)]) + i * 7
        bw = 1.5 + (v % 3)
        bars += f'<rect x="{cur:.1f}" y="{y}" width="{bw:.1f}" height="{h}" fill="{WHITE}"/>'
        cur += bw + 1.5 + (v // 3 % 3)
        i += 1
    return bars


def idcard():
    p = "i"
    W, H = 900, 640
    px = 640  # pivot x
    css = f'''
.{p}fade{{animation:{p}in .8s ease both}}
@keyframes {p}in{{from{{opacity:0;transform:translateX(-14px)}}to{{opacity:1;transform:none}}}}
'''
    # damped pendulum then gentle +/-1.7deg swing (single SMIL track, long loop)
    vals, kts = [], []
    total = 600.0
    damp = [16, -11, 7, -4.5, 2.8, -1.9]
    t = 0.0
    pts = [(0.0, 0.0)]
    step = 0.9
    for d in damp:
        t += step; pts.append((t, d))
    per = 1.5
    while t + per < total:
        t += per; pts.append((t, -1.7 if (len(pts) % 2) else 1.7))
    pts.append((total, pts[-1][1]))
    kts = ";".join(f"{a/total:.6f}" for a, _ in pts)
    vals = ";".join(f"{b} {px} 0" for _, b in pts)
    swing = (f'<animateTransform attributeName="transform" type="rotate" begin="0s" dur="{total:.0f}s" repeatCount="indefinite" '
             f'calcMode="spline" keyTimes="{kts}" values="{vals}" keySplines="{";".join(["0.45 0 0.55 1"]*(len(pts)-1))}"/>')
    drop = (f'<animateTransform attributeName="transform" type="translate" begin="0s" dur="1.2s" fill="freeze" calcMode="spline" '
            f'keyTimes="0;1" keySplines=".3 1 .5 1" values="0 -420;0 0" additive="replace"/>')

    m = ""
    for i, (v, l) in enumerate(C["metrics"]):
        y = 150 + i * 96
        m += (f'<g class="{p}fade" style="animation-delay:{i*.18+.3:.2f}s">'
              f'<rect x="48" y="{y}" width="340" height="80" rx="18" fill="{WHITE}" fill-opacity=".04" stroke="{BLUE}" stroke-opacity=".35"/>'
              f'<text x="72" y="{y+54}" class="{p}d" font-size="46" font-weight="700" fill="{WHITE}">{v}</text>'
              f'<text x="150" y="{y+48}" class="{p}m" font-size="15" fill="{WHITE}" fill-opacity=".7">{l}</text></g>')
    cardx, cardy, cw, ch = px - 150, 190, 300, 410
    sweep = (f'<g clip-path="url(#{p}cc)"><rect x="{cardx-120}" y="{cardy-20}" width="70" height="{ch+40}" fill="url(#{p}foil)" transform="skewX(-20)">'
             f'<animate attributeName="x" begin="0s" dur="6s" repeatCount="indefinite" keyTimes="0;.6;1" values="{cardx-120};{cardx+cw+120};{cardx+cw+120}"/></rect></g>')
    defs = f'''
<clipPath id="{p}cc"><rect x="{cardx}" y="{cardy}" width="{cw}" height="{ch}" rx="22"/></clipPath>
<linearGradient id="{p}foil" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="{p}card" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#101a36"/><stop offset="1" stop-color="#0b1022"/></linearGradient>
<linearGradient id="{p}metal" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a93a8"/><stop offset=".5" stop-color="#e9edf5"/><stop offset="1" stop-color="#8a93a8"/></linearGradient>'''
    card = f'''
<g>{drop}<g>{swing}
<polygon points="{px-30},0 {px+30},0 {px+14},{cardy-34} {px-14},{cardy-34}" fill="{RED}"/>
<polygon points="{px-30},0 {px-14},0 {px-2},{cardy-34} {px-14},{cardy-34}" fill="#000" fill-opacity=".18"/>
<rect x="{px-22}" y="{cardy-40}" width="44" height="22" rx="6" fill="url(#{p}metal)"/>
<rect x="{px-9}" y="{cardy-24}" width="18" height="30" rx="8" fill="none" stroke="url(#{p}metal)" stroke-width="5"/>
<rect x="{cardx}" y="{cardy}" width="{cw}" height="{ch}" rx="22" fill="url(#{p}card)" stroke="url(#{p}hair)" stroke-width="2"/>
<rect x="{px-34}" y="{cardy+14}" width="68" height="10" rx="5" fill="{NAVY}" stroke="{WHITE}" stroke-opacity=".3"/>
<text x="{px}" y="{cardy+50}" text-anchor="middle" class="{p}m" font-size="12" fill="{BLUE}" letter-spacing="4">DEVELOPER ID</text>
<circle cx="{px}" cy="{cardy+130}" r="62" fill="{BLUE}" fill-opacity=".15" stroke="{BLUE}" stroke-opacity=".6"/>
<image href="data:image/png;base64,{PORTRAIT}" x="{px-52}" y="{cardy+68}" width="104" height="125" preserveAspectRatio="xMidYMid meet"/>
<text x="{px}" y="{cardy+235}" text-anchor="middle" class="{p}d" font-size="28" font-weight="700" fill="{WHITE}">{C["name1"].title()} {C["name2"].title()}</text>
<text x="{px}" y="{cardy+262}" text-anchor="middle" class="{p}m" font-size="14" fill="{RED}">{C["roles"][0]}</text>
<text x="{px}" y="{cardy+286}" text-anchor="middle" class="{p}m" font-size="12" fill="{WHITE}" fill-opacity=".6">github.com/{C["user"]}</text>
<g transform="translate(0,0)">{barcode(C["user"], px-110, cardy+314, 220, 56)}</g>
<text x="{px}" y="{cardy+392}" text-anchor="middle" class="{p}m" font-size="10" fill="{WHITE}" fill-opacity=".5" letter-spacing="3">{C["user"].upper()}</text>
{sweep}
</g></g>'''
    body = f'''
<text x="48" y="78" class="{p}m" font-size="14" fill="{BLUE}" letter-spacing="3">GITHUB SNAPSHOT</text>
<text x="48" y="108" class="{p}m" font-size="13" fill="{WHITE}" fill-opacity=".6">Verified {C["metrics_date"]}</text>
{m}
<text x="48" y="470" class="{p}m" font-size="12" fill="{WHITE}" fill-opacity=".5">Counts from the public profile on the date above.</text>
{card}'''
    write("id-dashboard.svg", wrap(p, W, H, css, body, defs))


# ---------------------------------------------------------------- connect
def connect():
    p = "c"
    W, H = 900, 440
    css = f'''
.{p}fade{{animation:{p}in .8s ease both}}
@keyframes {p}in{{from{{opacity:0;transform:translateX(16px)}}to{{opacity:1;transform:none}}}}
'''
    cards = ""
    for i, (label, handle, ic) in enumerate(C["socials"]):
        y = 96 + i * 100
        if ic == "in":
            mark = (f'<rect x="0" y="0" width="34" height="34" rx="7" fill="#0A66C2"/>'
                    f'<text x="17" y="25" text-anchor="middle" class="{p}d" font-size="20" font-weight="700" fill="#fff">in</text>')
        else:
            mark = icon(ic, 34)
        arrow = (f'<g transform="translate(404,{y+42})"><g>'
                 f'<animateTransform attributeName="transform" type="translate" begin="0s" dur="1.6s" repeatCount="indefinite" keyTimes="0;.5;1" values="0 0;8 0;0 0"/>'
                 f'<path d="M0,-9 L10,0 L0,9" fill="none" stroke="{RED}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g></g>')
        cards += (f'<g class="{p}fade" style="animation-delay:{i*.2:.1f}s">'
                  f'<rect x="440" y="{y}" width="420" height="84" rx="20" fill="{WHITE}" fill-opacity=".05" stroke="url(#{p}hair)" stroke-opacity=".7"/>'
                  f'<g transform="translate(468,{y+25})">{mark}</g>'
                  f'<text x="524" y="{y+38}" class="{p}d" font-size="22" font-weight="700" fill="{WHITE}">{label}</text>'
                  f'<text x="524" y="{y+62}" class="{p}m" font-size="14" fill="{WHITE}" fill-opacity=".65">{handle}</text></g>{arrow}')
    body = f'''
<text x="48" y="64" class="{p}m" font-size="14" fill="{BLUE}" letter-spacing="3">LET'S CONNECT</text>
<circle cx="220" cy="250" r="190" fill="{BLUE}" fill-opacity=".10"/>
<image href="data:image/png;base64,{POINTING}" x="20" y="60" width="400" height="360" preserveAspectRatio="xMidYMax meet"/>
{cards}'''
    write("connect.svg", wrap(p, W, H, css, body))


if __name__ == "__main__":
    hero(); about(); stack(); idcard(); connect()
