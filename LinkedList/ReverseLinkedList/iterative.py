# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Understand: 
    1. Edge Case: No nodes => return head 
    2. Edge Case: 1 node => return head (no reversing needed on single node)
    
    Evaluate: Iterative Solution
        Time: O(N) 
        Space: O(1)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Base Case: 1 node or no nodes (no reversing needed)
        if head is None or head.next is None: 
            return head 
        
        ### 2 or more nodes => Nodes need to be reversed!
        prev, curr = None, head 
        
        while curr: #every node needs to be processed  
            nextNode = curr.next
            curr.next = prev 
            prev = curr 
            curr = nextNode 
        
        #Based on the while loop, since we stop when curr becomes null, return "prev" since it's still on the previous NODE
        return prev 
            