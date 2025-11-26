'''- Given a list of names, print only the ones that contain “a” or “A”.

```python
Input: ["Meera", "John", "Kavi", "Sona"]
Output: Meera Kavi Sona
Explanation: These names include the letter 'a'
'''

def is_letter(foo):
    count = 0
    new =""

    for i in foo:
        for j in i :
            if j == "a" or j == "A" :
                count += 1
        if count == 1:
            new = new +i+" "
            count = 0
    print(new)
        
is_letter(["Meera", "John", "Kavi", "Sona"])




