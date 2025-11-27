'''a list of students
a list of scores (same length)
 Return the names of students whose name has more than 3 vowels AND whose score is above average score.
 Use nested loops (one to count vowels, one to compute average).
Input:
 students = ["Aravind", "Bala", "Eeshwar", "Louis", "Gita"]
 scores = [85, 70, 92, 88, 60]
Output:
 ["Aravind", "Eeshwar", "Louis"]'''

def is_vowels_avg(std,scr):
    if len(std) == len(scr):
        print("Invalid")
    else:
        avg = 0
        for i in scr:
            avg += i
    total_avg = avg / len(scr)
    print(total_avg)

is_vowels_avg(["Aravind", "Bala", "Eeshwar", "Louis", "Gita"],[85, 70, 92, 88, 60])
            
