from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ct = Counter(text)
        b = Counter("balloon")

        res = len(text)
        for c in b:
            res = min(res, ct[c] // b[c])
        return res