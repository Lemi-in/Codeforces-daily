class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Traverse the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    # Insert at a specific position (1-based index)
    def insert_at_position(self, data, position):
        if position <= 1:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 2):
            if not current.next:
                break
            current = current.next
        if not current.next:  # Insert at end if position exceeds list length
            self.insert_at_end(data)
        else:
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    # Delete at the beginning
    def delete_at_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Delete at the end
    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            current.prev.next = None
        else:
            self.head = None

    # Delete at a specific position (1-based index)
    def delete_at_position(self, position):
        if position <= 1:
            self.delete_at_beginning()
            return
        current = self.head
        for _ in range(position - 1):
            if not current:
                print("Position out of bounds.")
                return
            current = current.next
        if not current:
            print("Position out of bounds.")
        elif not current.next:
            self.delete_at_end()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev


# Example Usage
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(5)
dll.insert_at_position(15, 3)
dll.traverse()  # Output: 5 <-> 10 <-> 15 <-> 20 <-> 30 <-> None

dll.delete_at_beginning()
dll.traverse()  # Output: 10 <-> 15 <-> 20 <-> 30 <-> None

dll.delete_at_end()
dll.traverse()  # Output: 10 <-> 15 <-> 20 <-> None

dll.delete_at_position(2)
dll.traverse()  # Output: 10 <-> 20 <-> None
