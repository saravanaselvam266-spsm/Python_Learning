# To find sum of number is divisible by 5 or not

A = int(input("Enter a number = "))
print(A)
B = int(input("Enter a  another number = "))
print(B)

if (A+B)%5== 0:
    print("'1'")
else :
    print("'0'")   
 
# To find the number is multiple of 7

x = int(input("Enter the number = "))
print(x)

if x%7== 0:
    print("yes")
else :
    print("no")

# To find the charge or free delivery

x = int(input("Enter the Amount = "))
print(x)

if x >500:
    print("Free")
    print("The total amount is =", x)
else :
    print("Charged")
    y = x + 50
    print("The total amount is =",y) 