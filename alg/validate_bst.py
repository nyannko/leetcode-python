# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, -sys.maxsize, sys.maxsize)

    def dfs(self, root, lower, upper):
        if not root:
            return True

        return root.val > lower and root.val < upper and \
               self.dfs(root.left, lower, root.val) and \
               self.dfs(root.right, root.val, upper)
