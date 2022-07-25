# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ 
    Understand: 
    1. Minimum number of nodes 
    2. All positive or negative? 
    3. Cycles in the list? 
    """
    """ Evaluate 
    Time: O(N)
    Space: O(1)
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ### Edge Case: 1 or less links 
        if head is None or head.next is None: 
            return head 
        ### At least 2 nodes exist  
        else: 
            #oddPointer
            oddPointer = head 
            #savedEvenStart is one ahead of oddPointer
            savedEvenStart = oddPointer.next 
            #evenPointer is one node ahead of oddPointer
            evenPointer = savedEvenStart 
            #while evenPointer isn't null and it's next is not null 
            while evenPointer is not None and evenPointer.next is not None: 
                #Advance both pointers by 2 nodes
                oddPointer.next = oddPointer.next.next
                oddPointer = oddPointer.next
                
                evenPointer.next = evenPointer.next.next
                evenPointer = evenPointer.next
            #Set oddPointer to point to "savedEvenStart"
            oddPointer.next = savedEvenStart
            #return head 
            return head 
            