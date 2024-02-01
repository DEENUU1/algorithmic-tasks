# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
from typing import List, Tuple, Dict


def main(matrix: List[List[int]]) -> List[List[int]]:
    zero_positions = find_zero(matrix)

    for row, col in zero_positions:
        # Set entire row to 0
        matrix[row] = [0] * len(matrix[0])

        # Set entire column to 0
        for i in range(len(matrix)):
            matrix[i][col] = 0

    return matrix


def find_zero(matrix: List[List[int]]) -> List[Tuple[int, int]]:
    zero_positions = []

    for row_idx, row in enumerate(matrix):
        for col_idx, val in enumerate(row):
            if val == 0:
                zero_positions.append((row_idx, col_idx))

    return zero_positions


print(main([[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 11, 12], [13, 0, 15, 16]]))
# 1 2 3 4
# 5 6 0 8
# 9 10 11 12
# 13 0 15 16

# 1 0 0 4
# 5 0 0 8
# 9 0 0 12
# 0 0 0 0