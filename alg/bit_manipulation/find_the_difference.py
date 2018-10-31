class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for i in (s + t):
            res ^= ord(i)
        return chr(res)
