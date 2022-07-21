class Solution:
    """
    Match: DFS with Backtracking 
    
    Plan: 
    1. Create a dictionary with each node as key and prereqs of that course as values (node: [prereq1, prereq2, , ....])
    2. Iterate over "prerequisites" and append each prereq to the proper node (key)
    3. Perform DFS with backtracking for each node, checking for cycles 
        - If any node returns "True" (cycle exists), return False immediately 
    4. Return True (all courses can be taken)
    
    Data Structure: 
    1. visitedSet holds all nodes that are visited in the current path 
    
    DFS Helper: 
    Base Cases: 
    1. Current node has already been visited 
        - Return True (A cycle was detected!)
    2. Current node has no prerequsities (End of path!)
        - Return False (No cycles were found) 
    
    Recursive Case: #current node has not been visited yet
    - Add current node to visitedSet
    - Iterate over all the neighbors of current node 
        - Perform DFS on each neighbor
            -If a neighbor's path contains a cycle, return True immediately 
    - Remove current node from visited 
    - Return False (no cycles detected)
    
    
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {node: [] for node in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        visitedSet = set() #maintain nodes that are visited in a path
        def dfs(course): 
            if course in visitedSet: 
                return True 
            elif prereqMap[course] == []: 
                return False 
            else: 
                visitedSet.add(course)
                for prereq in prereqMap[course]: 
                    if dfs(prereq):
                        return True 
                visitedSet.remove(course) #Make sure visitedSet is clean before exploring a new path, since visitedSet is declared outside the function and will be passed on to the next course that is explored
                prereqMap[course] = [] #If no cycle is found within the current node, no need to re-explore it in the future 
                return False 
        for course in range(numCourses):
            if dfs(course): #if cycle exists 
                return False 
        return True 
        
        
        
        
        