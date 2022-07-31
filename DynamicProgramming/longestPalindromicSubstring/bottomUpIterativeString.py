class Solution:
    """
    Evaluate: 
        Time: O(N^2) - for each index, traversing the entire array 
            O(N) indices * O(N) traverse entire array for each index = O(N^2)
        Space: O(N) - store result string, which is the length of s 
    """
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLength = 0 
        
        """Treat every index as the middle of the palindrome"""
        for i in range(len(s)): 
            """Odd length palindromic string""" 
            left, right = i, i #odd length has a single element as the center 
            #While pointers are within the boundaries of the string, and the elements match
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                lengthOfCurrentString = right - left + 1 #must add 1 to get length 
                if lengthOfCurrentString > resLength: 
                    res = s[left: right + 1] #past end 
                    resLength = lengthOfCurrentString
                #Expand outwards! Left keeps moving left, right moves right 
                left -= 1 
                right += 1
            
            """Even length palindromic string"""
            left, right = i, i + 1 #even length has two elements as the "center"
            """EVERYTHING BELOW IS THE EXACT SAME AS FOR THE ODD LENGTH PALINDROME!!"""
            #While pointers are within the boundaries of the string, and the elements match
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                lengthOfCurrentString = right - left + 1 #must add 1 to get length 
                if lengthOfCurrentString > resLength: 
                    res = s[left: right + 1] #past end 
                    resLength = lengthOfCurrentString
                #Expand outwards! Left keeps moving left, right moves right 
                left -= 1 
                right += 1
        return res

        