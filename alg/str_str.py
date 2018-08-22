class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

        # Or directly use find...... see the raw implementation in compare_str
a = Solution()
print(a.strStr("aaaa", "bba"))