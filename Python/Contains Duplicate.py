# Solution 1

class Solution(object):
    def containsDuplicate(self, nums):
        set_nums = set(nums)
        if len(set_nums) != len(nums):
            return True
        return False 
    
# Solution 2

class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 