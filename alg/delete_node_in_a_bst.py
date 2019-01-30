class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left or not root.right:
                return root.left or root.right

            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        return root

    def find_min(self, root):
        while root.left:
            root = root.left
        return root
