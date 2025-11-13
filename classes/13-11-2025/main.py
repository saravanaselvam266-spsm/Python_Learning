# Classes

class ContactBook:
    # constructor
    def __init__(self):
        self.contacts = []

    # methods
    def add_contact(self,name,phone_number,email):
        current_list = {"name" : name,"phone_number" :phone_number,"email" :email}
        self.contacts.append(current_list)

    def view_list(self):
        print(self.contacts)

    
    def get_phone(self,name):
        self.name = name
        for el in self.contacts:
            if el["name"] == self.name:
                print(el["phone_number"])
            # else:
            #     print("invalid name")
    
    def update_phone(self,name, phone_number):
        self.name = name
        self.phone_number = phone_number
        for ch in self.contacts :
            if ch["name"] == self.name:
                ch["phone_number"] = self.phone_number
                print("Updated successfully")

            # else:
            #     print("Invalid Name")
            
    def delete_contact(self,name):
        self.name = name
        for el in self.contacts:
            if el["name"] == self.name:
                self.contacts.remove(el)
                print("Delete successfully")
            # else:
            #     print("Invalid Name")

my_book = ContactBook()

my_book.add_contact("John", "9994254379", "alice@email.com")
my_book.add_contact("Bob", "9876543210", "bob@email.com")

my_book.get_phone("John")# Should output: 123-456-7890
my_book.get_phone("Charlie") # Should output: Contact not found.
my_book.view_list()


my_book.update_phone("John","8994254379") # should update the contact
my_book.view_list()

my_book.delete_contact("Bob") # should delete and print output: "Deletion Completed"
my_book.view_list()



# my_book.view_list()

my_book.delete_contact("Ram") # Should Print: Contact Not found

            