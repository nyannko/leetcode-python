# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        #         if not root:
        #             return TreeNode(val)
        #         if val < root.val:
        #             root.left = self.insertIntoBST(root.left, val)
        #         else:
        #             root.right = self.insertIntoBST(root.right, val)
        #         return root

        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        else:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        return root

    def insertIntoBST(self, root, val):
        node = TreeNode(val)
        cur = root
        while cur:
            if cur.val > val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = node
                    break
        return root if root else node
