class Solution(object):
    def strStr_kmp(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
        # https://leetcode.com/problems/implement-strstr/discuss/12956/C++-Brute-Force-and-KMP
        A, B = len(haystack), len(needle)
        if not B: return 0
        lps = self.create_lps(needle)
        i, j = 0, 0
        while i < A:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == B:
                return i - j
            if i < A and haystack[i] != needle[j]:  # i < A in front
                if j:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def create_lps(self, needle):
        # For the pattern “AABAACAABAA”,
        # lps[] is [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
        length = len(needle)
        lps = [0] * length
        dis = 0
        i = 1
        while i < length:
            if needle[i] == needle[dis]:
                dis += 1
                lps[i] = dis
                i += 1
            elif dis:
                dis = lps[dis - 1]  # ababb
            else:
                lps[i] = 0
                i += 1
        return lps

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # brute force
        for i in range(len(haystack) - len(needle) + 1):
            j = i
            k = 0
            while k < len(needle) and haystack[j] == needle[k]:
                j += 1
                k += 1
            if k == len(needle): return i
        return -1

    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


a = Solution()
print(a.create_lps("AABAACAABAA"))
print(a.strStr_kmp("AAAAABAAABA", "BAAAA"))
