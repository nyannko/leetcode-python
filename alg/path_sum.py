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
        res = []
        self.dfs(root, [], res, sum)
        return res

    def dfs(self, root, path, res, sum):
        if not root: return
        path.append(root.val)
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            res.append(list(path))
        self.dfs(root.left, path, res, sum)
        self.dfs(root.right, path, res, sum)
        path.pop()

    # slow
    def pathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        path = []
        self.dfs2(sum, root, path, res)
        return res

    def dfs2(self, sum, root, path, res):
        if sum == root.val and not root.left and not root.right:
            path.append(root.val)
            # print(path)
            res.append(path)
            return

        # print(path)
        if root.left:
            self.dfs2(sum - root.val, root.left, list(path) + [root.val], res)
        if root.right:
            self.dfs2(sum - root.val, root.right, list(path) + [root.val], res)
