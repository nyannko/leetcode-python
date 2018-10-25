class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # two pass
        res = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums))[::-1]:
            res[i] = res[i] * right
            right = right * nums[i]
        return res
