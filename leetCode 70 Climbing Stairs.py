class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1, 2]
        for i in range(2, n):
            memo.append(memo[i - 1] + memo[i - 2])

        return memo[n - 1]


if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.climbStairs(3))
