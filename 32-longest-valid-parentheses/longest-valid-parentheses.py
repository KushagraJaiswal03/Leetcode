class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # sentinel base index

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    # No matching '(' — this ')' becomes the new base
                    stack.append(i)
                else:
                    # Valid substring found; length = current index - new top of stack
                    max_len = max(max_len, i - stack[-1])

        return max_len