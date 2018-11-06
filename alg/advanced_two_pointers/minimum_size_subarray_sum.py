class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float('inf')
        i, j = 0, 0
        res = 0
        while j < len(nums):
            # move the second pointer
            res += nums[j]
            j += 1
            # move the first pointer
            while res >= s:
                min_length = min(min_length, j - i)
                res -= nums[i]
                i += 1
        return 0 if min_length == float('inf') else min_length./auto
