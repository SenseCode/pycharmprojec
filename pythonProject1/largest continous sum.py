'''
list=[ 0,1,-1,2, 3, 4, 5]
max continous sum
'''
def maxSum(list):
    # sum=[float('-inf')]
    if len(list)==0:
        return 0
    curr_sum=list[0]
    max_sum=list[0]
    for num in list[1:]:
        curr_sum=max(curr_sum+num,num)
        max_sum=max(curr_sum,max_sum)
    return max_sum

list=[ 0,1,-1,2, 3, 4, 5]
m=maxSum(list)
print(m)


