class Solution:
    
    """
    Evaluate: 
        Time: O(2^n) - generate all combinations of all items 
        Space: O(N) - recursive call stack
    """
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        # Base Case
        if W < 0 : 
            return float('-inf')
        elif n == 0 or W == 0: 
            return 0 
        else: 
            return max(val[0] + self.knapSack(W-wt[0], wt[1:], val[1:], n-1), self.knapSack(W, wt[1:], val[1:], n-1))
        # Recursive Case 