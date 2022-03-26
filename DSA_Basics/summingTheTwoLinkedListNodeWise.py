# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        carryActivated = False
        arrayList = []
        temp = dummy = ListNode(0)
        
        while l1 and l2:
            arrayList.append((l1.val+l2.val+carry)%10)
            carry = (l1.val+l2.val+carry) // 10
            if l1.next == None:
                l1 = l1.next
                l2 = l2.next
                break
            if l2.next == None:
                l1 = l1.next
                l2 = l2.next
                break
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            arrayList.append((l1.val+carry)%10)
            carry = (l1.val+carry) // 10
            l1 = l1.next
        while l2:
            arrayList.append((l2.val+carry)%10)
            carry = (l2.val+carry) // 10
            l2 = l2.next
        if carry > 0:
            arrayList.append(carry)
        
        for i in range(len(arrayList)):
            newNode = ListNode(arrayList[i])
            dummy.next = newNode
            dummy = dummy.next
            
        return temp.next
            
            