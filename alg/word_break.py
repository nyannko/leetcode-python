class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok = [True]
        max_len = max(map(len, wordDict + ['']))
        wordDict = set(wordDict)
        for i in range(1, len(s) + 1):
            ok += any(ok[j] and (s[j:i] in wordDict) for j in range(max(0, i - max_len), i)),
        return ok[-1]

    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {}

        def helper(s):
            if s == "":
                return True
            if s in memo:
                return memo[s]
            for word in wordDict:
                if s.startswith(word):
                    if helper(s[len(word):]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False

        return helper(s)


a = Solution()
a.wordBreak("applepenapple", ["apple", "pen"])
