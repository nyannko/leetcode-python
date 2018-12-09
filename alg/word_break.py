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

    def wordBreak_II(self, s, wordDict):
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, d):
        if s in d:
            return d[s]
        res = []
        if len(s) == 0:
            # res.append("")
            res += "",
            return res
        for word in wordDict:
            if s.startswith(word):
                length = len(word)
                sub_list = self.dfs(s[length:], wordDict, d)
                for sub in sub_list:
                    mid = "" if len(sub) == 0 else " "
                    # res.append(word + mid + sub)
                    res += word + mid + sub,
        d[s] = res
        return res

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
# a.wordBreak("applepenapple", ["apple", "pen"])
print(a.wordBreak_II("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
