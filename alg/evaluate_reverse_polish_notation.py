class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            else:
                f, s = stack.pop(), stack.pop()
                if i == '+':
                    stack.append(s + f)
                if i == '-':
                    stack.append(s - f)
                if i == '*':
                    stack.append(s * f)
                if i == '/':
                    stack.append(int(s / f))
        return stack[0]
