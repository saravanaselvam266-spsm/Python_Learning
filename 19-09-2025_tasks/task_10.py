#TASK-10 An e-commerce app gives different messages based on payment mode:

payment = input("Enter your payment mode('UPI','Card','NetBanking','COD') :")

match payment :
    case "UPI" :
        print("You selected UPI payment")
    case "Card" :
        print("You selected Debit/Credit Card payment")
    case "NetBanking" :
        print("You selected Net Banking")
    case "COD" :
        print("You selected Cash on Delivery")
    case _ :
        print("Invalid Payment Mode")
