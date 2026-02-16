'''Input: A list of numbers → [54, 546, 548, 60]
Task: Arrange the numbers so that they form the largest possible number when concatenated.
Output: 6054854654
Note: Do not use sorting functions. You must implement your own comparison logic.
'''

def rearrange_num(num):
    result = ""
    for i in range(len(num)-1,-1,-1):
        result += str(num[i])
    print(result)

rearrange_num([54, 546, 548, 60])