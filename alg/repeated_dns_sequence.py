class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = set()
        p = set()
        for i in range(len(s) - 10 + 1):
            sub = s[i:i + 10]
            if sub not in m:
                m.add(sub)
            else:
                p.add(sub)
        return list(p)
