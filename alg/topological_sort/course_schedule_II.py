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


class SolutionDFS:
    def __init__(self):
        self.graph = defaultdict(set)

    def findOrder(self, num, prerequisite):
        for child, parent in prerequisite:
            self.graph[parent].add(child)
            # find all nodes
            # self.all_nodes.add(child)
            # self.all_nodes.add(parent)
        all_nodes = {x for x in range(num)}
        visited = {key: -1 for key in all_nodes}

        stack = []
        for any_node in all_nodes:
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


class SolutionBFS:

    def __init__(self):
        self.graph = defaultdict(set)
        self.in_degree = defaultdict(int)
        self.d = deque()

    def findOrder(self, numCourses, prerequisites):
        for child, parent in prerequisites:
            self.graph[parent].add(child)
        all_nodes = {n for n in range(numCourses)}
        # compute in degree
        for child, parent in prerequisites:
            self.in_degree[child] += 1
        for node in all_nodes:
            if node not in self.in_degree:
                self.in_degree[node] = 0
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

        return res if cnt == numCourses else []
