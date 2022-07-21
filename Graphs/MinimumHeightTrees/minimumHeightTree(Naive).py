from collections import deque
from collections import defaultdict
class Solution:
    """
    Runtime: Does not meet requirements due to O(n^2) time complexity
        1. Naive Solution: Use every node as the root and perform BFS each time to find its height 
            Time: O(n * (iterate over all nodes/edges for each node)) = O(n * (n + e)) = O(n^2 + n*e)
                Let E = # of edges, n = # of nodes 
         
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        visitedSet = set()
        graph = self.createGraph(edges)
        height_dict = defaultdict(list)
        queue = deque() 
        
        for node in range(n):
            queue.append(node)
            visitedSet.add(node)
            level = 0 
            
            while queue: 
                level += 1 
                length = len(queue)
                for i in range(length): #number of nodes in current level 
                    currNode = queue.popleft() 
                    for neighbor in graph[currNode]:
                        if neighbor not in visitedSet: 
                            queue.append(neighbor)
                            visitedSet.add(neighbor)
                if not queue: #Queue is empty after visiting all nodes in the current level => no more levels 
                    height_dict[level].append(node)
                    #print(node, level)
                    #print(graph)
            visitedSet = set()
        minHeight = min(height_dict.keys()) #O(n) 
        return height_dict[minHeight]
                
            
                
        #Iterate over all possible roots (n): 
            #Perform BFS, keeping track of the number of levels
                #If the queue is empty after iterating over all the nodes in the current level 
                    #Save the current node and its height in the dictionary 
            #Reset visitedArr 
        #Sort height_dict by key (heights)
        #Return the list associated with the min height key

    def createGraph(self, edges):
        #Input: list of EDGES 
        #Ouput: Dictionary (Node: neighbors)
        graph = defaultdict(list) #default is empty list 
        for start, end in edges: 
            graph[start].append(end)
            graph[end].append(start)
        return graph
    
        