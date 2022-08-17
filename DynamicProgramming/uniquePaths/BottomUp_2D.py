class Solution:
    """
    Evaluate: 
        Time: O(m*n) - Iterate over the array right to left, bottom to the top 
        Space: O(m*n) - 2D array to store the number of unique paths for every position on the board 
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        # set the last row to 1, know there's only 1 way to get to destination
        for i in range(n): 
            dp[m-1][i] = 1
        # set the last column to 1, know there's only 1 way to get to destination
        for i in range(m):
            dp[i][n-1] = 1
        
        #Iterate from bottom up, right to left, skipping last row, last column
        for row in range(m-2, -1, -1): 
            for col in range(n-2, -1, -1): 
                dp[row][col] = dp[row+1][col] + dp[row][col+1]
        #Return what we get at the starting point
        return dp[0][0]