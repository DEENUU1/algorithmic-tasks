class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for n in range(len(nums)):
            res += n - nums[n]
        return res 