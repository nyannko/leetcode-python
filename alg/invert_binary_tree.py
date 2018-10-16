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
            ele = queue.popleft()
            if ele:
                ele.right, ele.left = ele.left, ele.right
                queue.append(ele.left)
                queue.append(ele.right)
        return root
