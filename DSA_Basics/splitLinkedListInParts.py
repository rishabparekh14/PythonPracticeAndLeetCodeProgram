# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        count = 0
        while curr:
            count +=1
            curr = curr.next
        
        width, remainder = divmod(count, k)
        ans = []
        cur = head
        for i in range(k):
            head = cur
            for j in range(width + (i < remainder) - 1):
                
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
         
        
                