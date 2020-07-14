class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for i in range(m)] for j in range(n)]

        for i in range(m):
            memo[0][i] = 1

        for j in range(n):
            memo[j][0] = 1

        for row in range(1, n):
            for col in range(1, m):
                memo[row][col] = memo[row - 1][col] + memo[row][col - 1]

        return memo[n - 1][m - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3))
