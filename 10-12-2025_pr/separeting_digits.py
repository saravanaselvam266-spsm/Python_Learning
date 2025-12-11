def separating_digit(num):
    q = num 
    rem = 0
    result = []
    while q > 0:
        rem = q % 10
        result.append(rem)
        q = q // 10
        
    print(result)

separating_digit(132)