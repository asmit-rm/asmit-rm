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

<!-- Left Panel -->
<rect x="40" y="60"
      width="360"
      height="560"
      rx="12"
      fill="#0d1117"/>

<text x="135"
      y="340"
      fill="#00d9ff"
      font-size="28"
      font-family="monospace">
Portrait
Coming Soon
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
