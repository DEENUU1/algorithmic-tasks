class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum, r_sum = 0, sum(nums)

        for idx, el in enumerate(nums):
            r_sum -= el
            if l_sum == r_sum:
                return idx
            l_sum += el
        return -1