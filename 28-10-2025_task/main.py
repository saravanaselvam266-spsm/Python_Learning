# Tasks 
# Part - 1
# Sum 1

word = "Python"
rev = ""
for i in range(len(word)):
    rev =word[i] + rev
print("Reversed:", rev)

# Sum 2

text = "Education"
count = 0
for ch in text:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count = count + 1
print("Vowels:", count)


# Sum 3

nums = [9, 5, 3, 8]
min_num = nums[0]
for i in nums:
    if i < min_num:
        min_num = i
print(min_num)

# Sum 4

def alt_number(num):
    a = []
    for i in range(0,len(num),2):
        a.append(num[i])
    print(a)

alt_number([10, 20, 30, 40, 50])

# Sum 5

nums = [-3, 5, -2, 7]
for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0
print(nums)



# Part - 2

# Sum 1


def vowels_letter(word):
    a = []
    b = ['a','e','i','o','u']
    for i in word:
        if i in b :
            a.append(i)
    print(a)

vowels_letter("education")

# Sum 2

# Sum 3

def array_of_integer(num):
    count = 0
    sum = 0
    dicts = {}
    for i in num :
        if i%2 == 0:
            count += 1
        else :
            sum += 1
    dicts["Even"] = count
    dicts["Odd"] = sum
    return dicts

print(array_of_integer([1, 2, 3, 4, 5, 6, 7]))