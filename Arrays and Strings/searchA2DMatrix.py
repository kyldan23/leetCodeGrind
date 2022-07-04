class Solution:
    """ Understand
    1. Minimum number of elements? At least one element
    2. Negative elements? Yes
    """
    """Evaluate
    Time: O(log(m*n)) <= log(# of elements)
    Space: O(1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        lastIndex = ROWS * COLS - 1
        def helper(left, right):
            if left <= right: 
                mid = (left + right) // 2
                row = mid // COLS
                col = mid % COLS
                if matrix[row][col] == target: 
                    return True 
                elif matrix[row][col] > target: 
                    return helper(left, mid - 1)
                else: #matrix[row][col] < target
                    return helper(mid + 1, right)
            else: 
                return False
        return helper(0, lastIndex)