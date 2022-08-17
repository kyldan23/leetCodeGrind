from collections import deque
class Solution:
    """
    Evaluate: 
        Time: O(m*n)
            Nested for loop: O(m*n) - visit each cell 
            BFS O(m*n) - visit all cells at most once 
        Space: O(m*n)
            worst case: all cells are rotten already and therefore stored in the queue
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #track number of fresh oranges
        freshRemaining = 0 #len(grid) * len(grid[0])
        time = 0 
        queue = deque() 
        for r in range(len(grid)): 
            for c in range(len(grid[0])):
                """
                if grid[r][c] == 0 or grid[r][c] == 2: 
                    freshRemaining -= 1 
                """
                if grid[r][c] == 1: #fresh orange
                    freshRemaining += 1
                if grid[r][c] == 2: 
                    queue.append((r, c))
        while queue: 
            # Edge Case 
            if freshRemaining == 0: 
                break
            time += 1
            size = len(queue)
            for i in range(size): 
                r, c = queue.popleft() 
                for position in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if self.validSquare(position[0], position[1], grid):
                        if grid[position[0]][position[1]] == 1: 
                            freshRemaining -= 1
                            grid[position[0]][position[1]] = 2 
                            queue.append(position)
        return time if not freshRemaining else -1
            
    """Returns whether (r,c) is a valid position within the grid 
    """
    def validSquare(self, r, c, grid):
        return not (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]))  