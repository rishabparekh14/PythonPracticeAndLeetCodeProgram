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
            
            