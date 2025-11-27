'''Given a list and a target value, return all indices where the target appears.
 Example: [1, 2, 3, 2, 4, 2] → target 2 → indices [1, 3, 5].'''


def is_index(num):
    foo = []
    for i in range(0,len(num),1):
        if num[i] == 2:
            foo.append(i)
    print(foo)

is_index([1, 2, 3, 2, 4, 2])
            
