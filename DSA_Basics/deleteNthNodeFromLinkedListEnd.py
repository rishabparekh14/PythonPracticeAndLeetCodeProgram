# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        
        current = forward = head
        count =0
        
        while forward:
            
            if count > n:
                current = current.next 
            count +=1
            forward = forward.next
        
        if count == 1:
            head = None
            return head
        elif count == n:
            head = current.next
        if  current.next and current.next.next!=None :
            current.next = current.next.next
        else:
            current.next = None
        return head

            