class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1 << n):  # 2^n
            res.append(self.gray(i))
        return res

    def gray(self, i):
        return i ^ i >> 1
