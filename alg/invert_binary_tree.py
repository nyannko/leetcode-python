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
            ele.right, ele.left = ele.left, ele.right
            if ele.left: queue.append(ele.left)
            if ele.right: queue.append(ele.right)
        return root

    def invertTree1(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

    def invertTree2(self, root):
        if not root: return []
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree3(self, root):
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root
