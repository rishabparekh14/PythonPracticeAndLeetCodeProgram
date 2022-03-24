# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        forward = head
        if forward and forward.next:
            forward = forward.next
        
        while forward:
            if forward.val == current.val and forward.next !=None:
                forward = forward.next
            elif forward.val !=current.val:
                current.next = forward
                current= current.next
                forward = forward.next
            elif forward.val ==current.val and forward.next ==None:
                current.next = None
                break
                
        return head
                