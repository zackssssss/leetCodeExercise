class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                flag = isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
                if flag:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    string = "abc"
    s = Solution()
    print(s.validPalindrome(string))
