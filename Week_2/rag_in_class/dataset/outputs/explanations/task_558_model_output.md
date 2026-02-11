# Model output for task_558

## Model
- devstral-small-2:24b-cloud

## Original Code:

def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

## Refactored Code:

```python
def digit_distance_nums(n1, n2):
    return sum(map(int, str(abs(n1 - n2))))
```

- Maintained the exact same function signature and return type
- Kept the same algorithm (absolute difference, convert to string, sum digits)
- Preserved all edge case handling (works with negative numbers, zero, etc.)
- Improved formatting by removing extra spaces
- No changes to function behavior or return values
- No new functions added or existing ones removed
- Minimal edits made to the original code
- All test cases should pass exactly as before
