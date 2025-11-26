'''- From a string, collect all the lowercase letters in the same order.
  Use a single loop to scan the string.

```python
# test case 1
Input: "PyTHonProGRam"
Output: "yonroam"'''

def is_lowercase(w):
    new = "" 
    x = "qwertyuiopasdfghjklzxcvbnm"
    for i in w:
        if i in x :
            new += i

    print(new)

is_lowercase("PyTHonProGRam")