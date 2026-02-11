# Model output for task_33

## Model
- devstral-small-2:24b-cloud

## Original Code:

def decimal_To_Binary(N): 
    B_Number = 0
    cnt = 0
    while (N != 0): 
        rem = N % 2
        c = pow(10,cnt)  
        B_Number += rem*c  
        N //= 2 
        cnt += 1
    return B_Number  

## Refactored Code:

```python
def decimal_To_Binary(N):
    B_Number = 0
    cnt = 0
    while N != 0:
        rem = N % 2
        c = pow(10, cnt)
        B_Number += rem * c
        N //= 2
        cnt += 1
    return B_Number
```

- Removed unnecessary parentheses around the while loop condition
- Improved spacing around operators for better readability
- Maintained all original logic, function name, and behavior
- Kept the same variable names and control flow
- Preserved the exact same return value handling
- No changes to the algorithm or edge case handling
- Formatted the code to follow PEP 8 guidelines
- Ensured all tests will pass without modification
