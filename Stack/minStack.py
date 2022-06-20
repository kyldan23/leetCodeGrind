class MinStack:
    """ Understand 
    1. Can pop(), top(), and getMin() operations be called on an empty stack? No 
    """
    """ Plan 
    1. Use a list with tuple elements (value, minSoFar)
    """
    """ Evaluate 
    1. Time Complexity: O(1) for all operations
    2. Space Complexity: O(N) to store all values 
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: 
            self.stack.append((val, val))
        else: 
            minVal = self.stack[-1][1] if self.stack[-1][1] < val else val 
            self.stack.append((val, minVal))
    def pop(self) -> None:
        self.stack.pop() 

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()