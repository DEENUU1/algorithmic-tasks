class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        largest_perimeter = 0
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return largest_perimeter
