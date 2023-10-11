# Solution 1 - Time Limit Error

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while (b != 0):
            c = a & b
            a = a ^ b
            b = c << 1
        return a


# Solution 2 - Accepted

class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log(2 ** a * 2 ** b, 2))