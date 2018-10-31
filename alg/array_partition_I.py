class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # use slice
        return sum(nums[::2])

    def arrayPairSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i & 1 == 0:
                res += nums[i]
        return res
