class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        pos = 1
        while m != n:
            m >>= 1
            n >>= 1
            pos <<= 1
            # print m, n, pos
        return m * pos
