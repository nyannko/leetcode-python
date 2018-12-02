class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # detect cycle
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        for i in range(numCourses):
            if not self.dfs(i, visited, graph):
                return False
        return True

    def dfs(self, node, visited, graph):
        if visited[node] == -1:
            return False
        if visited[node] == 1:
            return True
        visited[node] = -1
        for i in graph[node]:
            if not self.dfs(i, visited, graph):
                return False
        visited[node] = 1
        return True
