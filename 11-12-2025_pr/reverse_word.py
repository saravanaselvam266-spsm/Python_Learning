'''2.Reverse only the words, not the whole sentence
Input: "I love python"
 Output → "I evol nohtyp"
 '''

def is_reverse(sen):
    result  = []
    words = ""
    sentence = ""
    for el in sen:
        if el !=" ":
            words += el

        else:
            result.append(words)
            words = ""
    result.append(words)
    print(result)

    for el in result:
        for j in range(len(el)-1,-1,-1):
            sentence +=el[j] + " "

    print(sentence)

is_reverse("I love python")
            
     