# Practices


'''- Given a list of numbers, print the list in reverse order without using list slicing ([::-1]).
python
# test case 1
Input: nums = [1,3,7,8,9]
Output: [9,8,7,3,1]
# test case 2
Input: nums = []
Output: []
'''

# sum 1
def is_reverse(num):
    result = []
    for i in range(len(num)-1,-1,-1):
        if len(num) != 0:
            result.append(num[i])
        else:
            return result
    print(result)
        
is_reverse([1,3,7,8,9])
is_reverse([])

#-----------------------------------------------------------------

'''python
#test case 1:
Input: nums = [4,6,9,2,3,11], k = 2
Output: [3,11,4,6,9,2]'''

# Sum 2

def is_find(a,k):
    tag = k
    result = []




#--------------------------------------------------------------------


'''python
# test case 1
Input: "HelloWorld"
Output: 2
# explanation -> H , W are upper case so, output is 2'''



def is_count(word):
    count = 0
    x = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for i in word:
        if i in x:
            count +=1
    print(f"The uppercase count is: {count}")
    
    
is_count("HelloWorld")
is_count("helloworld")

#-----------------------------------------------------------------------

'''- Write a program that finds the longest word in a given sentence.
  (Bonus: If you are too studious, try without using `split(" ")` and solve)
```python
# test case 1
Input: "Johannesburg is the most populous city of South Africa"
Output: "Johannesburg"
# based on the word length -> it is Johannesburg'''


def is_longest(word):
    x=""
    result =[]
    for i in word:
        if i !=" ":
            x+=i
        else:
            result.append(x)
            x=""
            
            
    max_len = len(result[0])
    max = ""  + result[0]
    for j in result:
        if len(j) > max_len :
            max_len = len(j)
            max = j
            
    print(max)
    
is_longest("Johannesburg is the most populous city of South Africa")


#--------------------------------------------------------------

''''''

def is_count(n):
    count =0
    for i in range(0,len(n),len(n)-1):
        count += n[i]
    print(count)

is_count([1,2,3,4,5])

#----------------------------------------------------------------

def is_find(num):
    x=[]
    for i in range(0,len(num),1):
        if num[i] == 5:
            x.append(i)
    print(f"First index: {x[0]},Last index: {x[-1]}")

is_find([5, 2, 3, 5, 7, 5, 8])

#------------------------------------------------------------------

