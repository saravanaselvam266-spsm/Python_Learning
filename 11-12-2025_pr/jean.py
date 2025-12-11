'''You are building a cart page for your website. The website sells
Mug - M - 500 INR Per piece
Jeans - J - 3000 INR Per piece
T shirt - T - 1500 INR Per piece
Pen - P - 10 INR Per piece


input: arr = ["M 3", "J 1", "T 2"]

Output
7500


Explanation
Sample Input
M is Mug, J is Jeans, T is for T shirt, P is for Pen
Sample Output
3 Mugs is 1500
1 Jeans is 3000
2 Tshirt is 3000

For example:

Test	Result
calculate_cart_total(["M 3", "J 1", "T 2"])
7500
calculate_cart_total(["P 5", "M 1"])
550
'''

def count_cart(cart):
    if len(cart) == 0:
        print("Invalid Input")
    else:
        jean = pen = mug = shirt = 0

        for entry in cart :
            item , qty = entry.split()
            qty = int(qty)


            if item == "M":
                mug += 500 * qty
            elif item == "J" :
                jean += 3000 * qty
            elif item == "P" :
                pen += 10 * qty
            elif item == "T":
                shirt += 1500 * qty

        print(mug + shirt + pen + jean)


count_cart(["M 3", "J 1", "T 2"])
count_cart(["P 5", "M 1"])