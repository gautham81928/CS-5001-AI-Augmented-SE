# Model output for task_144

## Model
- devstral-small-2:24b-cloud

## Original Code:

def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

## Refactored Code:

```python
def sum_Pairs(arr, n):
    sum = 0
    for i in range(n - 1, -1, -1):
        sum += i * arr[i] - (n - 1 - i) * arr[i]
    return sum
```

- Maintained the exact function signature and return type
- Preserved the original algorithm and control flow
- Kept the same variable names and initialization
- Maintained the exact same loop structure and iteration
- Preserved the exact same arithmetic operations
- Kept the same return value behavior
- No changes to edge case handling
- Only improved formatting (consistent spacing around operators)
- No functional changes made to the implementation
