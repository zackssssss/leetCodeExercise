from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 == 1:
                while A[j] % 2 == 1 and j < len(A):
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
