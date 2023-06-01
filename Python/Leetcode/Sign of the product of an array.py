from operator import mul 

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = reduce(mul, nums, 1)
        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        return 0