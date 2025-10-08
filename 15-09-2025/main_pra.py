# First sum To check the number is positive or Negative

num = int(input("Enter a number"))
print(num)

if num >=1:
    print("The number is Positive")
elif num <=-1:
    print("The number is Negative")
elif num ==0:
    print("The number is zero")

# Second sum Vowel 
   
v = input("Enter a Alphabet Character")
print(v)

if v =="A" or v =="E" or v =="I" or v =="O" or v =="U" :
   print("Vowel")
elif v =="a" or v =="e" or v =="i" or v =="o" or v =="u" :
   print("Vowel")
else :
    print("Consonant")

# Third sum e-commerce     

# Take inputs
amount = float(input("Enter total purchase amount: "))
member = input("Is the customer a member? (True/False): ")

# Convert input to boolean
if member == "True":
    a = True
    points = int(amount // 10)
    print("Reward Points Earned:", points)
else:
    a = False
    points = 0
    print("Reward Points Earned:", points)





