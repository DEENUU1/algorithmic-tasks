
# Solution 1 - Time error

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        res = []
        while nums:
            num = nums.pop()
            diff = k - num
            if diff in nums:
                res.append((diff, num))

                nums.remove(diff)
        res.reverse()

        return len(res)


# Solution 2

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        i, j = 0, len(nums) - 1
        res = 0

        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                i += 1
                j -= 1
                res += 1
            elif s < k:
                i += 1
            else:
                j -= 1
        return res