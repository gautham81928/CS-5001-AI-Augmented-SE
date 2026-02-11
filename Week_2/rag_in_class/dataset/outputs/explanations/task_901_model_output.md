# Model output for task_901

## Model
- devstral-small-2:24b-cloud

## Original Code:

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

## Refactored Code:

```python
def smallest_multiple(n):
    if n <= 2:
        return n
    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if a == factors[-1] and i % a == 0:
                return i
```

- Maintained the exact same function signature and return type
- Preserved the original logic and algorithm without changes
- Improved indentation and spacing for better readability
- Kept all control flow structures identical
- Maintained the same edge case handling (n <= 2)
- Preserved the exact same variable names and initialization
- Kept the same loop structures and break/return conditions
- Maintained the original list comprehension syntax
- Ensured all test cases will pass without modification
- No functional changes were made, only formatting improvements
