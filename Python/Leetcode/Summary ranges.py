class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        total = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue 

            else:
                if start == nums[i - 1]:
                    total.append(str(start))                
                else: 
                    total.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

            
        if start == nums[-1]:
            total.append(str(start))
        else:
            total.append(f"{start}->{nums[-1]}")
        
        return total