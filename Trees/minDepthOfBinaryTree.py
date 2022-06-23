from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ Understand
    
    """
    """ Plan 
    
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """ Recursive Solution
        if root is None:  
            return 0 
        else:
            minLeft = self.minDepth(root.left)
            minRight = self.minDepth(root.right)
            
            #Edge Case: If tree has a single branch, then one branch is guaranteed to return 0, but doesn't represent a leaf. 
            if not minLeft or not minRight: 
                return 1 + max(minLeft, minRight)
            return 1 + min(minLeft, minRight)
        """
        #smallestDepth = float('inf')
        new_deque = deque()
        depth = 0 
        if not root: 
            return 0
        else: 
            new_deque.append(root)
            while new_deque: 
                depth += 1 
                length = len(new_deque)
                for i in range(length):
                    curr = new_deque.popleft()
                    if curr.left == None and curr.right == None: 
                        #smallestDepth = min(smallestDepth, depth)
                        return depth
                    else: 
                        if curr.left: 
                            new_deque.append(curr.left)
                        if curr.right: 
                            new_deque.append(curr.right)
            #return smallestDepth
        