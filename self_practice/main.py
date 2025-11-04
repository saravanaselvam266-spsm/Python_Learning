# Sum 1

print("-----------sum-1-----------")
def rev_words(word):
    if len(word) == 0 :
        print("Invalid Input")
    else :
        result = " "
        for i in range(0,len(word),1):
            result = word[i] + result
        print(result)
            
rev_words("Python")

# Sum 2 

print("-----------sum-2-----------")

def palindrome(word):
    if len(word) == 0 :
        print("Invalid Input")
    else :
        result = ""
        for i in range(len(word)-1,-1,-1):
            result += word[i]
        if word == result :
            return "The give word is Palindrome"
        else :
            return "The give word is not a Palindrome"

print(palindrome("madam"))
print(palindrome("hello"))


# Sum 3

print("-----------sum-3-----------")

def number(x,y):
    if len(x) == 0 :
        print("Invalid Input")
    else:
        a = []
        for i in x :
            if i in y :
                a.append(i)  
        print(a)

number([3,4,5],[3,4,6])


# Sum 4

print("-----------sum-4-----------")

def words(x):
    long = x[0]
    short = x[0]
    for i in x:
        if len(x) < len(short) :
            short = i
        elif len(x) > len(long):
            long = i
    print(f"Short_word is :{short}")
    print(f"Long_word is  :{long}")
            


words(["dog","elephant","cat","lion"])

# Sum 5

print("-----------sum-5-----------")


def duplicate(y):
    a = []
    for i in y:
        if i not in a:
            a.append(i)
    print(a)
    

duplicate([1,2,2,3,4,4,5])

# Sum 6

# print("-----------sum-6-----------")

def space_remove(text):
    result = ""
    for ch in range(0,len(text),1):
        if text[ch] != " ":
            result += text[ch]
    return result 


print(space_remove("Python is Nice") )

# Sum 7

print("----------Sum-7----------")

def char_count(word):
    visited = []  # to avoid printing duplicates
    for i in range(len(word)):
        if word[i] not in visited:
            count = 0
            for j in range(len(word)):
                if word[i] == word[j]:
                    count += 1
            print(word[i], "->", count)
            visited.append(word[i])

char_count("banana")

# Sum 8

print("----------Sum-8----------")

def count_types(text):
    upper = 0
    lower = 0
    digit = 0

    for i in text:
        if 'A' <= i <='Z':
            upper += 1
        elif 'a' <= i <='z':
            lower += 1
        elif '0' <= i <='9':
            digit += 1
    print(f"Total upper case letter :{upper}")
    print(f"Total lower case letter :{lower}")
    print(f"Total digits :{digit}")

count_types("Hello123")

# Sum 9 

# print("-----------sum-9-----------")

def duplicate(y):
    a = ""
    for i in y:
        if i not in a:
            a += i
    print(a)
    
duplicate("Programming")        
    

# Sum 10

#print("----------sum-10----------")
 
