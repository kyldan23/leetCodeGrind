class Solution:
    """ Understand 
    1. Always equal number of opening and closing characters? No 
    Input: s = "({[]})", output = True
    Input: s = "(", output = False (Base Case: a single character is not closed)
    Uneven Opening/Closing Character Test cases: 
    Input: s = "({", output = False (Only opening brackets)
    Input: s = "()]", output = False (More closing than opening characters)
    """
    """ Plan 
    1. Stack, Hashmap, Hashset
    Stack - keep track of all opening characters IN ORDER 
    Hashmap - map opening to closing brackets
    Hashset - store all opening brackets
    
    Pseduo: 
    Stack mapping each opening to closing bracket 
    Iterate over all elements 
        If element is an opening bracket, add to stack 
        else: 
            If stack is not empty: 
                Pop element off stack
                Check if current element is equal to closing character of popped element
                    return False if not equal
            else: return False 
    If stack is not empty: return False 
    else: return True
    """
    """ Evaluate
    1. Time Complexity: O(N) - one pass over all elements. Key lookup in dictionary is O(1)
    2. Space Complexity: O(N) - at most all opening characters, filling the stack 
    """
    
    def isValid(self, s: str) -> bool:
        """More Efficient Code"""
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'}

        for c in s: 
            if c in closeToOpen:  
                if stack and stack[-1] == closeToOpen[c]: 
                    stack.pop()
                else: 
                    return False 
            else: 
                stack.append(c)
        return not stack
        
        """ Own Solution - Passed All Test Cases
        mapping = {'(':')', '[':']', '{':'}'}
        opening = {"(", "[", "{"}
        stack = []
        for c in s: 
            if c in opening: 
                stack.append(c)
            else: 
                if not stack: 
                    return False 
                else: 
                    prevOpen = stack.pop()
                    prevClose = mapping[prevOpen]
                    if c != prevClose: 
                        return False 
        return not stack #True if stack is empty, False otherwise
    """