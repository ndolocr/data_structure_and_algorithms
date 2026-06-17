class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return new_node
    
    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.value} --> ", end="")
            temp = temp.next
        print("None")
    
    def get_values_as_int(self):
        temp = self.head
        num = ""
        while temp is not None:
            num = num + f"{temp.value}"
            temp = temp.next
        return num
    
    def reverse_linked_list(self):
        temp = self.head
        
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

def main():
    # l1 = LinkedList(9)
    # l1.append_node(9)
    # l1.append_node(9)
    # l1.append_node(9)
    # l1.append_node(9)
    # l1.append_node(9)
    # l1.append_node(9)
    # l1.print_linked_list()

    # l2 = LinkedList(9)
    # l2.append_node(9)
    # l2.append_node(9)
    # l2.append_node(9)
    # l2.print_linked_list()

    l1 = LinkedList(2)
    l1.append_node(4)
    l1.append_node(3)
    l1.print_linked_list()

    l2 = LinkedList(5)
    l2.append_node(6)
    l2.append_node(4)
    l2.print_linked_list()

    num_1 = l1.get_values_as_int()
    num_2 = l2.get_values_as_int()
    
    print()
    print(f"List One Numbers --> {num_1}")
    print(f"List Two Numbers --> {num_2}")
    print()

    l1.reverse_linked_list()
    num_1_reversed = l1.get_values_as_int()
    l1.print_linked_list()

    l2.reverse_linked_list()
    num_2_reversed = l2.get_values_as_int()
    l2.print_linked_list()

    print()
    print(f"List One Reversed Numbers --> {num_1_reversed}")
    print(f"List Two Reversed Numbers --> {num_2_reversed}")

    sum = int(num_1_reversed) + int(num_2_reversed)
    print(f"Sum:--> {sum}")

    sum_str = f"{sum}"
    l3 = LinkedList(int(sum_str[0]))
    for letter in range(1, len(sum_str), 1):
        l3.append_node(int(sum_str[letter]))
    
    print()
    print("L3")
    l3.print_linked_list()
    print("Reversed Linked List")
    l3.reverse_linked_list()
    l3.print_linked_list()

if __name__ == "__main__":
    main()