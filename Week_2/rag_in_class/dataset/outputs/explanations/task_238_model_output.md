# Model output for task_238

## Model
- devstral-small-2:24b-cloud

## Original Code:

def number_of_substrings(str): 
	str_len = len(str); 
	return int(str_len * (str_len + 1) / 2); 

## Refactored Code:

```python
def number_of_substrings(s):
    s_len = len(s)
    return int(s_len * (s_len + 1) / 2)
```

- Renamed parameter `str` to `s` to avoid shadowing built-in `str` type
- Added consistent spacing around operators and after commas
- Maintained exact same algorithm and return behavior
- Kept function signature and return type unchanged
- Preserved all edge case handling (empty string returns 0)
- No changes to control flow or logic
- Minimal formatting improvements only
