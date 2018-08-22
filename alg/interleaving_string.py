class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # create a table for dp
        row = len(s1) + 1
        col = len(s2) + 1
        print(row+col, len(s3)+2)
        if row + col != len(s3) + 2:
            return False

        table = [[True for _ in range(col)] for _ in range(row)]  # col --> row
        print(table)

        # fill edge values
        for i in range(row):
            if i < 1: continue
            table[i][0] = s1[i - 1] == s3[i - 1] and table[i - 1][0]

        for i in range(col):
            if i < 1: continue
            table[0][i] = s2[i - 1] == s3[i - 1] and table[0][i - 1]

        # fill internal values
        for i in range(row):
            if i < 1: continue
            for j in range(col):
                if j < 1: continue
                table[i][j] = (s1[i - 1] == s3[i + j - 1] and table[i - 1][j]) or \
                              (s2[j - 1] == s3[i + j - 1] and table[i][j - 1])

        print(table)
        return table[row - 1][col - 1]


a = Solution()
print(a.isInterleave("a", "b", "a"))
