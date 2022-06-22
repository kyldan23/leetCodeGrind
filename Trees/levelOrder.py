from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ Evaluate 
    Time Complexity: O(N) - visiting all nodes once 
    Memory Complexity: O(N) - largest amount of nodes is O(N/2) => O(N), which occurs when all the nodes at the height 0 are added. 
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        new_deque = deque()
        final = [] 
        if root is None: 
            return final
        else: 
            new_deque.append(root)
            while new_deque: 
                currLength = len(new_deque) #keeps track of number of nodes in the current level
                level = [] #stores all the nodes' values in the current level 
                for i in range(currLength):
                    curr = new_deque.popleft()
                    if curr.left is not None:   
                        new_deque.append(curr.left)
                    if curr.right is not None: 
                        new_deque.append(curr.right)
                    level.append(curr.val)
                final.append(level)
            return final
        