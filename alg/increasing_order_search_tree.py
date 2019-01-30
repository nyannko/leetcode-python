# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root, tail=None):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # res = inorder(root.left) + root + inorder(root.right)
        if not root:
            return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res

a = Solution()
b = TreeNode(5)
b.left = TreeNode(3)
b.right = TreeNode(6)
a.increasingBST(b)
