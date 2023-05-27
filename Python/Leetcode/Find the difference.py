class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in t:
            if c in count:
                count[c] -= 1
            else:
                count[c] = -1
        for c, val in count.items():
            if val == -1:
                return c
