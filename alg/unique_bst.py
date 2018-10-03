class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0 for i in range(n + 1)]
        f[0] = 1
        f[1] = 1
        for i in range(2, n + 1):
            for k in range(i + 1):
                f[i] += f[k - 1] * f[i - k]
        return f[-1]
