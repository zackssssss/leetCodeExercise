class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1
        backSpaceS = 0
        backSpaceT = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    backSpaceS += 1
                    i -= 1
                elif backSpaceS > 0:
                    i -= 1
                    backSpaceS -= 1
                else:
                    break

            while j >= 0:
                if T[j] == "#":
                    backSpaceT += 1
                    j -= 1
                elif backSpaceT > 0:
                    j -= 1
                    backSpaceT -= 1
                else:
                    break
            if (i < 0 <= j) or (j < 0 <= i):
                return False
            if i < 0 and j < 0:
                return True

            if S[i] != T[j]:
                return False
            i -= 1
            j -= 1

        return True
