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


a = Solution()
print(a.searchRange([], 6))
