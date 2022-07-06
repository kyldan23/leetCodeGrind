class Graph: 
    def __init__(self):
        self.edges = {}
    def add_edge(self, start_node, end_node):
        if start_node not in self.edges: 
            self.edges[start_node] = []
        if end_node not in self.edges: # need to make sure end_node also exists in the dictionary too 
            self.edges[end_node] = []
        self.edges[start_node].append(end_node)

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 1)
graph.add_edge(1, 3)
graph.add_edge(1, 4) #Check that it creates an empty list for a key value of 4
print(graph.edges)