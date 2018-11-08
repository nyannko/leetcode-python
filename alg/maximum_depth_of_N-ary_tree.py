"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        # do not forget this condition
        if not root.children:
            return 1
        return max(map(self.maxDepth, root.children)) + 1
        # return max([self.maxDepth(c) for c in root.children]) + 1
