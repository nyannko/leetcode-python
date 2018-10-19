class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd = even = 0
        for i in range(len(nums)):
            if i & 1 == 0:
                odd = max(odd + nums[i], even)
            else:
                even = max(even + nums[i], odd)
        return max(odd, even)
