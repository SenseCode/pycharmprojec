
def compress(s):
    counter=0
    res=""
    if len(s)==0:
        return ""
    if len(s)==1:
        return s+"1"
    i=1
    while i<len(s):
        if s[i]==s[i-1]:
            counter+=1
        else:
            res=res+s[i-1]+str(counter)
            counter=1
        i+=1
    res=res+s[i-1]+str(counter)
    return res
s="AAbbbCCCddd"
str=compress(s)
print(str)