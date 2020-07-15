class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        pre2 = 0
        pre1 = 1
        res = 0
        for i in range(2, N + 1):
            res = pre2 + pre1
            pre2 = pre1
            pre1 = res
        return res
