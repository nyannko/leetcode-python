class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # compare two maps
        if not s or not words: return []
        from collections import Counter, defaultdict
        counts = Counter(words)
        # for i in words:
        #     counts[i] += 1
        # if i in counts:
        #     counts[i] += 1
        # else:
        #     counts[i] = 1

        indexes = []

        for i in range(len(s) - len(words) * len(words[0]) + 1):
            j = 0
            seen = defaultdict(int)
            while j < len(words):
                word = s[i + j * len(words[0]):i + (j + 1) * len(words[0])]
                if word in counts:
                    seen[word] += 1
                    # if word in seen:
                    #     seen[word] += 1
                    # else:
                    #     seen[word] = 1
                    if seen[word] > counts[word]:
                        break
                else:
                    break
                j += 1
                if j == len(words):
                    indexes.append(i)
        return indexes
