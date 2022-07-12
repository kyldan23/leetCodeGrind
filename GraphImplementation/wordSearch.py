class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, index):
            ### BASE CASE (2) 
            if index == len(word): 
                return True 
            """
            elif row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[index] or (row, col) in visited: 
                return False 
            ### RECURSIVE CASE: current letter on board is valid 
            else: 
                visited.append((row, col))
                print(visited)
                found =  dfs(row, col + 1, index + 1, visited) or dfs(row, col - 1, index + 1, visited) or dfs(row + 1, col, index + 1, visited) or dfs(row - 1, col, index + 1, visited)
                visited.remove((row, col))
                return found"""
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[index]:
                return False 
            temp = board[row][col]
            board[row][col] = " "
            found = dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1) or dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1)
            board[row][col] = temp
            return found
        for row in range(len(board)): 
            for col in range(len(board[row])):
                if dfs(row, col, 0): 
                    return True 
        return False 