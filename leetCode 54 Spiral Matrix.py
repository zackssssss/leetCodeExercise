from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if len(matrix) == 0:
            return []

        res = []
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0
        direction = 'right'

        while top <= bottom and left <= right:
            if direction == 'right':
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
                direction = 'bottom'

            elif direction == 'bottom':
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1
                direction = 'left'

            elif direction == 'left':
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                direction = 'top'

            elif direction == 'top':
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                direction = 'right'
        return res


if __name__ == '__main__':
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    p = Solution()
    print(p.spiralOrder(mat))
