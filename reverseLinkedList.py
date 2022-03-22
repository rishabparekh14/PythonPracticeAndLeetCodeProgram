# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current =next
            
## Another Approach
#         current = self.head
#         tempArr = []
#         while current:
#             tempArr.append(current.data)
#             current =current.next

#         for i in range(0,len(tempArr)):
#             newNode = ListNode(tempArr[i])
#             newNode.next = self.head
#             self.head = newNode
        return prev
    