'''Count how many words contain digits
Input:
 "room1 is bigger than room2 but room3 is small"
 Output:
 3'''

def count_word(sen):
    count = 0
    temp = sen.split()
    for el in temp:
        for ch in el:
            if ch in "0123456789" :
                count += 1
    print(count)

count_word("room1 is bigger than room2 but room3 is small")