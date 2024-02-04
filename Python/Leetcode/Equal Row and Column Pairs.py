class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        equal_pairs_count = 0

        for i in range(n):
            row = grid[i]

            for j in range(n):
                col = [grid[k][j] for k in range(n)]

                if row == col:
                    equal_pairs_count += 1

        return equal_pairs_count

