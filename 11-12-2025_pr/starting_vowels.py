'''Count how many words start with a vowel
# Problem:
# Use split() to extract words and count the ones starting with a, e, i, o, u.
# Input:
# "apple is on the orange table"
# Output:
# 3'''

def starting_vowels(sen):
    count = 0
    temp = sen.split()
    for el in temp:
        if el[0] in "aeiouAEIOU" :
            count += 1
    print(count)
        

starting_vowels("apple is on the orange table")