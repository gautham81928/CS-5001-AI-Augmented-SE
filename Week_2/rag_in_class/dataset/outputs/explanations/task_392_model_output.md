# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    res = [0, 1]
    for i in range(2, n + 1):
        res.append(max(i, res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5]))
    return res[n]
```

- Replaced `list()` with list literal `[0, 1]` for clarity
- Replaced `while` loop with `for` loop for more Pythonic iteration
- Replaced `int(i / x)` with `i // x` for integer division
- Improved indentation and spacing for better readability
- Removed unnecessary variable `i` increment by using `range`
- Maintained exact same logic and behavior as original implementation
- Kept all function signatures and return types unchanged
- Preserved all edge case handling from original implementation
