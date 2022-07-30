class Solution:
    """
    Plan: 
        Maintain the currSum and maxSum 
        Iterate over all the values of nums (except first value since we used it as default value)
            if currSum is negative, that would not contribute to the greatest sum, it serves only as a detriment to finding the greatest sum, it would take away from future values.
            => Need to reset currSum to 0 to start a new running sum from the current value 
        
            else: currSum is positive and will add to the running sum 
        
            Always check if the currSum is greater than the max sum seen so far 
    Evaluate: 
        Time: O(N) - runs thruogh array once 
        Space: O(1) - only two constant variables 
    """
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0] #current sum 
        maxSum = nums[0]  #holds the maximum sum so far 
        
        for num in nums[1:]: 
            """ Works 
            currSum += num 
            if currSum < num: 
                currSum = num 
            maxSum = max(maxSum, currSum)
            """
            if currSum < 0: 
                currSum = 0 
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum