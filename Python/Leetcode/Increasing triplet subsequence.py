# Solution 1 - doesnt work

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        size = 3

        for i in range(len(nums) - size + 1):
            w = nums[i: i + size]
            print(w)
            if w[0] < w[1] < w[2]:
                return True

        return False

s = Solution()
s.increasingTriplet([20,100,10,12,5,13])


# Solution 2

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        min1 = float('inf')
        min2 = float('inf')

        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True

        return False