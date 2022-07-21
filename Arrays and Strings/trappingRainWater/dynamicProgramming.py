class Solution:
    """ 
    Match: Dynamic Programming -Storing information we need in separate arrays
    
    Evaluate: 
    Time: O(N)
    Space: O(N)
    """
    def trap(self, height: List[int]) -> int:
        #maxArrayLeft 
        #maxArrayRight
        #total 
        #Iterate from second element to second to last element 
            #total += min(maxArrayLeft[index], maxArrayRight[index]) - height[index]
        #return total 
        maxFromLeft, total = height[0], 0
        maxArrayRight = height[:] 
        for i in range(len(height)-2, -1, -1): #past end, we are stopping at 0
            maxArrayRight[i] = max(maxArrayRight[i+1], maxArrayRight[i])
        
        for i in range(1, len(height)-1): #1st and last element never contain water (not possible)
            total += max(0, (min(maxFromLeft, maxArrayRight[i])) - height[i])
            print(total)
            if height[i] > maxFromLeft: 
                maxFromLeft = height[i]
        return total
            
            
            
        
        
        
        
        