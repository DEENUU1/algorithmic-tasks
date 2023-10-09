class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l, r = 0, len(height) - 1

        lmax, rmax = height[l], height[r]

        res = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]

            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]

        return res
