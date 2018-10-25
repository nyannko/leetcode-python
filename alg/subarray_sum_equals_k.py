class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0: 1}
        res, pre_sum = 0, 0
        for i in nums:
            pre_sum += i
            res += d.get(pre_sum - k, 0)
            d[pre_sum] = d.get(pre_sum, 0) + 1
        return res
