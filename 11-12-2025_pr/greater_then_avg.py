'''Problem: Count How Many Numbers Are Greater Than the Average
You are given a list:

[4, 8, 1, 9, 3, 10, 5]
'''

def is_avg_greater(num):
    sum = 0
    count = 0
    for el in num:
        sum+= el
    avg = sum / len(num)
    for el in num:
        if el > avg:
            count += 1
    print(count)

is_avg_greater([4, 8, 1, 9, 3, 10, 5])

    