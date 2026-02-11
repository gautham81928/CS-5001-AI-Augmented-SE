def rgb_to_hsv(r, g, b):
    # Normalize RGB values to [0, 1] range
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Find max and min values
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn

    # Calculate Hue
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360

    # Calculate Saturation
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100

    # Calculate Value
    v = mx * 100

    return h, s, v
