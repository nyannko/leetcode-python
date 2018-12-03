class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res

    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]

    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findKthSmallest(nums, len(nums) + 1 - k)

    def findKthSmallest(self, nums, k):
        pos = self.partition(nums, 0, len(nums) - 1)
        # print pos, nums, nums[pos+1:], nums[:pos]
        if k > pos + 1:
            return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
        elif k < pos + 1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]

    def partition(self, nums, first, last):
        p_index = first
        pivot = nums[last]
        for i in range(first, last):
            if nums[i] <= pivot:
                nums[i], nums[p_index] = nums[p_index], nums[i]
                p_index += 1
        nums[last], nums[p_index] = nums[p_index], nums[last]
        return p_index
