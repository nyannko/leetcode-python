import collections
import string


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        level = {beginWord}
        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for i in range(len(beginWord)):
                    for j in string.ascii_lowercase:
                        # accelerate
                        if word[i] != j:
                            next_word = word[:i] + j + word[i + 1:]
                            if next_word in wordSet and next_word not in parents:
                                next_level[next_word].add(word)
            level = next_level
            parents.update(next_level)
        print(parents)

        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]

        return res


a = Solution()
a.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
