'''8. Filter numbers that contain digit '0' in the end.
# Input: [10, 101, 2005, 340, 89]
#  Output: 10 340 (edited) '''

def is_last_zero(num):
    rev = []
    # el = 100
    for el in num:
        if el % 10 == 0:
            rev.append(el)
    print(rev)
    

is_last_zero([10, 101, 2005, 340, 89])
            
