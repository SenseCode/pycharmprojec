def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    解题思路：
    bucket sort， replace the sorted color and put it back，since they ask a in place replace instead, have to do a swap.

    two pointers:
    定义 l，r pointers 和 i
    i 是0 就和左边换，i是2就和右边换。i<r 的时候执行。i和右边换的时候i不需要加移动。
    最后执行完nums就还是原位swap的nums
    """

    l, r = 0, len(nums) - 1
    i = 0

    def swap(i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    while i <= r:
        if nums[i] == 0:
            swap(l, i)
            l = l + 1
        elif nums[i] == 2:
            swap(i, r)
            r = r - 1
            i = i - 1
        i = i + 1
