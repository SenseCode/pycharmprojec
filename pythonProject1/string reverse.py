# sen=" this is the best"
# def stringReverse():
#     # sen.split()
    # print(sen.split())
    # print(reversed(sen.split()))

    # return " ".join(reversed(sen.split())) #do the same
    # return " ".join(sen.split()[::-1])

def rev_word(s):
    words=[]
    length=len(s)
    spaces=[" "]

    i=0
    while i<length:
        if s[i] not in spaces:
            word_start=i
            while i<length and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])

        i+=1
    print("words", words)

    return " ".join(reversed(words))


s="  John, how are you "

str=rev_word(s)
print(str)