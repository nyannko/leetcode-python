class Solution(object):

    def __init__(self):
        self.parent = range(1001)

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        for e in edges:
            if self.union(e[0], e[1]):
                return e

    def find(self, val):
        if self.parent[val] != val:
            return self.find(self.parent[val])
        else:
            return self.parent[val]

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return True
        else:
            self.parent[p1] = p2
            return False
