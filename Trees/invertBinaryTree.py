from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ Understand 
    1. No nodes? Return original 
    2. Can the values be negative? Yes 
    3. What to do if only a single child? Set the other branch to that value?
    Test Cases: 
    1. root = [1, 2, 3], Output: [1, 3, 2]
    2. root = [1, 2, null], Output: [1, null, 2] (One child)
    3. root = [1, null, 2], Output: [1, 2, null] (One child)
    4. root = [1], Output: [1] (No children)
    """
    """ Plan
    1. Recursive (DFS) Solution
        Base Case: 
        1. root is None or No Children, Return: root
        Recursive Case: 
        1. Switch left and right branches 
        2. Recurse on left branch 
        3. Recurse of right branch 
        4. Return root 
    2. Iterative - DFS 
        Initialize stack 
        Add root to stack 
        while stack: 
            curr = pop from stack 
            Switch curr's left and right child 
            if left child exists: (Doesn't matter if left or right child is added first)
                Add left child to stack 
            if right child exists: 
                Add right child to stack 
    """
    """ Evaluate 
    1. Recursive DFS 
        Time: O(N)
        Space: O(N)
    2. Iterative DFS 
        Time: O(N)
        Space: O(N) - depending on the tree's structure 
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Recursive (DFS) Solution 
        if root is None: 
            return root 
        else: 
            left = root.left 
            root.left = root.right
            root.right = left 
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root """
        """Iterative - DFS """
        stack = deque()
        if not root: 
            return root 
        else: 
            stack.append(root)
            while stack: 
                curr = stack.pop()
                left = curr.left 
                curr.left = curr.right
                curr.right = left 
                if curr.left: 
                    stack.append(curr.left)
                if curr.right: 
                    stack.append(curr.right)
            return root
        
        