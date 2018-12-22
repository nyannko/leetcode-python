class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s[::-1] == s

    def isPalindrome_half(self, x):
        if x < 0 or (x != 0 and x % 10 == 0): return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x / 10
        return (rev == x) or (x == rev / 10)  # use floor divide

    def isPalindrome_whole(self, x):
        if x < 0 or (x != 0 and x % 10 == 0): return False
        res, rev = x, 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x / 10
        return rev == res
