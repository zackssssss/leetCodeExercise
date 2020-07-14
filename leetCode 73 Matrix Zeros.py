from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowHasZero = False
        firstColHasZero = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                firstColHasZero = True
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                firstRowHasZero = True

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if firstRowHasZero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        if firstColHasZero:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        print(matrix)


if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s = Solution()
    s.setZeroes(matrix)
