class Solution:
    """ Understand
    Constraints: 
    - Cannot use extra space, must modify original input matrix 
    Questions:
    1. Can the numbers be negative? Yes 
    2. Can there be multiple 0's? Yes 
    3. Is the matrix guaranteed to be square? No 
    4. Size of matrix. Guaranteed to have at least one row. 
    """
    """ Plan 
    Brute Force: 
    1. Create a separate matrix of the same size
        - Each time a 0 is spotted, set all squares in the row and column to 0. 
        Time Complexity: Each square O(m*n) * O(m+n) work = O(m*n(m+n)) , Space Complexity: O(m*m)
        Drawback: Lots of repeated work and copying initial matrix takes up extra space. 
    2. Notice: Each cell has the ability to change an entire ROW and COLUMN 
        - Two arrays: One for columns and One for rows. Each position that hits a 0 will have the row and column position marked.
        Time Complexity: O(m*n), Space Complexity: O(m+n)
        Drawback: Still requires extra space for the two additional arrays. Still an improvemeent, since not creating a complete copy, same info represented by two arrays. 
    3. Time Complexity can't be improved any further, but goal is space complexity of O(1). 
        - Constant Space would require either storing the info in the original input data structure somehow or constant size variables. 
        - Strategy: Store information within the input "matrix" itself and utilize one additional constant space variable. 
        - Time: O(m*n), Space: O(1)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZeroInfo = False #Purple box in diagram
        
        """Iterate over all squares, determining which rows and columns need to be zeroed out"""
        for r in range(ROWS): 
            for c in range(COLS):
                if matrix[r][c] == 0: 
                    matrix[0][c] = 0  #green array (all stored in first row), can set directly 
                    """Row has an extra variable due to first spot taken by the column info"""
                    if r == 0: 
                        rowZeroInfo = True #edge case variable, purple array has one missing space  
                    else: 
                        matrix[r][0] = 0 #purple array (all stored in the first column), set directly
        
        """Start setting rows/columns to zeros, EXCEPT for the first row and first column, since they store the data!"""
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0: #Check both the two storage arrays if current square needs to be set to 0 
                    matrix[r][c] = 0 
        
        """Check if first column needs to be set to 0 (Based on column data array)"""
        if matrix[0][0] == 0: 
            for r in range(ROWS): 
                matrix[r][0] = 0 
        
        """Check if first row needs to be set to 0 (Based on the extra row variable for the first row)"""
        if rowZeroInfo: 
            for c in range(COLS): 
                matrix[0][c] = 0 
        
            
                
                        
                
                    
        