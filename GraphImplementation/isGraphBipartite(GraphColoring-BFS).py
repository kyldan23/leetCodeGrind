from collections import deque
class Solution:
    """Understand
    - Graph is undirected
    - Not guaranteed to be connected (need to iterate over every node in the 2d array just in case)
    """
    
    """Match
    1. Graph Coloring (BFS)
    """
    """Plan 
    Solution 1: Graph Coloring 
    0 - not colored 
    1 - blue 
    -1 - red
    
    Helper: 
    1. Check if node is already colored. If it's already colored, return True only if it's currently the same color. Otherwise, return false. 
    
    """
    """Evaluate:
    Time: O(V+E) - inital for loop ensures all vertices are explored. 
    Space: O(V) - call stack can only go as deep as the number of vertices, since the helper returns immediately if a node has been explored already. The stack only builds with a path of unexplored nodes. 
    """
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*len(graph) #holds colors for each node, all nodes are initially uncolored         
        for i in range(len(graph)): #Graph may be disconnected, ensures EVERY node is checked
            if color[i] == 0: #only sets the color initially if the node hasn't been visited. Only possible for starting off the traversal and for disconnected nodes. 
                queue = deque()
                queue.append(i) #add starting node 
                color[i] = 1 #mark the node as "visited" by setting its color 
            while queue: 
                node = queue.popleft() 
                for neighbor in graph[node]: #iterate over all neighbors of the popped "node"
                    if color[neighbor] != 0: #colored (visited) already
                        if color[neighbor] == color[node]: #if the neighbor's color is the same as the current node 
                            return False
                    else: 
                        queue.append(neighbor) 
                        color[neighbor] = -color[node] #same pattern: mark node as visited after adding to queue. Neighbor's color must be opposite the current node's color.
        return True
        