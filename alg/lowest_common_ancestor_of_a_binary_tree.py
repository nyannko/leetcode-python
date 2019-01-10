# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or (root.val == p.val) or (root.val == q.val):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        # if not left:
        #     return right
        # else:
        #     return left
        return left if not right else right


a = Solution()
# root = TreeNode(3)
# root.left = TreeNode(5)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(2)
# root.right = TreeNode(1)

# [1,2,3,null,4]4,3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
p = root.left.right
q = root.right
a.lowestCommonAncestor(root, p, q)
