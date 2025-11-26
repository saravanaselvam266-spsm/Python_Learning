'''- Filter numbers satisfying 3 conditions
  Problem:
  Print numbers that:

1. are 4 digits
2. end with an even digit

```python
#Test Case:
Input: [2481, 3572, 602, 7890, 4214]
Expected Output: [3572,7890 ,4214]
'''

def is_four_digit(num):
    result = []
    for i in num:
        if i >= 1000 or i <=9999 :
            if i%2 == 0 :
                result.append(i)
    print(result)

is_four_digit([2481, 3572, 602, 7890, 4214])