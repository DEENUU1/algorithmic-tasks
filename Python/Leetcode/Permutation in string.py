# Solution 1 - Memory limit error

from itertools import permutations


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        per = permutations(s1)
        per_lst = []
        res = False

        for p in list(per):
            per_lst.append("".join(p))

        for p in per_lst:
            if p in s2:
                res = True

        return res


# Solution 2 - Sliding window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1C, s2C = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1C[ord(s1[i]) - ord("a")] += 1
            s2C[ord(s2[i]) - ord("a")] += 1

        m = 0
        for i in range(26):
            m += 1 if s1C[i] == s2C[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if m == 26:
                return True

            idx = ord(s2[r]) - ord("a")
            s2C[idx] += 1
            if s1C[idx] == s2C[idx]:
                m += 1
            elif s1C[idx] + 1 == s2C[idx]:
                m -= 1

            idx = ord(s2[l]) - ord("a")
            s2C[idx] -= 1
            if s1C[idx] == s2C[idx]:
                m += 1
            elif s1C[idx] - 1 == s2C[idx]:
                m -= 1

            l += 1

        return m == 26

