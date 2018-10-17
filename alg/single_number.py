class Solution(object):
    # xor
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= res
        return res

    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        enc = 0
        for i in nums:
            enc ^= i
        for i in nums:
            res = enc ^ i
            if res in nums:
                return [i, res]
