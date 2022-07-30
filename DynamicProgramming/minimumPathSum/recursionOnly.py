class Solution:
    """Evaluate: Pure recursion, no memoization 
        Time: O(2^(m+n)) - for each square, there each move, there are 2 options. 
        Space: O(m+n) - recursion depth is the total number of squares possible, which at most is (m+n) - going the full number of rows and columns to get to the destination. 
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Returns the minimum path to the bottom right"""
        rowBound, colBound = len(grid) - 1, len(grid[0]) - 1
        def helper(row, col, sumSoFar): 
            """Return the minimum path to the bottom right from position (row, col)"""
            #Base Case 1: Out of bounds 
                #return infinity 
            #Base Case 2: Reached target 
                #return current value 
            ###Recursive Case
                #return minimum of EITHER traveling to the right or down 
            if row > rowBound or col > colBound: 
                return float('inf')
            elif row == rowBound and col == colBound: 
                return sumSoFar + grid[row][col]
            ###Valid position, haven't reached target yet though
            else: 
                currSum = sumSoFar + grid[row][col]
                return min(helper(row, col + 1, currSum), helper(row + 1, col, currSum))
        return helper(0, 0, 0)
        
        