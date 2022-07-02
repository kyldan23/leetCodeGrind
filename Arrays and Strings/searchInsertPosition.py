class Solution:
    """ Understand: 
    Input: nums = [1, 3, 5, 6], target = 2 
    Output: 1
    Edge Cases: 
    Input: nums = [3], target = 4
    Output: 1 
    Input: nums = [3], target = 2 
    Output: 0
    Input: nums = [2, 4], target = 3
    Output: 1 
    """
    """ Plan 
    Recursive Function
        Helper Method:
        Input: leftPos, rightPos
        Base Case: 
        1. Left Pos > rightPos #searched through all the possible values, no other values to search
        Recursive Case: 
        1. Target is greater than mid 
            -Recursively call with an updated left position 
        2. Target is less than mid 
            -Recursively call with an updated right position 
    """
    """ Evaluate 
    Time: O(logN)
    Space: O(logN) due to call stack. If iterative, then space would be O(1). 
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        def helper(leftPos, rightPos): 
            if leftPos > rightPos:
                return leftPos
            
            mid = (leftPos + rightPos) // 2
            if nums[mid] == target: 
                return mid 
            if target > nums[mid]:
                return helper(mid+1, rightPos)
            else: 
                return helper(leftPos, mid - 1)

        
        return helper(0, len(nums)-1)