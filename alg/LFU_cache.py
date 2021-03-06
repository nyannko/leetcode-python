from collections import defaultdict
from collections import OrderedDict


class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.min = -1
        self.vals = {}
        self.counts = {}
        self.lists = defaultdict(OrderedDict)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.vals:
            return -1

        # update count
        count = self.counts[key]
        self.counts[key] = count + 1

        # update list
        self.lists[count].pop(key)
        self.lists[count + 1].update({key: None})

        # update min value
        if count == self.min and len(self.lists[count]) == 0:
            self.min += 1

        return self.vals[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap <= 0:
            return

        if key in self.vals:
            self.vals[key] = value
            self.get(key)
            return

        # remove the least used element
        if len(self.vals) >= self.cap:
            # retrieve elements without moving it
            ele = next(iter(self.lists[self.min]))
            self.lists[self.min].pop(ele)
            self.vals.pop(ele)

        # update new element
        self.vals[key] = value
        self.counts[key] = 1
        self.min = 1
        self.lists[1].update({key: None})


# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
# param_1 = obj.get(key)
# obj.put(key,value)
# ["LFUCache","put","put","get","get","put","get","get","get"]
# [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]
obj.put(2, 1)
obj.put(2, 2)
obj.put(2, 3)
obj.get(4)
print(obj.vals, obj.counts, obj.lists)
