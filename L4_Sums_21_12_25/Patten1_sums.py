def nums_patten(num):
    for i in range(num):
        for j in range(i + 1):
            print("*",end=" ")
        print()

nums_patten(5)