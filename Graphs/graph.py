class Graph:
    def __init__(self,edeges):
        self.edeges = edeges
        self.graph = {}
        for edge in self.edeges:
            if edge[0] in self.graph:
                self.graph[edge[0]].append(edge[1])
            else:
                self.graph[edge[0]] = [edge[1]]
    def show(self):
        print(self.graph)
if __name__ == "__main__":
    edge = [("A","B"),
            ("A","D"),
            ("B","A"),
            ("B","D"),
            ("B","C"),
            ("D","B"),
            ("D","A"),
            ("D","E"),
            ("E","D"),
            ("E","C"),
            ("C","B"),
            ("C","E"),
            ]
    g = Graph(edge)
    g.show()