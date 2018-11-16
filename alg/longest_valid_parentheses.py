class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':  # push (
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    last_pos = -1  # for a pair of parentheses that split by others in between
                    if stack:
                        last_pos = stack[-1]
                    max_len = max(max_len, i - last_pos)
                else:  # push )
                    stack.append(i)
        return max_len
