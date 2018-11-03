class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        res = 0
        for i in nums:
            res ^= i
        return res

    def singleNonDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(logn)
        first, last = 0, len(nums) - 1
        while first < last:
            mid = (first + last) / 2
            if mid & 1 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                last = mid
            else:
                first = mid + 2
        return nums[first]

    def singleNonDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)
