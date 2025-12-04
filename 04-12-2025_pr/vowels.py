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
        result = sentence.split()
        print(result)
        count = 0 
        res = []
        max = 0
        for word in result:
            for ch in word:
                if ch in "aeiouAEIOU":
                    count += 1
            res.append(count)
        for i in range(0,len(res),1):
            if res(i) > max:
                num = i
        print(sentence(num))

is_long_vowels("Learning Python is interesting")

            
      



is_long_vowels("Learning Python is interesting")
        