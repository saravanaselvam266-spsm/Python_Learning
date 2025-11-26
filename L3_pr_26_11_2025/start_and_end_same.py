'''- Write a Program that Keep Words That Start and End With the Same Letter

```python
Case-insensitive matching.
Example:
 Input: ["level", "Apple", "mana", "cool"]
 Output: ["level"]'''

def is_start_and_end(words):
    new = []
    for i in range(0,len(words),1):
        if words[i][0] == words[i][-1]:
            new.append(words[i])
    print(new)

is_start_and_end(["level", "Apple", "mana", "cool"])
