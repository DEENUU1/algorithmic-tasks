class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:

        res = [nums[0]]



        for i in range(1, len(nums)):

            nums[i] += nums[i-1]

            res.append(nums[i])



        return res

