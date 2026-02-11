# Model output for task_853

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,int(math.sqrt(n) + 1)): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum  
    if n >= 2: 
        res *= (1 + n) 
    return res 

## Refactored Code:

```python
import math

def sum_of_odd_Factors(n):
    res = 1
    # Remove all factors of 2
    while n % 2 == 0:
        n = n // 2

    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n) + 1)):
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum

    # If remaining n is a prime > 2
    if n >= 2:
        res *= (1 + n)
    return res
```

- Maintained the exact same function signature and return type
- Preserved all control flow and algorithm logic
- Kept the same variable names and structure
- Only improved formatting and added comments for clarity
- No changes to edge case handling
- All existing behavior remains unchanged
- Code is more readable while being functionally identical
- No new functions or modifications to existing ones
- Followed minimal edit approach as required
