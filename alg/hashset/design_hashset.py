class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._set = [False] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            return

        index = self.compute_hash(key)
        self._set[index] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if not self.contains(key):
            return

        index = self.compute_hash(key)
        self._set[index] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = self.compute_hash(key)
        # if self._set[index] == 0: return True
        if self._set[index] is not False:  # False == 0..
            return True
        return False
        # return self._set[index]

    def compute_hash(self, e):
        return e % len(self._set)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
