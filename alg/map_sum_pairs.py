class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.d[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return sum([self.d[i] for i in self.d if i.startswith(prefix)])


class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.score = 0


class MapSumTrie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.root = TrieNode()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        delta = val - self.d.get(key, 0)
        self.d[key] = val
        cur = self.root
        cur.score += delta
        for c in key:
            cur = cur.children.setdefault(c, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
a = MapSumTrie()
a.insert("apple", 3)
a.insert("ap", 2)
a.insert("y", 1)
