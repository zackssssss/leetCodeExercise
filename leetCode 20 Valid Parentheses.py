class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in range(len(s)):
            # 左括号的情况
            if s[i] in parentheses:
                stack.append(parentheses.get(s[i]))
            # 右括号的情况
            else:
                if len(stack) == 0 or stack.pop() != s[i]:
                    return False

        if len(stack) > 0:
            return False
        return True


if __name__ == "__main__":
    s = "][]}"
    check = Solution()

    print(check.isValid(s))
