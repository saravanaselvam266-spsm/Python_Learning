'''Convert a number into digits manually

Input → 4567
Output → [4, 5, 6, 7]'''

def is_separate_num(num):
    result = []
    while num > 0:
        rem = num % 10
        quo = num // 10 
        result.append(rem)
        num = quo 
    final = []
    for i in range(len(result)-1,-1,-1):
        final.append(result[i])


    print(final)

is_separate_num(4567) 
