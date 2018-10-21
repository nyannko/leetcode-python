class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in [2, 3, 5]:
            while num % p == 0 and num > 0:
                num /= p
        return num == 1

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        for _ in range(n - 1):
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
        return ugly[-1]

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        index = [0 for _ in primes]
        for _ in range(n - 1):
            u = [ugly[x] * y for x, y in zip(index, primes)]
            umin = min(u)
            for i, v in enumerate(u):
                if v == umin:
                    index[i] += 1
            ugly.append(umin)
        return ugly[-1]
