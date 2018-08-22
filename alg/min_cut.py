class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        # Init table p, f
        p = [[False for _ in range(length + 1)] for _ in range(length + 1)]
        f = []
        print(p)

        # Fill table f with the worst cut number
        for i in range(length + 1):
            f.append(length - 1 - i)
        print(f)

        # Fill table p with True if the string is the palindrome
        # Then substitute new minimum value in table f
        for i in reversed(range(length)):
            for j in range(i, length):
                if s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1]):
                    print(p[i + 1][j - 1])
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]

    def min_cut(self, s):
        length = len(s)

        p = [[False for _ in range(length)] for _ in range(length)]
        f = []

        for i in range(length + 1):
            f.append(length - 1 - i)

        for i in reversed(range(length)):
            for j in range(i, length):
                if s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1]):
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]


a = Solution()
print(a.min_cut('aab'))
