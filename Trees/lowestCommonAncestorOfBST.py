# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
""" 
Understand: 
1. Is p <= q? No, q could be greater than p 

Evaluate: 
1. Recursive: 
    Time: O(height of tree) = O(N)
    Space: O(height of tree) = O(N)
2. Iterative: 
    Time: O(height of Tree) = O(N)
    Space: O(1) 
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ Recursive Solution 
        if root.val == p.val: 
            return p
        elif root.val == q.val: 
            return q
        elif p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val: 
            return root
        else: 
            if q.val < root.val and p.val < root.val: # Both p and q are less than the root (must be in left subtree)
                return self.lowestCommonAncestor(root.left, p, q)
            else: #Both p and q are greater than the root (must in right subtree)
                return self.lowestCommonAncestor(root.right, p, q)
        """
        ### Iterative Solution
        curr = root 
        while curr:
            if p.val > curr.val and q.val > curr.val: 
                curr = curr.right 
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else: 
                return curr