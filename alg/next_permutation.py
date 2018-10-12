class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return []

        # find id1
        prev = nums[-1]
        id1 = 0
        for i in range(len(nums))[::-1]:
            if nums[i] >= prev:
                prev = nums[i]
                id1 = i
            else:
                break

        # find id2
        if id1 - 1 >= 0:
            id1 -= 1
            id2 = 0
            for i in range(len(nums))[::-1]:
                if nums[i] > nums[id1]:
                    id2 = i
                    break

            # swap
            nums[id1], nums[id2] = nums[id2], nums[id1]

            # reverse after id1
            nums[id1 + 1:] = nums[id1 + 1:][::-1]
        else:
            nums.reverse()
