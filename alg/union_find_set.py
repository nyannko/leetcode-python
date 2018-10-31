class UnionFind:
    def __init__(self):
        # size of the array
        self.up = [0 for _ in range(12)]

    def find(self, val):
        i = val
        while self.up[i] != 0:
            i = self.up[i]
        return i

    def find_compress_path(self, val):
        # find root
        r = val
        while self.up[r] != 0:
            r = self.up[r]
        # compress path
        if val == r: return r
        old_parent = self.up[val]
        while old_parent != r:
            self.up[val] = r
            val = old_parent
            old_parent = self.up[val]
        return r

    def union(self, child, parent):
        self.up[child] = parent


a = UnionFind()
a.union(1, 0)
a.union(2, 5)
a.union(3, 6)
a.union(4, 6)
a.union(5, 4)
a.union(6, 0)
a.union(7, 3)
a.union(8, 3)
a.union(9, 5)
a.union(10, 2)
a.union(11, 2)
print(a.find(3))
print(a.find_compress_path(3))
print(a.up)
