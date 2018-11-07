class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def back(stack, c):
            # print stack, c
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
            return stack

        s1, s2 = [], []
        for i in S:
            back(s1, i)

        for i in T:
            back(s2, i)
        return s1 == s2
        # or use reduce: for a list returns the result, just like fold
        # in haskell
        # return reduce(back, S, []) == reduce(back, T, [])
