from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]

        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    s = Solution()
    print(s.findMin(nums))
