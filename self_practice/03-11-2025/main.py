# Practices

# Sum - 1

def replace_symbol(text):
    if len(text) == 0 :
        print("Invalid Input")
    else:
        a = "" 
        for i in  text :
            if i == " ":
                a += "-"
            else:
                a += i
        print(a)

replace_symbol("Python is nice")
replace_symbol("Python is Amazing")
replace_symbol("")

print("-------------------Sum - 2 ----------------------")

# Sum - 2

def find_index(num,tag):
    if len(num) == 0 :
        print("invalid Input")
    else:
        a = 0 
        for i in range(0,len(num),1):
            if num[i] == tag :
                a = i
        print(a)

find_index([11,22,33,44,55],33)
find_index([],7)
find_index([0],2)

print("----------------- Sum-3 ------------------------")

# Sum - 3

def find_marks(last_mon,this_mon):
    if len(last_mon) == 0:
        print("invalid Input")
    else:
        if len(last_mon) == 0 :
            print("Invalid Input")
        else:
            count = 0
        for i in range(0,len(last_mon),1):
            if last_mon[i] <= this_mon[i]:
                count += 1
        print(count)

find_marks([45, 60, 70, 55, 80],[50, 58, 75, 65, 78])
find_marks([],[])

print("-------------------Sum - 4 ----------------------")

# Sum - 4

def find_balance(string):
    if len(string) == 0:
        print("Invalid Input")
    else :
        count = 0 
        for i in range(0,len(string),1):
            if i == "{[(" :
                count += 1
            elif i == ")]}" :
                count -= 1 
        if count == 0 :
            print("Balanced")
        else:
            print("Not Balance")

find_balance("{[()]}")
find_balance("")

print("---------------------Sum - 5 ---------------------")

# sum - 5 

