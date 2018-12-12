# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1, res2 = [], []
        self.dfs(root1, res1)
        self.dfs(root2, res2)
        return res1 == res2

    def dfs(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            # print(root.val)
            res.append(root.val)
            return
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)
