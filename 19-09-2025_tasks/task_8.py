#TASK-8 A movie theater shows different slots:

time = int(input("Enter the time in '24hour' format:"))

if time >=9 and time <12 :
    print("Morning Show")
elif time >=13 and time <16 :
    print("Matinee Show")
elif time >=16 and time <20 :
    print("Evening Show")
else :
    print("Night Show")
    