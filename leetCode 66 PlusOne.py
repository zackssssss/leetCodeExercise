from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        res = [1] + digits
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.plusOne(nums))
