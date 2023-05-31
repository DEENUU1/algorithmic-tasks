class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = set(nums1).difference(nums2)
        num2 = set(nums2).difference(nums1)

        return [list(num1), list(num2)]