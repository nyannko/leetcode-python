# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        count = 0
        while count != k and curr:
            curr = curr.next
            count += 1
        if count == k:
            curr = self.reverseKGroup(curr, k)
            while count > 0:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                count -= 1
            head = curr
        return head
