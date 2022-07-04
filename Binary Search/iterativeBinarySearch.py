def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right: 
        middleIndex = (left + right) // 2
        if nums[middleIndex] == target: 
            return True 
        elif target > nums[middleIndex]:
            right = middleIndex - 1
        else: 
            left = middleIndex + 1
    return False