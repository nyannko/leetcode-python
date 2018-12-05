class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            n = self.d[key]
            self._remove(n)
            self._add(n)
            return n.v
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
            self._remove(self.d[key])
        n = Node(key, value)
        self._add(n)
        self.d[key] = n
        if len(self.d) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.d[n.k]

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


from collections import OrderedDict


class LRUCache1:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.d = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        v = self.d.pop(key)
        self.d[key] = v
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
            self.d.pop(key)
        else:
            if self.cap > 0:
                self.cap -= 1
            else:
                self.d.popitem(last=False)
        self.d[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
