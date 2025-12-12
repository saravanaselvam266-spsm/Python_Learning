'''input=["1/2", "2/09", "3/06"]
7:32
ouput=6
add all dates

imagine first is date secnd one is month'''

def adding_date(num):
    new = 0
    for i in range(0,len(num),1):
        temp = num[i].split("/")
        new = new + int(temp[0])
    print(new)

adding_date(["1/2", "2/09", "3/06"])

