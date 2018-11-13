class Solution(object):
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        table = {}
        res = ''
        if n % d == 0:
            return str(n / d)

        if n / d < 0:
            res += '-'

        n, d = abs(n), abs(d)

        res += str(n / d) + '.'

        n = n % d
        i = len(res)
        while n != 0:
            if n not in table:
                table[n] = i
            else:
                i = table[n]
                return res[:i] + "(" + res[i:] + ")"
            n = n * 10
            res += str(n / d)
            n = n % d
            i += 1
        return res
