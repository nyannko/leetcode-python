class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # usage of zip
        import operator
        return sum([sum(map(operator.ne, [0] + row, row + [0])) for row in grid + map(list, zip(*grid))])
