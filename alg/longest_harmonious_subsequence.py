class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        res = 0
        for i in c:
            if i + 1 in c:
                res = max(res, c[i] + c[i + 1])
        return res
