# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        current = head
        if head != None:
            forward = head.next
        else:
            forward = None
            return head
        arrayList = []
        while forward:
            count +=1
            if count%2 ==0:
                arrayList.append(forward.val)
            elif count%2!=0:
                current.next = forward
                if forward.next != None:
                    current = forward
            forward = forward.next
         
        while current.next:
            if count %2 == 0:
                current.next = None
            else:
                current = current.next
        
        
        for i in range(len(arrayList)):
            listNode = ListNode(arrayList[i])
            current.next = listNode
            current = current.next
            
        
        return head              


## Alternate and easy approach
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd =head
        even = head
        if head == None:
            return None
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even= even.next
        odd.next = evenHead
        return head
            
            