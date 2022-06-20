class Solution:
    """ Understand
    1. Can the number of asteroids be very large? -If very large => need to pass through once, YES there can be 10^4 asteroids. 
    2, If two planets are initially not going to collide, can one of them collide with an opposing planet in the future?
    3. What to do if no asteroids or a single asteroid? Will not happen given constraint
    
    Collision: Can only occur if the last element in the stack is moving right and current 
    asteroid is moving to the left. Will miss otherwise. 
    
    Insight: At each step, we are checking if a collision occured. 
    
    Own Test Case: 
    
    Basic (Two elements):
    1. Input: asteroids: [8, -8], Output: [] #collision, same size, both destroyed 
    2. Input: asterpids: [-8, 8], Output: [-8, 8] #no collision, moving in opposite direction
    3. Input: asteroids: [2, -8], Output: [-8] #collision, right size bigger size
    
    Expansion: 
    1. Input: asteroids: [5, 8, -8], Output: [5]
    2. Input: asteroids: [5, 2, -8], Output: [-8]
    3. Input: asteroids: [=2, 2, -8], Output: [-2, -8] #move in same direction, after collision
    """
    """Plan
    1. Stack - order of planets matters
    """
    """ Evaluate
    Time Complexity: O(N) - only add/delete each element ONCE.
    Space Complexity: O(N) - only possibly add all elements into the stack ONCE
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for curr in asteroids:
            while stack and stack[-1] > 0 and curr < 0: #Check if collision occured FIRST
                diff = curr + stack[-1]
                if diff < 0: #current planet wins (right side) 
                    stack.pop()
                elif diff > 0: #previous planet wins (left side)
                    curr = 0 # guaranteed no asteroid is 0 and break out of loop
                else: #planets are same size 
                    curr = 0 
                    stack.pop()
            if curr: 
                stack.append(curr)
        return stack
                
        
        """ WRONG solution, kept running into cases that I hadn't thought of 
        stack = deque()
        stack.append(asteroids[0])
        for curr in asteroids[1:]:
            if curr/stack[-1] > 0 or (stack[-1] < 0 and curr > 0): #same direction or still a miss 
                stack.append(curr)
            else: #different direction
                while stack: 
                    leftSize = abs(stack[-1])
                    rightSize = abs(curr)
                    if leftSize > rightSize: 
                        break
                    elif leftSize == rightSize: 
                        stack.pop()
                        break
                    else: 
                        stack.pop()
                        if not stack: 
                            stack.append(curr)
                            break
        return list(stack) #used a deque for stack 
        """