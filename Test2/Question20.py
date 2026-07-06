class Graph:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "D"],
            "D": ["B", "C"]
        }

    def dfs(self, vertex, visited):
        visited.append(vertex)
        print(vertex, end=" ")

        for node in self.graph[vertex]:
            if node not in visited:
                self.dfs(node, visited)


g = Graph()

visited = []

print("DFS Traversal:")
g.dfs("A", visited)