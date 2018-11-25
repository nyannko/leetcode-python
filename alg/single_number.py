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
        d = dict.fromkeys(nums)
        enc = 0
        for i in nums:
            enc ^= i
        # enc = reduce(lambda x, y: x ^ y, nums)
        for i in nums:
            res = enc ^ i
            if res in d:
                return [i, res]
