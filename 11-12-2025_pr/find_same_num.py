'''
Find the common elements between two lists A and B.
Return a new list containing only the elements that appear in both lists,
in the same order as they appear in A.
TEST CASE 1
Input:

A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
Output:

[3, 4]
Test Case 2
Input:

A = [10, 20, 30, 40]
B = [50, 60, 70]
Output:

[]
'''

def is_common_num(num1,num2):
    result = []
    for i in range(0,len(num1),1):
        if num1[i] in num2:
            result.append(num1[i])

    return result

print(is_common_num([10, 20, 30, 40],[50, 60, 70]))
print(is_common_num([1, 2, 3, 4],[3, 4, 5, 6]))
