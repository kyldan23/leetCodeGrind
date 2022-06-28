# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ pruneTree Function
    Return: tree
    """
    """ Evaluate 
    Time: O(N) - visit all nodes once
    Space: O(N) - call stack is based on height of tree, which is a linear tree in the worst case
    Space:
    """
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Helper method 
        Prunes children of "root" as needed and RETURNS whether a 1 is present in the root's children 
        """
        def helper(root): 
            if root is None: 
                return False 
            else: 
                #Check if left subtree contains a 1 
                leftContainsOne = helper(root.left) 
                #if root.left and (root.left.val == 0) and not leftContainsOne: 
                if not leftContainsOne:
                    #Prune left child
                    root.left = None
                rightContainsOne = helper(root.right)
                #if root.right and (root.right.val == 0) and not rightContainsOne:  
                if not rightContainsOne:
                    #Prune right child
                    root.right = None               
                """if root.val is 1: 
                    return True 
                else: 
                    return leftContainsOne or rightContainsOne"""
                """Simplify the return statement to one line"""
                return root.val or leftContainsOne or rightContainsOne
        result = helper(root)
        """if not root: 
            return None
        if root.val is 0 and not result:
            return None 
        return root"""
        return root if helper(root) else None