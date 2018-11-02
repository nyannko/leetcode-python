class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, last = 0, len(nums) - 1
        while first < last:
            if nums[first] < nums[last]:
                return nums[first]
            mid = first + (last - first) / 2
            if nums[mid] >= nums[last]:
                first = mid + 1
            if nums[mid] < nums[last]:
                last = mid
        return nums[first]

    def findMin1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        minimum = nums[0]
        for i in nums:
            if i < minimum:
                minimum = i
        return minimum

    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # w pointers
        min_num = nums[0]
        first, last = 0, len(nums) - 1
        while first <= last:
            if nums[first] < nums[last]:
                min_num = min(min_num, nums[first])
                last -= 1
            if nums[first] > nums[last]:
                min_num = min(min_num, nums[last])
                first += 1
            else:
                min_num = min(min_num, nums[first])
                first += 1
                last -= 1
        return min_num

    def findMin3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # stupid
        nums.sort()
        return nums[0]
