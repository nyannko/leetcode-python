class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0 if n == 0 else nums[0]
        return max(self.robber(nums, 1, n - 1), self.robber(nums, 0, n - 2))

    def robber(self, nums, l, r):
        pre = cur = 0
        for i in range(l, r + 1):
            tmp = max(pre + nums[i], cur)
            pre = cur
            cur = tmp
        return cur
