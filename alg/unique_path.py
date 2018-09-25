class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = [[-1] * n for _ in range(m)]
        table[0][0] = 1

        def dfs(m, n):
            if m < 0 or n < 0:
                return 0
            if m == 0 and n == 0:
                return table[0][0]

            if table[m][n] != -1:
                return table[m][n]
            else:
                table[m][n] = dfs(m - 1, n) + dfs(m, n - 1)
                return table[m][n]

        def dfs1(m, n):
            if table[m][n] == -1:
                if m < 0 or n < 0:
                    return 0
                if m == 0 and n == 0:
                    return table[0][0]
                table[m][n] = dfs(m - 1, n) + dfs(m, n - 1)

            return table[m][n]

        return dfs1(m - 1, n - 1)


a = Solution()
print(a.uniquePaths(3, 2))
