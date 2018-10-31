class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) == len(B):
            if B in (A * 2):
                return True
        return False

    def rotateString1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # ugly
        from collections import deque
        a = deque(A)
        for _ in range(len(A)):
            a.rotate()
            if ''.join(a) == B:
                return True
        return ''.join(a) == B
