from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ### Build graph (Dictionary of dictionaries)
        graph = self.buildGraph(equations, values)
        ### Process all elements in "queries" 
        result = []
        for numerator, denominator in queries: 
        #Case 1: Verify each variable in query exists 
            if numerator not in graph or denominator not in graph: 
                result.append(-1)
        #Case 2: Both variables exist, need to perform regular division => Perform DFS 
            else: 
                result.append(self.dfs(graph, numerator, denominator, set(), 1))
        return result 
            
    def dfs(self, graph, currNode, targetNode, visited, product):
        """Performs DFS with backtracking, starting with "currNode" (numerator). Attempts to find a path to the "targetNode" (denominator). Each time a node is visited, its added to "visited" set. 
        Output: Returns the product if the "targetNode" is reached, -1 otherwise. 
        """
        #Base Case 
        #1. currNode == targetNode (reached the destination node)
        if currNode == targetNode: 
            return product 
        #2. currNode has already been visited 
        elif currNode in visited: 
            return -1 
        
        #Recursive Case (Need to keep searching!)
        visited.add(currNode)
        for neighbor, value in graph[currNode].items(): #use .item() to get key, value pair from the current node's corresponding value
            temp = self.dfs(graph, neighbor, targetNode, visited, product * value)
            if temp != -1: 
                return temp 
        return -1
        """visited.add(currNode)
        neighbors = graph[currNode]
        answer = -1 
        
        if targetNode in neighbors: 
            answer = product * neighbors[targetNode]
        else: 
            for neighbor, value in neighbors.items(): 
                if neighbor not in visited: 
                    answer = self.dfs(graph, neighbor, targetNode, visited, product * value)
                if answer != -1:
                    break 
        return answer"""
        
    
    def buildGraph(self, equations, values):
        """
        Input: equations (list of 2 element lists), values (value of each corresponding equation)
        Returns a graph (dictionary of dictionaries) 
        """
        graph = defaultdict(defaultdict)
        
        for index, (numerator, denominator) in enumerate(equations):
            graph[numerator][denominator] = values[index]
            graph[denominator][numerator] = 1 / values[index]
        
        return graph
        