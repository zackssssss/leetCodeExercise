class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s.isspace():
            return True

        lows = s.lower()
        head = 0
        end = len(lows) - 1
        while head < end:
            if not lows[head].isalnum():
                head += 1
                continue
            if not lows[end].isalnum():
                end -= 1
                continue
            if lows[head] != lows[end]:
                return False
            head += 1
            end -= 1

        return True


if __name__ == '__main__':
    string = "A man, a plan, a canal: Panama"
    s = Solution()
    print(s.isPalindrome(string))
