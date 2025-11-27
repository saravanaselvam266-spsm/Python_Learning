"""Words Ending in "ing"
Input:
["playing", "run", "walking", "see", "coding"]
Expected Output:
["playing", "walking", "coding"]"""


def is_ing_end(word, target):
    word_list = []
    l = len(target) #3 
    for el in word:
        temp = el[-l:]
        if temp == target:
            word_list.append(el)
    print(word_list)


is_ing_end(["playing", "run", "walking", "see", "coding"], "ing")
is_ing_end(["playing", "run", "walking", "see", "coding"], "ding")
