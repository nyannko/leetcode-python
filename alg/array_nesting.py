class Solution(object):

    def arrayNesting(self, nums):
        d = {}
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            next_index = d[num]

    def array_nesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        v = set()
        for i, num in enumerate(nums):
            if i not in v:
                print(i, v)
                length, visited = self.dfs_length(nums, i, num)
                res = max(res, length)
                v = v.union(visited)

        return res

    def dfs_length(self, nums, start_index, start_element):
        visited = set([start_index])
        stack = [start_element]

        while stack:
            next_index = stack.pop()
            if next_index not in visited:
                stack.append(nums[next_index])
                visited.add(next_index)
        return len(visited), visited


a = Solution()
print(a.array_nesting([5, 4, 0, 3, 1, 6, 2]))
