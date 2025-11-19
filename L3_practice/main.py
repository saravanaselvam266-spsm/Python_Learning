
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








