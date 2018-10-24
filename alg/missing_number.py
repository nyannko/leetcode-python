class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i, v in enumerate(nums):
            res ^= i ^ v
        return res ^ (i + 1)

    def missingNumber2(self, nums):
        return sum(range(0, len(nums) + 1)) - sum(nums)
