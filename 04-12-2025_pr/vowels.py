'''2. Write a Python program to find the word that has maximum number of vowels from the given sentence
Sample Input:
Learning Python is interesting
Sample Output:

interesting
'''

def is_long_vowels(sentence):
    if len(sentence) == 0 :
        print("Invalid")
    else:
        words = sentence.split()
        vowels = "aeiou"
        max_vowels = ""
        for word in words:
            count = 0
            for ch in word:
                if ch in vowels:
                    count += 1
                    max_vowels = word
        print(max_vowels)
                

        
        

is_long_vowels("Learning Python is interesting")

    
        