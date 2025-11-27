'''Count Numbers That Increase Compared to Previous

Given a list, count how many elements are greater than the previous element.

Input: [10, 12, 11, 14, 20, 19]
Output: 3'''

def is_previous(num):
    count = 0
    for i in range(0,len(num)-1,1):
        if num[i] < num[i+1]:
            count += 1
    print(count)

is_previous([10, 12, 11, 14, 20, 19]) 