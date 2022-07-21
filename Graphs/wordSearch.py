class Solution:
    """Match 
    DFS Recursive 
    """
    """Evaluate
    Definitions: 
    n = height of board, m = width of board, w = length of the word
    Time: O(traverse through every element of board) * O(dfs on each element) = O(m*n) * O(4^w)
    Why is the DFS runtime O(4^w)? Look at notion 
    Space: O(w)
    Why? The depth of the call stack is at its max when we find a path. In that case, the path is the size of the word itself. Otherwise, we wouldn't returned false before even reaching the same number of letters as the word. 
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, index):
            ### BASE CASE (2) 
            if index == len(word): 
                return True 
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[index]:
                return False 
            ### RECURSIVE CASE: current letter is valid 
            #Mark the current location, so that it is not explored again within the same path 
            temp = board[row][col]
            board[row][col] = " "
            # Check all 4 neighbor directions
            found = dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1) or dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1)
            #Revert the change (unmark the current location) before backtracking to try a different path, that doesn't include this current node in the new path 
            board[row][col] = temp
            """Alternatively: You only need to revert the change if a path ISN'T FOUND. Otherwise, you stop searching immediately after finding a path anyways, so reversing the change is not really needed.
            if not found: 
                board[row][col] = temp
            """
            return found
        
        for row in range(len(board)): 
            for col in range(len(board[row])):
                if dfs(row, col, 0): 
                    return True 
        return False 