'''
1.Print numbers that appear more than once (duplicates only)
Input: [1,4,2,7,4,1,8,2,2]
Output → 1, 2, 4
'''


def is_duplicate_only(num):
    result = num
    for i in range(0,len(num),1):
        print(num[i],"->",num.count(num[i]))

is_duplicate_only([1,4,2,7,4,1,8,2,2])
