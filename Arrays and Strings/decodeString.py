from collections import deque
class Solution:
    """Match 
    1. Stack 
    """
    """ Evaluate
    Time: O(N) - iterate over String "s" once
    Space: O(N) - worst case all are nested brackets 
    """
    def decodeString(self, s: str) -> str:
        stack = []
        for element in s:
            if element != "]":
                stack.append(element) 
            else: 
                substr = deque()
                while stack[-1] != "[":
                    substr.appendleft(stack.pop())
                stack.pop()#pop one more element to remove "["
                
                number = deque() 
                while stack and stack[-1].isdigit():
                    number.appendleft(stack.pop()) 
                
                substrString = "".join(substr)
                numberString = "".join(number)
            
                #append the resulting string to the stack
                stack.append(substrString * int(numberString))
        return "".join(stack)