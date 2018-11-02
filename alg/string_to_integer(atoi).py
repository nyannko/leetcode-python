class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ls = list(str.strip())

        if not ls: return 0
        if ls[0] == '-':
            sign = -1
        else:
            sign = 1
        # del sign digit
        if ls[0] in ['+', '-']:
            del ls[0]

        res, i = 0, 0
        # if the first element is char, we won't enter the loop
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))
