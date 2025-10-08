# TASK-4 Ola has a minimum fare of ₹50.

ola = int(input("Enter the distance in number :"))
print(ola)

if ola ==5 :
    print(ola*10)
elif ola >=6 and ola <15 :
    print(ola*8)
elif ola >= 15 :
    print(ola*6)
elif ola >=1 :
    print(50)
else :
    print("Invalid Input")