#Advance problems

def is_duplicate(text):
    a =""
    for i in range(0,len(text),1):
        if text[i] not in a:
            a+=text[i]
    print(a)
    
is_duplicate("Programming")

#---------------------------------------------

def is_anagram(x,y):
    a=""
    for i in x:
        if i in y :
            a+=i
        else: 
            print("Not Anagram")
            return
    if len(a) == len(y):
        print("Anagram")
    else:
        print("Not Anagram")
        
is_anagram("listen","silent")
is_anagram("liisten","siilent")
is_anagram("pool","loop")

#----------------------------------------------------

def is_consonant(word):
    a="aeiouAEIOU"
    b=""
    for i in word:
        if i not in a:
            b+=i
    print(b)
    
is_consonant("education")


#-----------------------------------------------------


def num_bet_zero(num):
    start = -1
    result =[]
    collect = False
    for i in range(0,len(num),1):
        if num[i] == 0:
            if start == -1 :
                start = i
                collect = True
            else:
                collect = False
                break
        elif collect and start != -1:
            result.append(num[i])
    if collect :
        return -1
    print(result)
    
    
num_bet_zero([1,2,0,3,4,5,6,0,8,8,9])

#-----------------------------------------------------

def find(num):
    a=[]
    for i in num:
        if i not in a:
            a.append(i)
    print(a)

find([1,2,3,1,2,4])

#--------------------------------------------------

def find_correct(symbol):
    count = 0
    for i in symbol:
        if count < 0:
            print(False)
            return
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        
    if count == 0:
        print(True)
    else:
        print(False)


find_correct("((()))")
find_correct("((()()")


#---------------------------------------------------

def is_count(word):
    count = 1
    for i in word:
        if i == " ":
            count +=1
    print(count)
    
is_count("I Love Python")

#-----------------------------------------------------

def is_palindrome(words):
    a=""
    for i in range(len(words)-1,-1,-1):
         a+=words[i]
    if words == a:
        print("Palindrome")
    else:
        print("Not Palindrome")
    # print(a)
    
is_palindrome("level")
is_palindrome("python")
            

#---------------------------------------------------------

def counts(a):
    b=[]
    for i in a:
        count = 0
        if i not in b:
            for j in a:
                if i == j:
                    count +=1
                    b.append(i)
            print(i,"->",count)
            
counts([1,2,3,2,3,3,4,5,6,7,7,7])


#----------------------------------------------------------



def is_target(num,target):
    for i in range(0,len(num),1):
        for j in range(2,len(num),1):
            if num[i] + num[j] == target:
                print("(",num[i],",",num[j],")")
                
is_target([1,2,3,4,5,6],7)

#-----------------------------------------------------------

def is_last(num):
    result = []
    for n in num:
        if n != 0:
            result.append(n)
        
    for n in num:
        if  n==0 :
            result.append(n)
            
    print(result)

is_last([0,2,3,1,0,12])

#-------------------------------------------------------------

text = [2, 3, 2, 5, 3, 6]
checked = []

for ch in text:
    if ch not in checked:
        count = 0
        for x in text:
            if ch == x:
                count += 1
        if count > 1:
            print(ch, end=" ")
        checked.append(ch)

#-------------------------------------------------------------

def temp_check(temps):
    # highest avg -> city name and lowest avg -> city name
    # all the keys from the dictionary temps
    cities = list(temps.keys())
    hotness = []
    # print(cities)
    for city, heat in temps.items():
        # sum of all temperatures
        total = sum(heat)
        avg = total / len(heat)
        hotness.append(avg)
    max = -100
    min = 100
    max_index = None
    min_index = None
    # maximum avg
    # minimum avg
    for i in range(0, len(hotness), +1):
        if hotness[i] > max:
            max = hotness[i]
            max_index = i
        if hotness[i] < min:
            min = hotness[i]
            min_index = i
    print(cities[min_index], cities[max_index])
temp_check(
    {
        "Chennai": [32, 33, 31, 35],
        "Bangalore": [27, 28, 26, 29],
        "Delhi": [35, 36, 38, 37],
    }
)

#-----------------------------------------------------------------------

