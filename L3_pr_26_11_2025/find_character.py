'''You are given two strings.
Your task is to check whether the strings differ by exactly one character.
This means:

Both strings must be of the same length, if both strings are not in same length print "Invalid"

Exactly one position must have different characters


All other characters must be identical


If the condition is satisfied, print "yes".
Otherwise, print "no".

Testcase 1:

Input:  s1 = "coding", s2 = "coting"

Output: “yes" 

Testcase 2:

Input: s1 = "apple", s2 = "abble"

Output: “no”

For example:

Test	Result
compare_strings("apple","apble")
yes
compare_strings("hello","hell")
Invalid
'''

def is_compare_strings(word1,word2):
    count = 0
    if len(word1) != len(word2) :
        print("Invalid")
    else:
        for i in range(0,len(word1),1):
            if word1[i] != word2[i]:
                count += 1
        if count == 1 :
            print("yes")
        else:
            print("no")


is_compare_strings("apple","apble")
is_compare_strings("hello","hell")
