class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1) + 1
        len2 = len(word2) + 1

        table = [[0] * len2 for _ in range(len1)]
        #print(table)
        for i in range(len2):
            table[0][i] = i

        for i in range(len1):
            table[i][0] = i

        #print(table)

        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    mn = min(table[i - 1][j], table[i][j - 1])
                    table[i][j] = min(table[i - 1][j - 1], mn) + 1
        #print(table)
        return table[len1 - 1][len2 - 1]


a = Solution()
print(a.minDistance("str1c", "str2d"))
