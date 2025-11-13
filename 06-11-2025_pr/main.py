import math
# Sum-1

def is_count_letter(word):
    count = 0
    b = word
    a =""
    for i in range(0,len(word),1):
        if word[i] == a :
            a += word[i]
    print(len(a))
    print(b)


is_count_letter("success")

#----------------------------------------------------

# Sum -2

# def is_count(word):
#     count = 0
#     for i in range(0,len(word),1):
#         pass
        
#--------------------------------------------------

# Sum - 3

numbers = [4, 7, 10, 13, 16]
even_sum = 0

for n in numbers:
    if n % 2 == 0:
        even_sum += n

print("Sum of even numbers:", even_sum)

# -----------------------------------------
def is_find(text):
    count = 0
    y=0
    a = "aeiouAEIOU"
    for i in text:
        if  i in a:
            count+=1
        elif i not in a:
             y += 1
        
            

    print("vowels : ", count)
    print("Consonants :", y)
is_find("python")

#--------------------------------
def min_max(n):
    mix_val=-math.inf
    min_val=math.inf
    for i in range(0,len(n),1):
        if mix_val < n[i]:
            mix_val = n[i]
        if min_val > n[i]:
            min_val = n[i]
    print(mix_val,"maximum")
    print(min_val,"minimum")
    
min_max([3,4,5,8,9])

# -----------------------------------

def get_ten(num):
    b =[]
    for i in range(0,len(num),1):
        if num[i] > 10:
            b.append(num[i])
    print(b)    
get_ten([4, 12, 9, 20, 15])

#-----------------------------------------
def uppercase(text):
    a =""
    a += text.upper()
    print(a)
    
uppercase("abc")

#--------------------------------------------

def  space(text):
    count = 0
    for i in text:
        if i==" ":
            count +=1
    print("Space:",count)
            
            
space("Hello world Python")


#---------------------------------------------------

def is_digit(text):
    a="0123456789"
    for i in range(0,len(text),1):
        if text[i] in a:
            print("Yes, it has digit")
            break
            
is_digit("abc123")

#-------------------------------------------------------

def is_even(x):
    a = ""
    b = "aeiouAEIOU"
    for i in range(0,len(x),1):
        if x[i] in b:
            a+="*"
        else:
            a+=x[i]
            
    print(a)
            
is_even("apple")


#---------------------------------------------------

def count_word(x):
    count = 1
    for i in range(0,len(x),1):
        if x[i] == " ":
            count+=1
            
    print(count)
    
    
count_word("I Love You")

#---------------------------------------------------

def is_new(text):
    word = text.split()
    x = word[0]
    for i in word:
        if len(x) < len(i):
            x = i
    print(x)

is_new("I Love Programming")

#------------------------------------------------------

def is_reverse(num):
    a = []
    for i in range(len(num)-1,-1,-1):
        a.append(num[i])
    print(a)

is_reverse([1,2,3,4])


#--------------------------------------------------

def avg_num(n):
    sum = 0
    for i in range(0,len(n),1):
        sum+=n[i]
    x = sum / len(n)    
        
        
    print(x)
    
avg_num([10,20,30])


#-------------------------------------------------


def find(num):
    count_1 = 0
    count_2 = 0
    for i in num:
        if i > 0:
            count_1  +=1
        elif i < 0 :
            count_2 += 1
    print("Positive: ",count_1)
    print("Negative: ",count_2)
    
    
find([1,-2,3,-4,5])

#--------------------------------------------------

def avg_num(n):
    sum = 1
    for i in range(0,len(n),1):
        sum = sum * n[i]
    print(sum)
avg_num([2,3,4])
        
        
        
    


#--------------------------------------------------

def find_even(n):
    a = []
    for i in range(0,len(n),1):
        if i%2 ==0 :
            a.append(n[i])
    print(a)
    
    
find_even([10,20,30,40,50])

#-------------------------------------------------

def is_ev_od(n):
    even = []
    odd = []
    for i in n:
        if i%2 == 0:
            even.append(i)
        else :
            odd.append(i)
            
    print("Even:" , even)
    print("Odd:" , odd)
    
is_ev_od([1,2,3,4,5,6])

#-------------------------------------------------

def is_array(num):
    sum = 0
    count=0
    for i in num:
        sum+=i
    a = sum/len(num)
    for j in num:
        if j > a:
            count+=1
            
    print(count)
    
    
is_array([10,20,30,40,50])

#-------------------------------------------------------

def is_extend(num,t):
    a = []
    for i in num:
        a.append(i)
    for j in t:
        a.append(j)
    print(a)
    
is_extend([1,2,3],[4,5])

#------------------------------------------------------

def min_max(n):
    mix_val=n[0]
    min_val=n[0]
    for i in range(0,len(n),1):
        if mix_val < n[i]:
            mix_val = n[i]
        if min_val > n[i]:
            min_val = n[i]
    # print(mix_val)
    print(mix_val-min_val)
    
min_max([8,3,15,6])

#------------------------------------------------------

def is_ascii(num):
    for ch in num:
        print(ch,"->", ord(ch))
        
        
is_ascii("123")

#-------------------------------------------------------

def is_character(text):
    al=0
    digit=0
    special =0
    
    for ch in text:
        if ("A" <= ch <= "Z") or ("a" <= ch <="z"):
            al +=1
        elif ("0" <= ch <="9"):
            digit += 1
        else:
            special +=1
    print("Alphabets:" , al)
    print("Digits:" , digit)
    print("Special Character:" , special)
    
    
is_character("Hello123@#")

#-------------------------------------------------------

def is_count(x):
    sum = 0
    for i in x:
        sum += i
    print(sum)
    
is_count([5,10,15])

#--------------------------------------------------------



