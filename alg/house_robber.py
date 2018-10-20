class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd = even = 0
        for i in range(len(nums)):
            if i & 1 == 0:
                print("1", odd, even)
                odd = max(odd + nums[i], even)
                print("2", odd, even)
            else:
                print("3", odd, even)
                even = max(even + nums[i], odd)
                print("4", odd, even)
        return max(odd, even)

a = Solution()
a.rob([2,1,1,2])
