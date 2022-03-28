# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arrayList = []
        curr = head
        count = 0
        while curr:
            count +=1
            arrayList.append(curr.val)
            curr = curr.next
        
        for i in range(count-1):
            if arrayList[i] > arrayList[i+1]:
                for j in range(i+1):
                    if arrayList[j] > arrayList[i+1]:
                        arrayList[j], arrayList[i+1] = arrayList[i+1], arrayList[j]
        head = None
        for k in range(count-1,-1,-1):
            newList = ListNode(arrayList[k])
            newList.next = head
            head = newList
        return head
            
                    
                
        