# ‘’‘
# 给出一个string，输出每个字母出现的次数，按照输出位置输入：
# str=‘abaac,’
# output=['a':3,'b':1,"c":1,",":1]
# ’‘’
# def strcount(str):
#     count={}
#     # import Count from collections:
#     for i in range(len(str)):
#         if str[i] not in count:
#             count[str[i]]=0
#         count[str[i]]+=1
#     return count.values()
# O(n)
# str="abaac,"
# s=strcount(str)
# print("s",s)
# ======================================================
#  两个数列，如［1，2，3，4，5］和［5，3，2，1，4］，求最少
# 要多少次swap能使两个相同。

# def swapArray(a, b):
#     count = 0
#     for i in range(len(a)):
#         for j in range(i, len(b)):
#             if a[i] == b[j]:
#                 if i == j:
#                     continue
#                 tem = b[i]
#                 b[i] = b[j]
#                 b[j] = tem
#                 count = count + 1
#     return count
#
#
# a = [1, 2, 3, 4, 5]
# b = [5, 3, 2, 1, 4]
# c = [1, 2, 3, 4, 5]
# d=[1,3,4,2,5]
# res=swapArray(a,d)
# print(res)
# =============================================================
#      '''第一题 checkMonotonicity, 给一个array, 要求return
#     一个新的boolean array, size 比input array 小2. 如果input array 连续三
#     个element 都上涨，就在新的array 对应位置填true, 否则填false. 举
#     例： input [1，2，3，4，3, 4, 5], output: [true, true, false, false, true].
#     # res=[true, true, false, false, true]
#     "sliding window" window size 3 i, i+2,compare'''

def checkIncre(a, k):
    # res = [False] * (len(a) - 2)
    # for i in range(len(a) - 2):
    #     # if a[i+1]<a[i]:
    #     #    res[i]="False"
    #
    #     if a[i + 1] > a[i] and a[i + 2] > a[i + 1]:
    #         res[i] = True
    #     else:
    #         res[i] = False
    # return res
    a = [1, 2, 3, 4, 3, 4, 5]
    ans = isEligible(a,3)
    print(ans)
#
# def isEligible(a, k):
#     res = [false] * k-2
#     for i in range(k-2):
#         while i < k:
#             if a[i + 1] > a[i] and a[i + 2] > a[i + 1]:
#                 res[i] = true
#             else:
#                 res[i] = false
#     return res
#
#
# a = [1, 2, 3, 4, 3, 4, 5]
# k = 3
# s = checkIncre(a, 3)
# print(s)
# 比如input string 是 abcdef, brute force 我是两个nested loop, 分别代表
# 第一段substring 和 第二段substring 的长度，从长度1开始loop, 所以所
# 有的情况就是 [a, b, cdef], [a,bc, def], [a, bcd ,ef], [a, bcde, f], [ab, c,
# def], [ab, cd, ef].........

# def splitStr(str):
#     res=[]
#     l=0
#     r=len(str)-1# index 0 start
#     while l<r:
#         str1=str[0:l+1]
#         str2=str[l+1:l+r]
#         str3=str[l+r:]
#         if str1+str3!=str2:
#             res.append([str1,str2, str3])
#             l=l+1
#         r=r-1
#
#     return res
# str='ababff'
# s=splitStr(str)
# print(s)
# '''Give a K, and n,
# N=len(ar)
# Return k length array with value not showed in ar.
# Output=[1,4, 7,8,9]
# '''Ar=[2,3,5,5,6]

def continious(arr,k):
    n=len(arr)
    res=[]
    index=1
    ar=set(arr)
    print(ar)
    while len(res)<k:
        if index not in ar:
            res.append(index)
        index += 1
        print('index', index)
    return res

arr=[2,3,5,5,6]
s=continious(arr,5)
print(s)







