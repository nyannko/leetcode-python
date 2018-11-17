class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        for i in range(length):
            while nums[i] > 0 and nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]

        for i in range(length):
            if nums[i] != i + 1:
                return i + 1

        return length + 1
