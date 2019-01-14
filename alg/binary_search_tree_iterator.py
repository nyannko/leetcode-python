# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.p = root
        while self.p:
            self.stack.append(self.p)
            self.p = self.p.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.stack or self.p:
            while self.p:
                self.stack.append(self.p)
                self.p = self.p.left
            else:
                next_node = self.stack.pop()
                self.p = next_node.right
                return next_node.val if next_node else None

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.stack and not self.p:
            return False
        return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
