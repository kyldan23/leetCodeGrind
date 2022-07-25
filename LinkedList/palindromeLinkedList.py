# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge Case: Single node is a palindrome 
        if head.next is None: 
            return True 
        
        #More than 2 nodes => Find mid and reverse second half, then compare each node
        else: 
            #Initialize a fast and slow pointer that start at the same place
            #While fast node is not null and it's next node is not null
                #Advance fast pointer twice
                #Advance slow pointer once 
            #Reverse nodes starting at slow pointer's node 
            #Iterate over nodes starting at head of original linked list and reversed linked list at same time 
                #if value is different, return false immediately 
                #otherwise, advance both pointers 
            #return True 
            
            fast, slow = head, head 
            while fast is not None and fast.next is not None:  
                fast = fast.next.next 
                slow = slow.next 
            
            ###Reverse the second half of the list starting at slow. (Reversing second half of list)
            prev, curr = None, slow #want the very first node that is reversed to point to null! 
            while curr: 
                nextNode = curr.next 
                curr.next = prev 
                prev = curr 
                curr = nextNode 
            #By the end of this loop, curr is pointing to null, prev is pointing at the start of the reversed nodes. 
            
            ### Compare the nodes starting at "head" and "prev"
            while head is not None and prev is not None: #Accounts for edge cases when number of nodes is even
                if head.val != prev.val: 
                    return False 
                else: 
                    head = head.next 
                    prev = prev.next 
            return True 
            