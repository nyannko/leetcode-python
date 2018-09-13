class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        head, tail = -1, -1
        for i, v in enumerate(nums):
            if v == target:
                head = i
                break

        for i in range(head, len(nums)):
            # print("i", i)
            if i > 0:
                if nums[i] == target:
                    tail = i

        # for i, v in enumerate(reversed(nums)):
        #     print(i, v)
        #     if v == target:
        #         tail = len(nums) - 1 - i
        #         break

        return head, tail

    def searchRange1(self, nums, target):

        if not nums:
            return -1, -1
        head, tail = -1, -1
        i, j = 0, len(nums) - 1
        while i < j:
            mid = int((i + j) / 2)
            if target > nums[mid]:
                i = mid + 1
            else:
                j = mid

        if nums[i] == target:
            head = i

        # print(i, j)
        j = len(nums) - 1
        while i < j:
            mid = int((i + j) / 2) + 1
            if target < nums[mid]:
                j = mid - 1
            else:
                i = mid
        if nums[i] == target:
            tail = i

        return head, tail


a = Solution()
print(a.searchRange1([], 5))
