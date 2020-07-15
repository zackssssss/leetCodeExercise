from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tempres = set(nums1)
        res = set()
        for elem in nums2:
            if elem in tempres:
                res.add(elem)

        return list(res)
