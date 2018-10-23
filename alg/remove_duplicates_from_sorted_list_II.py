# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        p = head.next
        if p.val == head.val:
            while p and head.val == p.val:
                p = p.next
            return self.deleteDuplicates(p)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
