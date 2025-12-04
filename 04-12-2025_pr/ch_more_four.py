'''3. Write a python program to find the words that has more than 4 characters
Sample Input:
This is a python program
Sample Output:
python
program'''

def is_more_four(sen):
    foo = sen.split(" ")
    print(foo)
    res = ""
    for el in foo:
        if len(el) > 4:
            res += el + " " 
    print(res)
is_more_four("This is a python program")
            


        


        