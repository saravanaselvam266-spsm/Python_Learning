'''Given a string, the task is to reverse the order of the words in the given string.

Examples:

Input: s = “hello everyone”

Output: s = “everyone hello”

Input: s = “i love programming very much”

Output: s = “much very programming love i”'''

def is_word_rev(sen):
    sentence = sen.split()
    result = ""
    for el in sentence:
        result = el + " "+ result
    print(result)

is_word_rev("i love programming very much")
        