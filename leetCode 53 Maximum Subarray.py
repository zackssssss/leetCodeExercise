from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = []
        maxRes = nums[0]
        memo.append(nums[0])
        for i in range(1, len(nums)):
            memo.append(max(nums[i], memo[i - 1] + nums[i]))
            maxRes = max(memo[i], maxRes)

        return maxRes


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = Solution()
    print(res.maxSubArray(nums))
