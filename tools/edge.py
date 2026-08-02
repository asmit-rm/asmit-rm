from PIL import Image, ImageOps, ImageFilter


def detect_edges(image_path: str) -> Image.Image:
    img = Image.open(image_path).convert("L")

    img = ImageOps.autocontrast(img)

    img = img.filter(ImageFilter.FIND_EDGES)

    img = ImageOps.invert(img)

    return img


if __name__ == "__main__":
    edge = detect_edges("assets/portrait.png")
    edge.save("assets/edges.png")
    print("✅ Generated: assets/edges.png")
