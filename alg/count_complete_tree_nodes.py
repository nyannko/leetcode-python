# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #         if not root:
        #             return 0
        #         else:
        #             return self.countNodes(root.left) + self.countNodes(root.right) + 1
        if not root:
            return 0
        leftDepth = self.get_depth(root.left)
        rightDepth = self.get_depth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def get_depth(self, root):
        if not root:
            return 0
        return self.get_depth(root.left) + 1
