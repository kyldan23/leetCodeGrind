#User function Template for python3

class Solution:
    
    """
    Plan: 
    2D array: 
        Start from 0 (no capacity and no items) as a base case  
        Why? 
        -If we have a single item that takes full capacity, will need to check column with 0 capacity left. 
        -If using item 1, will need to compare with previous row with 0 items 
    Evaluate: 
        Time: O(n*W) 
            Test every single capacity from 0 to W and test every item 0 to m 
            Time improved from exponential (2^n) to polynomial, basically O(n^2)
        Space: O(n * W)
            2D array, #rows = items 0 to n, #cols = capacity of 0 to W 
        Definitions: 
        1. n = number of items 
        2. W = capacity 
    """
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        """ Pseudo-Code
        2D array - each row represents an item (with its weight and value) and column with increasing capacities 
        maxVal = 0 
        #Iterate over the 2D array starting with base case (0 capacity, 0 items): 
        Iterate over rows (items): 
            Iterate over columns (capacity):
                if row or column is 0: #unecessary, default value for all squares is 0 
                    set[row][col] = 0 
                elif current item <= capcity: 
                    set[row][col] = max([row - 1][capacity - weight of current item], [row - 1][col]) 
                else: 
                    set[row][col] = [row - 1][col] #same capacity, without current item 
                if [row][col] > maxVal: 
                    maxVal = [row][col]
        return maxVal 
        """
        """Additional row and column for base case """
        dp = [[0] * (W + 1) for _ in range(n + 1)] # (rows = items, cols = capacity)
        maxVal = 0 
        
        for item in range(1, n + 1): 
            for capacity in range(1, W + 1): 
                itemValue = val[item - 1]
                itemWeight = wt[item - 1]
                if itemWeight <= capacity: 
                    dp[item][capacity] = max(itemValue + dp[item - 1][capacity - itemWeight], dp[item - 1][capacity])
                else: 
                    dp[item][capacity] = dp[item - 1][capacity]
                maxVal = max(maxVal, dp[item][capacity])
        return maxVal
                
        

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends