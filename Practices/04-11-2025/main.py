# Sum - 1
'''Question 1:
Write a Python program to check if a given string is a Pangram or not.
A Pangram is a sentence that contains every letter of the English alphabet (a–z) at least once. 
The check should be case-insensitive, meaning both uppercase and lowercase letters are treated the same.

Test Case 1:
Input:The quick brown fox jumps over the lazy dog
Output:True'''

# def find_alpha(words):
#     count = 0
#     for i in range(0,len(words),1):
#         alpha = "abcdefghijklmnopqrstuvwxyz" 
#         if words[i] in words.lower():
#             if i in alpha:
                
                
#     if count == 26 :
#         print(True)
#     else:
#         print(False)
        
        
# find_alpha("The quick brown fox jumps over the lazy dog")

# def find_pali(a):
#     b = ""
#     c = ""
#     for i in a:
#         b += i
#         c = i + c
#     if b == c :
#         print("Palindrome")
#     else:
#         print("Not a Palindrome")
        
# find_pali("Too hot to hoot")


def is_count_vowels(text):
    count = 0
    c = 0
    a = "aeiouAEIOU"
    b = "0123456789"
    for i in text:
        if i  in b:
            c = c + 1
        elif i in a :
            count += 1
    if count == c:
        print(True)
    else:
        print(False)
  

is_count_vowels("I bought 1 apple and 4 eggs")