class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegrees, graph = self.degreesAndNeighbors(prerequisites, numCourses)
        leaves_stack = []
        result = []
        #Add all currrent courses with inDegree of 0 
        for course in range(numCourses): 
            if inDegrees[course] == 0: 
                leaves_stack.append(course)
        while leaves_stack: 
            curr = leaves_stack.pop() 
            result.append(curr) #curr node can be added directly to result, since it has no dependencies (no prereqs)
            neighbors = graph[curr]
            for neighbor in neighbors: 
                inDegrees[neighbor] -= 1 
                if inDegrees[neighbor] == 0: 
                    leaves_stack.append(neighbor)
        return len(result) == numCourses
            
    def degreesAndNeighbors(self, prerequisites, numCourses):
        """
        Input: List of prerequisites 
        Output: Dictionary of inDegrees for each course
        """
        inDegrees = {node: 0 for node in range(numCourses)}
        neighbors = {node: [] for node in range(numCourses)}
        
        for course, prereq in prerequisites: 
            inDegrees[course] += 1 #inDegree represents number of prereqs for a course 
            neighbors[prereq].append(course) 
        
        return inDegrees, neighbors
    
            
        