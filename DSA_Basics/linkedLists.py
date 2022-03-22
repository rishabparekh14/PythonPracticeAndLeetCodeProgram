



class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, newData):

        new_node = Node(newData)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self,prevNode, newData):

        new_node = Node(newData)

        if prevNode is None:
            return
        
        # tempNode = self.head
        # while tempNode.data == prevNode:
        #     tempNode = tempNode.next
        new_node.next = prevNode.next
        prevNode.next = new_node
        
    def append(self, newData):
        last = self.head
        new_node = Node(newData)
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            previous = temp
            temp = temp.next

        if temp == None:
            return

        previous.next = temp.next
        temp = None

    def deleteNodeAtPosition(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        prev = self.head
        curr = self.head
        temp = self.head

        while curr is not None:
            if index == position:
                temp = curr.next
                break
            prev = curr
            curr = curr.next
            index +=1
        prev.next= temp
        return prev

    def deleteFullLinkedList(self):
        current = self.head
        while current:
            forwarNode = current.next

            del current.data
            current = forwarNode

    def getCount(self):
        temp = self.head
        count = 0
        while temp:
            count +=1
            temp = temp.next
        return count

    def searchAnElement(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next

    def findNthNodeFromEnd(self, position):
        
        length = self.getCount()
        temp= self.head
        if position > length:
            print("Location is greater than the length in linkedlist")
            return
        
        for i in range(0, length-position):
            temp = temp.next
        return temp.data

    def detectLoop(self):
        s =set()
        temp = self.head

        while temp:

            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False


            





if __name__=='__main__':

    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    llist.append(5)
    #llist.insertAfter(2,6)


    llist.printList()
    llist.deleteNode(5)
    print("New List after deletion")
    llist.printList()
    print("Delete node at a position")
    llist.deleteNodeAtPosition(3)
    llist.printList()
    # print("Deleting full linked list ")
    # llist.deleteFullLinkedList()
    print("Count of linkedlist:", llist.getCount())
    print("Searching the number in linkedlist:",llist.searchAnElement(4))
    print("Finding Nth Node from the end in the linkedList:", llist.findNthNodeFromEnd(1))
    if llist.detectLoop():
        print("Loop Detected")
    else:
        print("Loop is not detected")




