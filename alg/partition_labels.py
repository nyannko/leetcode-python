class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # record the last index of each letter
        d = {}
        for i, v in enumerate(S):
            # key = ord(v) - ord('a')
            d[v] = i

        res = []
        first, last = 0, 0
        for i, v in enumerate(S):
            # print i, v, first, last
            last = max(last, d[v])
            # reach the maximum length
            if last == i:
                res.append(last - first + 1)
                first = last + 1
        return res
