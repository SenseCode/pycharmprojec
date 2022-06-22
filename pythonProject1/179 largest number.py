from functools import cmp_to_key


def largestNumber(nums) :
    '''
    解题思路：
    先把array 里的整数改成string，可以对string进行排序，和对整数一样。
    对str的组合进行排序。
    排序后对整个array里的数组合就是最大数。此时【0,0,0】的情况应该转换成int后再转换成string，返回结果。

    '''

    for i, n in enumerate(nums):
        nums[i] = str(n)


    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1


    nums = sorted(nums, key=cmp_to_key(compare))
    return str(int("".join(nums)))
nums=[1, 24, 30, 9, 8]
print(largestNumber(nums))
