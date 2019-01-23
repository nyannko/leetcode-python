class Solution(object):
    # naive
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) >= 2:
            new_list = self.merge2_lists(lists[-1], lists[-2])
            lists.insert(0, new_list)
            del lists[-2:]  # del the last teo element
        if len(lists) == 1:
            return lists[0]
        return []

    def merge2_lists(self, l1, l2):
        p = ListNode(0)
        head = p
        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
                p = p.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
                p = p.next
        p.next = l1 if l1 else l2
        return head.next
