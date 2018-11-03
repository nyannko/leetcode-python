class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        res = Counter((A + " " + B).split(' '))
        return [i[0] for i in res.items() if i[1] == 1]
