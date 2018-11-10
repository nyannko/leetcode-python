# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # bfs
        from collections import deque
        if not root: return []
        q = deque([root])
        ret = [root.val]
        while q:
            res = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    res.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    res.append(cur.right.val)
            if res:
                ret.append(sum(res) / len(res))
        return ret

