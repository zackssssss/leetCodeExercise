from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProductMemo = [nums[0]]
        minProductMemo = [nums[0]]
        maxRes = nums[0]
        for i in range(1, len(nums)):
            maxProductMemo.append(max(nums[i], nums[i] * maxProductMemo[i - 1], nums[i] * minProductMemo[i - 1]))
            minProductMemo.append(min(nums[i], nums[i] * maxProductMemo[i - 1], nums[i] * minProductMemo[i - 1]))
            maxRes = max(maxRes, maxProductMemo[i])

        return maxRes


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    s = Solution()
    print(s.maxProduct(nums))
