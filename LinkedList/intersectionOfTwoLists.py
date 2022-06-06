# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
""" Tactics
1. Two Pointers - a pointer starts with listA, the other starts with listB. When each pointer finishes one list, they iterate over the other. 
"""
"""Complexity 
1. Time: O(m+n) - time to traverse both lists, when there is no intersection. 
2. Space: O(1) - only storing two pointers 
"""
""" Explanation 
1. Having each pointer traverse both lists guarantees that if there is no intersection, both will hit "null" at the same time, since they travel the same distance. 
2. listA and listB can be difference sizes. Therefore, traveling both lists guarantees they will "meet up" at the intersection eventually since they have to travel 
the same total distance. Proof: They must travel the same distance. Past the intersection, is the same distance. If they travel the same distance, they eventually will have the same 
"last shared stretch" to run. 
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None: 
            return None
        aPoint = headA #traverses A first 
        bPoint = headB #traverses B first 
        #Have two pointers, one traversing A then B, the other traversing B then A. 
        while aPoint != bPoint: 
            if aPoint is None: 
                aPoint = headB 
            else: 
                aPoint = aPoint.next
                
            if bPoint is None: 
                bPoint = headA 
            else: 
                bPoint = bPoint.next 
        return aPoint #Guaranteed to have a common node, since both hit null eventually after traversing both lists in their entirety. 
        
        """ Meets time/space requirements, but code is not as efficient as can be
        aPoint = headA 
        aLength = 0 
        while aPoint: 
            aLength += 1 
            aPoint = aPoint.next
        aPoint = headA #reset pointer
        bPoint = headB 
        bLength = 0 
        while bPoint: 
            bLength += 1 
            bPoint = bPoint.next
        bPoint = headB #reset pointer
        
        if aLength > bLength: 
            diff = aLength - bLength
            while diff: 
                aPoint = aPoint.next 
                diff -= 1
        else: 
            diff = bLength - aLength
            while diff: 
                bPoint = bPoint.next 
                diff -= 1
        
        while aPoint: 
            if aPoint == bPoint: 
                return aPoint 
            aPoint = aPoint.next
            bPoint = bPoint.next
        return None
        """