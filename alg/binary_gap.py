class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        max_len, pos = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                max_len = max(max_len, i - pos)
                pos = i
        return max_len
