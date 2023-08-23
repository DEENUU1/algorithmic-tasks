class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not target in nums:
            return -1

        sorted(nums)
        return nums.index(target)