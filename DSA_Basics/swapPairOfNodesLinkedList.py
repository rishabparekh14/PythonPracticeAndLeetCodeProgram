# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if head == None or head.next == None:
            return head
        forward = head.next
        temp = 0
        while forward:
            current.val, forward.val = forward.val, current.val
            if forward.next == None:
                break
            current = forward.next
            forward = current.next
            
        return head
      