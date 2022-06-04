# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""Tactics 
1. Dummy Node 
2. Two Pointers 
"""
"""Runtime
Time: O(N) - Iterate through the list once 
Space: O(1) - Only saving 2 pointers regardless of input size
"""
""" Explanation
1. Two Pointers that are updated in each step  are 'prev' and 'curr'. We get the other pointer 'right' from 'curr' and therefore don't technically keep track of it. 
2. The 'dummy' node is automatically corrected when 'prev' is correct pointing to the new left node in each swap, since 'prev' initially points to the 'dummy' node. 
3. While loop condition ensures there's at least 2 nodes left to swap. 
4. 'prev' in the loop has its current node point to the new left node (after the swap) THEN updates itself to reference the new right node (after swap).
"""


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, dummy.next #prev points to dummy, which inadvertently fixes it later
        
        while curr and curr.next: #at least 2 nodes left 
            right = curr.next 
            #Perform Swap
            curr.next = right.next
            right.next = curr 
            #Update previous pointer to point at the new left node (of the swapped pair), which fixes the dummy node as well!
            prev.next = right 
            #update the two pointers to prep for next pair to be swapped
            prev = curr
            curr = prev.next 
        return dummy.next
            
        """ Incorrect - does not set the previous node's pointer to the swapped nodes (Make sure to run with full list of [1, 2, 3, 4] to see the error)
        dummy = ListNode(0, head)
        dummyCorrect = False
        while head and head.next: 
            leftNode = head 
            rightNode = head.next 
            leftNode.next = rightNode.next 
            rightNode.next = leftNode
            if not dummyCorrect: 
                dummyNode = rightNode 
                dummyCorrect = True 
            head = leftNode.next
        return dummyNode.next 
        """
        
            
        