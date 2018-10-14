# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head: return []
        lp = ListNode(head.val)
        rp = ListNode(head.val)
        l, r = lp, rp

        node = head
        while node:
            if node.val < x:
                lp.next = node
                lp = node
            else:
                rp.next = node
                rp = node
            node = node.next

        rp.next = None
        lp.next = r.next

        return l.next
