class Solution:
    """ Understand 
    1. "/home/" => "/home" (No trailing "\")
    2. "/../" => "/" (Edge case, cannot go up higher than root directory)
    3. "/home//foo/" => "/home/foo" (remove double slash, remove trailing slash)
    """
    """ Plan
    1. Stack - need to keep track of file order 
    """
    """Evaluate
    1. Time complexity: O(N) - only making single pass 
    2. Space Complexity: O(N) - stack could possibly hold the entire string input 
    """
    def simplifyPath(self, path: str) -> str:
        stack, fileBuilder = deque(), []
        for c in path + "/": 
            if c == "/":
                currFile = "".join(fileBuilder)
                if currFile == "..": 
                    if stack: stack.pop()
                elif currFile and currFile != ".":
                    stack.append(currFile)
                fileBuilder = []
            else: 
                fileBuilder.append(c)
        return "/" + "/".join(stack)
        """ Does not work with triple dot case 
        dot, stack, fileBuilder = False, deque(), [] 
        for c in path: 
            if c == "." and dot: 
                if stack: 
                    stack.pop()
                dot = False 
            elif c == ".":
                dot = True 
            else: 
                dot = False
                if c == "/":
                    if fileBuilder:
                        stack.append("".join(fileBuilder))
                    fileBuilder = []
                else: #just a letter
                    fileBuilder.append(c)
        if fileBuilder: #Does not account for trailing double dot with no ending "/"
            stack.append("".join(fileBuilder))
        if not stack: 
            return "/"
        resultBuilder = []
        while stack: 
            resultBuilder.append("/")
            resultBuilder.append(stack.popleft())
        return "".join(resultBuilder)
        """
        