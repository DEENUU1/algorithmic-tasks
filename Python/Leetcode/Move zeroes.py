class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        norm = []
        zero = []

        for num in nums:
            if num == 0:
                zero.append(0)
            else:
                norm.append(num)
        
        nums[:] = norm + zero
        return nums