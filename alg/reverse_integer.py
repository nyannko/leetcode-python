class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        if x >= 0:
            res = self.rev(x)
        else:
            res = - self.rev(-x)
        return res if self.is_range(res) else 0

    def rev(self, x):
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x / 10
        return rev

    def is_range(self, res):
        return -2 ** 31 < res < 2 ** 31 - 1  # range has limited input
