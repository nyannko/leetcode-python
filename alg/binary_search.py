class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def search_dfs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end = len(nums) - 1
        return self.dfs(nums, 0, end, target)

    def dfs(self, nums, start, end, target):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.dfs(nums, start, mid - 1, target)
        return self.dfs(nums, mid + 1, end, target)
