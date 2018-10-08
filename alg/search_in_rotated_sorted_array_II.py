class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        first, last = 0, len(nums)
        while first < last:
            mid = (first + last) // 2
            if target == nums[mid]:
                return True
            if nums[first] < nums[mid]:
                if nums[first] <= target < nums[mid]:
                    last = mid
                else:
                    first = mid + 1
            elif nums[first] > nums[mid]:
                if nums[mid] < target <= nums[last - 1]:
                    first = mid + 1
                else:
                    last = mid
            elif nums[first] == nums[mid]:
                first += 1

        return False
