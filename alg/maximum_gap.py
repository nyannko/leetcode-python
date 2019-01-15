class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(0, len(nums) - 1):
            val = nums[i + 1] - nums[i]
            if val > res:
                res = val
        return res
