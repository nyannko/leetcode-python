class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generate(1, n + 1)

    def generate(self, start, end):
        sub_tree = []
        if start > end: return None

        for m in range(start, end):
            l = self.generate(start, m)
            r = self.generate(m + 1, end)
            # print(start, end, l, r)
            for i in l or [None]:
                for j in r or [None]:
                    node = TreeNode(m)
                    node.left = i
                    node.right = j
                    # print("node", node.val)
                    sub_tree.append(node)
        return sub_tree
