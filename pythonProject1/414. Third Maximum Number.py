class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        maxi = max(nums)
        if len(nums) < 3:
            return maxi
        nums.remove(maxi)
        sec_max = max(nums)
        nums.remove(sec_max)
        return max(nums)
