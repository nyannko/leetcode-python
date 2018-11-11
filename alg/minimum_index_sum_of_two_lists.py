class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {v: i for i, v in enumerate(list1)}
        res, best = [], float('inf')
        for j, v in enumerate(list2):
            i = d.get(v, float('inf'))
            if i + j < best:
                best = i + j
                res = [v]
            elif i + j == best:
                res.append(v)
        return res
