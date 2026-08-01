from pathlib import Path
from rembg import remove
from PIL import Image, ImageOps

INPUT = Path("input/profile.jpg")
OUTPUT = Path("assets/portrait.png")

if not INPUT.exists():
    raise FileNotFoundError(f"{INPUT} not found")

print("[1/5] Loading image...")
img = Image.open(INPUT).convert("RGBA")

print("[2/5] Removing background...")
img = remove(img)

print("[3/5] Cropping to square...")
img = ImageOps.contain(img, (700, 700))

canvas = Image.new("RGBA", (700, 700), (0, 0, 0, 0))

x = (700 - img.width) // 2
y = (700 - img.height) // 2

canvas.paste(img, (x, y), img)

print("[4/5] Saving portrait...")
canvas.save(OUTPUT)

print("[5/5] Done!")
print(f"✅ Generated: {OUTPUT}")
