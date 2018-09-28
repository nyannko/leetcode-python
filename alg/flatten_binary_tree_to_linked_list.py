class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.flatten(root.left)
        self.flatten(root.right)

        if not root.left: return

        node = root.left
        while node.right:
            node = node.right
        node.right = root.right
        root.right = root.left
        root.left = None
