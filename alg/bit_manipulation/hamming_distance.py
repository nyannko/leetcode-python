class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            if (x & 1) ^ (y & 1) == 1:
                res += 1
            x >>= 1
            y >>= 1
        return res

    def hammingDistance1(self, x, y):
        return bin(x ^ y).count('1')
