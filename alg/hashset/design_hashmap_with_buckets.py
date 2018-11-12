class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._map = [[] for _ in range(1000)]

    def compute_hash(self, key):
        return key % 1000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = self.compute_hash(key)
        bucket = self._map[index]
        if self.get(key) == -1:
            bucket.append([key, value])
        else:
            for i, e in enumerate(bucket):
                if e[0] == key:
                    bucket[i][1] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = self.compute_hash(key)
        bucket = self._map[index]
        for e in bucket:
            if e[0] == key:
                return e[1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = self.compute_hash(key)
        bucket = self._map[index]
        for e in bucket[:]:
            if e[0] == key:
                bucket.remove(e)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
