class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        l = ['qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM']
        for w in words:
            for r in l:
                if len(set(w) - set(r)) == 0:
                    res.append(w)
                    break
        return res
