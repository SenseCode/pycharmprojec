def solution(a, b, k):
    count = 0
    l = 0
    r = len(b) - 1
    while l:
        sa = str(a[l])

        sb = str(b[r])
        # r=r-1
        if int(sa + sb) < k:
            count = count + 1
        l = l + 1
        r = r - 1

    return count

a = [1, 2, 3],
b = [1, 2, 3],
k=31
res=solution(a,b,k)
print("result",res)