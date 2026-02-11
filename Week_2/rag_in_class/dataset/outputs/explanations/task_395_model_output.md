# Model output for task_395

## Model
- devstral-small-2:24b-cloud

## Original Code:

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

## Refactored Code:

```python
def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return None
```

- Maintained the exact same function signature and return types
- Preserved the original algorithm and control flow
- Kept the same variable names and structure
- Ensured identical handling of edge cases (returns None when no non-repeating character exists)
- No changes to the logic or behavior of the function
- Formatting improvements limited to consistent spacing
- All test cases should pass exactly as before
- No new functions or modifications to existing ones
- Original functionality remains unchanged
