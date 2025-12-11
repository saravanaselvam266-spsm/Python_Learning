'''2. An e-commerce platform imports product descriptions from various vendors, but the text often includes unwanted punctuation marks.
 You must remove all pundiagonal_reverse_flat(mat)ctuation and return only letters (case unchanged) and spaces.
Input: Best-Selling! Laptop, 2024 Edition.
 Output: BestSelling Laptop 2024 Edition
Input: Fresh, Organic; Apples.
 Output: Fresh Organic Apples'''

def e_commerce(product):
    result = ""
    alp = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    num = "0123456789"

    for ch in product:
        if ch in alp or ch in num or ch == " ":
            result += ch
    print(result)

e_commerce("Best-Selling! Laptop, 2024 Edition.")
e_commerce("Fresh, Organic; Apples.")
 