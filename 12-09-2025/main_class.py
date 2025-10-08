# option 1

d = int(input("Enter your Amount"))
print(d)

if d >=1000 :
    a = d * (10/100)
    b = d - a
    print(b)
elif d <1000 and d >=500 :
    a = d * (5/100)
    b = d - a
    print(b)
elif d <500 :
    print(d)

# option 2

amt = int(input("Enter your Amount"))
print(amt)

if amt >=1000 :
    price = amt * 0.90
    print(price)
elif amt >=500 and amt <1000 :
    print(amt * 0.95)
else :
    print(amt)

