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
        res = []
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                for c in cur.children:
                    q.append(c)
                level.append(cur.val)
            res.append(level)
        return res
