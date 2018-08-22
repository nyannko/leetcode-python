import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -sys.maxsize - 1
        f = 0
        for i, num in enumerate(nums):
            f = max(f + num, num)
            result = max(result, f)

        return result

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

