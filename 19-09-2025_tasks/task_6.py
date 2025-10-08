#TASK-6 Write a program that takes a number as input and prints:

num = int(input("Enter any number :"))

match num :
    case _ if num%3 ==0 and num%5 ==0 :
        print("FizzBuzz")
    case _ if num%3 ==0 :
        print("Fizz")
    case _ if num%5 ==0 :
        print("Buzz")
    case _ :
        print("Invalid Number")