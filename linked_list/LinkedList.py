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
        Class Contructor.
        This is used to initiate a linked list by creating the initial Node. 
        Process of creating a Linked list include:- 
        1.) Create a new Node
        2.) Set Linked list head to the new node
        3.) Set Linked list tail to the new node
        4.) Increase Linked List lenght.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        LinkedList.length += 1
    
    def append(self, value):
        """
        The Append method adds a new node at the end of the linked list
        0(1)

        Process:
        1. Check if Linked List has any node. 
            a.)If Linked List does not have any node, 
                i.) Create the Node.
                ii.) Set head to the created Node.
                iii.) Set tail to the created Node.
                iv.) Update Linked List Lenght by one.
            b.) If linked List has Nodes
                i.) Create a new Node
                ii.) Point tail.next to the new Node.
                iii.) set new Node to be tail.
                iv.) Update Linked List Lenght by one.

        """
