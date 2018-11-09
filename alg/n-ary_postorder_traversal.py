"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = [] if not root else [root]
        res = []

        while stack:
            cur = stack.pop()
            stack += [c for c in cur.children]
            res.append(cur.val)
        return res[::-1]

    def postorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        res = self.dfs(root, [])
        res.append(root.val)
        return res

    def dfs(self, root, res):
        for c in root.children:
            self.dfs(c, res)
            res.append(c.val)
        return res
