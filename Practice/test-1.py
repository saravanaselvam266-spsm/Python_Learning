# print("To find Area of a rectangle")
# length = input("Enter the length ")
# breadth = input("Enter the breadth")

# len = int(length)
# bre = int(breadth)

# AR = len * bre
# print(AR)


firstName = "Stephen"
lastName = "Hawking"
# + is a string concatenation operator
fullname = firstName + " " + lastName 
print(fullname)
def calculator(operator, number1, number2):
    match operator :
        case "+" :
            print(number1 + number2)
        case "-" :
            print(number1 - number2)
        case "*" :
            print(number1 * number2)
        case "/" :
            print(number1 / number2)
        case _ :
            print("Invalid Operator")
calculator('%',20 ,10)