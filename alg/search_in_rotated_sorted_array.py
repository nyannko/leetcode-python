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

    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first, last = 0, len(nums)
        while first < last:
            mid = (first + last) // 2
            if target == nums[mid]:
                return mid
            if nums[first] <= nums[mid]:
                if nums[first] <= target < nums[mid]:
                    last = mid
                else:
                    first = mid + 1
            else:
                if nums[mid] < target <= nums[last - 1]:
                    first = mid + 1
                else:
                    last = mid
        return -1


a = Solution()
print(a.search([4, 5, 6, 7, 0, 1, 2], 22))
