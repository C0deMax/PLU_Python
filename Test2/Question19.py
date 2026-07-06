class Graph:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "D"],
            "D": ["B", "C"]
        }

    def bfs(self, start):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while len(queue) > 0:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for node in self.graph[vertex]:
                if node not in visited:
                    visited.append(node)
                    queue.append(node)


g = Graph()

print("BFS Traversal:")
g.bfs("A")