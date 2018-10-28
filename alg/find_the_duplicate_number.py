class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) space
        d = {}
        for i, v in enumerate(nums):
            if v in d:
                return v
            d[v] = i
