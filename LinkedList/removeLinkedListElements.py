# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Understand: 
    Mutate the original linked list, removing nodes of "val"
    
    Match: 
    1. Dummy Node: Allows you to treat all the nodes the same way. Return dummyNode.next in the end. 
    2. 2 pointers: previous node and current node. 
    
    Plan: 
    sentinelNode = empty Link, with next pointing to "head"
    prev, curr = sentinalNode, head 
    while curr is not null: 
        if curr has value of "val": 
            prev's next should point to the node after curr 
        else: #current node is not equal to val, it doesn't get deleted 
            prev = curr 
        move curr to the next node 
    return sentinelNode.next
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinelNode = ListNode(0, head)
        prev, curr = sentinelNode, head 
        while curr: 
            if curr.val == val: 
                prev.next = curr.next 
            else: 
                prev = curr 
            curr = curr.next 
        return sentinelNode.next 