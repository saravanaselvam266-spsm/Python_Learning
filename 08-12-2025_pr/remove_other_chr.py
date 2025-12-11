'''1. An online shopping platform receives coupon codes typed by customers,
but many of them contain spaces, symbols, or uppercase characters.
 Your task is to clean the coupon code so it contains only uppercase alphabets and digits; remove everything else.
Input: ab#12!cd@EF3
Output: AB12CDEF3
Input: !!SAVE20!!
Output: SAVE20'''

def coupon_code(code):
    result = ""
    alp = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    num = "0123456789"

    for ch in code:
        if ch in alp:
            result +=ch.upper()
        if ch in num:
            result += ch
    print(result)

coupon_code("ab#12!cd@EF3")
coupon_code("!!SAVE20!!")