# Practices

# Sum 1
'''Level 3:
Find the smallest word in a sentence.
Input: "Python is super powerful"
Output: is'''



def is_smallest(word):
    x=""
    result = []
    for i in word:
        if i !=" ":
            x+=i
        else:
            result.append(x)
            x=""
    result.append(x)        
    # print(result)
    max_value = len(result[0])
    max = "" 
    for j in result:
        if len(j) < max_value:
            max_value = len(j)
            max = j
    print(max)
            
            
is_smallest("Python is super powerful")


'''2. A list is strictly increasing if every next element is greater than the previous one.
Example:
[1,3,5,9] → True
[2,2,5] → False (because 2 is NOT less than 2)
[10,5,6] → False (because 5 < 10)'''

# Sum2
def is_greater(num):
    a = num[0]
    print(a)
    for i in range(0,len(num),1):
        if a >= num[i]:

            return False
    return True


print(is_greater([1,2,3,4]))


        
    




'''
4. Replace characters at odd indexes with *.
Example: "hello" → "h*l*o" 
'''

# Sum 4
def is_odd(s):
    result = ""
    for i in range(0,len(s),1):
        if i % 2 != 0 :
            result+="*"
        else:
            result += s[i]
    print(result)
        
is_odd("hello")


