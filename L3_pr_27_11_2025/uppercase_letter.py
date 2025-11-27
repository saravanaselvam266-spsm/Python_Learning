'''1.Print characters that are uppercase
Question:
 Given a string, print only the uppercase characters.
 Input: "HeLLoWorld"
 Output: H L L W'''

def is_uppercase(word):
    new = ""
    for i in word:
        if i.isupper():
            new += i
        else:
            new += " "
    print(new)
is_uppercase("HeLLoWorld")