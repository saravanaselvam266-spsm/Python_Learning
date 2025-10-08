## TASK-2    You are given a 2 digit positive number ‘n’. You have to tell whether a number is great or
# not. A great number is a number whose sum of digits let (m) and product of digits let(j) when
# summed together gives the number back
# m+j=n
# Input Description:
# You are given a number n;
# Output Description:
# Print Great if a number is great else print the no 

#Input
 
n = int(input("Enter any Two digit number :"))

# separating the digits

first_digit = n // 10
second_digit = n * 10

# calculate sum and product of the digit

m = first_digit + second_digit
j = first_digit * second_digit

# checking the conditions
if m + j == n :
    print("Great")
else :
    print("No")