from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPosition = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= maxPosition:
                maxPosition = i
        return maxPosition == 0


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    s = Solution()
    print(s.canJump(nums))
