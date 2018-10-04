# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        postorder.reverse()
        return self.dfs(inorder, postorder)

    def dfs(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        in_first, in_last = inorder[0], inorder[-1]
        post_first, post_last = postorder[0], postorder[-1]

        if in_first == in_last: return TreeNode(in_first)
        if post_first == post_last: return TreeNode(post_first)

        root = TreeNode(post_first)
        in_root_pos = inorder.index(post_first)
        left_size = len(inorder) - in_root_pos
        # print(in_root_pos, left_size)
        # print(inorder[:in_root_pos],postorder[left_size:],inorder[in_root_pos + 1:],postorder[1:left_size])
        root.left = self.dfs(inorder[:in_root_pos], postorder[left_size:])
        root.right = self.dfs(inorder[in_root_pos:], postorder[1:left_size])

        return root
