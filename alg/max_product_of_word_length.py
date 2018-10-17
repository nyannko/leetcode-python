class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        value = [0 for _ in range(length)]
        for i, v in enumerate(words):
            value[i] = 0
            for c in v:
                # shift char to left and add the previous value
                value[i] |= 1 << (ord(c) - ord('a'))
        maxp = 0
        for i in range(length):
            for j in range(i, length):
                # no repeat char
                if value[i] & value[j] == 0 and len(words[i]) * len(words[j]) > maxp:
                    maxp = len(words[i]) * len(words[j])
        return maxp
