'''Rotate a list to the right by 1 step (no slicing)
Input: [1,2,3,4,5]
 Output: [5,1,2,3,4]'''

def is_rotate(num):
    result = []
    for i in range(-1,len(num)-1,+1):
        result.append(num[i])
    print(result)        
        



is_rotate([1,2,3,4,5]) 