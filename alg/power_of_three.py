class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while n % 3 == 0:
            n = n / 3
        return n == 1

    def isPowerOfThree1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # tricky 3 ** 19
        return n > 0 and 1162261467 % n == 0
