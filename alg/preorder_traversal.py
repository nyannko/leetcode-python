class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)
        return self

    def search(self, val):
        if val == self.val:
            return True
        elif val < self.val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False


class Solution:

    # stack
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]

        while stack:
            p = stack.pop()
            res.append(p.val)

            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)

        return res

    def inorderTraversal(self, root):
        res = []
        stack = []
        cur = root

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res


a = Solution()
tree = TreeNode(5).insert(2).insert(1).insert(3).insert(7).insert(6).insert(8)
print(tree.search(7))
print(a.preorderTraversal(tree))
print(a.inorderTraversal(tree))
# https://pasteboard.co/HFh1qvW.png