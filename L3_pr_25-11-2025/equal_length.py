'''
- Given two equal-length arrays maths and science,
  return the indexes of students who scored > 80 in both subjects.
```python
#test case 1
Input:
maths [92, 45, 81], science [88, 90, 70]
Output: [0]'''


def is_equal_length(maths,science):
    new = []
    for i in range(0,len(maths),1):
        if maths[i] > 80 and science[i] > 80:
            new.append(i)
    print(new)

is_equal_length([92, 45, 81],[88, 90, 70])