# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # dfs
    def cloneGraph(self, node):
        if not node:
            return None
        return self.clone(node, {})

    def clone(self, node, visited):
        if node in visited:
            return visited[node]

        new_node = UndirectedGraphNode(node.label)
        visited[node] = new_node
        for n in node.neighbors:
            new_node.neighbors.append(self.clone(node, visited))
        return new_node

    def cloneGraph_bfs(self, node):
        if not node:
            return None
        q = []
        d = {}
        q.append(node)
        d[node] = UndirectedGraphNode(node.label)
        while q:
            cur = q.pop(0)
            for n in cur.neighbors:
                if n in d:
                    d[cur].neighbors.append(d[n])
                else:
                    new_node = UndirectedGraphNode(n.label)
                    d[n] = new_node
                    d[cur].neighbors.append(new_node)
                    q.append(n) # make sure append original node here
        return d[node]

    def cloneGraph_queue(self, node):
        import collections
        if not node:
            return

        d = {}
        d[node] = UndirectedGraphNode(node.label)
        queue = collections.deque([node])
        while queue:
            cur = queue.popleft()
            for n in cur.neighbors:
                if n not in d:  # neighbor is not visited
                    new_node = UndirectedGraphNode(n.label)
                    d[n] = new_node
                    d[cur].neighbors.append(new_node)
                    queue.append(n)
                else:
                    d[cur].neighbors.append(d[n])
        return d[node]


a = UndirectedGraphNode(0)
b = UndirectedGraphNode(1)
c = UndirectedGraphNode(2)
a.neighbors.append(b)
a.neighbors.append(c)
b.neighbors.append(UndirectedGraphNode(4))
s = Solution()
q = s.cloneGraph_bfs(a)
print(q.label, [i.label for i in q.neighbors])
