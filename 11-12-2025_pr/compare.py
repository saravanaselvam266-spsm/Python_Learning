'''Determine if Two Words Are Almost Identical

Two words are “almost identical” if they differ by only one character.

Example:
"cat" and "bat" → True
"cat" and "cart" → False'''

def almost_identical(a, b):
    if len(a) != len(b):
        return False
    
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    
    return diff == 1

print(almost_identical("cat","bat"))
print(almost_identical("cart","cat"))
print(almost_identical("bat",""))