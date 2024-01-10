
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [int(math.pow(x, 2)) for x in nums]
        return sorted(res)
