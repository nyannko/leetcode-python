import string
import collections


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        visited = set()
        q = collections.deque([(beginWord, 1)])
        alphabet = string.ascii_lowercase

        while q:
            word, length = q.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                for c in alphabet:
                    new_word = word[:i] + c + word[i + 1:]

                    if new_word in wordList and new_word not in visited:
                        q.append((new_word, length + 1))
                        visited.add(new_word)

        return 0


a = Solution()
print(a.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
