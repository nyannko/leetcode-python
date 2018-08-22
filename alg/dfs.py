class Solution(object):
    def dfs(self, graph, start):
        visited = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in reversed(graph[vertex]):
                    stack.append(neighbor)
        return visited

    def dfs_recursive(self, graph, vertex, visited=[]):
        visited.extend([vertex])

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited = self.dfs_recursive(graph, neighbor, visited)

        return visited


a = Solution()
graph = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [], 5: [], 6: [], 7: []}
graph2 = {1: [2, 3], 2: [4, 5],
          3: [5], 4: [6], 5: [6],
          6: [7], 7: []}
# print(a.dfs(graph, 1))

print(a.dfs_recursive(graph, 1))
# [1, 2, 4, 5, 3, 6, 7] Preorder
