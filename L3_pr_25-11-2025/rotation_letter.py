'''- Given two strings, S_1 and S_2, determine if S_2 is a rotation of S_1.
  For example, "waterbottle" is a rotation of "erbottlewat".
  Assume both strings have the same number of characters. Print True or False.

```python
# test case 1
Input: s1 = "ABCDE", s2 = "CDEAB"
Output: True

# test case 2
Input: s1 = "ABCDE", s2 = "ACDEB"
Output: False'''

def compare_strings(left,right):
    #start
    if len(left) == 0 or len(right) == 0:
        print("Invalid input")
    else:
        final = left
        output = False
        for i in range(0,len(left),+1):
            temp = final[1:] + final[0]
            final = temp
            if final == right:
                output = True
        print(output)
    #stop

compare_strings("ABCDE","CDEAB")
        








