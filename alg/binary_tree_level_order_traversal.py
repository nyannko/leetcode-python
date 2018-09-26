class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]
        queue = [root]

        while queue:
            val = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    val.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    val.append(node.right.val)
            if val:
                res.append(list(val))
        return res

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]
        queue = [root]

        while queue:
            val = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    val.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    val.append(node.right.val)
            if val:
                res.insert(0, val)
        return res

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]
        queue = [root]

        flag = True
        while queue:

            val = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    val.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    val.append(node.right.val)
            if val:
                if flag:
                    val.reverse()
                    flag = False
                else:
                    flag = True

                res.append(val)

        return res
