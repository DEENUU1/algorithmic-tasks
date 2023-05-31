class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        n = len(nums)
        
        for ele in nums:
            if ele in counter:
                counter[ele] += 1
            else:
                counter[ele] = 1
        
        for ele, count in counter.items():
            if count > n // 2:
                return ele
