# Python list problem solving practice

# Sum 1
# print how many are even and how many are odd.

def count_even_odd(num):
    a = 0
    b = 0
    for i in num :
        if i % 2 == 0 :
            a += 1
        else :
            b += 1
    print("Total count of Even numbers :", a)
    print("Total count of Odd numbers  :", b)


count_even_odd([4, 7, 2, 9, 6])


# Sum 2
# print biggest and smallest number.

def small_big_numbers(n):
    for i in n :
        if n < i:
            print(i)
        elif n < i :
            print(i)
            
small_big_numbers([10, 3, 55, 23, 5])

