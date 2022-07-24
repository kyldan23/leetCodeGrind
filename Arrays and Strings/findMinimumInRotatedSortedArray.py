class Solution:
    """
    Undertand: 
        Guaranteed: All the elements are unique and sorted already
        
    Evaluate: 
        Time: O(logN)
        Space: O(1)
    """
    def findMin(self, nums: List[int]) -> int:
        ###Edge Case: Only 1 element 
        if len(nums) == 1: 
            return nums[0]
        
        ###Edge Case: No rotations, minimum element is the first element! 
        if nums[0] < nums[-1]: 
            return nums[0]
        
        ###Perform Binary Search (Rotation must have occured)
        left = 0 
        right = len(nums) - 1
    
         # Binary search way: find exactly where the point of change occured (This is where it's no longer "sorted", since you are going from a greater number to a smaller number, instead of ascending which is smaller followed by greater)
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value. Next value must be the minimum!
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            else: 
                if nums[0] < nums[mid]: 
                    left = mid + 1
                else: 
                    right = mid - 1
         

       