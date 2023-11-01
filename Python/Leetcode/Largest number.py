# Solution 1 - Time Limit Exceeded

import itertools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        perm = list(itertools.permutations(nums))

        l = []
        for p in perm:
            s = ""
            for n in p:
                s += str(n)
            l.append(int(s))

        return str(max(l))


# Solution 2

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key = cmp_to_key(compare))

        return str(int("".join(nums)))
