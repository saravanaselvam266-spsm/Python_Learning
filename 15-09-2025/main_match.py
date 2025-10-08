import signal

t = input("Enter the colour in upper case")
print(t)

match signal :
    case "RED":
        print("Stop")
    case "YELLOW" :
        print("Ready")
    case "GREEN" :
        print("Go")
    case _:
        print("Invalid Colour")    
