class Trie:
    root = {}
    end = '/'

    def add(self, word):
        word = word.split('.')
        node = self.root
        for c in word:
            # 如果中间节点(如abc)已经出现就删除结尾的None值
            if self.end in node:
                del node[self.end]
            node = node.setdefault(c, {})
            print("add:", self.root)
        node[self.end] = None
        print("end:", self.root)

    def find(self, word):
        word = word.split('.')
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.end in node


trie = Trie()
word_list = ['abc', 'abc.asd', 'abc.asd.as', 'abc.asd.qq', 'abc.qq', 'abc.qq.asd', 'abc.ww', 'acc']
for w in word_list:
    trie.add(w)
for w in word_list:
    if trie.find(w) is True:
        print(w)
