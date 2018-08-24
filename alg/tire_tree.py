class Trie:
    root = {}
    end = '/'

    def add(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
            print("add:", self.root)
        node[self.end] = None
        print("end:", self.root)

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
            print("find", node)
        return self.end in node


a = Trie()
a.add('abc')
print(a.find('abc'))
