import itertools

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        possible_codes = 2 ** k
        uniq = set()

        for i in range(len(s) - k + 1):
            code = s[i:i + k]
            uniq.add(code)

            if len(uniq) == possible_codes:
                return True

        return False