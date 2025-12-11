'''You are provided with a number 'n'. Your task is to tell whether that number is saturated. A saturated number is a number which is made by exactly two digits.

 

Input Description:

You are given with a number n. N is strictly a POSITIVE NUMBER between 1 and 9999




Output Description:

Print Saturated if it is saturated else it is Unsaturated




Sample Input:

121

Sample Output:

Saturated

Explanation: 121 is made with two distinct number 1 and 2, so it is “Saturated”

For example:

Test	Result
saturated(121)
Saturated
'''

def saturated(n):
    # start
    if n == 0:
        print("Unsaturated")
    else:
        x = n
        nums = []
        while x > 0:
            div = x % 10 #121 % 10 = 1
            quot = x // 10 # 
            print(quot)
            nums.append(div)
            x = quot


        count = 0
        result = []
        for i in range(0, len(nums), +1):
            if nums[i] in nums[i : len(nums) - 1]:
                count += 1
            if count == 1:
                result.append(nums[i])
            count = 0
        if len(result) == 2 :
            print("Saturated")
        else:
            print("Unsaturated")
    # stop


saturated(121)