def findMaxAverage(nums, k):
    g=sum(nums[:k])
    sumMax=g
    for i in range(len(nums)-k):
        g=g+nums[i+k]-nums[i]

        sumMax=max(sumMax,g)
    return sumMax/k

nums=[1,12,-5,-6,50,3]
k=4

res=findMaxAverage(nums,k)
print("res",res)

