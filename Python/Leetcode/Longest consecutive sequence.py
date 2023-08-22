class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        sortnums = sorted(nums) 

        longest_streak = 1  
        current_streak = 1  

        for i in range(1, len(sortnums)):
            if sortnums[i] == sortnums[i - 1] + 1:  
                current_streak += 1
            elif sortnums[i] != sortnums[i - 1]: 
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        return max(longest_streak, current_streak)