from collections import defaultdict
class Graph: 
    """
    Class to repesent Graphs
    """
    def __init__(self, numVertices): 
        self.graph = defaultdict(list) #default graph (Adjacency Set)
        self.numVertices = numVertices
    def addEdge(self, u, v):
        """ Adds an edge connecting node u to node v
        """
        self.graph[u].append(v) 

    def khanAlgo(self): 
        nodesWithNoIncomingEdges = [] #current nodes to process  
        result = []
        #Set the default indegree (edges incoming to the node) for ALL NODES to 0 
        inDegrees = {node: 0 for node in range(self.numVertices)}
        #For each node in the graph dictionary, get all neighbors and increment each of their inDegrees. 
        for node in self.graph: 
            for neighbor in self.graph[node]: 
                inDegrees[neighbor] += 1
        #Find all current nodes with no incoming edges, add the node directly to result
        for node in range(self.numVertices): 
            if inDegrees[node] == 0: 
                nodesWithNoIncomingEdges.append(node)
        #Process current leaves: add the current leaf to result and decrement its neighbors' inDegrees.
        while nodesWithNoIncomingEdges: 
            currNode = nodesWithNoIncomingEdges.pop() 
            result.append(currNode)
            for neighbor in self.graph[currNode]: #get all neighbors of the current node 
                inDegrees[neighbor] -= 1 #since the current node is being removed, the inDegree of its neighbor must be decremented by 1
                if inDegrees[neighbor] == 0: #check if neighbor has no other incoming edges now 
                    nodesWithNoIncomingEdges.append(neighbor)
        return result 

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print (g.khanAlgo())

g = Graph(6)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.addEdge(5, 4)
print(g.khanAlgo())