class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.replace('i', '').split('+')
        b = b.replace('i', '').split('+')
        real = []
        comp = 0
        for i in a:
            l = []
            for j in b:
                res = int(i) * int(j)
                l.append(res)
            real.append(l)

        real[1].reverse()
        res = zip(*real)
        real = str(res[0][0] - res[0][1])
        comp = str(res[1][0] + res[1][1])
        res = real + "+" + comp + 'i'
        return res
