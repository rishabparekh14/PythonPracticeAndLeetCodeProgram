def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        while node:
            forward = node.next
            node.val = forward.val
            if forward.next is None:
                node.next = None
                break
            node = node.next
        