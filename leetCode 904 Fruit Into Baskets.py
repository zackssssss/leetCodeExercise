from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        baskets = {}
        j = 0
        res = 1
        for i in range(len(tree)):
            baskets[tree[i]] = i
            if len(baskets) > 2:
                mindex = len(tree)
                for (fruit, index) in baskets.items():
                    if mindex > index:
                        mindex = index
                del baskets[tree[mindex]]
                j = mindex + 1
            res = max(i - j + 1, res)
        return res
