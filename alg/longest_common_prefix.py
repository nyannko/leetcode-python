class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        shortest_str = min(strs, key=len)
        for i, v in enumerate(shortest_str):
            for word in strs:
                if word[i] != v:
                    return shortest_str[:i]
        return shortest_str
