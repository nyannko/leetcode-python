class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = list(pattern)
        str = str.split(' ')
        return len(set(zip(pattern, str))) == len(set(pattern)) == len(set(str)) and \
               len(pattern) == len(str)
# similar problem with isomorphic strings
