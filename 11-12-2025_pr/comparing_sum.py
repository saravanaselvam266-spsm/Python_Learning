'''Count pairs of numbers whose sum is even

Input list → [1, 2, 3, 4, 5]
Pairs: (1,3), (1,5), (2,4), (3,5)…
Output → 4'''

def count_pairs(num):
    even_count = 0
    odd_count = 0
     
    for el in num:
        if el % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    even_num = (even_count * (even_count - 1)) // 2
    odd_num = (odd_count * (odd_count - 1)) // 2


    print(even_num + odd_num)


count_pairs([1, 2, 3, 4, 5])



 # option 
 
def count_pairs_new(num):
    count = 0
    for el in num :
        for j in range(el+1,len(num),1):
            if (el + num[j]) % 2 == 0:
                count += 1
    print(count)

count_pairs_new([1, 2, 3, 4, 5])