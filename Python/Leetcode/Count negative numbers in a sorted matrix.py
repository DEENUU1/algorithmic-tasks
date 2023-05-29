class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for lst in grid:
            for el in lst:
                if el < 0:
                    count += 1

        return count