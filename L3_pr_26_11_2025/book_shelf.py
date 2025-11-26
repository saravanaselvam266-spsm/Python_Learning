'''An organization named “Higginbothams” maintains a library where all books with unique serial numbers are arranged in strict descending order (largest to smallest).

A new book arrives with a unique serial number. The librarian wants to insert it in the correct position so the order remains unchanged. 

Given:

A list of integers representing book serial numbers (sorted in descending order)

An integer representing the new book’s serial number

The first book is in position 1

If the list is empty , return -1 
Note: You cannot add books in the first or last position, you can add in between the first and the last book 

Input:

Books = [98, 75, 60, 50, 40, 25]

NewBook = 55

Output:
4

Explanation:
55 is greater than 60 and less than 50, so it has to be placed at index 4

For example:

Test	Result
book_shelf([98, 75, 60, 50, 40, 25], 55)
4
book_shelf([], 75)
-1'''

def book_shelf(books, newBook):
    #Write your code here
    if len(books) == 0:
        print(-1)
    else:
        x = newBook
        for i in range(0,len(books),1):
            if x > books[i] :
                print(i+1)
                return
            


book_shelf([98, 75, 60, 50, 40, 25], 55)
book_shelf([], 75)
