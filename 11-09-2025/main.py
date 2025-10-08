# conditions
# x = 5
# y = 3
# print(x > y) #true
# print(x < y) #false
# print(x == y) #false
# print(x >= y) #true
# print(x <= y) #false
# print(x != y) #true

# # To find number is Even or Odd

# # step getting a input fro the user
# x = int(input("Enter a number = "))
# print(x)
# if x%2 == 0:
#    print("Even")
# else :
#   print("Odd")

# To find the leap year
# my code
# n = int(input("Enter the year in four digit = "))
# print(n)
# if n%4 == 0:
#   print("The given year is leap year")
# else :
#   print("The given year is not a leap year")  

# To find the leap year

# A = int(input("Enter the year in positive integer ="))
# print(A)

# if A%4 ==0 :
#     print("Y")
# else : 
#     print("N")    

# To find Division for 3 or 5

# N = int(input("Enter a number in positive integer = "))
# print(N)

# if N%3== 0 or N%5==0:
#     print("Divisible")
# else :
#     print ("Not Divisible")

#  To check if the year falls within the 21st century

# A = int(input("Enter the year in positive integer = "))
# print(A)

# if A>=2001 and A<=2100 :
#     print("21st Century")
# else :
#     print("Not in 21st Century")  


# To find the leap year in all conditions

A = int(input("Enter the year in positive integer = "))
print(A)

if A%4 ==0 or A%400 ==0 and A%25 !=0:
    print("Y")
else : 
    print("N")  



