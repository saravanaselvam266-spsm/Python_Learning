'''Given two arrays:

names → list of student names

birthdates → list of dates in "dd/mm" format

Write a program that prints the names of students who were born between January and  June (both months inclusive).

Hint: Use split() to extract day and month.

Sample Test Case:

names = ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"]

birthdates = ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]

Output: 

['Arun', 'Cathy', 'David', 'Farhan', 'Gita']

For example:

Test	Result
born_in_first_half(["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"], ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"])
['Arun', 'Cathy', 'David', 'Farhan', 'Gita']'''


def born_in_first_half(names,birthdates):
    name_list = []
    for i in range(0,len(birthdates),1):
        day = int(birthdates[i].split("/")[0])
        month = int(birthdates[i].split("/")[1])
        if month > 0 and month < 7 :
            name_list.append(names[i])
    print(name_list)
    
    
born_in_first_half(["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"],
["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"])
born_in_first_half(["Asha", "Ravi", "Mehul"],["05/01", "12/09", "30/06"])

