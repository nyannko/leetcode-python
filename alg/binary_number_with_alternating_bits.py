class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)
        return '00' not in s and '11' not in s
