from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for eum in nums:
            if eum in res:
                return True
            else:
                res.add(eum)
        return False
