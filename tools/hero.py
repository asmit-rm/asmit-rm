from pathlib import Path

SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="1200"
     height="700"
     viewBox="0 0 1200 700">

<rect width="1200" height="700" fill="#05070d"/>

<!-- Border -->
<rect x="20" y="20" width="1160" height="660"
      rx="18"
      fill="none"
      stroke="#00d9ff"
      stroke-width="2"/>

<!-- Left Cyber Panel -->

<rect x="40"
      y="60"
      width="360"
      height="560"
      rx="18"
      fill="#0d1117"
      stroke="#00d9ff"
      stroke-width="2"/>

<circle
    cx="220"
    cy="230"
    r="105"
    fill="none"
    stroke="#00d9ff"
    stroke-width="3"/>

<circle
    cx="220"
    cy="230"
    r="92"
    fill="#08131d"/>

<text
    x="220"
    y="220"
    text-anchor="middle"
    fill="#00d9ff"
    font-size="42"
    font-family="monospace"
    font-weight="bold">
PX
</text>

<text
    x="220"
    y="255"
    text-anchor="middle"
    fill="#58a6ff"
    font-size="16"
    font-family="monospace">
ASCII ENGINE
</text>

<line x1="100" y1="390" x2="340" y2="390"
      stroke="#00d9ff"
      stroke-width="1"/>

<text
    x="220"
    y="430"
    text-anchor="middle"
    fill="#58a6ff"
    font-size="18"
    font-family="monospace">
CYBER PROFILE
</text>

<text
    x="220"
    y="460"
    text-anchor="middle"
    fill="#3fb950"
    font-size="15"
    font-family="monospace">
ASCII Portrait Loading...
</text>

<text
    x="220"
    y="485"
    text-anchor="middle"
    fill="#8b949e"
    font-size="12"
    font-family="monospace">
Soon replacing with
</text>

<text
    x="220"
    y="505"
    text-anchor="middle"
    fill="#00d9ff"
    font-size="13"
    font-family="monospace">
Real ASCII Portrait
</text>

<!-- Right Panel -->
<rect x="430"
      y="60"
      width="730"
      height="560"
      rx="12"
      fill="#0d1117"/>

<text x="470"
      y="120"
      fill="#58a6ff"
      font-size="28"
      font-family="monospace">
$ whoami
</text>

<text x="500"
      y="165"
      fill="white"
      font-size="24"
      font-family="monospace">
Asmit Kumar Bera
</text>

<text x="470"
      y="240"
      fill="#58a6ff"
      font-size="28"
      font-family="monospace">
$ alias
</text>

<text x="500"
      y="285"
      fill="white"
      font-size="24"
      font-family="monospace">
PROXY
</text>

<text x="470"
      y="360"
      fill="#58a6ff"
      font-size="28"
      font-family="monospace">
$ role
</text>

<text x="500"
      y="405"
      fill="white"
      font-size="24"
      font-family="monospace">
AI Developer • Telegram Bot Engineer
</text>

<text x="470"
      y="480"
      fill="#58a6ff"
      font-size="28"
      font-family="monospace">
$ status
</text>

<text x="500"
      y="525"
      fill="#3fb950"
      font-size="24"
      font-family="monospace">
Building Intelligent Automation...
</text>

</svg>
"""

Path("assets/hero.svg").write_text(SVG, encoding="utf-8")

print("✅ assets/hero.svg generated")
