import sys


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s = -sys.maxsize
        self.dfs(root)
        return self.s

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        sum = root.val

        if left > 0:
            sum += left
        if right > 0:
            sum += right
        self.s = max(sum, self.s)

        if max(right, left) > 0:
            return max(right, left) + root.val
        else:
            return root.val
