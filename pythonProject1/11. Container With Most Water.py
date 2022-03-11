def maxArea( height) :
    '''
    height = [1,8,6,2,5,4,8,3,7]

    '''
    res = []
    n = len(height)
    for i in range(1, n - 1):
        for j in range(i+1, n):

            res.append(min(height[i], height[j])* (j - i))
    # res=max(water,min(i-j)*(j-i))
    return max(res)
height = [1,8,6,2,5,4,8,3,7]
water=maxArea(height)
print(water)

