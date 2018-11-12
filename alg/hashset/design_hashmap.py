class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._map = [None for _ in range(1000000)]

    def compute_hash(self, key):
        return key % 1000000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = self.compute_hash(key)
        self._map[index] = value
        # print(self._map)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = self.compute_hash(key)
        # if key in map
        if self._map[index] is not None:
            return self._map[index]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = self.compute_hash(key)
        self._map[index] = None

# Your MyHashMap object will be instantiated and clled as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
