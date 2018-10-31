class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # too slow!
        a = sorted(ransomNote)
        b = sorted(magazine)
        p1, p2 = 0, 0
        while p1 < len(ransomNote) and p2 < len(magazine):
            if a[p1] == b[p2]:
                p1 += 1
                p2 += 1
            elif a[p1] != b[p2]:
                p2 += 1
        return p1 == len(ransomNote)
