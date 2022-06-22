# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Evaluate
    Recursive: 
        Time Complexity: O(N)
        Recursive Complexity: O(depth of the tree) - max height of stack is max depth of tree, would be N if tree is not balanced. 
    Iterative: 
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive Solution
        Base Case: (Leaf) => return empty list 
        Recursive Case: Add itself, recurse left tree, recurse right tree
        
        if root is None: 
            return []
        else: 
            left_vals = self.preorderTraversal(root.left)
            right_vals = self.preorderTraversal(root.right)
            return [root.val] + left_vals + right_vals 
        """
        """Iterative Solution"""
        #Initialize empty queue 
        #Initialize empty list 
        #Check if root is null
            #If null: return empty list 
            #Else: Add root to queue
        #While queue is not empty 
            #Pop off stack and add element to list 
            #Add children nodes to stack if they are not null
        stack = [] 
        preOrder = [] 
        if root is None:
            return preOrder 
        else: 
            stack.append(root)
            while stack: 
                curr = stack.pop()
                preOrder.append(curr.val)
                if curr.right is not None: #since stack if LIFO 
                    stack.append(curr.right)
                if curr.left is not None: 
                    stack.append(curr.left)
            return preOrder