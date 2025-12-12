'''Find Pairs With Given Sum

Input:

arr = [2, 4, 3, 5, 7, 8, 9]
target = 10'''

def pairs_by_sum(num,tar):
    for el in num:
        for j in range(el+1,len(num),1):
            if el + num[j] == tar:
                print(f"({el},{num[j]})")


pairs_by_sum([2, 4, 3, 5, 7, 8, 9],10)