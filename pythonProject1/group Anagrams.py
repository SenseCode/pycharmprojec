def groupAnagrams(strs):
    from collections import defaultdict
    dic=defaultdict(list)
    for c in strs:
        sorted(c)
        "".join(sorted(c))
        dic["".join(sorted(c))].append(c)
    return list(dic.values())
strs=["eat","tea","tan","ate","nat","bat"]
s=groupAnagrams(strs)
print(s)
c="eat"
s1=sorted(c)
s2="".join(sorted(c))
print("s1",s1)
print("s2",s2)


