class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = {}
        res = n
        while True:
            res = sum([int(c) ** 2 for c in str(res)])
            if res == 1:
                return True
            elif res in visited:
                return False
            else:
                visited[res] = None
