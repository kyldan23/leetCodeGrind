class Solution:
    """Pseudo-Code"""
        #Initialize empty hashmap (Key: Letter, Value: Count)
        #res = longest "valid" substring (default is 0)
        #Initialize left pointer to start at index 0 
        #Iterate over all the values for the right pointer 
            #windowSize = right pointer - left pointer + 1 
            #add current letter to hashmap
            #corrections = windowSize - most frequent letter 
            #if corrections <= k: 
                #res = compare between max window size seen so far to current window size 
            #else: (# of corrections exceeds k, current substring is not valid)
                #while corrections > k: 
                    #Decrease the count of the current letter in the hashmap 
                    #Advance left pointer by 1
                    #update corrections
        #return corrections
    """Evaluate 
    Time: O(N)
    Space: O(k) - where k is the number of unique letters in the input string "s". At most, there are 26 letters in the alphabet, so it's independent from the input regardless. 
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0 
        leftPointer = 0 
        for rightPointer in range(len(s)):
            #Add current letter to hashmap 
            count[s[rightPointer]] = 1 + count.get(s[rightPointer], 0) #REVIEW: .get() sets default value if not found
            
            """Verify current window is valid """
            windowSize = rightPointer - leftPointer + 1 #Check for off by one error (add 1 for size)
            greatestLetter = max(count.values())
            numCorrections = windowSize - greatestLetter
            
            """Want to shift left pointer while the substring is not valid"""
            while numCorrections > k:
                count[s[leftPointer]] -= 1
                leftPointer += 1
                #Update number of corrections (copy of three lines above while loop)
                windowSize = rightPointer - leftPointer + 1
                greatestLetter = max(count.values())
                numCorrections = windowSize - greatestLetter
            
            """Substring is valid"""
            res = max(res, windowSize)
        return res
                
                
                
            
        
            