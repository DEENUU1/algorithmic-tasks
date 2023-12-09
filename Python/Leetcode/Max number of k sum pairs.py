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