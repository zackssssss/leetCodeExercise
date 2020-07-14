from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            memo.append(max(memo[i - 1], nums[i] + memo[i - 2]))

        return memo[len(nums) - 1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    s = Solution()
    print(s.rob(nums))
