from collections import defaultdict

class Graph: 
    """
    Class to repesent Graphs
    """
    def __init__(self, numVertices): 
        self.graph = defaultdict(list) #default graph (Adjacency List)
        self.numVertices = numVertices
    def addEdge(self, u, v):
        """ Adds an edge connecting node u to node v
        """
        self.graph[u].append(v) 
    
    
    
    def topologicalSort(self):
        stack = [] #holds the result in reverse order 
        visited = [0] * self.numVertices
        
        def dfs_helper(node): 
            """Recursively performs DFS on all adjacent nodes before adding current node to the stack. 
            Input: node (int)
            Return: None
            """
            visited[node] = 1
            for neighbor in self.graph[node]:
                if visited[neighbor] == 0: #only perform DFS on neighbor if it hasn't been visited 
                    dfs_helper(neighbor)
            stack.append(node)
        
        for node in range(self.numVertices): #accounts for disconnected graph 
            if visited[node] == 0: #only perform DFS on the node if it hasn't been visited yet  
                dfs_helper(node)
        
        return stack[::-1] #Result is the opposite of the current order of the stack

# Test Code 1 by Neelam Yadav
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print ("Following is a Topological Sort of the given graph")
# Function Call
print(g.topologicalSort())

#Test Code 2 by me
g = Graph(6)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.addEdge(5, 4)
print ("Following is a Topological Sort of the given graph")
print(g.topologicalSort())