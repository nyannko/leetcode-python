class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dvd = abs(dividend)
        dvs = abs(divisor)
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        res = 0
        # print sign 15 / 3
        while dvd >= dvs:
            tmp = dvs
            multiple = 1
            while dvd >= (tmp << 1):
                tmp <<= 1
                multiple <<= 1
                # print tmp, multiple 4
            dvd -= tmp
            # print res, multiple
            res += multiple
        # print res
        if sign == 1:
            return min(res, 2 ** 31 - 1)
        else:
            return max(-res, -2 ** 31)
