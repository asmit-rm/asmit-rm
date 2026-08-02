from PIL import Image

ASCII = "█▓▒░@#8&%MWB$Q0O*+=-:. "


def image_to_ascii(image_path, width=90):
    img = Image.open(image_path).convert("L")

    w, h = img.size
    ratio = h / w
    height = int(width * ratio * 0.55)

    img = img.resize((width, height))

    pixels = img.load()

    lines = []

    for y in range(height):
        line = ""

        for x in range(width):
            p = pixels[x, y]

            # Background → blank
            if p < 25:
                line += " "
                continue

            idx = int((p / 255) * (len(ASCII) - 1))
            line += ASCII[idx]

        lines.append(line.rstrip())

    return "\n".join(lines)


if __name__ == "__main__":
    art = image_to_ascii("assets/edges.png")

    with open("assets/portrait.txt", "w", encoding="utf-8") as f:
        f.write(art)

    print("✅ Generated: assets/portrait.txt")


