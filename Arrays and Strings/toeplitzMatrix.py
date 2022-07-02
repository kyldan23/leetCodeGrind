class Solution:
    """ Understand 
    Input: matrix(List)
    Output: boolean (T/F)
    
    1. Minimum size of the matrix? 1 square 
    2. Are all the values positive? Yes 
    """
    """ Plan 
    1. Iterate over all the columns (as starting points), except last 
        - Go diagonally, checking if it's a valid square first 
        - If any square is not the same, return False 
    2. Iterate over all the rows (as starting point), except last 
        - Go diagonally, checking if it's a valid square first 
        - If any square is not the same, return False 
    3. Return True, since checked all the possible diagonals 
    """
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def isValid(r, c): 
            if r >= len(matrix) or c >= len(matrix[0]): 
                return False 
            return True 
        for r in range(len(matrix)): 
            c = 0 
            firstVal = matrix[r][c]
            tempr = r 
            while isValid(tempr, c): 
                if matrix[tempr][c] != firstVal: 
                    return False 
                tempr, c = tempr + 1, c + 1
            
        for c in range(len(matrix[0])): 
            r = 0 
            firstVal = matrix[r][c]
            tempc = c 
            while isValid(r, tempc): 
                if matrix[r][tempc] != firstVal: 
                    return False 
                r, tempc = r + 1, tempc + 1
        return True
                