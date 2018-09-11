class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target == nums[0]:
            return 0
        if target >= nums[0]:
            for i, v in enumerate(nums):
                print(i, v)
                if v == target:
                    return i
        if target <= nums[0]:
            for i, v in enumerate(reversed(nums)):
                if v == target:
                    return len(nums) - i
        return -1


a = Solution()
print(a.search([4,5,6,7,0,1,2], 22))
