# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.convert(head, self.list_length(head))

    def convert(self, head, length):
        if length == 0: return None
        if length == 1: return TreeNode(head.val)

        step = length // 2
        mid_node = self.index(head, step)
        node = TreeNode(mid_node.val)

        node.left = self.convert(head, step)
        node.right = self.convert(mid_node.next, (length - 1) // 2)
        return node

    def list_length(self, node):
        count = 0
        while node:
            node = node.next
            count += 1
        return count

    def index(self, head, step):
        for _ in range(step - 1):
            head = head.next
        return head


values = [2, 3, 4, 5, 6, 7]
head = ListNode(1)
node = head
for i in values:
    head.next = ListNode(i)
    head = head.next
res = Solution().sortedListToBST(node)
