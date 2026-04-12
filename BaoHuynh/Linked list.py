
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # Print the list for easy visualization
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # add(data): Adds a new node to the tail of the list
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the old tail to the new node
            self.tail = new_node  # Update the tail pointer to the new node
        self.count += 1

    # add_at(data, index): Inserts data at a specific index
    def add_at(self, data, index):
        if index < 0 or index > self.count:
            print("Index out of bounds")
            return

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            if self.count == 0:  # If list was empty, head and tail are the same
                self.tail = new_node
            self.count += 1
            return

        if index == self.count:
            self.add(data)  # Reuse the add method since it handles tail updates perfectly
            return

        new_node = Node(data)
        current = self.head
        # Traverse to the node just before the insertion point
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.count += 1

    # remove(data): Removes the first occurrence of data. Returns True if successful, False if not.
    def remove(self, data):
        current = self.head
        prev = None

        while current:
            if current.data == data:
                # Case 1: Removing the head
                if prev is None:
                    self.head = current.next
                    if self.head is None:  # If the list is now empty, tail must also be None
                        self.tail = None
                # Case 2: Removing from middle or tail
                else:
                    prev.next = current.next
                    if current.next is None:  # If we removed the tail, update the tail pointer
                        self.tail = prev

                self.count -= 1
                return True  # Successfully removed

            prev = current
            current = current.next

        return False  # Data was not found

    # remove_at(index): Removes the node at the specified index
    def remove_at(self, index):
        if index < 0 or index >= self.count:
            print("Index out of bounds")
            return None

        current = self.head
        # Case 1: Removing the head
        if index == 0:
            self.head = current.next
            if self.head is None:
                self.tail = None
            self.count -= 1
            return current.data

        # Case 2: Removing from middle or tail
        prev = None
        for _ in range(index):
            prev = current
            current = current.next

        prev.next = current.next
        if current.next is None:  # If we removed the tail
            self.tail = prev

        self.count -= 1
        return current.data

    # search(data): Returns the index of the first occurrence of data, or -1 if not found
    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    # clear(): Empties the entire list
    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0


# Testing the Custom Linked List
ll = LinkedList()

# Testing add(data)
ll.add(10)
ll.add(20)
ll.add(30)
ll.print_list()  # 10 -> 20 -> 30 -> None

# Testing add_at(data, index)
ll.add_at(15, 1)  # Insert 15 at index 1
ll.add_at(5, 0)  # Insert 5 at index 0 (new head)
ll.add_at(35, 5)  # Insert 35 at the end (new tail)
ll.print_list()  # 5 -> 10 -> 15 -> 20 -> 30 -> 35 -> None

# Testing count
print(f"Total count: {ll.count}")  # 6

# Testing search(data)
print(f"Index of 20: {ll.search(20)}")  # 3
print(f"Index of 99: {ll.search(99)}")  # -1

# Testing remove(data)
is_removed = ll.remove(15)
print(f"Was 15 removed? {is_removed}")  # True
ll.print_list()  # 5 -> 10 -> 20 -> 30 -> 35 -> None

# Testing remove_at(index)
removed_val = ll.remove_at(4)  # Removing the tail (35)
print(f"Removed value at index 4: {removed_val}")  # 35
ll.print_list()  # 5 -> 10 -> 20 -> 30 -> None

# Testing clear()
ll.clear()
ll.print_list()  # None
print(f"Count after clear: {ll.count}")  # 0

#Stacks (LIFO - Last In, First Out)
#For a Stack, we push and pop from the "top".
#To make this efficient O(1), we treat the 'head' of our LinkedList as the top.

class Stack:
    def __init__(self):
        #Composition: The Stack HAS A LinkedList
        self._list = LinkedList()

    #push(data): Adds an item to the top of the stack (the head of the list)
    def push(self, data):
        self._list.add_at(data, 0)

    #pop(): Removes and returns the top item
    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Cannot pop from an empty stack.")
            return None
        return self._list.remove_at(0)

    #peek(): Returns the top item without removing it
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self._list.head.data

    #is_empty(): Returns True if stack has no items
    def is_empty(self):
        return self._list.count == 0

    #size(): Returns the number of items in the stack
    def size(self):
        return self._list.count

    def print_stack(self):
        print("Top ->", end=" ")
        self._list.print_list()


#Testing the Stack
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

my_stack.print_stack() # Output: Top -> 30 -> 20 -> 10 -> None

print(f"Popped item: {my_stack.pop()}") # 30
print(f"Current top item: {my_stack.peek()}") # 20
my_stack.print_stack() # Output: Top -> 20 -> 10 -> None


#15. Queues (FIFO - First In, First Out)
#Queues add to the "back" and remove from the "front".
#Using our LinkedList, the 'tail' is the back (enqueue) and 'head' is the front (dequeue).
#Because our LinkedList tracks the tail, both operations are O(1) efficient.

class Queue:
    def __init__(self):
        self._list = LinkedList()

    #enqueue(data): Adds an item to the back of the queue (the tail of the list)
    def enqueue(self, data):
        self._list.add(data) # Our add() method already appends to the tail

    #dequeue(): Removes and returns the item at the front of the queue (the head)
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow: Cannot dequeue from an empty queue.")
            return None
        return self._list.remove_at(0)

    #peek(): Returns the front item without removing it
    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self._list.head.data

    def is_empty(self):
        return self._list.count == 0

    def size(self):
        return self._list.count

    def print_queue(self):
        print("Front ->", end=" ")
        self._list.print_list()


#Testing the Queue
my_queue = Queue()
my_queue.enqueue("Alice")
my_queue.enqueue("Bob")
my_queue.enqueue("Charlie")

my_queue.print_queue() # Output: Front -> Alice -> Bob -> Charlie -> None

print(f"Dequeued person: {my_queue.dequeue()}") # Alice
print(f"Next in line (peek): {my_queue.peek()}") # Bob
my_queue.print_queue() # Output: Front -> Bob -> Charlie -> None

