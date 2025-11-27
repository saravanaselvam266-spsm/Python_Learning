'''Print numbers ending with digit 7
Input: [17, 23, 47, 59, 70]
 Output: 17 47'''

def is_last_num(num):
    foo = ""
    for i in num:
        if i[-1] == 7:
            foo += i
    print(foo)

is_last_num([17, 23, 47, 59, 70])