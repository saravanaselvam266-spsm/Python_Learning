'''- Write a function that merges two lists by taking elements alternately.

```python
Input: x= [1, 2, 3] y= ['a', 'b', 'c']
Output: [1, 'a', 2, 'b', 3, 'c']'''

def is_element_alter(x,y):
    new = []
    for i in range(len(x)):
        new.append(x[i])
        new.append(y[i])

    print(new)

is_element_alter([1, 2, 3],['a', 'b', 'c'])