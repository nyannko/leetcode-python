"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root: return []
        q = deque([root])
        res = [[root.val]]
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                for c in cur.children:
                    level.append(c.val)
                    q.append(c)
            if level:
                res.append(level)
        return res
