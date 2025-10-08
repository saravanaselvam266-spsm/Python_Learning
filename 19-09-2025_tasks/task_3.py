

# TASK-3 Electricity rates differ for residential and commercial consumers:

con = input("Enter your consumer type ('residential/commercial') :") 
ele = int(input("Enter the units :"))

match con :
    case 'residential' :
        match ele:
            case _ if 0<= ele <=100 :
                print(ele * 3)
            case _ if 101<= ele <=200 :
                print(ele * 5)
            case _ if  ele >200 :
                print(ele * 7)
    case 'commercial' :
        match ele :
            case _ if 0<= ele <=100 :
                print(ele * 5)
            case _ if 101<= ele <=200 :
                print(ele * 7)
            case _ if  ele >200 :
                print(ele * 10)
    case _ :
        print("Invalid Input")