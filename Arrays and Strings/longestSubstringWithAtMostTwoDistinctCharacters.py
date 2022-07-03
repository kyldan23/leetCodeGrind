from collections import defaultdict
class Solution:
    """ Understand
    Input: s (list)
    Output: longest substring (number)
    
    1. Input: s = "eceba", output: 3 
    2. Input: s = "eeeba", output: 4 
    3. Input: s = "ccaabbb", output: 5 (best choice starts at 'a') 
    
    Questions: 
    1. Empty list? Nope, minimum length is 1 
    2. Only have to worry about lowercase letters? Yes 
    """
    """Match
    Sliding window - substring is continuous, therefore drag each character to the right as much as possible 
    """
    """Evaluate 
    Time: O(N)
    Space: O(1)
    """
    
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ### PseudoCode
        #maxLength = 0
        #empty hashmap 
        #left = 0 
        #right index iterate over all indices of s
            #add current to the hashmap (increasing its frequency)
            #if window conditin: 
                #compare current length to the maxLength 
            #else 
                #keep shrinking the window until window is valid again 
                
        maxLength = 0 
        word_dict = defaultdict(int)
        left = 0 
        for right in range(len(s)):
            word_dict[s[right]] += 1
            while len(word_dict) > 2: #fix window condition if needed
                word_dict[s[left]] -= 1 
                if not word_dict[s[left]]:
                    del word_dict[s[left]]
                left += 1
            #Window is valid 
            windowLength = right - left + 1
            maxLength = max(maxLength, windowLength)
        return maxLength
                    
                    
                
            
            