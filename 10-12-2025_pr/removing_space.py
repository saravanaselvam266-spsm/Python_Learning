def remove_spaces(sentence):
    #start
    result = []
    word = ""
    # loop
    for i in range(0,len(sentence),+1):
        # single whitespace
        if sentence[i] != " ":
            word = word + sentence[i]
        else:
             # push word into result
            if word not in result:
                result.append(word)
            word = ""
    result.append(word)
    print(result)
    final = ""
    for word in result :
        final = final + word + " "
    print(final)
    #stop
remove_spaces("secret  mission  starts   here")