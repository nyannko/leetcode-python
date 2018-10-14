class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        s = s[::-1]
        for i, v in enumerate(s):
            sum += (ord(v) - 64) * 26 ** i
        return sum

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        import string
        capitals = list(string.ascii_uppercase)
        result = []
        while n > 0:
            result.insert(0, capitals[(n - 1) % 26])
            n = (n - 1) // 26
        return ''.join(result)

# Positional notation
