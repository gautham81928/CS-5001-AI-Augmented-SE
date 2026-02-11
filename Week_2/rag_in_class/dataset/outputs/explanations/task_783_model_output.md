# Model output for task_783

## Model
- devstral-small-2:24b-cloud

## Original Code:

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

## Refactored Code:

```python
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
```

- Maintained all function signatures and return types
- Preserved exact algorithm and control flow
- Added clear comments for each calculation step
- Kept all edge case handling unchanged
- No changes to variable names or return values
- Formatted code for better readability while keeping logic identical
- Ensured all calculations remain mathematically equivalent
- No new functions or modifications to existing ones
