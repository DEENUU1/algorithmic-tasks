class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0

        n = len(nums)

        for start in range(n-1):
            for i in range(start + 1, n):
                if nums[i] == nums[start]:
                    res += 1            

        return res 
