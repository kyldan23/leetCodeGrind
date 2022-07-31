class Solution:
    """
    Evaluate: 
        Time: O(N^2) - From the bottom to the top of the table number of positions to calculate is 1+2+3+4+... = O(N^2)
        Space: O(N^2) - 2D memo table 
    """
    def longestPalindrome(self, s: str) -> str:
        res = ""
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s) -1, -1, -1): # Build the 2D dp array from bottom up
            for j in range(i, len(s)): #start at j=i (leftmost) and move to the right 
                """Base case 1: single element is always a palindrome"""
                if i == j: # (1 element)
                    dp[i][j] = True
                """Base case 2: two elements, simply see if the two elements are equal"""
                elif j - i == 1: # 2 elements
                    dp[i][j] = s[i] == s[j]
                """Recursive Case: Compare the elements on the ends, the recurse on what's left in the middle"""
                else: 
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1] == True
                """If the current is a palindrome, possible for it to be the longest string"""
                if dp[i][j]: 
                    if len(res) < j - i + 1:
                        res = s[i:j+1]
        return res

        