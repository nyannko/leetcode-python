from collections import defaultdict


class GraphDFS:

    def __init__(self, num):
        self.num = num
        self.graph = defaultdict(set)
        self.all_nodes = {x for x in range(self.num)}
        # all_nodes = {x for x in string.ascii_letters[:self.num]}

    def draw_graph(self, prerequisite):
        for child, parent in prerequisite:
            self.graph[parent].add(child)

    def topological_sort(self):
        stack = []
        visited = {key: -1 for key in self.all_nodes}
        for any_node in self.all_nodes:
            if visited[any_node] == -1:
                if not self.dfs(any_node, visited, stack):
                    return []
        return stack

    def dfs(self, node, visited, stack):
        if visited[node] == 0:
            return False
        visited[node] = 0
        for neighbor in self.graph[node]:
            if visited[neighbor] == -1:
                if not self.dfs(neighbor, visited, stack):
                    return False
            elif visited[neighbor] == 0:
                return False
        visited[node] = 1
        stack.insert(0, node)
        return True


a = GraphDFS(7)
a.draw_graph([['f', 'g'], ['c', 'a'], ['c', 'b'], ['e', 'b'], ['d', 'c'], ['f', 'd'], ['g', 'f']])
a = GraphDFS(7)
a.draw_graph([['c', 'a'], ['c', 'b'], ['e', 'b'], ['d', 'c'], ['f', 'd'], ['g', 'f']])
a = GraphDFS(2)
a.draw_graph([[0, 1], [1, 0]])
a = GraphDFS(4)
a.draw_graph([[1, 0], [2, 0], [3, 1], [3, 2]])
a = GraphDFS(2)
a.draw_graph([])
a = GraphDFS(4)
a.draw_graph([[1, 0]])
a = GraphDFS(4)
a.draw_graph([[1, 0], [2, 0], [3, 1], [3, 2]])
print(a.topological_sort())
# https://pasteboard.co/HPJeKFV.png
