# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

            # split list: mid
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # reverse list: pre
        pre, cur = None, mid
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # merge two lists
        dummy = head
        while dummy and pre:
            node = dummy.next
            # print node.val
            dummy.next, dummy, pre = pre, pre, node
