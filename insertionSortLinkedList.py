# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # arrayList = []
        # curr = head
        # count = 0
        # while curr:
        #     count +=1
        #     arrayList.append(curr.val)
        #     curr = curr.next
        
        # for i in range(count-1):
        #     if arrayList[i] > arrayList[i+1]:
        #         for j in range(i+1):
        #             if arrayList[j] > arrayList[i+1]:
        #                 arrayList[j], arrayList[i+1] = arrayList[i+1], arrayList[j]
        # head = None
        # for k in range(count-1,-1,-1):
        #     newList = ListNode(arrayList[k])
        #     newList.next = head
        #     head = newList
        # return head

        dummy = ListNode()
        curr = head

        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev = dummy

            # find the position to insert the current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            next = curr.next
            # insert the current node to the new list
            curr.next = prev.next
            prev.next = curr

            # moving on to the next iteration
            curr = next

        return dummy.next



            
                    
                
        