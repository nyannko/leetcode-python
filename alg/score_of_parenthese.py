class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(-1)
            else:
                cur = 0
                while stack[-1] != -1:
                    cur += stack.pop()
                stack.pop()
                if cur == 0:
                    stack.append(1)
                else:
                    stack.append(cur * 2)
        return sum(stack)

    def scoreOfParentheses1(self, S):
        """
        :type S: str
        :rtype: int
        """
        layer, result = 0, 0

        for i, c in enumerate(S):
            if (c == '('):
                layer += 1
            else:
                layer -= 1
                if (S[i - 1] == '('):
                    result += 2 ** layer
        return result

a = Solution()
a.scoreOfParentheses1("(()(()))")