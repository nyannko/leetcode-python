class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        res = []
        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            res.append(max(window))
        return res
