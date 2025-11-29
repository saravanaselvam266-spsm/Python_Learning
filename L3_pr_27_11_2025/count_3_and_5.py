'''Count Numbers Divisible by 3 or 5 (Not Both)

Given a list of numbers, count how many are divisible by 3 OR 5 but not both.

Input: [3,5,15,18,20,30,7,9]
Output: 3'''

def is_three_five(num):
    count_single = 0
    #count_both = 0
    for el in num:
        if el%3 == 0 and el%5 == 0:
            #count_both +=1
            continue
        elif el%3 ==0 or el%5 ==0:
            count_single += 1
    # print(count_single)
    # print(f"hi{count_both}")
    print(count_single)

is_three_five([3,5,15,18,20,30,7,9])