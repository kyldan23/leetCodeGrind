class Solution:
    """
    Plan: Brute Force 
    Base Case: 
        1. s is empty => Nothing left to search, return True 
    Recursive Case: 
        1. Get current length of the string 
        2. Iterate over indices starting from 1 to the length of the string S 
            - Get substring from index 0 to the index 
                - If the substring exists in the dictionary, recurse on the rest of the word
    Evaluate: 
        Time: 
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0: 
            return True 
        else: 
            wordLen = len(s)
            for pastEndIndex in range(1, wordLen + 1): #represents end index (pastEnd)
                if s[:pastEndIndex] in wordDict and self.wordBreak(s[pastEndIndex:], wordDict): 
                    return True 
            return False 
                                
            
        