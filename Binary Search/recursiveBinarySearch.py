def binary_search(nums, target):
    def helper(left, right):
        if left > right: #Base Case 
            return False 
        else: #left <= right
            middleIndex = (left + right) // 2
            if nums[middleIndex] == target: 
                return True 
            elif target > nums[middleIndex]:
                return helper(left, middleIndex - 1) #since you've just checked middleIndex
            else: 
                return helper(middleIndex + 1, right) 
    return helper(0, len(nums)-1)
