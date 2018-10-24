class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = {}
        m = n = head
        while m:
            d[m] = RandomListNode(m.label)
            m = m.next
        while n:
            d[n].next = d.get(n.next)
            d[n].random = d.get(n.random)
            n = n.next
        return d.get(head)

l = RandomListNode(1)
l.next = RandomListNode(2)
l.next.next = RandomListNode(3)

a = Solution()
a.copyRandomList(l)