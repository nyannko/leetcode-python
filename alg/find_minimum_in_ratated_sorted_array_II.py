class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, last = 0, len(nums) - 1
        while first < last:
            mid = (first + last) / 2
            if nums[mid] < nums[last]: # [5,1,2,3,4]
                last = mid
            elif nums[mid] > nums[last]: # [5,6,7,8,1,2,3]
                first = mid + 1
            else:
                last = last - 1
        return nums[first]
