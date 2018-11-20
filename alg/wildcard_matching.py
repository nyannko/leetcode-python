class Solution(object):
    def isMatch(self, string, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s, p, match, starIdx = 0, 0, 0, -1
        while s < len(string):
            # advance both pointers
            if p < len(pattern) and (pattern[p] == '?' or pattern[p] == string[s]):
                s += 1
                p += 1
            # advance pattern pointer(*)
            elif p < len(pattern) and pattern[p] == '*':
                starIdx = p
                match = s
                p += 1
            # last pointer is *, advance string pointer
            elif starIdx != -1:
                p = starIdx + 1
                match += 1
                s = match
            # current pointer is not star, last pattern pointer is not *
            # chars do not match
            else:
                return False

        # check for remaining characters in pattern
        while p < len(pattern) and pattern[p] == '*':
            p += 1

        return p == len(pattern)
