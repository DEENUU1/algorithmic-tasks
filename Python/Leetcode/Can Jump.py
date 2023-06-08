class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = len(nums) - 1

        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= res:
                res = i
            
        return res == 0