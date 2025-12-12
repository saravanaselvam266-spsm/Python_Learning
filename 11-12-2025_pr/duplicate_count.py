'''
1.Print numbers that appear more than once (duplicates only)
Input: [1,4,2,7,4,1,8,2,2]
Output → 1, 2, 4
'''


def is_duplicate_only(num):
    result = ""
    count = 0
    for i in range(0,len(num),1):
        for j in range(i + 1,len(num),1):
            if num[i] == num[j]:
                count += 1
            if count > 0 :
                count = 0
                if str(num[i]) not in result :
                    result += str(num[i]) +" "
            

    print(result)

is_duplicate_only([1,4,2,7,4,1,8,2,2])
