import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            # sort string
            d.setdefault(''.join(sorted(s)), []).append(s)
        # dict to list
        return list(d.values())

    def groupAnagrams1(self, strs):
        # count different anagrams
        count = collections.Counter([tuple(sorted(s)) for s in strs])
        # Counter({('a', 'e', 't'): 3, ('a', 'n', 't'): 2, ('a', 'b', 't'): 1})
        # list = []
        # for x in strs:
        #     if count[tuple(sorted(x))]>1:
        #         print(x)
        # # print(list)
        return filter(lambda x: count[tuple(sorted(x))] > 1, strs)



a = Solution()
print(a.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"]))