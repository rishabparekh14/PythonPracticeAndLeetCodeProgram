from heapq import merge
from operator import le
from turtle import right
from linked_list import LinkedList

def merge_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head == None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint 
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    Merges 2 linkedlist sorting data in nodes. Return a new merged list 
    """
    merged = LinkedList()

    ## Adding a head which will be discarded 
    merged.add(0)

    current = merged.head

    ## Obtaining the head nodes for left and right linked lists 
    left_head = left.head
    right_head = right.head

    ## Iterate over each side until we reach tail nodes of both lists 
    while left_head or right_head:

        if left_head is None:
            current.next_node = right_head
        ## Call next on right to set loop condition to false 
        ## if the head node of right is none we are past tail add the tail node from left to merged linked list 
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            ## obtain node data to perform operations
            left_data = left_head.data
            right_data = right_head.data
            ## If left is less than right data then set left node as current node 
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            ## else vice versa 
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        ## Move current to next_node 
        current = current.next_node

    ## Discard fake head and set first merged node as head 
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(10)
l.add(46)
l.add(1)
l.add(23)
l.add(89)
l.add(66)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)

                
    

