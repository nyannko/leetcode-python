class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # two pointers
        vowels = set('aeiouAEIOU')
        s = list(s)
        first, last = 0, len(s) - 1
        while first < last:
            if s[first] in vowels and s[last] in vowels:
                s[first], s[last] = s[last], s[first]
                first += 1
                last -= 1
            if s[first] not in vowels:
                first += 1
            if s[last] not in vowels:
                last -= 1
        return ''.join(s)
