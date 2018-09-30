class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        last = len(nums)
        return self.convert(nums, 0, last)

    def convert(self, nums, first, last):
        distance = last - first
        if distance <= 0: return

        mid = (first + last) / 2
        print(first, last, mid, nums[mid])

        node = TreeNode(nums[mid])
        node.left = self.convert(nums, first, mid)
        node.right = self.convert(nums, mid + 1, last)

        return node

# 0 7 3 4
# 0 3 1 2
# 0 1 0 1
# 2 3 2 3
# 4 7 5 6
# 4 5 4 5
# 6 7 6 7
# 0 1 0 1
