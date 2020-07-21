from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        origin = image[sr][sc]
        if origin == newColor:
            return image

        def dfs(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != origin:
                return
            image[row][col] = newColor
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        dfs(sr, sc)
        return image
