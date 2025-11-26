'''- You are given a list containing integers, floats and strings.
Create a new list containing only the float values using one loop.
```python
Example:
Input: [10, 3.5, "hello", 8.2, 6]
Output: [3.5, 8.2]'''

def is_float(num):
    result = []
    for i in num:
        if type(i) == float :
            result.append(i)
    print(result)

is_float( [10, 3.5, "hello", 8.2, 6])