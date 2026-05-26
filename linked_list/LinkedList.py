from linked_list.Node import Node

class LinkedList:
    """
    Data Structure: - Linked List
    This is a data structure that stores data where each item in the linked list 
    points to the next item in the Linked list.

    The following can be perfomed on a linked list:-
    1.) Append - create a node and attache it to the end of the linked list
    2.) Pre-append - create a node and attache it to the beginning f the linked list
    3.) Pop - delete the last node of a linked list.
    4.)
    """
    length = 0
    def __init__(self, value):
        """
        
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        LinkedList.length += 1
    
    

