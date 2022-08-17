def knapSack(W, wt, val, n):
    """
    Evaluate: 
        Time: O(N*W) - reduced to polynomial complexity, since explore each possibility ONCE. 
        Space: O(N*W) + O(N)
            2D array: O(N*W)
            Recursion Call Stack: O(N) - go through every item in the worst case
    """
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    def helper(wt, val, W, n):
        # base conditions
        if W < 0:
            return float('-inf')
        elif n == 0 or W == 0:
            return 0
        if t[n][W] > -1:
            return t[n][W]
        # choice diagram code
        else:
            t[n][W] = max(val[n-1] + helper(wt, val, W-wt[n-1], n-1), helper(wt, val, W, n-1))
            return t[n][W]
    return helper(wt, val, W, n)