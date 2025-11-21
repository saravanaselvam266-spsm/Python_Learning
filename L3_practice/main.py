
# compare_print_g_b("APPLE", "APRON")
# GGBBB

def compare_print(x,y):
    output= ""
    for i in range(0,len(x)):
        if x[i] == y[i]:
            output += "G"
        else:
            output += "B"
    print(output)
    
    
compare_print("APPLE", "APRON")
compare_print("sleep", "sleep")
compare_print("trust", "list")

#---------------------------------------------------------------------

'''Print True if the number of opening parentheses match the

closing parenthesis in a string, else print False

Input	Output
"())("	False
"((()))"	True
For example:

Test	Result
bracket_match("((()))")
True
bracket_match("())(")
False'''

def is_bracket_match(string):
    count = 0
    for i in range(0,len(string),1):
        if count < 0:
            print(False)
            return
        if string[i] == "(":
            count += 1
        elif string[i] == ")":
            count -=1
    if count == 0:
        print(True)
    else :
        print(False)

is_bracket_match("((()))")
is_bracket_match("())(")

#------------------------------------------------------------

'''You are given two lists:

One list shows the gender of each student ('M' for male, 'F' for female).

The other list shows their marks in the same order.

Write a Python program to:

Find the average marks of male students.

Find the average marks of female students.

Print "Male <average>" if male students have the higher average, or "Female <average>" if female students have the higher average.

For example:

Test	Result
find_higher_average(['M','F','M','F','M','F','M'],
                    [81.5, 70.0, 98.5, 60.0, 75.0, 50.0, 85.0]) 
Male 85.0
find_higher_average(['M','F','M','F','M','F','M'],
                    [59.5, 80.0, 61.0, 79.0, 60.5, 81.0, 60.0])
Female 80.0'''

def is_find_higher_average(gen_list, marks_list):
    male = 0
    male_count = 0
    female = 0
    female_count = 0
    for i in range(0,len(gen_list),1):
        if gen_list[i] == "M":
            male += marks_list[i]
            male_count +=1
        elif gen_list[i] == "F" :
            female += marks_list[i]
            female_count += 1
    male_avg = male / male_count
    female_avg = female / female_count

    if male_avg > female_avg :
        print(f"Male {male_avg}")
    else:
        print(f"Female {female_avg}")

is_find_higher_average(['M','F','M','F','M','F','M'],
                    [81.5, 70.0, 98.5, 60.0, 75.0, 50.0, 85.0])
is_find_higher_average(['M','F','M','F','M','F','M'],
                    [59.5, 80.0, 61.0, 79.0, 60.5, 81.0, 60.0])
 

#---------------------------------------------------------------------

'''Given 4 arrays, names, maths_marks, physics_marks and chemistry_marks.  Find the names of students who got more than 90 marks in all three marks and print the name of the student who got the highest total among them.

Print "No student found" if there are no students how have score more than 90 in all 3 subjects. 

For example:

Test	Result
highest_marks(["jason", "priya", "madhan", "syed"], 
              [91, 92, 81, 75],
              [91, 89, 100, 90],
              [91, 95, 100, 90])

output :jason

highest_marks(["Ameer", "Bobby", "Clara", "Divya", "Elvin", "Fazil", "Geeta", "Hari", "Ila", "Jay"],
[85, 88, 89, 90, 86, 87, 84, 83, 89, 88],
[84, 87, 88, 89, 85, 86, 83, 82, 88, 87],
[86, 85, 84, 83, 87, 88, 82, 81, 85, 86])
output:No student found'''


def highest_marks(name,maths,physics,chemistry):
    n_name = []
    n_maths = []
    n_phys = []
    n_chem = []

    for i in range(0,len(name),1):
        if maths[i] > 90 and physics[i] > 90 and chemistry[i] >90 :
            n_name.append(name[i])
            n_maths.append(maths[i])
            n_phys.append(physics[i])
            n_chem.append(chemistry[i])

    if len(n_name) == 0:
        print("No students found")
    else:
        max_name = n_name[0]
        max_num = n_maths[0] + n_phys[0] + n_chem[0]
        
        for i in range(1,len(n_name),1):
            sum = n_maths[i] + n_phys[i] + n_chem[i]
            if sum > max_num :
                max_name = n_name[i]
                max_num = sum 

                
        print(max_name)



highest_marks(["jason", "priya", "madhan", "syed"], 
              [91, 92, 81, 75],
              [91, 89, 100, 90],
              [91, 95, 100, 90])
highest_marks(["Ameer", "Bobby", "Clara", "Divya", "Elvin", "Fazil", "Geeta", "Hari", "Ila", "Jay"],
[85, 88, 89, 90, 86, 87, 84, 83, 89, 88],
[84, 87, 88, 89, 85, 86, 83, 82, 88, 87],
[86, 85, 84, 83, 87, 88, 82, 81, 85, 86])


#----------------------------------------------------------------------------------------------------

'''Given a string "python" print all the characters in the even position,
 taking the first position as 1 and print it in reverse

1 2 3 4 5 6
p y t h o n  

For example:

Test	Result
str_rev_even("python")
output :nhy
'''
def str_rev_even(word):
    #Write your code here
    result = ""
    rev =""
    for i in range(0,len(word),1):
        if i % 2 != 0:
            result+=word[i]
            rev = word[i] + rev
    
    print(rev)
    
    
str_rev_even("python")

# option 2
def str_rev_even(word):
    #Write your code here
    result = ""
    for i in range(0,len(word),1):
        if i % 2 != 0:
            result+=word[i]
    rev =""
    for j in range(len(result)-1,-1,-1):
        rev+=result[j]
    print(rev)


#--------------------------------------------------------------------------------------------------------

'''Write a function find_first_occurence(arr, value) that prints the index of the first occurrence of a given value in the array.
If the value is not found, prints -1. (Do this without using any library function). If its an empty array, the output will be -1.

Input = [9, 7, 4, 1, 7, 0], 7

output

1

For example:

Test	Result
find_first_occurence([9, 7, 4, 1, 7, 0], 7)
output :1'''

def find_first_occurence(arr,value):
    if len(arr) == 0:
        print(-1)
    else:
        for i in range(0,len(arr),1):
            if arr[i] == value:
                print(i)
                return
        print(-1)
            
   
            

find_first_occurence([],2)
find_first_occurence([9, 7, 4, 1, 7, 0], 7)

#option 2


def find_first_occurence(arr,value):
    if len(arr) == 0:
        print(-1)
    else:
        x = []
        for i in range(0,len(arr),1):
            if arr[i] == value:
                x.append(i)
                
        if len(x)==0:
            print(-1)
        else:
            print(x[0])


#---------------------------------------------------------------------------------------

''' Selection Sort (Manual Implementation)
Logic

Find the smallest number in the list.

Swap it with the first element.

Then find the next smallest and swap with second element.

Continue this until sorted.'''

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example
print(selection_sort([5, 3, 8,10,0,2, 1]))

#-----------------------------------------------------------------------------------

'''Bubble Sort (Manual Implementation)
Logic

Compare two numbers side-by-side.

If the left one is bigger, swap them.

Repeat until the list becomes sorted.
'''

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap

    return arr

print(bubble_sort([5, 3, 8, 2, 1]))

#------------------------------------------------------------------------

'''1.Find the indices of numbers between the first 0 and second 0.
Input:
[5, 4, 0, 9, 8, 7, 0, 3, 2]
Output:
[3, 4, 5]  
2.Find the indices of numbers between the first 7 and second 7..Input:
[1, 7, 4, 3, 7, 9, 2, 7]
Output:
[2, 3]

'''
def extract_index(nums,k):
    


    zeros = []
    result = []
    for i in range(0,len(nums),1):
        if nums[i]== k:
            zeros.append(i)
    
    
    for j in range(zeros[0]+1,zeros[1],1):
        result.append(j)
    print(result)
    
extract_index([5, 4, 0, 9, 8, 7, 0, 3, 2],0)
extract_index([1, 7, 4, 3, 7, 9, 2, 7],7)


#-------------------------------------------------------------------------------------

'''```python
Input:
# nums = [2, 7, 11, 15]
# target = 9
Output:
# [0,1]

Input:
# nums = [3,2,4], target = 6
Output:
# [1,2]
```'''
def is_find(num,k):
    for i in range(0,len(num),1):
        for j in range(i+1,len(num),1):
            if num[i] + num[j] == k :
                print(f"[{i},{j}]")

    
is_find([2, 7, 11, 15],9)
is_find([3,2,4],6)
is_find([2,4,3,5,6,7,8,9],10)

# New sums 

def is_find(num,k):
    for i in range(0,len(num),1):
        for j in range(i+1,len(num),1):
            if num[i] + num[j] == k :
                print(f"[{num[i]},{num[j]}]")

    
is_find([2, 7, 11, 15],9)
is_find([3,2,4],6)
is_find([2,4,3,5,6,7,8,9],10)

#-----------------------------------------------------------------------------------------

'''- Given an integer array nums, return true if any value appears at least twice in the 
array, and return false if every element is distinct.

```python
Input: nums = [1,2,3,1]
Output: True

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True

Input:  nums = [1,2,3,4]
Output: False
'''

def is_twice(num):
    for i in range(0,len(num),1):
        for j in range(i+1,len(num),1):
            if num[i] == num[j]:
                print(True)
                return
    print(False)

is_twice([1,2,3,1])
is_twice([1,1,1,3,3,4,3,2,4,2])
is_twice([1,2,3,4])

#----------------------------------------------------------------------------------------

# Find how many words are in a sentence.

def is_count(sen):
    count = 1
    for i in sen:
        if i == " ":
            count +=1
    print(count)

is_count("I Love Python")


#--------------------------------------------------------------------------------------

# Reverse each word in a sentence. Example: "hello world" → "olleh dlrow"

def is_find(n):
    a= ""
    res = []
    for i in n :
        if i != " ":
            a+=i
        else:
            res.append(a)
            a= ""
    res.append(a)
    print(res)
    
    for j in range(len(n)):
        print(j[::-1],end=" ")
        
    
is_find("Hello world")


#---------------------------------------------------------------------------------
'''
Find the longest word in a sentence

Input: "I love programming" → Output: "programming"'''

def is_long_word(word):
    r = ""
    rev = []
    for i in word:
        if i != " ":
            r += i
        else:
            rev.append(r)
            r= ""
    rev.append(r)
    
    max_word = rev[0]
    for j in rev:
        if j > max_word :
            max_word = j 
    print(max_word)
    
    
is_long_word("I Love python")

#---------------------------------------------------------------------------------

































