# TASK-5 A triangle can be classified based on its sides as:

r = int(input("Enter the first value :"))
l = int(input("Enter the second value :"))
b = int(input("Enter the third value :"))
  

if r == l ==b :
    print("Equilateral")
elif r ==l or l ==b or b ==r :
    print("Isosceles")
elif (r + l <= b) or (l + b <= r) or (b + r <= l): 
    print("Not a valid triangle") 
else :
    print("Scalene")