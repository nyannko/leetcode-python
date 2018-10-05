# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            prev = None
            next_node = None
            while root:
                if not next_node:
                    next_node = root.left if root.left else root.right
                if root.left:
                    if prev:
                        prev.next = root.left
                    prev = root.left
                if root.right:
                    if prev:
                        prev.next = root.right
                    prev = root.right
                root = root.next

            root = next_node
