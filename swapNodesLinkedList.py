# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        ## Array approach but slow
        # arrayList = []
        # current = head
        # count = 0
        # while current:
        #     count +=1
        #     arrayList.append(current.val)
        #     current =current.next
        # arrayList[k-1], arrayList[count-k] = arrayList[count-k],arrayList[k-1]
        # head = None
        # for i in range(count-1, -1, -1):
        #     linkedList = ListNode(arrayList[i])
        #     linkedList.next = head
        #     head = linkedList
        # return head

        ## faster approach than array
        slow = fast = tracker = head
        count = 0
        startNode = False
        i = 0
        # trackerNode = False
        while fast:
            count +=1
            if count != k and startNode == False:
                slow = slow.next
            elif count == k :
                startNode = True
            fast = fast.next
        
        
        while i != count-k+1:
            i+=1
            if i == count -k+1:
                slow.val, tracker.val = tracker.val, slow.val
            tracker = tracker.next
        
        
        return head


    
     ## Alternate solution     
    #   currentNode = head
    #     endNode = head
    #     for i in range(k-1):
    #         currentNode = currentNode.next
    #     forwardNode = currentNode.next
    #     while forwardNode:
    #         forwardNode = forwardNode.next
    #         endNode = endNode.next
    #     currentNode.val, endNode.val = endNode.val, currentNode.val
    #     return head    
            
        
                    
                
            
            
                