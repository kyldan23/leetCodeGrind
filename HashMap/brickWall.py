from collections import defaultdict
class Solution:
    """ Understand 
    Questions:
    1. What if there is only a single brick in each row (edge case)? Return the length of the original input list
    2. Can the width/height be very large? Yes 
    
    Brute force: 
    1. Create a copy of the bricks (into linked list)
    2. Iterate over every column (up to the width)
    2. Iterate over all the rows in that column 
    3. If the brick in the row is not size 1 or just previously moved, then add 1 
    4. Compare with the least number of bricks moved (default to infinity)
    5. Return the number of minimum number of bricks crossed 
    """
    """Match 
    1. Array of linked lists, iterating over every single possible column up to the width:
    Time: O(r*c) to create the array of linked lists + O(m*n) to iterate over all of it = O(m*n)
    Space: O(r*c)  
    Issue: Need to iterate over every single column. If the widths are a billion, you will have to iterate a billion times to cover all possible column, even 
    if there is only a single brick that takes up a billion in width.
    
    2. Hashmap: (Key: position of the gap, value: # of occurences of a gap in that position)
    Time: O(r*c) - visit every BRICK  
    Space: O(r*c) - explained below in Evaluate 
    Key Difference: Despite having the same worst case complexity asympotically, we are only iterating over the actual bricks. If a single brick has a width of 
    a billion, we traverse through only that single element and not 1 to a billion. 
    """
    """ Plan 
    1. Initialize an empty hash table
    2. Iterating through all the rows 
    3. In each row, identify the locations of each gap 
    4. Update the count in the hashmap 
    5. Return total # of rows in the wall minus maximum number of gaps within hashtable
    """
    """ Evaluate - Let r = # of rows, Let c = # of columns
    Time Complexity: O(r*c)
    Reason: Visit every single brick in the wall 
    Space Complexity: O(r*c) 
    Reason: Although you can say the worst case space complexity is the total width of a row, its much eaisier to just give the upper bound as every 
    brick producing its own entry in the hashset. 
    """
    def leastBricks(self, wall: List[List[int]]) -> int:
    wall_dict = defaultdict(int)

    for currWall in wall:
        position = 0
        
        for brick in currWall[:-1]:
        position += brick
        wall_dict[position] += 1
        
        # if position in wall_dict:
        #   wall_dict[position] += 1
        # else:
        #   wall_dict[position] = 1
            
    # if not wall_dict:
    #   return len(wall)
        
    return len(wall) - max(wall_dict.values(), default = 0)
