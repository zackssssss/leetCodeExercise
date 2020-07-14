from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return []

        maplist = {}

        for eachStr in strs:
            characters = [0] * 26
            for eachChar in eachStr:
                index = ord(eachChar) - 97
                characters[index] += 1

            key = ''.join(map(str, characters))

            if key in maplist:
                maplist.get(key).append(eachStr)
            else:
                maplist[key] = [eachStr]

        result = []
        for value in maplist.values():
            result.append(value)
        return result


if __name__ == "__main__":
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    check = Solution()

    print(check.groupAnagrams(s))
