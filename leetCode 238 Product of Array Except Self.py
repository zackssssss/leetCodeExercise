from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1 for i in range(len(nums))]
        tempProduct = 1
        for i in range(len(nums)):
            res[i] = tempProduct * res[i]
            tempProduct = tempProduct * nums[i]

        tempProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = tempProduct * res[i]
            tempProduct = tempProduct * nums[i]

        return res
