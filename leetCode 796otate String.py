class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        A += A
        if A.find(B) != -1:
            return True
        return False
