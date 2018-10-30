class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        from collections import deque
        s = deque()
        for i in S:
            if s and s[-1] == '(' and i == ')':
                s.pop()
            else:
                s.append(i)
        return len(s)
