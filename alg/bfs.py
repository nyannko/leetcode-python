import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == '__main__':
    graph = {0:[1,2], 1:[2], 2:[]}
    bfs(graph, 0)