class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0
        length = len(nums)
        for i in range(length):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]

        return index + 1

    def removeDuplicates1(self, nums):
        # different when u execute this in python repl and leetcode
        nums[:] = list(set(nums))
        return len(nums)

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i

    def removeDuplicates3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        index = 2
        for i in range(2, len(nums)):
            if nums[index - 2] != nums[i]:
                nums[index] = nums[i]
                index += 1
        print(nums)
        return index


a = Solution()
print(a.removeDuplicates2([1, 1, 1, 1, 2, 2, 3]))
