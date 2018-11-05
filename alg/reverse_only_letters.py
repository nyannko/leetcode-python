class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        first, last = 0, len(S) - 1
        S = list(S)
        while first < last:
            con1, con2 = S[first].isalpha(), S[last].isalpha()
            if not con1:
                first += 1
            elif not con2:
                last -= 1
            elif con1 and con2:
                S[first], S[last] = S[last], S[first]
                first += 1
                last -= 1
        return ''.join(S)
