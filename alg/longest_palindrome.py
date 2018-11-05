class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        c = Counter(s)
        odds = sum([i & 1 for i in c.values()])
        # sub all odds except for one(if there are some)
        return len(s) - odds + bool(odds)
