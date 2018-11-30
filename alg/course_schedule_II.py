class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # dfs
        from collections import defaultdict
        dic = defaultdict(set)
        nei = defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            nei[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]  # [0]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in nei[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []
