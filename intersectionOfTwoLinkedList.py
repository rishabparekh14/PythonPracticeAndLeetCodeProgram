# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headA:
            list2 = headB
            while list2:
                if headA == list2:
                    return list2
                list2 = list2.next
            headA = headA.next
        return None