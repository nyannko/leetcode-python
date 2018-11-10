class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # return ''.join(sorted(list(T), key=lambda x: S.find(x)))
        # make a new dict to record the count of each char in T
        # d = {}
        # for i in T:
        #     if i not in d:
        #         d[i] = 1
        #     else:
        #         d[i] += 1
        # one line create a dict
        d = {i: T.count(i) for i in T}

        # construct new result according to the order in S and
        # the counter in T.
        res = []
        for i in S:
            if i in d:
                res.append(i * d[i])

        # append remaining char
        for i in T:
            if i not in S:
                res.append(i)
        return ''.join(res)

    def customSortString1(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = []
        for i in S:
            res.append(i * T.count(i))
            
        for i in T:
            if i not in S:
                res.append(i)
        return ''.join(res)
