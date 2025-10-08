#TASK-9 Write a Python program that asks the user to enter:

km = float(input("Enter  value in kilometers :"))
choice = int(input("Enter your choice :\n 1 ->Convert to meters \n 2 ->Convert to centimeters \n 3 ->Convert to millimeters \n 4 ->Convert to miles \n "))

match choice :
    case 1:
        print(f"{km} km = {km * 1000} meters")
    case 2 :
        print(f"{km} km = {km * 100000} centimeters")
    case 3 :
        print(f"{km} km = {km * 1000000} millimeters")
    case 4 :
        print(f"{km} km = {km * 0.621371} miles")
    case _ :
        print("Invalid Conversion")
