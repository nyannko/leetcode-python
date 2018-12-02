import string
from collections import defaultdict, deque


class GraphBFS:

    def __init__(self, num):
        self.num = num
        self.graph = defaultdict(set)
        self.in_degree = defaultdict(int)
        self.d = deque()

    def draw_graph(self, prerequisites):
        for child, parent in prerequisites:
            self.graph[parent].add(child)
        all_nodes = {x for x in range(self.num)}  # for nums
        # all_nodes = {x for x in string.ascii_letters[:self.num]} # for_letters
        # compute indegree O(V+E)
        for child, parent in prerequisites:
            self.in_degree[child] += 1
        for node in all_nodes:
            if node not in self.in_degree:
                self.in_degree[node] = 0
        print(self.in_degree)

    def topological_sort(self):
        for node in self.in_degree:
            if self.in_degree[node] == 0:
                self.d.append(node)

        res = []
        cnt = 0
        while self.d:
            pop_node = self.d.pop()
            res.append(pop_node)
            cnt += 1
            for neighbor in self.graph[pop_node]:
                self.in_degree[neighbor] -= 1

                if self.in_degree[neighbor] == 0:
                    self.d.append(neighbor)

        # Detect cycle
        return res if cnt == self.num else []


b = GraphBFS(7)
b.draw_graph([['c', 'a'], ['c', 'b'], ['e', 'b'], ['d', 'c'], ['f', 'd'], ['g', 'f'], ['f', 'e']])
b = GraphBFS(7)
b.draw_graph([['f', 'g'], ['c', 'a'], ['c', 'b'], ['e', 'b'], ['d', 'c'], ['f', 'd'], ['g', 'f'], ['f', 'e']])
b = GraphBFS(2)
b.draw_graph([[0, 1], [1, 0]])
b = GraphBFS(4)
b.draw_graph([[1, 0], [2, 0], [3, 1], [3, 2]])
b = GraphBFS(2)
b.draw_graph([])
b = GraphBFS(4)
b.draw_graph([[1, 0]])
print(b.topological_sort())
