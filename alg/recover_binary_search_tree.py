# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.a = None
        self.b = None
        self.prev = TreeNode(-sys.maxint-1)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.dfs(root)

        self.a.val, self.b.val = self.b.val, self.a.val

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)

        if not self.a and self.prev.val >= root.val:
            self.a, self.b = self.prev, root
            # self.a = self.prev

        if self.b and self.prev.val >= root.val:
            self.b = root
        self.prev = root

        self.dfs(root.right)
