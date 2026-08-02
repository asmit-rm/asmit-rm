from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps
from rembg import remove

INPUT = Path("input/profile.jpg")
OUTPUT = Path("assets/portrait.png")

SIZE = 700


def crop_square(img):
    w, h = img.size

    side = min(w, h)

    left = (w - side) // 2
    top = (h - side) // 2

    return img.crop((left, top, left + side, top + side))


def main():
    print("[1/6] Loading image...")
    img = Image.open(INPUT).convert("RGBA")

    print("[2/6] Removing background...")
    img = remove(img)

    print("[3/6] Cropping...")
    img = crop_square(img)

    print("[4/6] Enhancing...")

    rgb = img.convert("RGB")

    rgb = ImageEnhance.Contrast(rgb).enhance(1.45)
    rgb = ImageEnhance.Sharpness(rgb).enhance(2.2)
    rgb = ImageEnhance.Color(rgb).enhance(1.08)

    alpha = img.getchannel("A")

    img = rgb.convert("RGBA")
    img.putalpha(alpha)

    print("[5/6] Resizing...")

    img = ImageOps.contain(img, (SIZE, SIZE), method=Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))

    x = (SIZE - img.width) // 2
    y = (SIZE - img.height) // 2

    canvas.paste(img, (x, y), img)

    print("[6/6] Saving...")

    OUTPUT.parent.mkdir(exist_ok=True)

    canvas.save(OUTPUT)

    print(f"✅ Generated: {OUTPUT}")


if __name__ == "__main__":
    main()
