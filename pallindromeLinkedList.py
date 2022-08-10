# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arrayList = []
        while head:
            arrayList.append(head.val)
            head = head.next
        return arrayList == arrayList[::-1]

### Alternate and best solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         slow =head
#         fast = head 
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next 
#         prev = slow
#         slow = slow.next 
#         prev.next = None
#         while slow:
#             next_node = slow.next
#             slow.next = prev
#             prev = slow
#             slow = next_node
#         while prev:
#             if head.val != prev.val:
#                 return False
#             prev= prev.next
#             head= head.next 
#         return True
        
        
            
            