class Solution:
    """Understand
    Questions: 
    1. Can the temperatures be negative? guaranteed to be positive 
    2. Empty list? guaranteed at least 30 temps in the list
    3. What to return if there is no higher temperature for current element(edge case)? 0 for that index 
    4. What to return if only 1 elment(edge case)? 0 for that element
    
    Input:  temperatures = [71, 72]
    Output: [1, 0]
    
    Input: temperatures = [71]
    Output: [0]
    
    Input: temperatures = [71, 69, 73]
    Output: [2, 1, 0]
    
    Keep Track of: Highest Temperature after current temp 
    Input: temps = [71, 69, 73]
            temps = [73, 69, 71]
    
    """
    """Plan
    Brute Force: 
    For each element, search the rest of the list for higher temperature O(N^2)
    
    Stack: Only iterates over the input once 
    1. Create a result list of size temperatures and default value of 0 
    2. Create a stack of tuples of the form (temp, index). Guaranteed to be a "Monotionic "Strictly" Decreasing or equal Stack" (invariant due to the comparison performed)
    3. Iterate over all the temperatures 
        a. For each temperature, check if it's greater than the temp at the top of the stack.
        b. If it is greater, then pop the element off the stack. Find the difference between their indices. Continue to go down the stack to check for temps that are less than current temp. 
        c. Append the current element (temp, index) tuple into the stack. 
    """
    """ Evaluation: 
    Time Complexity: O(N) - iterate over all the elements once 
    Space Complexity: O(N) - create a result list of the same size as the input
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #list of tuples (temp, index)
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #second condition could hit edge case if stack is empty
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t, i))
        return res