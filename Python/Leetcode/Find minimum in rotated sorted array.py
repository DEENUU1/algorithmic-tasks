class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = float('inf')

        if l < r:
            mid = (r + l) // 2

            res = min(res, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid - 1

        return min(res, nums[l])