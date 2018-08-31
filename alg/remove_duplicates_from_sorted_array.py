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

    # wrong
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        index = 0
        length = len(nums)
        for i in range(2, length):
            if nums[index] != nums[i]:
                if index + 2 >= length:
                    return i + 1
                else:
                    index += 2
                    nums[index] = nums[i]
        print(nums)
        # from 0
        return index + 1

    # wrong
    def removeDuplicates3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        index = 2
        length = len(nums)
        for i in range(2, length):
            if nums[i] != nums[index - 2]:
                if index + 1 < length:
                    index += 1
                    nums[index] = nums[i]
                else:
                    index = i + 1
        print(nums)
        # from 0
        return index


a = Solution()
print(a.removeDuplicates1([1, 1, 1, 2, 2, 3]))
