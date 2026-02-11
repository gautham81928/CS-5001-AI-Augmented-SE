# Model output for task_107

## Model
- devstral-small-2:24b-cloud

## Original Code:

def count_Hexadecimal(L,R) :  
    count = 0;  
    for i in range(L,R + 1) : 
        if (i >= 10 and i <= 15) : 
            count += 1;  
        elif (i > 15) : 
            k = i;  
            while (k != 0) :  
                if (k % 16 >= 10) : 
                    count += 1;  
                k = k // 16;  
    return count;  

## Refactored Code:

```python
def count_Hexadecimal(L, R):
    count = 0
    for i in range(L, R + 1):
        if i >= 10 and i <= 15:
            count += 1
        elif i > 15:
            k = i
            while k != 0:
                if k % 16 >= 10:
                    count += 1
                k = k // 16
    return count
```

- Removed unnecessary semicolons for better readability
- Added consistent spacing around operators and after commas
- Maintained all original logic, function names, and control flow
- Preserved exact behavior including edge case handling
- Kept the same return type and values
- No changes to the algorithm or function signatures
- Improved code formatting while keeping the structure identical
