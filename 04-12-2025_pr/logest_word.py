'''1.Write a Python program that splits a sentence into words and finds the longest word in it.
Sample Input:

Data science evolves every year
Sample Output:

Longest word: science
'''
def longest_word(sentence):
    if len(sentence) == 0:
        print("Invalid")
    else:
        result = []
        x = ""
        for ch in sentence:
            if ch != " ":
                x += ch
            else:
                result.append(x)
                x= ""
        result.append(x)

        
        max_word = result[0]
        for word in result:
            if len(max_word) < len(word):
                max_word = word
        print(max_word)

longest_word("Data science evolves every year")
    

# option 2