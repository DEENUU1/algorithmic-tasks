class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        w = set()
        l = 0

        for i in range(len(nums)):
            if i - l > k:
                w.remove(nums[l])
                l += 1
            if nums[i] in w:
                return True
            w.add(nums[i])
        return False
