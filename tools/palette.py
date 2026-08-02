ASCII = "█▓▒░@#8&%MWB$Q0O*+=-:. "

def pixel_to_char(value):
    index = int(value / 255 * (len(ASCII) - 1))
    return ASCII[index]
