'''A company records the energy output (in kWh) from a solar panel for 15 days.
An “efficiency drop streak” occurs when three consecutive days show decreasing output.
Given the list, determine how many such streaks occur.
Example: [50, 48, 45, 49, 47, 46, 44]
Output: 2
Explanation:
(Streaks: 50→48→45 and 49→47→46)
So the count becomes 2 (edited)'''


def  drop_streaks(energy):
    #Start
    if len(energy) == 0:
        return "Invalid Input"
    else:
        count = 0
        for i in range(0,len(energy),+3):
            temp = energy[i : i + 3]
            if len(temp) == 3:
                if temp[0] > temp[1] and temp[1] > temp[2]:
                    count += 1
        return count
    #Stop

print(drop_streaks([50, 48, 45, 49, 47, 46, 44]))

