class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 1
        while num >= mask:
            num ^= mask
            mask <<= 1
        return num
