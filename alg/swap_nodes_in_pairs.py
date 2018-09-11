class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

    def reverse_list(self, head):
        if head is None or head.next is None:
            return head
        cur = head
        pre = None
        while cur:
            # store node
            tmp = cur.next
            # reverse link
            cur.next = pre
            # step forward
            pre = cur
            cur = tmp
        return pre

    def reverse_list_recursive(self, head, new_head):
        if head is None:
            return
        if head.next is None:
            new_head = head
        else:
            new_head = self.reverse_list_recursive(head.next, new_head)
            head.next.next = head
            head.next = None

        return new_head

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        length = 0
        while node is not None:
            node = node.next
            length += 1
        loc = length - n - 1
        new_node = head
        # first and other nodes
        if loc < 0:
            return head.next

        for _ in range(loc):
            new_node = new_node.next
        new_node.next = new_node.next.next
        return head


l = [1, 2]

head = ll = ListNode(1)
for i in range(2, len(l) + 1):
    ll.next = ListNode(i)
    ll = ll.next

a = Solution()
# print(a.swapPairs(head).next.next.val)
# a.reverse_list_recursive(head, None)
print(a.removeNthFromEnd(head, 1).val)
