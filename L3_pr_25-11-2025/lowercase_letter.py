'''
- Given a list of words, print only the ones that start with an uppercase letter.
  Use a single loop to check their first character.

python
# test case 1
Input: ["Apple", "ball", "Cat", "dog"]
Output: Apple Cat
#Explanation: They start with capital letters.
'''

def is_find_word(word):
    new = ""
    x = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for i in range(0,len(word),1):
        if word[i][0] in x:
            new += word[i]

    print(new)

is_find_word(["Apple", "ball" , "Cat" , "dog"])








