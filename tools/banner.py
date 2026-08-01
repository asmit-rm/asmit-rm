from config import NAME, ALIAS, ROLE, TAGLINE  # ← "tools." HATAYA
from pathlib import Path

WIDTH = 1200
HEIGHT = 320

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{WIDTH}"
     height="{HEIGHT}"
     viewBox="0 0 {WIDTH} {HEIGHT}">

    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#05070d"/>
            <stop offset="100%" stop-color="#0b1220"/>
        </linearGradient>

        <linearGradient id="title" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#00d9ff"/>
            <stop offset="100%" stop-color="#7df9ff"/>
        </linearGradient>
    </defs>

    <rect width="100%" height="100%" fill="url(#bg)"/>

    <line x1="50" y1="275" x2="1150" y2="275"
          stroke="#00d9ff"
          stroke-width="2"/>

    <text
        x="60"
        y="90"
        font-size="54"
        font-family="monospace"
        font-weight="bold"
        fill="url(#title)">
        {NAME}
    </text>

    <text
        x="60"
        y="135"
        font-size="24"
        font-family="monospace"
        fill="#7df9ff">
        AKA {ALIAS}
    </text>

    <text
        x="60"
        y="180"
        font-size="22"
        font-family="monospace"
        fill="#ffffff">
        {ROLE}
    </text>

    <text
        x="60"
        y="225"
        font-size="18"
        font-family="monospace"
        fill="#8b949e">
        {TAGLINE}
    </text>

</svg>
"""

Path("assets/banner.svg").write_text(svg, encoding="utf-8")

print("✅ assets/banner.svg generated")
