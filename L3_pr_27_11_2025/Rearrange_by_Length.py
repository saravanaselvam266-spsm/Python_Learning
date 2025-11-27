'''Rearrange by Length
Given a list of words, rearrange them so shorter words come first.
 (Don't use sort() or sorted())
Input:
 ["banana", "cat", "watermelon", "apple"]
Output:
 ["cat", "apple", "banana", "watermelon"]'''

def is_length(sen):
    temp = 0
    for i in range(0,len(sen),1):
        for j in range(i+1,len(sen),1):
            if len(sen[i]) > len(sen[j]):
                temp = sen[i]
                sen[i] = sen[j]
                sen[j] = temp
    print(sen)
                
                
            
is_length(["banana", "cat", "watermelon", "apple"])
        
        