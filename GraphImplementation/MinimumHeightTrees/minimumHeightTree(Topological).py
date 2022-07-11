from collections import defaultdict
class Solution:
    """
    Runtime: 
        Definitions: 
            V = # of nodes 
            (V-1) = # of edges (in a tree, there's always V-1 edges)
        Time: 
        - Construct graph by iterating over all "edges": O(# of edges) = O(V-1)
        - Retrieve initial set of leaves by iterating over all nodes: O(V)
        - Remove all nodes except for the centroids would take close to O(V)
        - Total: O(V) 
        Space: 
        - Construct graph with adjacency list. There are O(V) nodes and O(V-1) edges => O(V) nodes + O(V-1) edges = O(V) 
        - Stack: Worst case is a star shape with one centroid and the rest are leaves
            leaves_stack in this case will have O(V-1) elements, since all but the center node are leaves
            newLeaves stack will have O(1) element, with just the center node 
        - Total: O(V) 
        
 
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = self.createGraph(edges)
        
        """Sneaky Edge Case: If n <=2 , then the graph is completely empty. Therefore, none of the elements will be added to the leaves_stack in the for loop. 
        """
        if n <= 2:  
            return [i for i in range(n)]
        
        leaves_stack = [] #store current layer of leaves
        #Store the the first layer of leaves 
        for i in range(n): 
            if len(graph[i]) == 1: #Find all nodes that are leaves 
                leaves_stack.append(i)
        
        remaining_nodes = n 
        while remaining_nodes > 2: #if less than or equal to 2 nodes, then you have the centroid(s) and no more processing is needed
            remaining_nodes -= len(leaves_stack)
            newLeaves = [] 
            
            while leaves_stack:
                leaf = leaves_stack.pop() 
                neighbor = graph[leaf].pop() 
                graph[neighbor].remove(leaf) #remove the neighbor's connection to the current "leaf"
                if len(graph[neighbor]) == 1: 
                    newLeaves.append(neighbor)
            leaves_stack = newLeaves 
        return leaves_stack 
            

    def createGraph(self, edges):
        #Input: list of EDGES 
        #Ouput: Dictionary (Node: set of neighbors)
        graph = defaultdict(set) #default is empty set
        for start, end in edges: 
            graph[start].add(end)
            graph[end].add(start)
        return graph
    
        