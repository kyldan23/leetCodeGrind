class Solution:
    """Understand
    - Graph is undirected
    - Not guaranteed to be connected (need to iterate over every node in the 2d array just in case)
    
    """
    
    """Match
    1. Graph Coloring - DFS Approach
    """
    """Plan 
    Solution 1: Graph Coloring 
    0 - not colored 
    1 - blue 
    -1 - red
    
    1. Color array acts the same as marking whether or not the node has already been visited. Default value of 0 means they all start off as "uncolored" or "unvisited". 
    

    Helper: 
    1. Check if node is already colored. If it's already colored, return True only if it's currently the same color. Otherwise, return false. 
    
    """
    """Evaluate:
    Time: O(V+E) - inital for loop ensures all vertices are explored. Inside helper, each node has all its neighbors checked (its adjacency list). 
    Space: O(V) - call stack can only go as deep as the number of vertices, since the helper returns immediately if a node has been explored already. The stack only builds with a path of unexplored nodes. 
    """
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*len(graph) #holds colors for each node, all nodes are initially uncolored
        def validColor(g, colorArr, currColor, node): 
            if colorArr[node] != 0: #If current node is colored already (meaning its already been visited)
                return colorArr[node] == currColor #Verify its color is the same as the color we want
            else: #Current node is not colored 
                colorArr[node] = currColor #set the color of the node, similar to "marking" the node as "visited"
                for neighbor in g[node]: #iterate over the neighbors of the current node
                    if not validColor(g, colorArr, -currColor, neighbor): #change the color for the node's neighbors 
                        return False #able to return right when a conflict is found 
                return True 
        for i in range(len(graph)): #Graph may be disconnected, ensures EVERY node is checked
            """Check performed only if the node is uncolored, otherwise, already assigned a color, pretty much same as only checking "unmarked" nodes"""
            if color[i] == 0 and (not validColor(graph, color, 1, i)):
                return False
        return True
        