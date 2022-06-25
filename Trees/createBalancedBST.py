# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ Plan
    - At each step, after finding middle, we are RECURSING on the left and right half. 
    Therefore, helper function needs 2 args, a left subtree and right subtree. 
    """
    """ Evaluate 
    Time: O(N) - iterate over all elements in nums once 
    Space: O(logN) - since the tree being produced is height balanced, the call stack will be 
    as tall as the height of the BALANCED binary tree. Despite the total output being O(N), the 
    output is not considered in space complexity. 
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Return the tree (BST) formed by the two pointers given"""
        def helper(left, right):
            if left > right: 
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            # Base Case Handles both of these recursive calls below 
            root.left = helper(left, mid-1) #right is moving left, eventually becoming less than left
            root.right = helper(mid+1, right) #left is moving right, eventually becoming greater than right 
            return root
        return helper(0, len(nums)-1)