from pathlib import Path
from html import escape

INPUT = Path("assets/portrait.txt")
OUTPUT = Path("assets/portrait.svg")

FONT_SIZE = 8
LINE_HEIGHT = 10
PADDING = 20
FONT = "JetBrains Mono, Consolas, monospace"

CYAN = "#00d9ff"


def main():

    if not INPUT.exists():
        raise FileNotFoundError(INPUT)

    lines = INPUT.read_text(encoding="utf-8").splitlines()

    if not lines:
        raise RuntimeError("portrait.txt is empty")

    max_width = max(len(line) for line in lines)

    width = PADDING * 2 + max_width * FONT_SIZE * 0.62
    height = PADDING * 2 + len(lines) * LINE_HEIGHT

    svg = []

    svg.append('<?xml version="1.0" encoding="UTF-8"?>')

    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{int(width)}" '
        f'height="{int(height)}" '
        f'viewBox="0 0 {int(width)} {int(height)}">'
    )

    svg.append("""
<defs>

<filter id="glow">

<feGaussianBlur stdDeviation="2.2" result="blur"/>

<feMerge>
<feMergeNode in="blur"/>
<feMergeNode in="SourceGraphic"/>
</feMerge>

</filter>

</defs>
""")

    svg.append(
        f'<g font-family="{FONT}" '
        f'font-size="{FONT_SIZE}" '
        f'fill="{CYAN}" '
        f'filter="url(#glow)">'
    )

    y = PADDING

    for line in lines:

        svg.append(
            f'<text x="{PADDING}" y="{y}">{escape(line)}</text>'
        )

        y += LINE_HEIGHT

    svg.append("</g>")
    svg.append("</svg>")

    OUTPUT.write_text("\n".join(svg), encoding="utf-8")

    print(f"✅ Generated: {OUTPUT}")


if __name__ == "__main__":
    main()
