# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # split
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse
        pre = None
        while slow:
            next_node = slow.next
            slow.next = pre  # change the head linked list
            pre = slow
            slow = next_node

        # compare
        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True
