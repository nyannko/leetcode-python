class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import string
        # combine two lists as dict
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabet = list(string.ascii_lowercase)
        d = dict(zip(alphabet, morse))
        res = set()
        for s in words:
            res.add(''.join([d[i] for i in s]))
        return len(res)
