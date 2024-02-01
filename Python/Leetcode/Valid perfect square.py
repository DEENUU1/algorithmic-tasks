class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res = math.sqrt(num)
        res_rounded = round(res)
        return res_rounded == res
