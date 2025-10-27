# Practice
# Sum 1

def is_number_present(a,b):
    if len(a) ==0 :
        print("Invalid Input")
    else :
        for num in a :
            if num == b :
                print("found")
                break
        else:
            print("not found")
            


is_number_present([1,2,3,],3)
is_number_present([],5)

#sum 2

def is_even_odd(num):
    if len(num) == 0:
        print("Invalid Input")
    else :
        sum = 0
        for i in num:
            sum += i
        if i % 2 == 0:
            print("Even")
        else :
            print("Odd")

is_even_odd([1,2,3,4])
is_even_odd([10,50])
is_even_odd([])


#sum 3

def num_list(num):
    if len(num) == 0 :
        print("Invalid Input")
    else :
        for i in num :
            if i>=10 and i <=20 :
                print(i)


num_list([8, 1, 0, 19, 11, 28, 3, 5])
