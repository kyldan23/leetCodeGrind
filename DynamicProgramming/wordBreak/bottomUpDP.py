class Solution:
    """
    Evaluate: 
        Time: O(n^3) - Two nested for loops, plus finding the substring. 
            1. O(N) to look through each index of the string "s" 
            2. O(M) to look through each element in "wordDict" for each index, since need to test all words that have the right length 
            3. O(N) to compare string "s" to each word in "wordDict", since the word could be the same length as "s" 
        Space: O(N) - length of the dp array 
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) 
        """After full word is searched, starting index is length of string, which means you are done searching! Therefore, this is True since you're done searching. """
        dp[len(s)] = True 
        
        for i in range(len(s) - 1, -1, -1): #Bottom up 
            for word in wordDict: #want to try every word each time 
                """
                1. Check if from the starting index i to the end of s, has at least the number of characters in the word being compared to 
                2. Check if the substring matches the word being compared to 
                Note: The word can be smaller than reaching all the way to the end, we just need to then check if the end is reachable from wherever we leave off
                """
                if (i + len(word)) <= len(s) and s[i:i+len(word)] == word: #just matched a word 
                    dp[i] = dp[i + len(word)] #need to check if wherever we leave off, the end is reachable. Should have been calculated already. 
                if dp[i] == True: 
                    break
        return dp[0]
            
        