#find the missing elements:
'''
finder([1,2,3,4,5,6,7],[ 3,7,2,1,4,6])
'''
# missing number in array

def finder(list1,list2):
    map={}
    for num in list1:
        if num  in map:
            map[num]+=1
        else:
            map[num]=1

    for num2 in list2:
        if num2 in map:
            map[num2]-=1
    for item in map:
        if map[item]!=0:
            return item
m=finder([1,2,3,4,5,6,7],[ 3,7,2,1,4,6])
print(m)



