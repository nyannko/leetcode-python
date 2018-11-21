class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = []
        from collections import defaultdict
        self.loc = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        exist = False
        if val not in self.loc:
            exist = True
        self.random_set.append(val)
        self.loc[val].add(len(self.random_set) - 1)
        return exist

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.loc[val]:
            removed_id, last_val = self.loc[val].pop(), self.random_set[-1]
            self.random_set[removed_id] = last_val
            if self.loc[last_val]:
                self.loc[last_val].add(removed_id)
                self.loc[last_val].discard(len(self.random_set) - 1)
            self.random_set.pop()
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return random.choice(self.random_set)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
