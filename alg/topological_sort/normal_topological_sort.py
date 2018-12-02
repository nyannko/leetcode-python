from collections import defaultdict, deque


class Graph:

    def __init__(self, num):
        self.num = num
        self.graph = defaultdict(set)
        self.visited = set()
        self.all_nodes = set()

    def draw_graph(self, prerequisite):
        for child, parent in prerequisite:
            self.graph[parent].add(child)
            # find all nodes
            self.all_nodes.add(child)
            self.all_nodes.add(parent)
        print(self.all_nodes)

    def topological_sort(self):
        stack = []
        for any_node in self.all_nodes:
            if any_node not in self.visited:
                self.dfs(any_node, self.visited, stack)
        return stack

    def dfs(self, node, visited, stack):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, stack)
        stack.insert(0, node)


a = Graph(7)
a.draw_graph([['f', 'g'], ['c', 'a'], ['c', 'b'], ['e', 'b'], ['d', 'c'], ['f', 'd'], ['g', 'f']])
a = Graph(7)
a.draw_graph([['c', 'a'], ['c', 'b'], ['e', 'b'], ['d', 'c'], ['f', 'd'], ['g', 'f'], ['f', 'e']])
a = Graph(2)
a.draw_graph([[0, 1], [1, 0]])
a = Graph(4)
a.draw_graph([[1, 0], [2, 0], [3, 1], [3, 2]])
a = Graph(2)
a.draw_graph([])
a = Graph(4)
a.draw_graph([[1, 0]])
a = Graph(4)
a.draw_graph([[1, 0], [2, 0], [3, 1], [3, 2]])
print(a.topological_sort())
# https://pasteboard.co/HPJeKFV.png
