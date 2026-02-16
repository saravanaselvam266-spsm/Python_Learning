# binary search algorithm 

def binary_search(arr,x):
    low = 0 
    high = len(arr) - 1 
    while low <= high :
        mid = (low + high) // 2    # or mid = low + (high - low) // 2
        if arr[mid] == x :
            return True , arr[mid] 
        elif x < arr[mid] :
            high = mid - 1
        elif x > arr[mid] :
            low = mid + 1
        
    return "This number you want is not in this array"
        
print(binary_search([1,2,3,4,5,6,7,8,9,10],3))
print(binary_search([1,2,3,4,5,6,7,8,9,10],5))
print(binary_search([1,2,3,4,5,6,7,8,9,10],6))
print(binary_search([1,2,3,4,5,6,7,8,9,10],9))
print(binary_search([1,2,3,4,5,6,7,8,9,10],4))
print(binary_search([1,2,3,4,5,6,7,8,9,10],12))