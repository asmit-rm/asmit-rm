from PIL import Image, ImageFilter, ImageOps

def detect_edges(image):
    image = ImageOps.grayscale(image)
    image = ImageOps.autocontrast(image)
    image = image.filter(ImageFilter.FIND_EDGES)
    return image
