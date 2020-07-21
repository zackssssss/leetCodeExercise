from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                return 0
            grid[row][col] = 0
            count = 1
            count += dfs(row - 1, col)
            count += dfs(row + 1, col)
            count += dfs(row, col - 1)
            count += dfs(row, col + 1)
            return count

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    tempCount = dfs(row, col)
                    res = max(res, tempCount)

        return res


if __name__ == '__main__':
    grids = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    s = Solution()
    print(s.maxAreaOfIsland(grids))
