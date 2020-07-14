from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        resMap = {}
        res = []
        for i in range(len(s) - 10):
            temp = s[i:i + 10]
            if not temp in resMap:
                resMap[temp] = 1
            elif resMap[temp] == 1:
                res.append(temp)
                resMap[temp] += 1
            else:
                resMap[temp] += 1
        return res


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    so = Solution()
    print(so.findRepeatedDnaSequences(s))
