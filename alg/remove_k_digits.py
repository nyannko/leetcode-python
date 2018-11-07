class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <= k:
            return '0'

        stack = []
        for i in num:
            while stack and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        # while k > 0:
        #     stack.pop()
        #     k -= 1
        if k:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'
