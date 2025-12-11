'''3. A new chat app removes consecutive repeated characters to prevent spam stretching (e.g., "heyyyy").
 Given the message, compress any sequence of repeated characters into a single character.
Input: heeelloooo
 Output: helo
Input: Yessss!!!!
 Output: Yes!'''

def remove_duplicate(word):
    result = ""
    for ch in word:
        if ch not in result:
            result += ch
    print(result)

remove_duplicate("heeelloooo")
remove_duplicate("Yessss!!!!")

#Option 2

def remove_dup(word):
    result = ""

    for ch in word:
        duplicate = False

        for existing in result:
            if existing == ch:
                duplicate = True
                break
        
        if duplicate == False:
            result += ch

    print(result)

remove_dup("heeelloooo")
remove_dup("Yessss!!!!")
