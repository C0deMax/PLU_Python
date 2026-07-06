class Graph:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "D"],
            "D": ["B", "C"]
        }

    def checkEdge(self, u, v):
        if v in self.graph[u]:
            print("Direct edge exists")
        else:
            print("Direct edge does not exist")


g = Graph()

g.checkEdge("A", "B")