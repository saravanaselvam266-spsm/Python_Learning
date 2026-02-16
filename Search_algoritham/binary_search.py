# binary search algorithm 

# option 1

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



# Option 2

def search_algorithm(arr,low,high,x):
    if (high < low):
        return False
    mid = (low + high) // 2
    if x > arr[mid] :
        return search_algorithm(arr,mid+1,high,x)
    elif x < arr[mid]:
        return search_algorithm(arr,low,mid-1,x)
    elif x == arr[mid]:
        return True , arr[mid]
    else :
        return False
    
print(search_algorithm([1,2,3,4,5,6,7,8,9,10],0,9,3))

    
