class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

    def dfs(self, root, res):
        if not root:
            return 0
        if not root.left and not root.right:
            return res * 10 + root.val

        # 0 * 10 + 4; 4 * 10 + 9:4 * 10 + 0; 49 * 10 + 5:49 * 10 + 1
        return self.dfs(root.left, res * 10 + root.val) + \
               self.dfs(root.right, res * 10 + root.val)
