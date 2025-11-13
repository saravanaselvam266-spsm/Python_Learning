class Orders:
    # constructor
    def __init__(self):
        self.order = []

    # methods

    def add_items(self,id,product_name,quantity,price):
        current_list = {"id":id,"product_name": product_name,"quantity":quantity,"price" :price }
        self.order.append(current_list)
        
    def view_list(self):
        print(self.order)    


    def remove_items(self,id):
        for i in range(len(self.order)):
            if self.order[i].id == id:
                del self.order[i]
            return "Product Deleted Successfully"


    def display_items(self):
        pass





alex=Orders()
alex.add_items(id=1,product_name="Cakes",quantity=2,price=20)
alex.add_items(id=2,product_name="coffee",quantity=3,price=45)
alex.view_list()
alex.remove_items(id=1)
alex.view_list()

