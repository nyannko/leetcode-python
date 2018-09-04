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


l = [1, 2, 3, 4]

head = ll = ListNode(1)
for i in range(2, len(l) + 1):
    ll.next = ListNode(i)
    ll = ll.next

a = Solution()
print(a.swapPairs(head).next.next.val)
