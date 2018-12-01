from collections import defaultdict


class Graph:

    def __init__(self, num):
        self.num = num
        self.graph = defaultdict(set)
        self.check_cycle = defaultdict(set)
        self.all_nodes = set()

    def compose_graph(self, prerequisite):
        if not prerequisite:
            return [i for i in range(self.num)[::-1]]
        for child, parent in prerequisite:
            self.graph[parent].add(child)
            self.check_cycle[child].add(parent)
            # find all nodes
            # self.all_nodes.add(child)
            # self.all_nodes.add(parent)
        self.all_nodes = {x for x in range(self.num)}
        self.visited = {key: -1 for key in self.all_nodes}

    def topological_sort(self):
        stack = []
        for any_node in self.all_nodes:
            if self.visited[any_node] == -1:
                if not self.dfs(any_node, self.visited, stack):
                    return []
        return stack

    def dfs(self, node, visited, stack):
        if self.visited[node] == 0:
            return False
        self.visited[node] = 0
        for neighbor in self.graph[node]:
            if visited[neighbor] == -1:
                if not self.dfs(neighbor, visited, stack):
                    return False
            elif visited[neighbor] == 0:
                return False
        self.visited[node] = 1
        stack.insert(0, node)
        return True


# a = Graph(7)
# a.compose_graph([['f', 'g'], ['c', 'a'], ['c', 'b'], ['e', 'b'], ['d', 'c'], ['f', 'd'], ['g', 'f']])
# a = Graph(7)
# a.compose_graph([['c', 'a'], ['c', 'b'], ['e', 'b'], ['d', 'c'], ['f', 'd'], ['g', 'f']])
# a = Graph(2)
# a.compose_graph([[0, 1], [1, 0]])
# a = Graph(4)
# a.compose_graph([[1,0],[2,0],[3,1],[3,2]])
a = Graph(2)
a.compose_graph([])
# a = Graph(4)
# a.compose_graph([[1,0]])
# a = Graph(4)
# a.compose_graph([[1,0],[2,0],[3,1],[3,2]])
print(a.topological_sort())
# https://pasteboard.co/HPJeKFV.png
