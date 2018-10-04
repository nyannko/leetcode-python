# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(preorder, inorder)

    def dfs(self, preorder, inorder):
        if not preorder and not inorder:
            return
        pre_first, pre_last = preorder[0], preorder[-1]
        in_first, in_last = inorder[0], inorder[-1]

        if pre_first == pre_last: return TreeNode(pre_first)
        if in_first == in_last: return TreeNode(in_first)

        root = TreeNode(pre_first)
        in_root_pos = inorder.index(pre_first)
        left_size = in_root_pos

        root.left = self.dfs(preorder[1:left_size + 1], inorder[:in_root_pos])
        root.right = self.dfs(preorder[left_size + 1:], inorder[in_root_pos + 1:])

        return root
