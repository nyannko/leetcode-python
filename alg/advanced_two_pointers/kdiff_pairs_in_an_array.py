class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i, j = 0, 0
        res = 0

        while i < len(nums) and j < len(nums):
            if i == j or nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            elif nums[j] - nums[i] == k:
                res += 1
                i += 1
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
        return res
