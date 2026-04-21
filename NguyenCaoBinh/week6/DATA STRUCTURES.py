# =================================================================
# WEEK 6: DATA STRUCTURES - LINKED LISTS, STACKS, AND QUEUES
# =================================================================
from collections import deque

# // --- SECTION 1: LINKED LIST IMPLEMENTATION ---

# // Exercise 1: Define a Node class and a SinglyLinkedList class.
# // The Linked List should support appending and displaying elements.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# // --- SECTION 2: STACK IMPLEMENTATION ---

# // Exercise 2: Implement a Stack using a Python List.
# // Create functions for push, pop, and peek operations.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

# // --- SECTION 3: QUEUE IMPLEMENTATION ---

# // Exercise 3: Implement a Queue using 'collections.deque' for O(1) performance.
# // Enqueue and Dequeue operations should be demonstrated.
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            return "Queue is empty"
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

# -----------------------------------------------------------------
# EXECUTION AND TESTING
# -----------------------------------------------------------------

# // Testing Linked List
print("--- Linked List Test ---")
llist = SinglyLinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.display()

# // Testing Stack
print("\n--- Stack Test (LIFO) ---")
browser_history = Stack()
browser_history.push("google.com")
browser_history.push("hcmut.edu.vn")
browser_history.push("github.com")
print(f"Current Page (Top): {browser_history.peek()}")
print(f"Back Button (Pop): {browser_history.pop()}")
print(f"New Current Page: {browser_history.peek()}")

# // Testing Queue
print("\n--- Queue Test (FIFO) ---")
printer_jobs = Queue()
printer_jobs.enqueue("Document_1.pdf")
printer_jobs.enqueue("Lab_Report.docx")
printer_jobs.enqueue("Schematic_Design.png")
print(f"Printing: {printer_jobs.dequeue()}")
print(f"Next in line: {printer_jobs.size()} jobs remaining.")

# // Exercise 4: Practical Challenge
# // Use a Stack to reverse a string "COMPUTER_ENGINEERING".
def reverse_string_with_stack(input_str):
    s = Stack()
    for char in input_str:
        s.push(char)
    
    reversed_str = ""
    while not s.is_empty():
        reversed_str += s.pop()
    return reversed_str

original = "COMPUTER_ENGINEERING"
print(f"\nReversed String: {reverse_string_with_stack(original)}")

# =================================================================
# END OF WEEK 6 PRACTICE
# =================================================================