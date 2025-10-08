# Write a program using nested match-case to decide an education path.

choice = input("Enter your choice ('Science','Commerce','Arts') :")

match choice :
    case 'Science' :
        sub_choice = input("Enter your sub-choice ('Medical','Engineering') :")
        match sub_choice :
            case  'Medical' :
                print("You chosen career path is Science -> Medical")
            case 'Engineering' :
                print("You chosen career path is Science -> Engineering")
            case _ :
                print("Invalid sub-choice for Science")
    case 'Commerce' :
        sub_choice = input("Enter your sub-choice ('CA','B Com') :")
        match sub_choice :
            case 'CA' :
                print("You chosen career path is Commerce -> CA")
            case 'B Com' :
                print("You chosen career path is Commerce -> B Com")
            case _ :
                print("Invalid sub-choice for Commerce")
    case 'Arts' :
        sub_choice = input("Enter your sub-choice ('History','Literature') :")
        match sub_choice :
            case 'History' :
                print("You chosen career path is Arts -> History")
            case 'Literature' :
                print("You chosen career path is Arts -> Literature")
            case _ :
                print("Invalid sub-choice for Arts")
    case _ :
        print("Invalid Input")


            