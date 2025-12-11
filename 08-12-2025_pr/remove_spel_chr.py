'''A website allows only lowercase letters, digits, and underscores in usernames.
Given a username, remove all other characters.
Input: "Ram!_Kumar@2024"
Output: ram_kumar2024
Input: "HELLO*123"
Output: hello123'''




def remove_spe_chr(x):
    alp = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    num = "0123456789"
    result = ""
    for ch in  x:
        if ch == "_" or ch in num:
            result += ch
        if ch in alp:
            result += ch.lower()
    print(result)

remove_spe_chr("Ram!_Kumar@2024")
remove_spe_chr("HELLO*123")




