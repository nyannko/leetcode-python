# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.dfs(head)

    def dfs(self, node, prev=None):
        if not node: return prev
        next_node = node.next
        node.next = prev
        return self.dfs(next_node, node)

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # some test cases do not cover.. like empty list.sth.
        lp = ListNode(head.val)
        kp = ListNode(head.val)
        rp = ListNode(head.val)
        l, k, r = lp, kp, rp

        node = head
        lcount = kcount = 0
        while node:
            if lcount < m - 1:
                lp.next = node
                lp = node
                lcount += 1
            elif kcount < n - m + 1:
                kp.next = node
                kp = node
                kcount += 1
            else:
                rp.next = node
                rp = node
            node = node.next

        lp.next, kp.next, rp.next = None, None, None

        prev = r.next
        cur = k.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        lp.next = prev
        return l.next
