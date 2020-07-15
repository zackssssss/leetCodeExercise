class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        for i in range(len(s)):
            if not s[i] in map1:
                map1[s[i]] = 1
            else:
                map1[s[i]] += 1

            if not t[i] in map1:
                map1[t[i]] = -1
            else:
                map1[t[i]] -= 1
        for elem in map1.values():
            if elem != 0:
                return False

        return True
