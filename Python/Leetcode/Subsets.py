import itertools


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combs = []
        for i in range(len(nums) + 1):
            combs += itertools.combinations(nums, i)

        return list(combs)