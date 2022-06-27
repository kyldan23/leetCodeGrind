# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ Evaluate 
    Time: O(N) - iterates over all the values once 
    Space: O(N) - height of the tree, worst case is linear tree that it has to keep recursing over. 
    """
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #returns the tail of the resulting tree and flattens the tree
        def helper(root):
            if not root: 
                return None #Can't flatten an empty tree
            if not root.left and not root.right:  
                return root 
            else: 
                leftTail = helper(root.left) #assume the recursive function works
                rightTail = helper(root.right) #assume the recursive function works
                
                if leftTail: #can only call leftTail.right if leftTail isn't null 
                    leftTail.right = root.right
                    root.right = root.left 
                    root.left = None 
                """Which is the tail?
                1. If rightTail exists, then rightTail is the tail of the flattened tree
                2. If rightTail doesn't exist, but leftTail exists, then leftTail is the tail of the flattened tree
                3. If both rightTail and leftTail don't exist, then the tail of the flattened tree is just the root itself
                """
                return rightTail or leftTail or root
                
        helper(root)