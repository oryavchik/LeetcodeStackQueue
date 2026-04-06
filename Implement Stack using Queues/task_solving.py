"""Implement Stack using Queues"""

class Node:
    """class Node"""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    """class Queue"""
    def __init__(self):
        """Function init"""
        self.head = None
        self.tail = None

    def empty(self):
        """Function checks if the stack is empty"""
        if self.head is None:
            return True
        return False

    def push(self, item):
        """Function adds a new element to the end of the queue"""
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        """Function removes and returns the front element of the queue"""
        if self.head:
            item = self.head.item
            self.head = self.head.next
            return item

    def peek(self):
        """Function returns the front element without removing it"""
        return self.head.item

    def __len__(self):
        """Lenght"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

class MyStack:
    """class MyStack"""
    def __init__(self):
        """Function init"""
        self.q = Queue()

    def push(self, x: int) -> None:
        """Function adds an element to the stack at the front"""
        self.q.push(x)

        for _ in range(len(self.q) - 1):
            self.q.push(self.q.pop())

    def pop(self) -> int:
        """Function removes and returns the top element of the stack"""
        return self.q.pop()

    def top(self) -> int:
        """Function returns the top element without removing it"""
        return self.q.peek()

    def empty(self) -> bool:
        """Function returns True if the stack is empty, otherwise False"""
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
