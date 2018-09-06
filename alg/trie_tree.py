# https://pasteboard.co/HAIdoF6.png do not split the words
# if you want to find the longest path


class Trie:
    root = {}
    end = '/'

    @classmethod
    def add(cls, word):
        # word = word.split('.')
        node = cls.root
        for c in word:
            # 如果中间节点(如abc)已经出现就删除结尾的None值
            if cls.end in node:
                del node[cls.end]
            # return provided default value
            node = node.setdefault(c, {})
            print("add:", cls.root)
        node[cls.end] = None
        print("end:", cls.root)

    @classmethod
    def find(cls, word):
        # word = word.split('.')
        node = cls.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return cls.end in node


word_list = ['abc', 'abc.asd', 'abc.asd.as', 'abc.asd.qq', 'abc.asd.qqq', 'abc.qq', 'abc.qq.asd', 'abc.ww', 'acc']
for w in word_list:
    Trie.add(w)
for w in word_list:
    if Trie.find(w) is True:
        print(w)
