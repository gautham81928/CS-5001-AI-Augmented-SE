# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a, b, c):
    vertex = ((-b / (2 * a)), ((4 * a * c) - (b * b)) / (4 * a))
    return vertex
```

- Removed unnecessary parentheses in the vertex calculation
- Improved spacing around operators for better readability
- Maintained exact same functionality and return values
- Kept all function signatures and algorithms unchanged
- Preserved all edge case handling
- No new functions added or removed
- No changes to control flow or return types
