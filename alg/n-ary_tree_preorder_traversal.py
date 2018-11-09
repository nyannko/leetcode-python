"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self.dfs(root, [])

    def dfs(self, node, res):
        if not node: return res  # this is for root = None(immediately return)
        res.append(node.val)
        for c in node.children:
            self.dfs(c, res)
        return res
    
    def iterative(self, root):
        res, q = [], root and [root]  # wtf
        while q:
            node = q.pop()
            res.append(node.val)
            q += [child for child in node.children[::-1] if child]
        return res

    # def preorder(self, root):
    #     """
    #     :type root: Node
    #     :rtype: List[int]
    #     """
    #     if not root: return []
    #     res = [root.val]
    #     return self.dfs(root, res)
    #
    # def dfs(self, node, res):
    #     for c in node.children:
    #         res.append(c.val)
    #         # print c.val, res
    #         self.dfs(c, res)
    #     return res
