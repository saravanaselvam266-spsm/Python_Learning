# mon = int(input("Enter the month only in numbers"))



mark = int(input("Enter the number"))
match mark :
    case _ if mark<=100 and mark >=80 :
        print("A")
    case _ if mark<=79 and mark >=60 :
        print("B")
    case _ if mark <=59 and mark >=49 :
        print("C")
    case _ if mark <40 :
        print("D")
    case _ :
        print("Invalid Mark")






        
         

