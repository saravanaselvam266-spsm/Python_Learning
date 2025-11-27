'''Find Student With Highest Average

names = ["Arun","Bala","Cathy"]
marks = [[80,90,70], [60,65,70], [95,85,80]]

Using a single loop, print the student with the highest total.

Output: "Cathy"'''

def is_find_total(names,marks):
    total=0
    for i in range(len(marks)):
        for j in range(len(marks[i])):
            total+=marks[i][j]
        marks[i]=total
        total=0
    max = 0
    for i in range(len(marks)):
        if marks[i]>marks[max]:
            max=i
    print(names[max])

    

is_find_total(["Arun","Bala","Cathy"],[[80,90,70], [60,65,70], [95,85,80]])



# Option 2
def is_find_total(names, marks):
    highest_total = -1
    highest_index = 0

    total = 0
    subject_count = len(marks[0])   # how many subjects (3)

    index = 0   # student index

    # single loop through all marks
    for i in range(len(marks) * subject_count):
        row = i // subject_count      # which student
        col = i % subject_count       # which subject

        total += marks[row][col]

        # when one student's subject finishing
        if col == subject_count - 1:
            # check highest
            if total > highest_total:
                highest_total = total
                highest_index = row
            total = 0   # reset for next student

    print(names[highest_index])
    
is_find_total(["Arun","Bala","Cathy"],[[80,90,70], [60,65,70], [95,85,80]])