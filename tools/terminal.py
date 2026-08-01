from pathlib import Path
from config import NAME, ALIAS, ROLE, TAGLINE

WIDTH = 1200
HEIGHT = 380

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{WIDTH}"
     height="{HEIGHT}"
     viewBox="0 0 {WIDTH} {HEIGHT}">

<rect width="100%" height="100%" rx="18" fill="#0d1117"/>

<rect width="100%" height="42" rx="18" fill="#161b22"/>

<circle cx="28" cy="21" r="7" fill="#ff5f56"/>
<circle cx="52" cy="21" r="7" fill="#ffbd2e"/>
<circle cx="76" cy="21" r="7" fill="#27c93f"/>

<text x="100" y="27"
font-family="monospace"
font-size="16"
fill="#8b949e">
proxy@github:~
</text>

<text x="40" y="80"
font-family="monospace"
font-size="22"
fill="#58a6ff">$ whoami</text>

<text x="60" y="115"
font-family="monospace"
font-size="20"
fill="#ffffff">{NAME}</text>

<text x="40" y="160"
font-family="monospace"
font-size="22"
fill="#58a6ff">$ alias</text>

<text x="60" y="195"
font-family="monospace"
font-size="20"
fill="#ffffff">{ALIAS}</text>

<text x="40" y="240"
font-family="monospace"
font-size="22"
fill="#58a6ff">$ role</text>

<text x="60" y="275"
font-family="monospace"
font-size="20"
fill="#ffffff">{ROLE}</text>

<text x="40" y="320"
font-family="monospace"
font-size="22"
fill="#58a6ff">$ status</text>

<text x="60" y="355"
font-family="monospace"
font-size="20"
fill="#3fb950">
Building Intelligent Automation...
</text>

</svg>
"""

Path("assets/terminal.svg").write_text(svg, encoding="utf-8")

print("✅ assets/terminal.svg generated")
