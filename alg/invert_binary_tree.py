class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        import collections
        queue = collections.deque([(root)])
        # queue = [root]
        res = []
        while queue:
            # O(1)
            ele = queue.popleft()
            if ele:
                ele.right, ele.left = ele.left, ele.right
                queue.append(ele.left)
                queue.append(ele.right)
        return root

    def invertTree1(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
