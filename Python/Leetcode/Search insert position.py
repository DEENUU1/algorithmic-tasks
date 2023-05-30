class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min_num = 0
        max_num = len(nums) - 1
        mid = 0

        while min_num <= max_num:

            mid = (min_num + max_num) // 2 
            if nums[mid] < target:
                min_num = mid + 1

            elif nums[mid] > target:
                max_num = mid - 1
            
            else:
                return mid
                
            
        return min_num