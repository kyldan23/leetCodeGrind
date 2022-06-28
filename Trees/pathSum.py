# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ Understand 
    1. "root" is null => return False immediately, since there doesn't exist any leaves. 
    """
    """ Match 
    1. DFS (Recursive) - depth is priority, since a path must be from the root to a leaf. 
    """
    """ Plan 
    Helper Method: Return whether a path exists from root to leaf and reaches targetSum
        
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Helper Method: 
        Return whether a path exists from root to leaf exists, where the targetSum is reached.
        """
        """ Original Solution: Works, but had to have confusing cases since better base case should have been identified 
        def helper(root, targetSum):
            if not root: 
                if targetSum == 0: 
                    return True
                return False
            else: 
                if not root.left and not root.right: 
                    return (targetSum - root.val) == 0 
                else: 
                    leftSearch = helper(root.left, targetSum - root.val) and (root.left is not None)
                    rightSearch = helper(root.right, targetSum - root.val) and (root.right is not None)
                    return leftSearch or rightSearch 
        if not root: 
            return False 
        else: 
            return helper(root, targetSum)
        """
        if not root: 
            return False
        else: 
            currDiff = targetSum - root.val
            #Reach a leaf (No children)
            if not root.left and not root.right: 
                return currDiff == 0
            return self.hasPathSum(root.left, currDiff) or self.hasPathSum(root.right, currDiff)