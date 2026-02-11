# Model output for task_397

## Model
- devstral-small-2:24b-cloud

## Original Code:

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

## Refactored Code:

```python
def median_numbers(a, b, c):
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c
    return median
```

- Maintained the exact same function signature and return type
- Preserved all control flow logic and conditional branches
- Kept the same variable naming and assignment patterns
- Ensured identical handling of all edge cases
- No changes to the algorithm or computation logic
- Formatting remains consistent with original
- All test cases will pass without modification
- No new functions or parameters were added
- Original behavior is completely unchanged
