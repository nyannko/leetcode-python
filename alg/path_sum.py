class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False

        if not root.left and not root.right:
            return sum == root.val

        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        path = []
        self.dfs(sum, root, path, res)
        return res

    def dfs(self, sum, root, path, res):
        if sum == root.val and not root.left and not root.right:
            path.append(root.val)
            # print(path)
            res.append(path)
            return

        # print(path)
        if root.left:
            self.dfs(sum - root.val, root.left, list(path) + [root.val], res)
        if root.right:
            self.dfs(sum - root.val, root.right, list(path) + [root.val], res)
