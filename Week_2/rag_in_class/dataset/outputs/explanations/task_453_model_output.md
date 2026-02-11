# Model output for task_453

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math 
def sumofFactors(n) : 
    if (n % 2 != 0) : 
        return 0
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1) :    
        count = 0
        curr_sum = 1
        curr_term = 1
        while (n % i == 0) : 
            count= count + 1
            n = n // i 
            if (i == 2 and count == 1) : 
                curr_sum = 0
            curr_term = curr_term * i 
            curr_sum = curr_sum + curr_term 
        res = res * curr_sum  
    if (n >= 2) : 
        res = res * (1 + n) 
    return res 

## Refactored Code:

```python
import math

def sumofFactors(n):
    if n % 2 != 0:
        return 0
    res = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count += 1
            n = n // i
            if i == 2 and count == 1:
                curr_sum = 0
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2:
        res *= (1 + n)
    return res
```

- Removed unnecessary parentheses around `int(math.sqrt(n))`
- Replaced `count = count + 1` with `count += 1`
- Replaced `curr_term = curr_term * i` with `curr_term *= i`
- Replaced `res = res * curr_sum` with `res *= curr_sum`
- Maintained all original logic, function signatures, and behavior
- Preserved all edge case handling exactly as in the original
- Kept the same variable names and control flow structure
- Ensured the function returns the same values for all inputs
