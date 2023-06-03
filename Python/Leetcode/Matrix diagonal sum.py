class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0 
        for i in range(len(mat)):
            res += mat[i][i] + (0 if len(mat) - i - 1 == i else mat[i][len(mat) - i - 1])
        return res