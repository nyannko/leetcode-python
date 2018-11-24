class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = set('aeiou')
        res = S.split()
        for i in range(len(res)):
            if res[i][0].lower() not in s:
                res[i] = res[i][1:] + res[i][0]
            res[i] += 'ma' + 'a' * (i + 1)
        return ' '.join(res)

    def toGoatLatin1(self, S):
        """
        :type S: str
        :rtype: str
        """

        return ' '.join(
            (w if w[0].lower() in 'aeiou' else w[1:] + w[0])
            + 'ma' + 'a' * (i + 1) for i, w in enumerate(S.split()))

    # without for
    def toGoatLatin2(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = set('aeiou')
        def latin(w, i):
            if w[0].lower() not in s:
                w = w[1:] + w[0]
            return w + 'ma' + 'a' * (i + 1)
        return ' '.join(latin(w, i) for i, w in enumerate(S.split()))