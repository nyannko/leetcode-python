class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_s = len(s) + 1
        len_t = len(t) + 1

        # build the table
        # table = [[0]*len_t for _ in range(len_s)]
        table = [[0]*len_t]*len_s
        print(table)
        for i in range(len_s):
            table[i][0] = 1
        print(table)

        for i in range(1, len_s):
            for j in range(1, len_t):
                if s[i - 1] != t[j - 1]:
                    table[i][j] = table[i - 1][j]
                else:
                    table[i][j] = table[i - 1][j] + table[i - 1][j - 1]
        print(table)
        return table[len_s - 1][len_t - 1]
#>>> a=[[0]*3]*2
# >>> a
# [[0, 0, 0], [0, 0, 0]]
# >>> a[0][0]=1
# >>> a
# [[1, 0, 0], [1, 0, 0]]
    def answer(self, s, t):
        dp = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)


a = Solution()
print(a.numDistinct("rabbbit", "rabbit"))
