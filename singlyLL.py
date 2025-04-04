from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert at a specific position (middle)
    def insert_at_position(self, val, pos):
        if pos == 0:
            self.insert_at_beginning(val)
            return
        current = self.head
        for _ in range(pos - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node = ListNode(val, current.next)
        current.next = new_node

    # Delete from the beginning
    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next

    # Delete from the end
    def delete_from_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    # Delete from a specific position (middle)
    def delete_from_position(self, pos):
        if not self.head:
            return
        if pos == 0:
            self.delete_from_beginning()
            return
        current = self.head
        for _ in range(pos - 1):
            if current is None or current.next is None:
                return
            current = current.next
        if current.next:
            current.next = current.next.next

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Convert to list (for easy debugging)
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
# Singly Linked List Test
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_beginning(0)
sll.insert_at_position(1.5, 2)
print("Singly Linked List:", sll.to_list())  # Output: [0, 1, 1.5, 2, 3]
sll.reverse()
print("Reversed:", sll.to_list())  # Output: [3, 2, 1.5, 1, 0]

class DListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, val):
        new_node = DListNode(val, None, self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, val):
        new_node = DListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    # Insert at a specific position (middle)
    def insert_at_position(self, val, pos):
        if pos == 0:
            self.insert_at_beginning(val)
            return
        current = self.head
        for _ in range(pos - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node = DListNode(val, current, current.next)
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    # Delete from the beginning
    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    # Delete from the end
    def delete_from_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    # Delete from a specific position (middle)
    def delete_from_position(self, pos):
        if not self.head:
            return
        if pos == 0:
            self.delete_from_beginning()
            return
        current = self.head
        for _ in range(pos):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    # Reverse the doubly linked list
    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node
            current = current.prev
        if prev_node:
            self.head = prev_node.prev

    # Convert to list (for easy debugging)
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def is_palindrome(self):
        vals = self.to_list()
        return vals == vals[::-1]



# Doubly Linked List Test
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_beginning(0)
dll.insert_at_position(1.5, 2)
print("Doubly Linked List:", dll.to_list())  # Output: [0, 1, 1.5, 2, 3]
dll.reverse()
print("Reversed:", dll.to_list())  # Output: [3, 2, 1.5, 1, 0]









class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sm = a + b + carry
            carry = sm // 10  
            current.next = ListNode(sm % 10)  
            current = current.next
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next


        return dummy.next 
